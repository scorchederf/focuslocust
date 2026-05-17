---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rpm

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rpm` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rpm covering command, inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rpm.md)
- Source verification: [source record](../../sources/gtfobins/rpm.md)

## Aliases

- `rpm`

## Source Verification

[source record](../../sources/gtfobins/rpm.md)

## Evidence Excerpt

````text
_body: ''
_name: rpm
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rpm
functions:
command:
- code: rpm -ivh x-1.0-1.noarch.rpm
comment: 'Generate the RPM package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
```
````
