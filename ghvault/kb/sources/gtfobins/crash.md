---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# crash

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `crash` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/crash` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [crash](../../tools/linux/crash.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | crash |
| name | crash |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/crash/ |

## Preserved Source Material

```yaml
_body: ''
_name: crash
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/crash
functions:
  command:
  - code: CRASHPAGER=/path/to/command crash -h
    contexts:
      sudo: null
      unprivileged: null
  inherit:
  - code: crash -h
    contexts:
      sudo: null
      suid: null
      unprivileged: null
    from: less
```
