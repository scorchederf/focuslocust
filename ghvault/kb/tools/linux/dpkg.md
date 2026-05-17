---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dpkg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dpkg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dpkg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dpkg covering inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dpkg.md)
- Source verification: [source record](../../sources/gtfobins/dpkg.md)

## Aliases

- `dpkg`

## Source Verification

[source record](../../sources/gtfobins/dpkg.md)

## Evidence Excerpt

```text
_body: ''
_name: dpkg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dpkg
functions:
inherit:
- code: dpkg -l
contexts:
sudo: null
```
