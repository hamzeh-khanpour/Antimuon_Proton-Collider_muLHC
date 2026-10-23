#!/usr/bin/env python3
"""Pure-Python kinematics, explicit pairing, beam checks, and SLHA inputs.
No numerical prediction is hard-coded. Units: GeV, cross sections elsewhere pb.
"""
from dataclasses import dataclass
import math
from pathlib import Path


def fnum(text):
    x = float(str(text).replace('D', 'E').replace('d', 'e'))
    if not math.isfinite(x):
        raise ValueError('Non-finite numerical input')
    return x


@dataclass(frozen=True)
class P4:
    E: float
    x: float
    y: float
    z: float

    def __post_init__(self):
        if not all(math.isfinite(v) for v in (self.E, self.x, self.y, self.z)):
            raise ValueError('Non-finite four-vector')
        if self.E < 0:
            raise ValueError('Negative particle energy')

    def __add__(self, other):
        return P4(self.E + other.E, self.x + other.x,
                  self.y + other.y, self.z + other.z)

    @property
    def mass2(self):
        return self.E**2 - self.x**2 - self.y**2 - self.z**2

    @property
    def mass(self):
        m2 = self.mass2
        if m2 < -1.e-7 * max(1., self.E**2):
            raise ValueError('Spacelike particle or pair in LHE kinematics')
        return math.sqrt(max(0., m2))

    @property
    def pt(self):
        return math.hypot(self.x, self.y)

    @property
    def eta(self):
        # Undefined for a zero spatial momentum; reject this measure-zero point.
        if self.pt == 0:
            return math.copysign(math.inf, self.z if self.z else 1.)
        return math.asinh(self.z / self.pt)

    def boost_z(self, rapidity):
        c, s = math.cosh(rapidity), math.sinh(rapidity)
        return P4(c*self.E + s*self.z, self.x, self.y,
                  s*self.E + c*self.z)


@dataclass(frozen=True)
class Particle:
    pid: int
    status: int
    p: P4


def pairing_masses(bottoms, antibottoms):
    if len(bottoms) != 2 or len(antibottoms) != 2:
        raise ValueError('Exactly two b and two bbar required')
    return (((bottoms[0]+antibottoms[0]).mass,
             (bottoms[1]+antibottoms[1]).mass),
            ((bottoms[0]+antibottoms[1]).mass,
             (bottoms[1]+antibottoms[0]).mass))


def select(bottoms, antibottoms, eta_max=5., mass_min=110., mass_max=130.):
    """Return (pass, number of passing pairings, best-mass-distance diagnostic).
    BOTH pairs must pass in at least one disjoint opposite-charge partition.
    The minimum-distance diagnostic never changes the primary selection.
    """
    if len(bottoms) != 2 or len(antibottoms) != 2:
        raise ValueError('Exactly two b and two bbar required')
    if any(abs(v.eta) >= eta_max for v in list(bottoms)+list(antibottoms)):
        return False, 0, False
    assignments = pairing_masses(bottoms, antibottoms)
    flags = [all(mass_min <= m <= mass_max for m in pair)
             for pair in assignments]
    n_valid = sum(flags)
    best = min(range(2), key=lambda i: sum((m-125.)**2 for m in assignments[i]))
    return n_valid > 0, n_valid, flags[best]


def scalar_to_bb(parent, rng, mb):
    """Isotropic two-body decay of a spin-zero on-shell scalar, then boost.
    The returned pair has exactly the parent's total four-momentum.
    """
    m = parent.mass
    if mb <= 0 or m <= 2*mb:
        raise ValueError('Need positive mb and mH > 2 mb')
    e = m/2.
    magnitude = math.sqrt(e*e - mb*mb)
    c = 2*rng.random()-1.
    s = math.sqrt(max(0., 1-c*c))
    phi = 2*math.pi*rng.random()
    v = (magnitude*s*math.cos(phi), magnitude*s*math.sin(phi), magnitude*c)
    spatial = (parent.x, parent.y, parent.z)
    norm = math.sqrt(sum(k*k for k in spatial))
    gamma = parent.E/m
    beta = norm/parent.E
    unit = tuple(k/norm for k in spatial) if norm else (0., 0., 1.)

    def boost(vec):
        parallel = sum(vec[i]*unit[i] for i in range(3))
        factor = (gamma-1.)*parallel + gamma*beta*e
        return P4(gamma*(e+beta*parallel),
                  *(vec[i]+factor*unit[i] for i in range(3)))
    return boost(v), boost(tuple(-k for k in v))


