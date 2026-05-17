---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bzip2

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bzip2` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bzip2` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bzip2](../../tools/linux/bzip2.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bzip2 |
| name | bzip2 |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bzip2/ |

## Preserved Source Material

```yaml
_body: ''
_name: bzip2
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bzip2
comment: There are also a number of other utilities that rely on `bzip2` under the hood, e.g., `bzless`, `bzcat`, `bunzip2`,
  etc. Besides having similar features, they also allow privileged reads if `bzip2` itself is SUID.
functions:
  file-read:
  - code: bzip2 -c /path/to/input-file | bzip2 -d
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
