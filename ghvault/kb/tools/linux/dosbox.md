---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dosbox

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dosbox` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dosbox covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dosbox.md)
- Source verification: [source record](../../sources/gtfobins/dosbox.md)

## Aliases

- `dosbox`

## Source Verification

[source record](../../sources/gtfobins/dosbox.md)

## Evidence Excerpt

```text
_body: ''
_name: dosbox
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dosbox
comment: Basically `dosbox` allows to mount the local file system, so that it can be altered using DOS commands. Note that
the DOS filename convention ([8.3](https://en.wikipedia.org/wiki/8.3_filename)) is used.
functions:
file-read:
- code: dosbox -c 'mount c /' -c 'type c:\path\to\input'
```
