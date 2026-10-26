"""Offline unit/regression tests. Synthetic fixtures are NOT collider predictions."""
import copy
import gzip
import importlib
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from physics import P4, Particle, pairing_masses, select, scalar_to_bb, lab_particles, model_inputs, parse_slha
from lhe_io import read_init, iter_events
from analyze_lhe import analyze, WeightedAcceptance
from configure_run import neutralize_registered_cuts, settings_for
from processes import COMPONENTS, GROUPS, card_text
from collect_results import collect
from run_workflow import fatal_log, discover_lhe

CONFIG=json.loads((ROOT/'configuration.json').read_text())
PARAM='''BLOCK SMINPUTS
 1 1.325070e2
 2 1.166390d-5
 3 1.180000e-1
BLOCK MASS
 5 4.700000e0
 11 0.
 13 0.
 25 1.250000e2
BLOCK YUKAWA
 5 4.700000e0
DECAY 25 6.38233934e-3
'''


def initial_cm():
    e=math.sqrt(5000*183)
    return [Particle(-13,-1,P4(e,0,0,e)),Particle(11,-1,P4(e,0,0,-e))]


def make_parts(mode='fourb',passed=True,lab=True):
    incoming=initial_cm()
    energy=125/2 if passed else 45.
    if mode=='fourb':
        p=math.sqrt(energy**2-4.7**2)
        final=[Particle(5,1,P4(energy,p,0,0)),Particle(-5,1,P4(energy,-p,0,0)),
               Particle(5,1,P4(energy,0,p,0)),Particle(-5,1,P4(energy,0,-p,0))]
    else:
        eh=math.sqrt(125**2+100**2)
        final=[Particle(25,1,P4(eh,100,0,0)),Particle(25,1,P4(eh,-100,0,0))]
    enu=(2*incoming[0].p.E-sum(p.p.E for p in final))/2
    final += [Particle(12,1,P4(enu,0,0,enu)),Particle(-14,1,P4(enu,0,0,-enu))]
    parts=incoming+final
    if lab:
        boost=.5*math.log(5000/183)
        parts=[Particle(p.pid,p.status,p.p.boost_z(boost)) for p in parts]
    return parts


def write_lhe(path,events,attributes=False,truncated=False,weight=1.,mode='fourb',lab=True):
    text='''<LesHouchesEvents version="3.0">
<header></header>
<init>
 -13 11 5000.0 183.0 0 0 0 0 3 1
 1.000000e-3 1.000000e-5 1.0 1
</init>
'''
    for passed in events:
        parts=make_parts(mode,passed,lab)
        text+='<event sample="synthetic">\n' if attributes else '<event>\n'
        text+=f'{len(parts)} 1 {weight:.12e} 125 0.007 0.118\n'
        for part in parts:
            p=part.p
            mass=p.mass if abs(part.pid) in (5,25) else 0.
            text+=f'{part.pid} {part.status} 0 0 0 0 {p.x:.12e} {p.y:.12e} {p.z:.12e} {p.E:.12e} {mass:.12e} 0 9\n'
        text+='<rwgt>\n<wgt id="unused"> 999 </wgt>\n</rwgt>\n</event>\n'
    text+='</LesHouchesEvents>\n'
    if truncated:
        text=text.rsplit('</event>',1)[0]
    if str(path).endswith('.gz'):
        with gzip.open(path,'wt') as stream:
            stream.write(text)
    else:
        Path(path).write_text(text)


