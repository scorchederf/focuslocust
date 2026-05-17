---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ntpdate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ntpdate` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ntpdate` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ntpdate](../../tools/linux/ntpdate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ntpdate |
| name | ntpdate |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ntpdate/ |

## Preserved Source Material

```yaml
_body: ''
_name: ntpdate
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ntpdate
functions:
  file-read:
  - binary: false
    code: ntpdate -a x -k /path/to/input-file -d localhost
    comment: The file is actually parsed and lines are leaked through error messages.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
