---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_ssl_cert

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-ssl-cert` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_ssl_cert` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_ssl_cert covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-ssl-cert.md)
- Source verification: [source record](../../sources/gtfobins/check-ssl-cert.md)

## Aliases

- `check-ssl-cert`
- `check_ssl_cert`

## Source Verification

[source record](../../sources/gtfobins/check-ssl-cert.md)

## Evidence Excerpt

```text
_body: ''
_name: check_ssl_cert
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_ssl_cert
comment: This is the `check_ssl_cert` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
shell:
- code: 'echo ''exec /bin/sh 0<&2 1>&2'' >/path/to/temp-file
chmod +x /path/to/temp-file
```
