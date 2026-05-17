---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# yt-dlp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `yt-dlp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yt-dlp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [yt-dlp](../../tools/linux/yt-dlp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | yt-dlp |
| name | yt-dlp |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/yt-dlp/ |

## Preserved Source Material

```yaml
_body: ''
_name: yt-dlp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yt-dlp
functions:
  shell:
  - code: 'yt-dlp ''https://www.youtube.com/watch?v=xxxxxxxxxxx'' --exec ''/bin/sh #'''
    comment: The URL must point to a valid YouTube video which will be actually downloaded.
    contexts:
      sudo: null
      unprivileged: null
```
