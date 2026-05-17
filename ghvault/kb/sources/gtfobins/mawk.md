---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mawk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mawk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [mawk](../../tools/linux/mawk.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | mawk |
| name | mawk |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/mawk/ |

## Preserved Source Material

```yaml
_body: ''
_name: mawk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mawk
functions:
  file-read:
  - code: mawk '//' /path/to/input-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: mawk 'BEGIN { print "DATA" > "/path/to/output-file" }'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: mawk 'BEGIN {system("/bin/sh")}'
    contexts:
      sudo: null
      suid:
        shell: true
      unprivileged: null
```
