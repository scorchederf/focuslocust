---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# apache2ctl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `apache2ctl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2ctl` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for apache2ctl covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/apache2ctl.md)
- Source verification: [source record](../../sources/gtfobins/apache2ctl.md)

## Aliases

- `apache2ctl`

## Source Verification

[source record](../../sources/gtfobins/apache2ctl.md)

## Evidence Excerpt

```text
_body: ''
_name: apache2ctl
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apache2ctl
functions:
file-read:
- binary: false
code: apache2ctl -c 'Include /path/to/input-file'
comment: The first line only is likely leaked as an error message.
```
