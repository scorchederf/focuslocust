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

## Summary

GTFOBins entry for rlwrap covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rlwrap.md)
- Source verification: [source record](../../sources/gtfobins/rlwrap.md)

## Aliases

- `rlwrap`

## Source Verification

[source record](../../sources/gtfobins/rlwrap.md)

## Evidence Excerpt

```text
_body: ''
_name: rlwrap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rlwrap
functions:
file-write:
- binary: false
code: rlwrap -l /path/to/output-file echo DATA
comment: This adds timestamps to the output file. This relies on the external `echo` command.
```
