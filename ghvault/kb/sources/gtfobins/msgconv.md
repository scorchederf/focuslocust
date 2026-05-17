---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgconv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgconv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgconv` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msgconv](../../tools/linux/msgconv.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msgconv |
| name | msgconv |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/msgconv/ |

## Preserved Source Material

```yaml
_body: ''
_name: msgconv
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgconv
functions:
  file-read:
  - binary: false
    code: msgconv -P /path/to/input-file
    comment: The file is parsed and displayed as a Java `.properties` file.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
