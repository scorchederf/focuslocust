---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dmidecode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dmidecode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmidecode` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dmidecode covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dmidecode.md)
- Source verification: [source record](../../sources/gtfobins/dmidecode.md)

## Aliases

- `dmidecode`

## Source Verification

[source record](../../sources/gtfobins/dmidecode.md)

## Evidence Excerpt

```text
_body: ''
_name: dmidecode
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dmidecode
functions:
file-write:
- binary: false
code: dmidecode --no-sysfs -d x.dmi --dump-bin /path/to/output-file
comment: 'It can be used to write files using a specially crafted SMBIOS file that can be read as a memory device by dmidecode.
```
