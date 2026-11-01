% hep-links-unsrt.bst -- compact HEP bibliography with linked journals, DOI and arXiv.
% Custom minimal numeric BibTeX style for research manuscripts, based on BibTeX postfix API.
% Maintains citation order, normal numerical labels, and standard \cite compatibility.
ENTRY
 { author title journal volume number pages year doi eprint archivePrefix primaryClass
   booktitle editor note url organization publisher school address howpublished type }
 {} { }
STRINGS { s t }
INTEGERS { nameptr namesleft numnames }
FUNCTION {format.names}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
  { namesleft #0 > }
  { s nameptr "{f.~}{vv~}{ll}{, jj}" format.name$ 't :=
    nameptr #1 >
      { namesleft #1 >
          { ", " * t * }
          { t "others" =
              { " et~al." * }
              { " and " * t * }
            if$
          }
        if$
      }
      { t }
    if$
    nameptr #1 + 'nameptr :=
    namesleft #1 - 'namesleft :=
  }
  while$
}
FUNCTION {format.authors}
{ author empty$ { "" } { author format.names } if$ }
FUNCTION {start.entry}
{ newline$
  "\bibitem{" cite$ * "}" * write$ newline$
}
FUNCTION {hep.entry}
{ start.entry
  format.authors 's :=
  s empty$ 'skip$ { s write$ ", " write$ } if$
  title empty$ 'skip$
    { "{\enquotehep{" write$ title write$ "}}, " write$ }
  if$
  journal empty$
    { year empty$ 'skip$ { "(" write$ year write$ ")" write$ } if$ }
    {
      doi empty$ 'skip$
        { "\href{https://doi.org/" doi * "}{" * write$ }
      if$
      "{\em " journal * "}" * write$
      volume empty$ 'skip$ { " \textbf{" write$ volume write$ "}" write$ } if$
      pages empty$ 'skip$ { ", " write$ pages write$ } if$
      year empty$ 'skip$ { " (" write$ year write$ ")" write$ } if$
      doi empty$ 'skip$ { "}" write$ } if$
    }
  if$
  "." write$
  doi empty$ 'skip$
    { " \href{https://doi.org/" doi * "}{doi:\nolinkurl{" * doi * "}}" * write$ }
  if$
  eprint empty$ 'skip$
    {
      " \href{https://arxiv.org/abs/" eprint * "}{arXiv:" * eprint * write$
      primaryClass empty$ 'skip$ { " [" primaryClass * "]" * write$ } if$
      "}" write$
    }
  if$
  newline$
}
FUNCTION {article} { hep.entry }
FUNCTION {misc} { hep.entry }
FUNCTION {book} { hep.entry }
FUNCTION {inproceedings} { hep.entry }
FUNCTION {techreport} { hep.entry }
FUNCTION {default.type} { hep.entry }
READ
FUNCTION {begin.bib}
{ "\begin{thebibliography}{99}" write$ newline$
  "\small" write$ newline$
  "\providecommand{\enquotehep}[1]{``#1''}" write$ newline$
}
EXECUTE {begin.bib}
ITERATE {call.type$}
FUNCTION {end.bib}
{ newline$ "\end{thebibliography}" write$ newline$ }
EXECUTE {end.bib}
