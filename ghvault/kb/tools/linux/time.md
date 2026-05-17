---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# time

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `time` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/time` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for time covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/time.md)
- Source verification: [source record](../../sources/gtfobins/time.md)

## Aliases

- `time`

## Source Verification

[source record](../../sources/gtfobins/time.md)

## Evidence Excerpt

```text
_body: ''
_name: time
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/time
functions:
shell:
- code: time /bin/sh
comment: Note that the shell might have its own builtin `time` implementation, which may behave differently than the binary,
which is often located at `/usr/bin/time`.
```
