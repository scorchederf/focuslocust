---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ip covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ip.md)
- Source verification: [source record](../../sources/gtfobins/ip.md)

## Aliases

- `ip`

## Source Verification

[source record](../../sources/gtfobins/ip.md)

## Evidence Excerpt

```text
_body: ''
_name: ip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ip
functions:
file-read:
- binary: false
code: ip -force -batch /path/to/input-file
comment: The read file content is corrupted by error prints.
```
