---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# fastfetch

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `fastfetch` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for fastfetch covering command, file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/fastfetch.md)
- Source verification: [source record](../../sources/gtfobins/fastfetch.md)

## Aliases

- `fastfetch`

## Source Verification

[source record](../../sources/gtfobins/fastfetch.md)

## Evidence Excerpt

```text
_body: ''
_name: fastfetch
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/fastfetch
functions:
command:
- code: 'echo ''{"modules":[{"type":"command","key":"x","text":"exec /path/to/command"}]}'' >/path/to/temp-file.jsonc
fastfetch -c /path/to/temp-file.jsonc'
contexts:
```
