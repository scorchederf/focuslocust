---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# atobm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `atobm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/atobm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for atobm covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/atobm.md)
- Source verification: [source record](../../sources/gtfobins/atobm.md)

## Aliases

- `atobm`

## Source Verification

[source record](../../sources/gtfobins/atobm.md)

## Evidence Excerpt

```text
_body: ''
_name: atobm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/atobm
functions:
file-read:
- code: atobm /path/to/input-file
comment: Outputs only the first line of the file to standard error without the `-` and `#` characters, this can be customized
with the `-c` option, by default is `-c -#`. Content can be retrieved with `awk -F "'" '{printf "%s", $2}'`.
```