def lab_particles(particles, beam_pdgs, energies):
    """Verify incoming beams and transform to the requested laboratory.
    Incoming momenta diagnose the frame; no unverified/double boost is applied.
    Valid for monochromatic, effectively massless, collinear incoming leptons.
    """
    incoming = [p for p in particles if p.status == -1]
    if len(incoming) != 2:
        raise ValueError('Exactly two incoming particles required')
    positive = [p for p in incoming if p.p.z > 0]
    negative = [p for p in incoming if p.p.z < 0]
    if len(positive) != 1 or len(negative) != 1:
        raise ValueError('Incoming particles must be oppositely directed along z')
    ordered = [positive[0], negative[0]]
    if [p.pid for p in ordered] != list(beam_pdgs):
        raise ValueError('Incoming PDGs/orientation do not match the baseline')
    total = incoming[0].p + incoming[1].p
    expected_s = 4*energies[0]*energies[1]
    if not math.isclose(total.mass2, expected_s, rel_tol=3.e-6, abs_tol=.02):
        raise ValueError('Event invariant energy differs from configured beams; ISR not supported')
    if any(p.p.pt > 1.e-5 or abs(p.p.mass2) > 1.e-5*p.p.E**2 for p in incoming):
        raise ValueError('Incoming beams are not massless collinear leptons')
    y_event = math.atanh(total.z/total.E)
    y_target = .5*math.log(energies[0]/energies[1])
    delta = y_target-y_event
    transformed = [Particle(p.pid, p.status, p.p.boost_z(delta)) for p in particles]
    for p, energy in zip(ordered, energies):
        if not math.isclose(p.p.boost_z(delta).E, energy, rel_tol=3.e-6, abs_tol=.002):
            raise ValueError('Post-boost beam-energy check failed')
    return transformed, delta


def parse_slha(text):
    values = {}
    block = None
    for line in text.splitlines():
        words = line.split('#', 1)[0].split()
        if not words:
            continue
        if words[0].lower() == 'block':
            block = words[1].lower()
        elif words[0].lower() == 'decay':
            values[('decay', int(words[1]))] = fnum(words[2])
            block = None
        elif block and len(words) == 2:
            try:
                index = int(words[0])
            except ValueError:
                continue
            values[(block, index)] = fnum(words[1])
    return values


def model_inputs(card):
    values = parse_slha(Path(card).read_text())
    required = [('mass', 5), ('mass', 25), ('yukawa', 5),
                ('sminputs', 2), ('decay', 25)]
    missing = [k for k in required if k not in values]
    if missing:
        raise ValueError('Missing SM inputs: '+repr(missing))
    mb, mh = values['mass', 5], values['mass', 25]
    ymb, gf, gh = values['yukawa', 5], values['sminputs', 2], values['decay', 25]
    if min(mb, ymb, gf, gh) <= 0 or mh <= 2*mb:
        raise ValueError('Invalid mass/Yukawa/width inputs; massive b required')
    # sm UFO: yb=sqrt(2)*ymb/v; v^2=1/(sqrt(2)*GF).
    partial = 3*gf*ymb**2*mh/(4*math.pi*math.sqrt(2))*(1-4*mb*mb/(mh*mh))**1.5
    br = partial/gh
    if not 0 < br <= 1:
        raise ValueError('Inconsistent Higgs inputs: Gamma(H->bb) exceeds total width')
    return {'mb_GeV': mb, 'mh_GeV': mh, 'ymb_GeV': ymb, 'GF_GeV_minus2': gf,
            'higgs_width_GeV': gh, 'hbb_partial_width_LO_GeV': partial,
            'br_hbb_model': br,
            'all_slha_inputs': {f'{b}:{i}': v for (b, i), v in values.items()}}
