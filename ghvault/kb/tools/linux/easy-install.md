---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# easy_install

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `easy-install` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/easy_install` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for easy_install covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/easy-install.md)
- Source verification: [source record](../../sources/gtfobins/easy-install.md)

## Aliases

- `easy-install`
- `easy_install`

## Source Verification

[source record](../../sources/gtfobins/easy-install.md)

## Evidence Excerpt

```text
_body: ''
_name: easy_install
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/easy_install
functions:
inherit:
- code: 'echo ''...'' >setup.py
easy_install .'
comment: 'This allows to run Python code (`...`). It executes a Python script named `setup.py` in the directory passed
```
