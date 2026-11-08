#!/usr/bin/env python3
"""Analyze one flavor component; no implicit branching factor or lab-frame guess."""
import argparse
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
import random
from physics import lab_particles, model_inputs, scalar_to_bb, select
from lhe_io import read_init, iter_events
from processes import COMPONENTS

ROOT = Path(__file__).resolve().parent


@dataclass
class WeightedAcceptance:
    n: int = 0
    sw: float = 0.
    sw2: float = 0.
    swa: float = 0.
    sw2a: float = 0.
    sw2a2: float = 0.
    positive: int = 0
    first_weight: float = 0.
    equal_weights: bool = True

    def add(self, weight, acceptance):
        if not math.isfinite(weight) or weight <= 0:
            raise ValueError('This LO analyzer requires strictly positive central event weights')
        if not math.isfinite(acceptance) or not 0 <= acceptance <= 1:
            raise ValueError('Acceptance must be in [0,1]')
        if self.n == 0:
            self.first_weight = weight
        else:
            self.equal_weights &= math.isclose(weight, self.first_weight, rel_tol=1.e-9)
        self.n += 1
        self.sw += weight
        self.sw2 += weight*weight
        self.swa += weight*acceptance
        self.sw2a += weight*weight*acceptance
        self.sw2a2 += weight*weight*acceptance*acceptance
        self.positive += int(acceptance > 0)

    def result(self):
        if self.n < 2 or self.sw <= 0:
            raise ValueError('At least two positive-weight production events required')
        acceptance = self.swa/self.sw
        # A cluster is one production event, including its D decay trials.
        # Never treat N*D daughter trials as independent production events.
        residual = max(0., self.sw2a2-2*acceptance*self.sw2a+acceptance**2*self.sw2)
        variance = self.n/(self.n-1)*residual/self.sw**2
        return {'n_events': self.n, 'n_events_with_any_acceptance': self.positive,
                'sum_weights': self.sw, 'acceptance': acceptance,
                'acceptance_mc_se': math.sqrt(variance),
                'effective_n': self.sw**2/self.sw2,
                'effective_n_selected': self.swa**2/self.sw2a2 if self.sw2a2 else 0.,
                'equal_weights': self.equal_weights}


