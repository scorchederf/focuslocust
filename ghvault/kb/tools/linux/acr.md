---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# acr

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `acr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/acr` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for acr covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/acr.md)
- Source verification: [source record](../../sources/gtfobins/acr.md)

## Aliases

- `acr`

## Source Verification

[source record](../../sources/gtfobins/acr.md)

## Evidence Excerpt

```text
_body: ''
_name: acr
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/acr
functions:
command:
- code: 'echo -e ''x:\n\t/bin/sh 1>&0 2>&0'' >/path/to/temp-file
chmod +x /path/to/temp-file
acr -r ./relative/path/to/temp-file'
```
