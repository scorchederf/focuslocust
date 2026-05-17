---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# nmap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `nmap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for nmap covering file-read, file-write, inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/nmap.md)
- Source verification: [source record](../../sources/gtfobins/nmap.md)

## Aliases

- `nmap`

## Source Verification

[source record](../../sources/gtfobins/nmap.md)

## Evidence Excerpt

```text
_body: ''
_name: nmap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nmap
functions:
file-read:
- binary: false
code: nmap -iL /path/to/input-file
comment: The file is actually parsed as a list of hosts/networks, lines are leaked through error messages.
```
