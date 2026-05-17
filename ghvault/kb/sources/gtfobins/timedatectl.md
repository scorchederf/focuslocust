---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# timedatectl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `timedatectl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/timedatectl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [timedatectl](../../tools/linux/timedatectl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | timedatectl |
| name | timedatectl |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/timedatectl/ |

## Preserved Source Material

```yaml
_body: ''
_name: timedatectl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/timedatectl
comment: This might not work if run by unprivileged users depending on the system configuration.
functions:
  inherit:
  - code: timedatectl list-timezones
    contexts:
      sudo: null
      unprivileged: null
    from: less
```
