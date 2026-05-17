---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rlwrap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rlwrap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlwrap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rlwrap](../../tools/linux/rlwrap.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rlwrap |
| name | rlwrap |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rlwrap/ |

## Preserved Source Material

```yaml
_body: ''
_name: rlwrap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlwrap
functions:
  file-write:
  - binary: false
    code: rlwrap -l /path/to/output-file echo DATA
    comment: This adds timestamps to the output file. This relies on the external `echo` command.
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  shell:
  - code: rlwrap /bin/sh
    contexts:
      sudo: null
      suid:
        code: rlwrap /bin/sh -p
        shell: false
      unprivileged: null
```
