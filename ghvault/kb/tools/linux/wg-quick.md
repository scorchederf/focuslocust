---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# wg-quick

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `wg-quick` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wg-quick` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for wg-quick covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/wg-quick.md)
- Source verification: [source record](../../sources/gtfobins/wg-quick.md)

## Aliases

- `wg-quick`

## Source Verification

[source record](../../sources/gtfobins/wg-quick.md)

## Evidence Excerpt

```text
_body: ''
_name: wg-quick
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wg-quick
functions:
shell:
- code: 'cat >/path/to/temp-file.conf <<EOF
[Interface]
PostUp = /bin/sh
```
