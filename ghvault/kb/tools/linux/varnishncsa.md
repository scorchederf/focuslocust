---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# varnishncsa

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `varnishncsa` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/varnishncsa` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for varnishncsa covering file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/varnishncsa.md)
- Source verification: [source record](../../sources/gtfobins/varnishncsa.md)

## Aliases

- `varnishncsa`

## Source Verification

[source record](../../sources/gtfobins/varnishncsa.md)

## Evidence Excerpt

```text
_body: ''
_name: varnishncsa
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/varnishncsa
comment: A running `varnishd` instance must be available.
functions:
file-write:
- binary: false
code: varnishncsa -g request -q 'ReqURL ~ "/xxxxxxxxxx"' -F '%{yyy}i' -w /path/to/output-file
```
