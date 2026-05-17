---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# composer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `composer` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/composer` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for composer covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/composer.md)
- Source verification: [source record](../../sources/gtfobins/composer.md)

## Aliases

- `composer`

## Source Verification

[source record](../../sources/gtfobins/composer.md)

## Evidence Excerpt

```text
_body: ''
_name: composer
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/composer
functions:
shell:
- code: 'echo ''{"scripts":{"x":"/bin/sh"}}'' >composer.json
composer run-script x'
contexts:
```
