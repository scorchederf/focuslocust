---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# dnf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `dnf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dnf` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for dnf covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/dnf.md)
- Source verification: [source record](../../sources/gtfobins/dnf.md)

## Aliases

- `dnf`

## Source Verification

[source record](../../sources/gtfobins/dnf.md)

## Evidence Excerpt

````text
_body: ''
_name: dnf
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/dnf
functions:
command:
- code: dnf install -y x-1.0-1.noarch.rpm --disablerepo=*
comment: 'Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
```
````
