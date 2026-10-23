"""Eight flavor-resolved integrations produce four requested totals."""
from pathlib import Path

GROUPS = ('mue_HH', 'mue_4b', 'mumu_HH', 'mumu_4b')
COMPONENTS = {}
for group in GROUPS:
    beam = 'mue' if group.startswith('mue_') else 'mumu'
    mode = 'signal' if group.endswith('_HH') else 'fourb'
    flavors = [('mixed', 've vm~', (12, -14))] if beam == 'mue' else [
        ('e', 've ve~', (12, -12)), ('mu', 'vm vm~', (14, -14)), ('tau', 'vt vt~', (16, -16))]
    for flavor, neutrinos, pdgs in flavors:
        name = group if beam == 'mue' else group+'_'+flavor
        incoming = 'mu+ e-' if beam == 'mue' else 'mu+ mu-'
        final = 'h h QCD=0 QED=4' if mode == 'signal' else 'b b~ b b~ QCD=2 QED=6'
        COMPONENTS[name] = dict(group=group, beam=beam, mode=mode,
            neutrino_pdgs=pdgs, process=f'{incoming} > {neutrinos} {final}')


def card_text(name):
    component = COMPONENTS[name]
    # Explicit non-grouping avoids beam-mirror/grouping ambiguity in asymmetric beams.
    # '=' means amplitude-order upper bound, not exact order equality ('==').
    return '\n'.join([
        '# No HH diagram removal or resonant restriction in the four-bottom amplitude.',
        'set automatic_html_opening False',
        'set group_subprocesses False',
        'import model sm',
        'generate '+component['process'],
        'output '+name,  # No -f: refuse overwriting an existing process directory.
        'quit', ''])


def write_cards(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    for name in COMPONENTS:
        (folder/(name+'.mg5')).write_text(card_text(name))


if __name__ == '__main__':
    write_cards(Path(__file__).parent/'cards')
