---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_statusfile

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-statusfile` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_statusfile` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [check_statusfile](../../tools/linux/check-statusfile.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-statusfile |
| name | check_statusfile |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-statusfile/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_statusfile
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_statusfile
comment: This is the `check_statusfile` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  file-read:
  - code: check_statusfile /path/to/input-file
    comment: The read file content is limited to the first line.
    contexts:
      sudo: null
      unprivileged: null
```
