---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh-keygen

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh-keygen` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-keygen` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ssh-keygen covering library-load.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ssh-keygen.md)
- Source verification: [source record](../../sources/gtfobins/ssh-keygen.md)

## Aliases

- `ssh-keygen`

## Source Verification

[source record](../../sources/gtfobins/ssh-keygen.md)

## Evidence Excerpt

```text
_body: ''
_name: ssh-keygen
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-keygen
functions:
library-load:
- code: ssh-keygen -D /path/to/lib.so
comment: The shared library must contain the `void C_GetFunctionList() {}` function.
contexts:
```
