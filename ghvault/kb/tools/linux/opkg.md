---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# opkg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `opkg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/opkg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for opkg covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/opkg.md)
- Source verification: [source record](../../sources/gtfobins/opkg.md)

## Aliases

- `opkg`

## Source Verification

[source record](../../sources/gtfobins/opkg.md)

## Evidence Excerpt

````text
_body: ''
_name: opkg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/opkg
functions:
shell:
- code: rpm opkg install x_1.0_all.deb
comment: 'Generate the Debian package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
```
````
