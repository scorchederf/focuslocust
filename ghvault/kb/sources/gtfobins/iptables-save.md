---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# iptables-save

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `iptables-save` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iptables-save` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [iptables-save](../../tools/linux/iptables-save.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iptables-save |
| name | iptables-save |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/iptables-save/ |

## Preserved Source Material

```yaml
_body: ''
_name: iptables-save
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iptables-save
functions:
  file-write:
  - binary: false
    code: 'iptables -A INPUT -i lo -j ACCEPT -m comment --comment DATA

      iptables -S

      iptables-save -f /path/to/output-file'
    comment: The content is written along with a number of `iptables` rules.
    contexts:
      sudo: null
```
