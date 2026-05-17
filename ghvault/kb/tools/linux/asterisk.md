---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# asterisk

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `asterisk` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/asterisk` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for asterisk covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/asterisk.md)
- Source verification: [source record](../../sources/gtfobins/asterisk.md)

## Aliases

- `asterisk`

## Source Verification

[source record](../../sources/gtfobins/asterisk.md)

## Evidence Excerpt

```text
_body: ''
_name: asterisk
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/asterisk
functions:
shell:
- code: 'asterisk -r
!/bin/sh'
comment: A server instance must be already running, otherwise it can be started with `sudo asterisk -F`. Moreover, the
```
