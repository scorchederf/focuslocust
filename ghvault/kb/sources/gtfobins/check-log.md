---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_log

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-log` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_log` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [check_log](../../tools/linux/check-log.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-log |
| name | check_log |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-log/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_log
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_log
comment: This is the `check_log` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  file-read:
  - code: check_log -F /path/to/input-file -O /dev/stdout
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: check_log -F /path/to/input-file -O /path/to/output-file
    contexts:
      sudo: null
      unprivileged: null
```
