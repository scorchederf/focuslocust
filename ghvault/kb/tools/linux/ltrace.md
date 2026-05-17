---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ltrace

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ltrace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ltrace covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ltrace.md)
- Source verification: [source record](../../sources/gtfobins/ltrace.md)

## Aliases

- `ltrace`

## Source Verification

[source record](../../sources/gtfobins/ltrace.md)

## Evidence Excerpt

```text
_body: ''
_name: ltrace
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ltrace
functions:
file-read:
- binary: false
code: ltrace -F /path/to/input-file /dev/null
comment: The file is parsed as a configuration file and its content is shown as error messages.
```
