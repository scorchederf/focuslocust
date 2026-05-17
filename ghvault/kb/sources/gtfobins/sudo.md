---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sudo

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sudo` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sudo` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [sudo](../../tools/linux/sudo.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sudo |
| name | sudo |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/sudo/ |

## Preserved Source Material

```yaml
_body: ''
_name: sudo
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sudo
functions:
  shell:
  - code: sudo /bin/sh
    contexts:
      sudo:
        comment: The invocation is actually `sudo sudo ...`.
```
