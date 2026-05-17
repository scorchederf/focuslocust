---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [cp](../../tools/linux/cp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cp |
| name | cp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/cp/ |

## Preserved Source Material

```yaml
_body: ''
_name: cp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cp
functions:
  file-read:
  - code: cp /path/to/input-file /dev/stdout
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  file-write:
  - code: echo DATA | cp /dev/stdin /path/to/output-file
    contexts:
      sudo: null
      suid: null
      unprivileged: null
  privilege-escalation:
  - code: cp /path/to/input-file /path/to/output-file
    comment: This can be used to copy and then read or write files from a restricted file systems or with elevated privileges.
      (The GNU version of `cp` has the `--parents` option that can be used to also create the directory hierarchy specified
      in the source path, to the destination folder.)
    contexts:
      sudo: null
      suid: null
  - code: cp --attributes-only --preserve=all /path/to/input-file /path/to/output-file
    comment: This can copy SUID permissions from any SUID binary (e.g., `/path/to/input-file`) to another.
    contexts:
      sudo: null
      suid: null
```
