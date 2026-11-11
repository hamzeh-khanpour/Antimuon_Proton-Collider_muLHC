#!/usr/bin/env python3
"""Fail-closed MadEvent run-card management, with MG5 v3.6.4 fixture coverage."""
import json
import math
import re
from pathlib import Path


def entry(line):
    core = re.split(r"[!#]", line, maxsplit=1)[0]
    if "=" not in core:
        return None
    value, key = core.split("=", 1)
    key = key.strip().lower()
    if not re.fullmatch(r"[a-z][a-z0-9_]*", key):
        return None
    return key, value.strip()


def parse(text):
    out = {}
    for line in text.splitlines():
        p = entry(line)
        if p:
            if p[0] in out:
                raise ValueError("Duplicate run-card key: " + p[0])
            out[p[0]] = p[1]
    return out


def replace(text, updates):
    seen = set()
    output = []
    for line in text.splitlines(keepends=True):
        p = entry(line)
        if p is None or p[0] not in updates:
            output.append(line)
            continue
        key, _ = p
        if key in seen:
            raise ValueError("duplicate run-card update: " + key)
        seen.add(key)
        ending = '\r\n' if line.endswith('\r\n') else ('\n' if line.endswith('\n') else '')
        body = line.rstrip('\r\n')
        comment_match = re.search(r'([!#].*)$', body)
        comment = (' ' + comment_match.group(1)) if comment_match else ''
        output.append(str(updates[key]) + ' = ' + key + comment + ending)
    if set(updates) != seen:
        raise ValueError('Missing expected run-card keys: ' + str(sorted(set(updates)-seen)))
    return ''.join(output)


# Explicitly remove all common *generation-level* transverse, angular, and
# pair separation cuts. Only update active fields present in actual card.
# The numerical values below preserve MG5's "disabled" convention.
CUTS_ZERO = (
    'ptj','ptb','pta','ptl','misset','ptheavy','xptj','xptb','xpta','xptl',
    'ptj1min','ptj2min','ptj3min','ptj4min',
    'ptl1min','ptl2min','ptl3min','ptl4min',
    'ptllmin','mmjj','mmbb','mmaa','mmll','mmnl','drjj','drbb','drll',
    'draa','drbj','draj','drjl','drab','drbl','dral', 'xetamin',
    'htjmin','ihtmin','ht2min','ht3min','ht4min','xqcut',
    'dsqrt_shat'
)
CUTS_MINUS_ONE = (
    'etaj','etab','etaa','etal','ptjmax','ptbmax','ptamax','ptlmax',
    'missetmax','drjjmax','drbbmax','drllmax','draamax','drbjmax','drajmax',
    'drjlmax','drabmax','drblmax','dralmax',
    'mmjjmax','mmbbmax','mmaamax','mmllmax','mmnlmax',
    'ptllmax','htjmax','ihtmax','ht2max','ht3max','ht4max','dsqrt_shatmax',
    'deltaeta'
)
# Optional extra generator cuts that must be empty if present.
EMPTY_DICTS = ('pt_min_pdg','pt_max_pdg','eta_min_pdg','eta_max_pdg',
               'mxx_min_pdg','e_min_pdg','e_max_pdg')
# Lower bounds: 0 means disabled; smaller than zero is also disabled.
CUTS_ETA_MIN = ('etajmin','etabmin','etaamin','etalmin')
REQUIRED = ('lpp1','lpp2','ebeam1','ebeam2','polbeam1','polbeam2',
            'nevents','iseed')


def desired(ebeam1, ebeam2, pol, nevents, seed, scale=125.0):
    if not (float(ebeam1) > 0 and float(ebeam2) > 0):
        raise ValueError('Invalid beam energies')
    if not (0 <= int(pol) <= 100 and int(pol) % 20 == 0):
        raise ValueError('invalid polarization scan point')
    if not (1 <= int(nevents) <= 1000000 and 1 <= int(seed) < 900000000):
        raise ValueError('invalid events/seed')
    a = {k:'0.0' for k in CUTS_ZERO}
    a.update({k:'-1.0' for k in CUTS_MINUS_ONE})
    a.update({k:'{}' for k in EMPTY_DICTS})
    a.update({k:'0.0' for k in CUTS_ETA_MIN})
    a.update({
        'lpp1':'0','lpp2':'0',
        'ebeam1':str(ebeam1),'ebeam2':str(ebeam2),
        'polbeam1':'0','polbeam2':str(pol),
        'nevents':str(nevents),'iseed':str(seed),
        'pdlabel':'none', 'gridpack':'False', 'cut_decays':'False',
        'ickkw':'0', 'auto_ptj_mjj':'False',
        'fixed_ren_scale':'True','scale':str(scale),
        'use_syst':'False',
    })
    return a


def _equal(a,b):
    a,b = a.strip(),b.strip()
    if a.lower() in ('true','false'):
        return a.lower() == b.lower() or (a.lower()=='true' and b.lower() in ('t','.true.')) or (a.lower()=='false' and b.lower() in ('f','.false.'))
    if a in ('none','{}'):
        return a == b.strip("'\"").lower() if a=='none' else b.replace(' ','') == '{}'
    try:
        return math.isclose(float(a.replace('D','E')),float(b.replace('D','E')),rel_tol=0,abs_tol=1e-9)
    except ValueError:
        return a == b


def configure(path, ebeam1, ebeam2, pol, nevents, seed, scale=125.0):
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    original=path.read_text()
    actual=parse(original)
    if set(REQUIRED)-set(actual):
        raise ValueError('Missing critical run-card fields: '+str(sorted(set(REQUIRED)-set(actual))))
    expected=desired(ebeam1,ebeam2,pol,nevents,seed,scale)
    enabled={k:v for k,v in expected.items() if k in actual}
    new=replace(original,enabled)
    verified=parse(new)
    mismatches={k:(v,verified.get(k)) for k,v in enabled.items() if not _equal(v,verified.get(k,''))}
    if mismatches:
        raise ValueError('Card verification failed: '+str(mismatches))
    path.write_text(new)
    return {'set_values':enabled,
            'optional_absent':sorted(set(expected)-set(enabled)),
            'required_present':list(REQUIRED),
            'ptl_field_present':('ptl' in actual),
            'original_ptl':actual.get('ptl'),
            'new_ptl':verified.get('ptl')}



def inspect_spectrum(param_path):
    text=Path(param_path).read_text()
    block=''
    masses={}
    for line in text.splitlines():
        core=line.split('#')[0].strip()
        if not core:continue
        tokens=core.split()
        if tokens[0].lower()=='block':
            block=tokens[1].lower() if len(tokens)>1 else ''
        elif tokens[0].lower()=='decay':block=''
        elif block=='mass' and len(tokens)>=2 and tokens[0].lstrip('+-').isdigit():
            masses[int(tokens[0])]=float(tokens[1].replace('D','E').replace('d','e'))
    if not (120 < masses.get(25,0) < 130):
        raise ValueError('Higgs mass not found or outside expected range')
    return {'Higgs_mass_GeV':masses[25], 'Z_mass_GeV':masses.get(23)}
