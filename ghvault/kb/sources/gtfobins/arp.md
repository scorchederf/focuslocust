---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# arp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `arp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [arp](../../tools/linux/arp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | arp |
| name | arp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/arp/ |

## Preserved Source Material

```yaml
_body: ''
_name: arp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arp
functions:
  file-read:
  - binary: false
    code: arp -v -f /path/to/input-file
    comment: Lines are likely leaked as error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
