---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# snap

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `snap` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/snap` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for snap covering command.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/snap.md)
- Source verification: [source record](../../sources/gtfobins/snap.md)

## Aliases

- `snap`

## Source Verification

[source record](../../sources/gtfobins/snap.md)

## Evidence Excerpt

````text
_body: ''
_name: snap
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/snap
functions:
command:
- code: snap install xxxx_1.0_all.snap --dangerous --devmode
comment: 'Generate the Snap package with [fpm](https://github.com/jordansissel/fpm) and upload it to the target.
```
````
