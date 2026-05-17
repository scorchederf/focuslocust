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

## Summary

GTFOBins entry for yt-dlp covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/yt-dlp.md)
- Source verification: [source record](../../sources/gtfobins/yt-dlp.md)

## Aliases

- `yt-dlp`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: yt-dlp 'https://www.youtube.com/watch?v=xxxxxxxxxxx' --exec '/bin/sh #' |

## Source Verification

[source record](../../sources/gtfobins/yt-dlp.md)

## Evidence Excerpt

```text
_body: ''
_name: yt-dlp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yt-dlp
functions:
shell:
- code: 'yt-dlp ''https://www.youtube.com/watch?v=xxxxxxxxxxx'' --exec ''/bin/sh #'''
comment: The URL must point to a valid YouTube video which will be actually downloaded.
contexts:
```
