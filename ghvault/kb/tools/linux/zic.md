---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# zic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `zic` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zic` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for zic covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/zic.md)
- Source verification: [source record](../../sources/gtfobins/zic.md)

## Aliases

- `zic`

## Source Verification

[source record](../../sources/gtfobins/zic.md)

## Evidence Excerpt

```text
_body: ''
_name: zic
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zic
functions:
command:
- code: 'echo ''Rule Jordan 0 1 xxx Jan lastSun 2 1:00d -'' >/path/to/temp-file
echo ''Zone Test 2:00 Jordan CE%sT'' >>/path/to/temp-file
zic -d . -y /path/to/command /path/to/temp-file'
```
