---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_cups

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-cups` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_cups` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [check_cups](../../tools/linux/check-cups.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-cups |
| name | check_cups |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-cups/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_cups
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_cups
comment: This is the `check_cups` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  file-read:
  - binary: false
    code: check_cups --extra-opts=@/path/to/input-file
    comment: The read file content is limited to the first line.
    contexts:
      sudo: null
      unprivileged: null
```
