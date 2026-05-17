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

## Summary

GTFOBins entry for pdflatex covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pdflatex.md)
- Source verification: [source record](../../sources/gtfobins/pdflatex.md)

## Aliases

- `pdflatex`

## Source Verification

[source record](../../sources/gtfobins/pdflatex.md)

## Evidence Excerpt

```text
_body: ''
_name: pdflatex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdflatex
functions:
file-read:
- code: 'pdflatex ''\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}''
pdftotext texput.pdf -'
comment: The read file will be part of the PDF output.
```