class Kinematics(unittest.TestCase):
    def test_beam_energy_and_boost(self):
        self.assertAlmostEqual(2*math.sqrt(5000*183),1913.112646970899)
        self.assertAlmostEqual(.5*math.log(5000/183),1.6538535192874082)

    def test_eta_definition(self):
        self.assertAlmostEqual(P4(150,20,0,80).eta,math.asinh(4))

    def test_undefined_eta_rejected(self):
        self.assertTrue(math.isinf(P4(4.7,0,0,0).eta))

    def test_strict_eta_boundary(self):
        edge=P4(math.cosh(5),1,0,math.sinh(5))
        self.assertEqual(select([edge,edge],[edge,edge])[0],False)

    def test_rest_scalar_decay(self):
        b,a=scalar_to_bb(P4(125,0,0,0),random.Random(4),4.7)
        self.assertAlmostEqual((b+a).mass,125.)
        self.assertAlmostEqual(b.mass,4.7)

    def test_boosted_decay_conservation(self):
        h=P4(math.sqrt(125**2+200**2),160,0,120).boost_z(1.4)
        b,a=scalar_to_bb(h,random.Random(6),4.7)
        for k in ('E','x','y','z'):
            self.assertAlmostEqual(getattr(b+a,k),getattr(h,k),places=9)

    def test_decay_threshold_fails(self):
        with self.assertRaises(ValueError):
            scalar_to_bb(P4(9.,0,0,0),random.Random(4),4.7)

    def test_boost_roundtrip(self):
        p=P4(70.,30.,20.,50.)
        q=p.boost_z(1.4).boost_z(-1.4)
        for k in ('E','x','y','z'):
            self.assertAlmostEqual(getattr(p,k),getattr(q,k))

    def test_massive_eta_is_not_rapidity(self):
        p=P4(math.sqrt(1.+4.7**2),1.,0.,0.)
        self.assertNotAlmostEqual(p.boost_z(1.4).eta,p.eta+1.4,places=2)

    def test_nonfinite_vector_fails(self):
        with self.assertRaises(ValueError):
            P4(math.nan,1.,0.,0.)

    def test_spacelike_mass_fails(self):
        with self.assertRaises(ValueError):
            _=P4(1,2,0,0).mass

    def test_already_lab_no_double_boost(self):
        _,delta=lab_particles(make_parts(lab=True),[-13,11],[5000,183])
        self.assertAlmostEqual(delta,0.)

    def test_cm_sample_boosted(self):
        parts,delta=lab_particles(make_parts(lab=False),[-13,11],[5000,183])
        self.assertAlmostEqual(delta,.5*math.log(5000/183))
        self.assertAlmostEqual(parts[0].p.E,5000.)
        self.assertAlmostEqual(parts[1].p.E,183.)

    def test_wrong_beams_fail(self):
        with self.assertRaises(ValueError):
            lab_particles(make_parts(),[-13,13],[5000,183])

    def test_wrong_invariant_energy_fails(self):
        with self.assertRaises(ValueError):
            lab_particles(make_parts(),[-13,11],[500,500])


class Pairing(unittest.TestCase):
    def setUp(self):
        self.b=[P4(62.5,62.5,0,0),P4(62.5,0,62.5,0)]
        self.a=[P4(62.5,-62.5,0,0),P4(62.5,0,-62.5,0)]

    def test_direct_pair_only(self):
        result=select(self.b,self.a)
        self.assertEqual(result,(True,1,True))
        self.assertAlmostEqual(pairing_masses(self.b,self.a)[1][0],88.3883476483)

    def test_cross_pair_only(self):
        self.assertTrue(select(self.b,list(reversed(self.a)))[0])
        masses=pairing_masses(self.b,list(reversed(self.a)))
        self.assertAlmostEqual(masses[1][0],125.)

    def test_both_assignments_count_once(self):
        b=[self.b[0],self.b[0]]; a=[self.a[0],self.a[0]]
        passed,nvalid,_=select(b,a)
        self.assertIs(passed,True)
        self.assertEqual(nvalid,2)
        self.assertEqual(int(passed),1)

    def test_reusing_one_bottom_is_forbidden(self):
        b=[self.b[0],P4(1,1,0,0)];a=[self.a[0],self.a[0]]
        self.assertFalse(select(b,a)[0])

    def test_same_charge_pairing_is_not_used(self):
        b=[self.b[0],self.a[0]];a=[self.b[1],self.a[1]]
        self.assertAlmostEqual((b[0]+b[1]).mass,125.)
        self.assertFalse(select(b,a)[0])

    def test_permutation_invariance(self):
        for b in (self.b,list(reversed(self.b))):
            for a in (self.a,list(reversed(self.a))):
                self.assertTrue(select(b,a)[0])

    def test_inclusive_mass_window_boundaries(self):
        b=[P4(55,55,0,0),P4(65,0,65,0)]
        a=[P4(55,-55,0,0),P4(65,0,-65,0)]
        self.assertTrue(select(b,a)[0])

    def test_bad_multiplicity_fails(self):
        with self.assertRaises(ValueError):
            select(self.b[:1],self.a)

    def test_any_valid_not_always_minchi(self):
        # Algebraic selection counterexample: (110,110) is inside, (125,130.1) not.
        # The second has smaller squared distance, so 'best first' can reject.
        distances=[(110-125)**2+(110-125)**2,(125-125)**2+(130.1-125)**2]
        self.assertLess(distances[1],distances[0])
        self.assertTrue(110<=110<=130)
        self.assertFalse(110<=130.1<=130)


