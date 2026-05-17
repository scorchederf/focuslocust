---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ffmpeg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ffmpeg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ffmpeg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ffmpeg covering library-load.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ffmpeg.md)
- Source verification: [source record](../../sources/gtfobins/ffmpeg.md)

## Aliases

- `ffmpeg`

## Source Verification

[source record](../../sources/gtfobins/ffmpeg.md)

## Evidence Excerpt

```text
_body: ''
_name: ffmpeg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ffmpeg
functions:
library-load:
- code: 'ffmpeg -f lavfi -i anullsrc -af ladspa=file=/path/to/lib.so /path/to/temp-file.wav
reset^J'
contexts:
```
