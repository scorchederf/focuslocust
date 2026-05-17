---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# iconv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `iconv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iconv` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for iconv covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/iconv.md)
- Source verification: [source record](../../sources/gtfobins/iconv.md)

## Aliases

- `iconv`

## Source Verification

[source record](../../sources/gtfobins/iconv.md)

## Evidence Excerpt

```text
_body: ''
_name: iconv
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/iconv
comment: The `8859_1` encoding is used as it accepts any single-byte sequence, thus it allows to read/write arbitrary files.
Other encoding combinations may corrupt the result.
functions:
file-read:
- code: iconv -f 8859_1 -t 8859_1 /path/to/input-file
```
