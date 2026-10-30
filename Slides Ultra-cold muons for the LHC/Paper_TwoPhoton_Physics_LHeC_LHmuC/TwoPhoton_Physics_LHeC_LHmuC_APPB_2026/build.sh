#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
base=TwoPhoton_Physics_LHeC_LHmuC
pdflatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
if command -v bibtex >/dev/null 2>&1; then
  bibtex "$base" >/dev/null
elif command -v bibtex.original >/dev/null 2>&1; then
  bibtex.original "$base" >/dev/null
else
  echo "ERROR: install BibTeX to resolve the references" >&2
  exit 1
fi
pdflatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
pdflatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null
pages=$(pdfinfo "$base.pdf" | awk '/^Pages:/{print $2}')
echo "Compiled $base.pdf: $pages page(s)."
if [[ "$pages" != 8 ]]; then echo 'ERROR: expected exactly 8 pages' >&2; exit 1; fi
if grep -Eq 'Citation.*undefined|Reference.*undefined|Overfull \\hbox' "$base.log"; then echo 'ERROR: unresolved citations/references or overfull text' >&2; exit 1; fi
