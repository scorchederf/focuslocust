---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nano

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nano` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nano covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nano.md)
- Source verification: [source record](../../sources/gtfobins/nano.md)

## Aliases

- `nano`

## Source Verification

[source record](../../sources/gtfobins/nano.md)

## Evidence Excerpt

```text
_body: ''
_name: nano
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nano
functions:
file-read:
- binary: false
code: nano /path/to/input-file
comment: The file content is displayed in the terminal interface.
```
