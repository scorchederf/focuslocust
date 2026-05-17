---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# terraform

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `terraform` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/terraform` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for terraform covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/terraform.md)
- Source verification: [source record](../../sources/gtfobins/terraform.md)

## Aliases

- `terraform`

## Source Verification

[source record](../../sources/gtfobins/terraform.md)

## Evidence Excerpt

```text
_body: ''
_name: terraform
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/terraform
functions:
file-read:
- binary: false
code: 'terraform console
file("/path/to/input-file")'
```
