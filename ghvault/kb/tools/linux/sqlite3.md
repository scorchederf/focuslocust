---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sqlite3

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sqlite3` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sqlite3 covering file-read, file-write, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sqlite3.md)
- Source verification: [source record](../../sources/gtfobins/sqlite3.md)

## Aliases

- `sqlite3`

## Source Verification

[source record](../../sources/gtfobins/sqlite3.md)

## Evidence Excerpt

```text
_body: ''
_name: sqlite3
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3
functions:
file-read:
- binary: false
code: 'sqlite3 <<EOF
CREATE TABLE x(x TEXT);
```
