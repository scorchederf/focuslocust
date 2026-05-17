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

## Summary

GTFOBins entry for latexmk covering file-read, inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/latexmk.md)
- Source verification: [source record](../../sources/gtfobins/latexmk.md)

## Aliases

- `latexmk`

## Source Verification

[source record](../../sources/gtfobins/latexmk.md)

## Evidence Excerpt

```text
_body: ''
_name: latexmk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latexmk
functions:
file-read:
- binary: false
code: 'echo ''\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}''
>/path/to/temp-file
```
