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

## Generated Concept Page

- [ffmpeg](../../tools/linux/ffmpeg.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ffmpeg |
| name | ffmpeg |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ffmpeg/ |

## Preserved Source Material

```yaml
_body: ''
_name: ffmpeg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ffmpeg
functions:
  library-load:
  - code: 'ffmpeg -f lavfi -i anullsrc -af ladspa=file=/path/to/lib.so /path/to/temp-file.wav

      reset^J'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
```
