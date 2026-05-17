---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# mysql

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `mysql` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mysql` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for mysql covering library-load, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/mysql.md)
- Source verification: [source record](../../sources/gtfobins/mysql.md)

## Aliases

- `mysql`

## Source Verification

[source record](../../sources/gtfobins/mysql.md)

## Evidence Excerpt

```text
_body: ''
_name: mysql
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/mysql
comment: A valid MySQL server must be available to connect to.
functions:
library-load:
- code: mysql --default-auth ../../../../../path/to/lib
comment: The following loads the `/path/to/lib.so` shared object.
```
