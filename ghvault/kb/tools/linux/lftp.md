---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lftp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lftp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lftp` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for lftp covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/lftp.md)
- Source verification: [source record](../../sources/gtfobins/lftp.md)

## Aliases

- `lftp`

## Source Verification

[source record](../../sources/gtfobins/lftp.md)

## Evidence Excerpt

```text
_body: ''
_name: lftp
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lftp
functions:
shell:
- code: lftp -c '!/bin/sh'
contexts:
sudo: null
```
