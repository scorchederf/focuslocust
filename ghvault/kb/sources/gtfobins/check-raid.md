---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_raid

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-raid` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_raid` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [check_raid](../../tools/linux/check-raid.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-raid |
| name | check_raid |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-raid/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_raid
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_raid
comment: This is the `check_raid` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  file-read:
  - code: check_raid --extra-opts=@/path/to/input-file
    comment: The read file content is limited to the first line.
    contexts:
      sudo: null
      unprivileged: null
```
