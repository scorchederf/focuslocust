---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# minicom

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `minicom` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/minicom` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for minicom covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/minicom.md)
- Source verification: [source record](../../sources/gtfobins/minicom.md)

## Aliases

- `minicom`

## Source Verification

[source record](../../sources/gtfobins/minicom.md)

## Evidence Excerpt

```text
_body: ''
_name: minicom
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/minicom
comment: Note that in some versions, `Meta-Z` is used in place of `Ctrl-A`.
functions:
shell:
- code: minicom -D /dev/null
comment: 'Start the following command to open the TUI interface, then:
```
