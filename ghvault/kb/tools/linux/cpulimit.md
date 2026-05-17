---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# cpulimit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `cpulimit` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpulimit` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for cpulimit covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/cpulimit.md)
- Source verification: [source record](../../sources/gtfobins/cpulimit.md)

## Aliases

- `cpulimit`

## Source Verification

[source record](../../sources/gtfobins/cpulimit.md)

## Evidence Excerpt

```text
_body: ''
_name: cpulimit
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/cpulimit
functions:
shell:
- code: cpulimit -l 100 -f -- /bin/sh
contexts:
sudo: null
```
