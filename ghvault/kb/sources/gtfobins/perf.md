---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# perf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `perf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [perf](../../tools/linux/perf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | perf |
| name | perf |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/perf/ |

## Preserved Source Material

```yaml
_body: ''
_name: perf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perf
functions:
  shell:
  - code: perf stat /bin/sh
    contexts:
      sudo: null
      suid:
        code: perf stat /bin/sh -p
        shell: false
      unprivileged: null
```
