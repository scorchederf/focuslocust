---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgfilter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgfilter` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgfilter` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for msgfilter covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/msgfilter.md)
- Source verification: [source record](../../sources/gtfobins/msgfilter.md)

## Aliases

- `msgfilter`

## Source Verification

[source record](../../sources/gtfobins/msgfilter.md)

## Evidence Excerpt

```text
_body: ''
_name: msgfilter
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgfilter
functions:
file-read:
- binary: false
code: msgfilter -P -i /path/to/input-file /bin/cat
comment: The file is parsed and displayed as a Java `.properties` file. `/bin/cat` can be replaced with any other *filter*
```
