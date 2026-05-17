---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_memory

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-memory` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_memory` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [check_memory](../../tools/linux/check-memory.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | check-memory |
| name | check_memory |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/check-memory/ |

## Preserved Source Material

```yaml
_body: ''
_name: check_memory
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_memory
comment: This is the `check_memory` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
  file-read:
  - code: check_memory --extra-opts=@/path/to/input-file
    comment: The read file content is limited to the first line.
    contexts:
      sudo: null
      unprivileged: null
```
