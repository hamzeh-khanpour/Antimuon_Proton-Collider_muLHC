#!/usr/bin/env python3
"""Streaming Les Houches reader; strict truncation/weight/structure checks."""
import gzip
import math
import re
from dataclasses import dataclass
from physics import Particle, P4, fnum


@dataclass(frozen=True)
class Init:
    beam_pdgs: tuple
    energies: tuple
    strategy: int
    subprocesses: tuple  # (cross section pb, error pb, LPRUP)

    @property
    def xsec_pb(self):
        return sum(row[0] for row in self.subprocesses)

    @property
    def error_pb(self):
        return math.sqrt(sum(row[1]**2 for row in self.subprocesses))


def open_lhe(path):
    return gzip.open(path, 'rt') if str(path).endswith('.gz') else open(path, 'rt')


def clean(line):
    return line.split('#', 1)[0].strip()


def read_init(path):
    data = []
    inside = done = False
    with open_lhe(path) as stream:
        for line in stream:
            if re.fullmatch(r'<init(?:\s[^>]*)?>', line.strip()):
                inside = True
                continue
            if inside and line.strip() == '</init>':
                done = True
                break
            if inside:
                text = clean(line)
                if text and not text.startswith('<'):
                    data.append(text.split())
    if not done or len(data) < 2 or len(data[0]) != 10:
        raise ValueError('Missing/truncated LHE init block')
    h = data[0]
    nprocesses = int(h[9])
    if len(data) != nprocesses+1:
        raise ValueError('LHE init subprocess-count mismatch')
    rows = []
    for row in data[1:]:
        if len(row) != 4:
            raise ValueError('Malformed LHE subprocess line')
        cross, err = fnum(row[0]), fnum(row[1])
        if cross <= 0 or err < 0:
            raise ValueError('Need positive cross section and nonnegative integration error')
        rows.append((cross, err, int(row[3])))
    return Init((int(h[0]), int(h[1])), (fnum(h[2]), fnum(h[3])), int(h[8]), tuple(rows))


def iter_events(path):
    inside = False
    head = None
    particles = []
    closed_document = False
    with open_lhe(path) as stream:
        for raw in stream:
            line = raw.strip()
            if re.fullmatch(r'<event(?:\s[^>]*)?>', line):
                if inside:
                    raise ValueError('Nested LHE event')
                inside = True
                head = None
                particles = []
                continue
            if line == '</LesHouchesEvents>':
                closed_document = True
            if line == '</event>':
                if not inside or head is None or len(particles) != head[0]:
                    raise ValueError('Incomplete LHE event')
                inside = False
                yield head[1], head[2], particles
                continue
            if not inside:
                continue
            text = clean(raw)
            if not text or text.startswith('<'):
                continue
            if head is None:
                fields = text.split()
                if len(fields) < 6:
                    raise ValueError('Malformed event header')
                head = (int(fields[0]), int(fields[1]), fnum(fields[2]))
                if head[0] < 2:
                    raise ValueError('Invalid event particle count')
            elif len(particles) < head[0]:
                fields = text.split()
                if len(fields) != 13:
                    raise ValueError('Malformed particle line')
                particles.append(Particle(int(fields[0]), int(fields[1]),
                    P4(fnum(fields[9]), fnum(fields[6]), fnum(fields[7]), fnum(fields[8]))))
            # All remaining lines are optional metadata/reweighting; central weight only.
    if inside:
        raise ValueError('Truncated last LHE event')
    if not closed_document:
        raise ValueError('LHE file has no closing document tag')
