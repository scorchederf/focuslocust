---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pkg

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pkg` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pkg` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pkg covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pkg.md)
- Source verification: [source record](../../sources/gtfobins/pkg.md)

## Aliases

- `pkg`

## Source Verification

[source record](../../sources/gtfobins/pkg.md)

## Evidence Excerpt

````text
_body: ''
_name: pkg
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pkg
functions:
command:
- code: pkg install -y --no-repo-update ./x-1.0.txz
comment: 'Generate the FreeBSD package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
```
````
