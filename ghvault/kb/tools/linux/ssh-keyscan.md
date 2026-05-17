---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh-keyscan

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh-keyscan` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-keyscan` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ssh-keyscan covering file-read.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ssh-keyscan.md)
- Source verification: [source record](../../sources/gtfobins/ssh-keyscan.md)

## Aliases

- `ssh-keyscan`

## Source Verification

[source record](../../sources/gtfobins/ssh-keyscan.md)

## Evidence Excerpt

```text
_body: ''
_name: ssh-keyscan
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-keyscan
functions:
file-read:
- code: ssh-keyscan -f /path/to/input-file
comment: The file content is actually parsed so only a part of each line is returned as a part of an error message.
contexts:
```
