---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# aws

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `aws` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aws` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for aws covering file-read, inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/aws.md)
- Source verification: [source record](../../sources/gtfobins/aws.md)

## Aliases

- `aws`

## Source Verification

[source record](../../sources/gtfobins/aws.md)

## Evidence Excerpt

```text
_body: ''
_name: aws
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aws
functions:
file-read:
- binary: false
code: aws ec2 describe-instances --filter file:///path/to/input-file
contexts:
```
