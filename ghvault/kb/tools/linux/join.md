---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# join

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `join` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/join` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for join covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/join.md)
- Source verification: [source record](../../sources/gtfobins/join.md)

## Aliases

- `join`

## Source Verification

[source record](../../sources/gtfobins/join.md)

## Evidence Excerpt

```text
_body: ''
_name: join
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/join
functions:
file-read:
- binary: false
code: join -a 2 /dev/null /path/to/input-file
contexts:
```