def sha256(path):
    digest = hashlib.sha256()
    with open(path, 'rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def analyze(path, component, param_card, config, decays=None, seed=None):
    spec = COMPONENTS[component]
    beams = config['beam_setups'][spec['beam']]
    cuts = config['selection']
    if cuts['min_pt_GeV'] != 0 or cuts['min_deltaR'] != 0:
        raise ValueError('This baseline intentionally supports no pT or DeltaR cut')
    if cuts['pairing'] != 'any_valid_disjoint_opposite_charge' or cuts['frame'] != 'laboratory':
        raise ValueError('Unsupported selection convention')
    if cuts['eta_boundary'] != 'strict' or cuts['mass_window_boundary'] != 'inclusive':
        raise ValueError('Unsupported cut boundary')
    if cuts['eta_abs_max'] <= 0 or not 0 < cuts['mass_window_GeV'][0] < cuts['mass_window_GeV'][1]:
        raise ValueError('Invalid fiducial cuts')
    ndecays = int(decays if decays is not None else config['runtime']['decays_per_hh_event'])
    if ndecays < 1:
        raise ValueError('At least one decay trial required')
    seed = int(seed if seed is not None else config['runtime']['seed'])
    rng = random.Random(seed)
    inputs = model_inputs(param_card)
    header = read_init(path)
    if len(header.subprocesses) != 1:
        raise ValueError('Analyze separate one-flavor runs, not an externally merged sample')
    # LHE IDWTUP signs encode event-weight conventions. MG5 may use
    # negative IDWTUP even for entirely positive-weight LO samples.
    # Do not infer negative event weights from the IDWTUP sign: iter_events
    # supplies each central XWGTUP, and WeightedAcceptance.add strictly
    # rejects zero, negative, or nonfinite weights on every event.
    if header.strategy not in (1, 3, 4, -1, -3, -4):
        raise ValueError(
            f'Unsupported LHE weight strategy IDWTUP={header.strategy}; '
            'positive-weight LO analysis only supports +/-1, +/-3, +/-4'
        )
    if tuple(beams['pdgs']) != header.beam_pdgs:
        raise ValueError('LHE init PDGs differ from the configuration')
    if not all(math.isclose(x,y,rel_tol=1.e-7,abs_tol=.001)
               for x,y in zip(header.energies,beams['energies_GeV'])):
        raise ValueError('LHE init energies differ from the configuration')
    stats = WeightedAcceptance()
    histogram = {0:0, 1:0, 2:0}
    minchi_sum = 0.
    total_decay_trials = 0
    reframed = 0
    expected_id = header.subprocesses[0][2]
    for process_id, weight, original_parts in iter_events(path):
        if process_id != expected_id:
            raise ValueError('Event IDPRUP not present in this component init block')
        parts, applied_boost = lab_particles(original_parts, beams['pdgs'], beams['energies_GeV'])
        reframed += abs(applied_boost) > 1.e-7
        final = [p for p in parts if p.status == 1]
        expected_final = sorted(list(spec['neutrino_pdgs']) +
                                ([25,25] if spec['mode']=='signal' else [5,5,-5,-5]))
        if sorted(p.pid for p in final) != expected_final:
            raise ValueError('Unexpected final-state content; use undecayed HH or direct 4b only')
        incoming = [p.p for p in parts if p.status == -1]
        incoming_total = incoming[0]+incoming[1]
        outgoing_total = final[0].p
        for p in final[1:]:
            outgoing_total = outgoing_total+p.p
        if any(abs(getattr(incoming_total,k)-getattr(outgoing_total,k)) > 3.e-5*incoming_total.E
               for k in ('E','x','y','z')):
            raise ValueError('LHE event violates four-momentum conservation')
        trials = ndecays if spec['mode'] == 'signal' else 1
        if spec['mode'] == 'signal':
            hh = [p.p for p in final if p.pid == 25]
            if any(not math.isclose(h.mass, inputs['mh_GeV'], rel_tol=2.e-5) for h in hh):
                raise ValueError('Signal input is not on-shell HH with the param-card mass')
        hits = chi_hits = 0
        for _ in range(trials):
            if spec['mode'] == 'signal':
                b0,a0 = scalar_to_bb(hh[0],rng,inputs['mb_GeV'])
                b1,a1 = scalar_to_bb(hh[1],rng,inputs['mb_GeV'])
                bottoms, antibottoms = [b0,b1],[a0,a1]
            else:
                bottoms = [p.p for p in final if p.pid == 5]
                antibottoms = [p.p for p in final if p.pid == -5]
                if any(not math.isclose(v.mass,inputs['mb_GeV'],rel_tol=.002,abs_tol=.002)
                       for v in bottoms+antibottoms):
                    raise ValueError('LHE bottom masses differ from the massive-b param card')
            passed, nvalid, chi = select(bottoms,antibottoms,cuts['eta_abs_max'],*cuts['mass_window_GeV'])
            histogram[nvalid] += 1
            hits += passed
            chi_hits += chi
        total_decay_trials += trials
        stats.add(weight,hits/trials)
        minchi_sum += weight*chi_hits/trials
    result = stats.result()
    branch_factor = inputs['br_hbb_model']**2 if spec['mode']=='signal' else 1.
    sigma = header.xsec_pb*result['acceptance']*branch_factor
    integration_error = header.error_pb*result['acceptance']*branch_factor
    selection_error = header.xsec_pb*result['acceptance_mc_se']*branch_factor
    warnings = ['Not convergence-validated. Repeat with independent seeds and increased statistics.',
                'Combined MC error below neglects covariance between generator normalization and selection; no theory/systematic errors included.']
    if result['n_events'] < config['runtime']['nevents_per_component']:
        warnings.append('LHE contains fewer production events than requested; check generator completion and statistics.')
    status = 'ESTIMATE_NOT_CONVERGENCE_VALIDATED'
    if result['n_events_with_any_acceptance']==0:
        status = 'NO_SELECTED_EVENTS_NOT_A_ZERO_MEASUREMENT'
        warnings.append('No selected events: primary sigma and uncertainty fields are null, not a measured zero.')
    elif result['effective_n_selected'] < 100:
        status = 'LOW_SELECTED_STATISTICS_NOT_CONVERGENCE_VALIDATED'
    if result['acceptance'] == 1:
        warnings.append('All trials passed; zero empirical selection SE does not prove exactly unit acceptance.')
    if spec['mode']=='signal' and abs(inputs['br_hbb_model']-config['physics_conventions']['reference_br_hbb']) > .01:
        warnings.append('The model-card branching fraction differs from 0.582. The reference normalization is separate and not used for the primary result.')
    null_result = result['n_events_with_any_acceptance']==0
    result.update({
        'component': component, 'group': spec['group'], 'mode': spec['mode'],
        'status': status, 'lhe_file':str(Path(path).resolve()), 'lhe_sha256':sha256(path),
        'param_card_sha256':sha256(param_card), 'beam_setup':beams,
        'sqrt_s_GeV':2*math.sqrt(math.prod(header.energies)),
        'lab_cm_rapidity':.5*math.log(header.energies[0]/header.energies[1]),
        'events_reframed_to_lab':int(reframed), 'model_inputs':inputs, 'selection':cuts,
        'n_decay_trials_per_production_event':trials if stats.n else 0,
        'decay_random_seed':seed, 'pairing_trial_histogram':histogram,
        'total_trials':total_decay_trials,
        'min_mass_distance_acceptance_diagnostic':minchi_sum/stats.sw,
        'lhe_idwtup_strategy':header.strategy,
        'generated_xsec_pb':header.xsec_pb, 'generated_integration_error_pb':header.error_pb,
        'branching_factor_applied':branch_factor,
        'fiducial_point_estimator_pb':sigma,
        'fiducial_xsec_pb':None if null_result else sigma,
        'fiducial_xsec_fb':None if null_result else 1000*sigma,
        'mc_integration_error_fb':None if null_result else 1000*integration_error,
        'mc_selection_error_fb':None if null_result else 1000*selection_error,
        'mc_error_quadrature_approx_fb':None if null_result else 1000*math.hypot(integration_error,selection_error),
        'warnings':warnings})
    if null_result and spec['mode']=='fourb' and result['equal_weights']:
        # Exact one-sided binomial upper bound conditional on generator normalization.
        upper = -math.expm1(math.log(.05)/stats.n)
        result['zero_selected_acceptance_upper_95pct'] = upper
        result['zero_selected_sigma_upper_95pct_fb_conditional'] = 1000*header.xsec_pb*upper
    if spec['mode']=='signal':
        reference = config['physics_conventions']['reference_br_hbb']
        result['reference_only_br_hbb'] = reference
        result['reference_only_sigma_fb'] = 1000*header.xsec_pb*result['acceptance']*reference**2
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('lhe',type=Path)
    p.add_argument('--component',choices=sorted(COMPONENTS),required=True)
    p.add_argument('--param-card',type=Path,required=True)
    p.add_argument('--config',type=Path,default=ROOT/'configuration.json')
    p.add_argument('--decays',type=int)
    p.add_argument('--seed',type=int)
    p.add_argument('--json',type=Path,required=True)
    args=p.parse_args()
    try:
        result=analyze(args.lhe,args.component,args.param_card,json.loads(args.config.read_text()),args.decays,args.seed)
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
        print(f"{result['component']}: {result['status']}")
        print(f"Generated sigma = {result['generated_xsec_pb']:.9g} pb; acceptance = {result['acceptance']:.8g}")
        if result['fiducial_xsec_fb'] is None:
            print('No measured fiducial cross section: zero accepted events. See JSON bounds/warnings.')
        else:
            print(f"Fiducial sigma = {result['fiducial_xsec_fb']:.9g} fb")
            print(f"MC errors [integration, selection] = [{result['mc_integration_error_fb']:.4g}, {result['mc_selection_error_fb']:.4g}] fb")
        for warning in result['warnings']:
            print('CAUTION:',warning)
    except (ValueError,OSError,KeyError) as exc:
        p.exit(2,'ERROR: '+str(exc)+'\n')


if __name__=='__main__':
    main()
