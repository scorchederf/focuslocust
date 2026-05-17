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

## Generated Concept Page

- [check_ssl_cert](../../tools/linux/check-ssl-cert.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-ssl-cert |
| name | check_ssl_cert |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-ssl-cert/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_ssl_cert
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_ssl_cert
comment: This is the `check_ssl_cert` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  shell:
  - code: 'echo ''exec /bin/sh 0<&2 1>&2'' >/path/to/temp-file

      chmod +x /path/to/temp-file

      check_ssl_cert --grep-bin /path/to/temp-file -H x'
    comment: The shell will be invoked multiple times.
    contexts:
      sudo: null
      unprivileged: null
```
