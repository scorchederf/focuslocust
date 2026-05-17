---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dnsmasq

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dnsmasq` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dnsmasq` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [dnsmasq](../../tools/linux/dnsmasq.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dnsmasq |
| name | dnsmasq |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/dnsmasq/ |

## Preserved Source Material

```yaml
_body: ''
_name: dnsmasq
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dnsmasq
functions:
  command:
  - code: dnsmasq --conf-script='/path/to/command 1>&2'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
