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

## Summary

GTFOBins entry for latex covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/latex.md)
- Source verification: [source record](../../sources/gtfobins/latex.md)

## Aliases

- `latex`

## Source Verification

[source record](../../sources/gtfobins/latex.md)

## Evidence Excerpt

```text
_body: ''
_name: latex
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latex
functions:
file-read:
- code: 'latex ''\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}''
strings texput.dvi'
comment: The read file will be part of the PDF output.
```
