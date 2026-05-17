---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# script

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `script` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/script` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for script covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/script.md)
- Source verification: [source record](../../sources/gtfobins/script.md)

## Aliases

- `script`

## Source Verification

[source record](../../sources/gtfobins/script.md)

## Evidence Excerpt

```text
_body: ''
_name: script
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/script
functions:
file-write:
- binary: false
code: script -q -c '# DATA' /path/to/output-file
comment: The content appears among the log prints.
```
