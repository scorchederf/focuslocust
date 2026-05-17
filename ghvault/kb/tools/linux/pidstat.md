---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pidstat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pidstat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pidstat` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pidstat covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pidstat.md)
- Source verification: [source record](../../sources/gtfobins/pidstat.md)

## Aliases

- `pidstat`

## Source Verification

[source record](../../sources/gtfobins/pidstat.md)

## Evidence Excerpt

```text
_body: ''
_name: pidstat
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pidstat
functions:
shell:
- code: pidstat -e /bin/sh
contexts:
sudo: null
```
