---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# expect

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `expect` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expect` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for expect covering file-read, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/expect.md)
- Source verification: [source record](../../sources/gtfobins/expect.md)

## Aliases

- `expect`

## Source Verification

[source record](../../sources/gtfobins/expect.md)

## Evidence Excerpt

```text
_body: ''
_name: expect
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/expect
functions:
file-read:
- code: expect /path/to/input-file
comment: The file is read and parsed as an `expect` command file, the content of the first invalid line is returned in
an error message.
```
