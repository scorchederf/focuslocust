---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# msgconv

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `msgconv` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgconv` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for msgconv covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/msgconv.md)
- Source verification: [source record](../../sources/gtfobins/msgconv.md)

## Aliases

- `msgconv`

## Source Verification

[source record](../../sources/gtfobins/msgconv.md)

## Evidence Excerpt

```text
_body: ''
_name: msgconv
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/msgconv
functions:
file-read:
- binary: false
code: msgconv -P /path/to/input-file
comment: The file is parsed and displayed as a Java `.properties` file.
```