class InputsAndCards(unittest.TestCase):
    def test_model_consistent_branching(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'param.dat';p.write_text(PARAM)
            inputs=model_inputs(p)
            self.assertAlmostEqual(inputs['br_hbb_model'],.8446399777362876)
            self.assertNotAlmostEqual(inputs['br_hbb_model'],.582)

    def test_massless_b_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'param.dat';p.write_text(PARAM.replace('5 4.700000e0','5 0.0'))
            with self.assertRaises(ValueError):
                model_inputs(p)

    def test_inconsistent_higgs_width_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'param.dat';p.write_text(PARAM.replace('6.38233934e-3','1e-3'))
            with self.assertRaises(ValueError):
                model_inputs(p)

    def test_fortran_exponents(self):
        self.assertAlmostEqual(parse_slha(PARAM)['sminputs',2],1.16639e-5)

    def test_four_totals_eight_components(self):
        self.assertEqual(len(GROUPS),4)
        self.assertEqual(len(COMPONENTS),8)
        self.assertEqual(sum(s['group']=='mumu_4b' for s in COMPONENTS.values()),3)

    def test_no_exclusion_or_destructive_output(self):
        for name in COMPONENTS:
            text=card_text(name)
            self.assertNotIn(' -f',text)
            self.assertNotIn('/ h',text)
            self.assertNotIn('$ h',text)
        self.assertIn('QCD=2 QED=6',card_text('mue_4b'))

    def test_beam_cuts_settings(self):
        s=settings_for(CONFIG,'mue_4b',1000,42)
        self.assertEqual((s['ebeam1'],s['ebeam2']),(5000,183))
        for key in ('ptb','ptj','drbb','drjj','mmbb','mmjj','misset'):
            self.assertEqual(s[key],0.)
        self.assertEqual(s['etab'],-1.)
        self.assertEqual(s['polbeam1'],0.)

    def test_mumu_energy_is_not_reset_to_match_mue(self):
        s=settings_for(CONFIG,'mumu_HH_mu',1000,42)
        self.assertEqual((s['ebeam1'],s['ebeam2']),(1000,1000))

    def test_hidden_cuts_neutralized(self):
        class Card(dict):
            pass
        card=Card(ptb=20.,ptbmax=300.,etab=2.5,etabmin=.5,cut_decays=True,
                  pt_min_pdg={25:200.},ihtmin=100.,drbb=.4,mmnl=20.)
        card.cuts_parameter={key:True for key in card}
        neutralize_registered_cuts(card)
        self.assertEqual(card['ptb'],0.)
        self.assertEqual(card['ptbmax'],-1.)
        self.assertEqual(card['etab'],-1.)
        self.assertEqual(card['etabmin'],0.)
        self.assertFalse(card['cut_decays'])
        self.assertEqual(card['pt_min_pdg'],{})
        self.assertEqual(card['ihtmin'],0.)
        self.assertEqual(card['drbb'],0.)
        self.assertEqual(card['mmnl'],0.)


class Statistics(unittest.TestCase):
    def test_equal_weight_acceptance_and_se(self):
        s=WeightedAcceptance()
        for a in (1,0,1,0):s.add(1,a)
        r=s.result()
        self.assertAlmostEqual(r['acceptance'],.5)
        self.assertAlmostEqual(r['acceptance_mc_se'],math.sqrt(1/12))

    def test_weight_scale_invariance(self):
        a=WeightedAcceptance();b=WeightedAcceptance()
        for w,f in ((2.,.2),(3.,.8),(1.,1.)):
            a.add(w,f);b.add(w*1.e-12,f)
        self.assertAlmostEqual(a.result()['acceptance'],b.result()['acceptance'])
        self.assertAlmostEqual(a.result()['acceptance_mc_se'],b.result()['acceptance_mc_se'])

    def test_decay_trials_clustered_by_production_event(self):
        s=WeightedAcceptance();s.add(1,.25);s.add(1,.75)
        r=s.result()
        self.assertEqual(r['n_events'],2)
        self.assertEqual(r['effective_n'],2)
        self.assertAlmostEqual(r['acceptance_mc_se'],.25)

    def test_negative_weight_rejected(self):
        with self.assertRaises(ValueError):WeightedAcceptance().add(-1,1)

    def test_too_few_events_fail(self):
        s=WeightedAcceptance();s.add(1,1)
        with self.assertRaises(ValueError):s.result()


class LHEAndAnalysis(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.param=self.root/'param.dat';self.param.write_text(PARAM)
    def tearDown(self):self.tmp.cleanup()

    def test_plain_and_gzip_and_event_attributes(self):
        for name in ('events.lhe','events.lhe.gz'):
            path=self.root/name;write_lhe(path,[True,False],attributes=True)
            self.assertAlmostEqual(read_init(path).xsec_pb,.001)
            self.assertEqual(len(list(iter_events(path))),2)

    def test_truncated_event_rejected(self):
        path=self.root/'events.lhe';write_lhe(path,[True,False],truncated=True)
        with self.assertRaises(ValueError):list(iter_events(path))

    def test_missing_document_close_rejected(self):
        path=self.root/'events.lhe';write_lhe(path,[True,False])
        path.write_text(path.read_text().replace('</LesHouchesEvents>',''))
        with self.assertRaises(ValueError):list(iter_events(path))

    def test_fourb_sigma_no_extra_branching(self):
        path=self.root/'events.lhe';write_lhe(path,[True,False,True,False])
        result=analyze(path,'mue_4b',self.param,CONFIG)
        self.assertAlmostEqual(result['acceptance'],.5)
        self.assertAlmostEqual(result['fiducial_xsec_fb'],.5)
        self.assertEqual(result['branching_factor_applied'],1.)
        self.assertEqual(result['events_reframed_to_lab'],0)

    def test_cm_and_lab_results_identical(self):
        a=self.root/'a.lhe';b=self.root/'b.lhe'
        write_lhe(a,[True,False,True,False],lab=False)
        write_lhe(b,[True,False,True,False],lab=True)
        ra=analyze(a,'mue_4b',self.param,CONFIG)
        rb=analyze(b,'mue_4b',self.param,CONFIG)
        self.assertEqual(ra['fiducial_xsec_fb'],rb['fiducial_xsec_fb'])
        self.assertEqual(ra['events_reframed_to_lab'],4)

    def test_zero_selected_not_measured_zero(self):
        path=self.root/'events.lhe';write_lhe(path,[False]*4)
        result=analyze(path,'mue_4b',self.param,CONFIG)
        self.assertIsNone(result['fiducial_xsec_fb'])
        self.assertEqual(result['fiducial_point_estimator_pb'],0.)
        self.assertGreater(result['zero_selected_acceptance_upper_95pct'],0.)

    def test_signal_branching_applied_once(self):
        path=self.root/'events.lhe';write_lhe(path,[True]*4,mode='signal')
        result=analyze(path,'mue_HH',self.param,CONFIG,decays=30)
        branch=model_inputs(self.param)['br_hbb_model']
        self.assertAlmostEqual(result['branching_factor_applied'],branch**2)
        self.assertAlmostEqual(result['fiducial_xsec_fb'],result['acceptance']*branch**2)
        self.assertEqual(result['n_events'],4)
        self.assertEqual(result['total_trials'],120)

    def test_wrong_mode_fails(self):
        path=self.root/'events.lhe';write_lhe(path,[True]*2)
        with self.assertRaises(ValueError):analyze(path,'mue_HH',self.param,CONFIG)

    def test_mismatched_header_fails(self):
        path=self.root/'events.lhe';write_lhe(path,[True]*2)
        path.write_text(path.read_text().replace('5000.0 183.0','500.0 500.0'))
        with self.assertRaises(ValueError):analyze(path,'mue_4b',self.param,CONFIG)

    def test_extra_pt_cut_refused(self):
        path=self.root/'events.lhe';write_lhe(path,[True]*2)
        c=copy.deepcopy(CONFIG);c['selection']['min_pt_GeV']=20
        with self.assertRaises(ValueError):analyze(path,'mue_4b',self.param,c)

    def test_cli_end_to_end_synthetic_only(self):
        path=self.root/'events.lhe';write_lhe(path,[True,False]*3)
        output=self.root/'report.json'
        proc=subprocess.run([sys.executable,str(ROOT/'analyze_lhe.py'),str(path),'--component','mue_4b',
                             '--param-card',str(self.param),'--json',str(output)],capture_output=True,text=True)
        self.assertEqual(proc.returncode,0,proc.stderr)
        self.assertAlmostEqual(json.loads(output.read_text())['fiducial_xsec_fb'],.5)


class Workflow(unittest.TestCase):
    def test_swallowed_error_is_detected(self):
        self.assertTrue(fatal_log('Error detected in "output test"\n'))
        self.assertTrue(fatal_log('Traceback (most recent call last):\n'))
        self.assertTrue(fatal_log('ERROR: Failed to compile\n'))
        self.assertFalse(fatal_log('Cross section and MC errors reported\n'))

    def test_ambiguous_event_outputs_fail(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            for tag in ('run_01','run_02'):
                p=root/'Events'/tag/'unweighted_events.lhe';p.parent.mkdir(parents=True);p.write_text('fixture')
            with self.assertRaises(RuntimeError):discover_lhe(root)

    def test_unrun_rows_are_blank_not_zero(self):
        with tempfile.TemporaryDirectory() as td:
            rows=collect(td)
            self.assertEqual(len(rows),4)
            self.assertTrue(all(r['sigma_fb'] is None and r['status']=='NOT_RUN' for r in rows))

    def test_partial_flavor_sum_not_reported(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);(root/'reports').mkdir()
            p=root/'param.dat';p.write_text(PARAM)
            fake={'component':'mumu_4b_mu','selection':CONFIG['selection'],'model_inputs':model_inputs(p)}
            (root/'reports'/'mumu_4b_mu.json').write_text(json.dumps(fake))
            rows=collect(root)
            row=next(r for r in rows if r['process']=='mumu_4b')
            self.assertEqual(row['status'],'INCOMPLETE')
            self.assertIsNone(row['sigma_fb'])

    def test_independent_flavors_sum_in_quadrature(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);(root/'reports').mkdir()
            p=root/'param.dat';p.write_text(PARAM)
            for name,spec in COMPONENTS.items():
                if spec['group']!='mumu_4b':continue
                fake={'component':name,'selection':CONFIG['selection'],'model_inputs':model_inputs(p),
                      'fiducial_xsec_fb':1.,'mc_integration_error_fb':.1,'mc_selection_error_fb':.2,
                      'mc_error_quadrature_approx_fb':math.hypot(.1,.2),'status':'ESTIMATE_NOT_CONVERGENCE_VALIDATED'}
                (root/'reports'/(name+'.json')).write_text(json.dumps(fake))
            row=next(r for r in collect(root) if r['process']=='mumu_4b')
            self.assertEqual(row['sigma_fb'],3.)
            self.assertAlmostEqual(row['mc_integration_error_fb'],math.sqrt(3)*.1)
            self.assertAlmostEqual(row['mc_selection_error_fb'],math.sqrt(3)*.2)

    def test_no_mg_path_fails_cleanly(self):
        proc=subprocess.run([sys.executable,str(ROOT/'run_workflow.py'),'--mg5','/definitely/no/bin/mg5_aMC'],
                            capture_output=True,text=True)
        self.assertNotEqual(proc.returncode,0)
        self.assertIn('complete local installation',proc.stderr)


    def test_full_workflow_with_explicit_offline_mock(self):
        """Mock MG process creation/adapter/launch/analysis/collection; NOT physics."""
        with tempfile.TemporaryDirectory() as td:
            root=Path(td);mgroot=root/'mock_mg';(mgroot/'bin').mkdir(parents=True)
            (mgroot/'madgraph'/'various').mkdir(parents=True)
            (mgroot/'madgraph'/'__init__.py').write_text('')
            (mgroot/'madgraph'/'various'/'__init__.py').write_text('')
            (mgroot/'VERSION').write_text('OFFLINE_MOCK_NOT_MADGRAPH')
            banner="""import json
from pathlib import Path
class RunCardLO(dict):
    def __init__(self,path):
        super().__init__(json.loads(Path(path).read_text()))
        self.cuts_parameter={k:True for k in ('ptb','ptj','ptheavy','drbb','drjj','etab','etaj','mmbb','mmbbmax','mmjj','mmjjmax','cut_decays','misset')}
    def write(self,path,write_hidden=False):
        Path(path).write_text(json.dumps(self))
"""
            (mgroot/'madgraph'/'various'/'banner.py').write_text(banner)
            fixture=root/'synthetic_only.lhe';write_lhe(fixture,[True,False]*3)
            baseline=settings_for(CONFIG,'mue_4b',6,42)
            baseline.update(ptb=20.,ptj=20.,drbb=.4,etab=2.5)
            generate="""import shutil
from pathlib import Path
p=Path.cwd()/'Events'/'run_01'
p.mkdir(parents=True)
shutil.copyfile(FIXTURE,p/'unweighted_events.lhe')
print('OFFLINE MOCK: copied synthetic fixture, no matrix element evaluated')
""".replace('FIXTURE',repr(str(fixture)))
            mgscript="""import json,sys
from pathlib import Path
text=Path(sys.argv[1]).read_text()
name=next(line.split()[1] for line in text.splitlines() if line.startswith('output '))
p=Path.cwd()/name
for sub in ('Cards','bin','SubProcesses'):(p/sub).mkdir(parents=True,exist_ok=True)
(p/'Cards'/'param_card.dat').write_text(PARAM)
(p/'Cards'/'run_card.dat').write_text(json.dumps(BASELINE))
(p/'Cards'/'pythia8_card.dat').write_text('SHOULD BE DISABLED')
(p/'bin'/'generate_events').write_text(GENERATE)
print('OFFLINE MOCK: created synthetic process skeleton, no MadGraph source generated')
""".replace('PARAM',repr(PARAM)).replace('BASELINE',repr(baseline)).replace('GENERATE',repr(generate))
            mg=mgroot/'bin'/'mg5_aMC';mg.write_text(mgscript)
            work=root/'new_run'
            proc=subprocess.run([sys.executable,str(ROOT/'run_workflow.py'),'--mg5',str(mg),
                                 '--only','mue_4b','--work',str(work),'--nevents','6'],
                                capture_output=True,text=True)
            self.assertEqual(proc.returncode,0,proc.stdout+proc.stderr)
            rows=json.loads((work/'results.json').read_text())
            row=next(r for r in rows if r['process']=='mue_4b')
            self.assertAlmostEqual(row['sigma_fb'],.5)
            audit=json.loads((work/'mue_4b'/'configuration_audit.json').read_text())
            self.assertEqual(audit['settings']['ptb'],0.)
            self.assertEqual(audit['settings']['etab'],-1.)
            self.assertIn('pythia8_card.dat',audit['secondary_stage_cards_disabled'])
            self.assertFalse((work/'mue_4b'/'Cards'/'pythia8_card.dat').exists())
            self.assertEqual(json.loads((work/'manifest.json').read_text())['overall_status'],
                             'FINISHED_NOT_CONVERGENCE_VALIDATED')
            repeated=subprocess.run([sys.executable,str(ROOT/'run_workflow.py'),'--mg5',str(mg),
                                     '--only','mue_4b','--work',str(work)],capture_output=True,text=True)
            self.assertNotEqual(repeated.returncode,0)
            self.assertIn('already exists',repeated.stderr)


if __name__=='__main__':unittest.main()
