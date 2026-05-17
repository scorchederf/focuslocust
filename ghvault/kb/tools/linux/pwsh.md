---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pwsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pwsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pwsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pwsh covering file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pwsh.md)
- Source verification: [source record](../../sources/gtfobins/pwsh.md)

## Aliases

- `pwsh`

## Source Verification

[source record](../../sources/gtfobins/pwsh.md)

## Evidence Excerpt

```text
_body: ''
_name: pwsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pwsh
functions:
file-write:
- code: pwsh -c '"DATA" | Out-File /path/to/output-file'
contexts:
sudo: null
```
