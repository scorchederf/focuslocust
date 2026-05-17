---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# watch

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `watch` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/watch` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for watch covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/watch.md)
- Source verification: [source record](../../sources/gtfobins/watch.md)

## Aliases

- `watch`

## Source Verification

[source record](../../sources/gtfobins/watch.md)

## Evidence Excerpt

```text
_body: ''
_name: watch
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/watch
functions:
shell:
- code: watch -x /bin/sh -c 'reset; exec /bin/sh 1>&0 2>&0'
contexts:
sudo: null
```
