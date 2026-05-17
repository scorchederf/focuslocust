---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# aria2c

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `aria2c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for aria2c covering command, download, file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/aria2c.md)
- Source verification: [source record](../../sources/gtfobins/aria2c.md)

## Aliases

- `aria2c`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: echo /path/to/command >/path/to/temp-file chmod +x /path/to/temp-file aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain |

## Source Verification

[source record](../../sources/gtfobins/aria2c.md)

## Evidence Excerpt

```text
_body: ''
_name: aria2c
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c
functions:
command:
- code: 'echo /path/to/command >/path/to/temp-file
chmod +x /path/to/temp-file
aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain'
```
