---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# forge

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `forge` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/forge` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for forge covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/forge.md)
- Source verification: [source record](../../sources/gtfobins/forge.md)

## Aliases

- `forge`

## Source Verification

[source record](../../sources/gtfobins/forge.md)

## Evidence Excerpt

```text
_body: ''
_name: forge
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/forge
functions:
shell:
- code: 'echo ''#!/bin/sh'' >/path/to/temp-file
echo -e "/bin/sh <$(tty) >$(tty) 2>$(tty)" >>/path/to/temp-file
chmod +x /path/to/temp-file
```
