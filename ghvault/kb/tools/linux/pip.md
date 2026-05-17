---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# pip

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `pip` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pip` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for pip covering inherit, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/pip.md)
- Source verification: [source record](../../sources/gtfobins/pip.md)

## Aliases

- `pip`

## Source Verification

[source record](../../sources/gtfobins/pip.md)

## Evidence Excerpt

```text
_body: ''
_name: pip
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pip
functions:
inherit:
- code: 'echo ''...'' >setup.py
pip install --break-system-packages .'
comment: 'This allows to run Python code (`...`). It executes a Python script named `setup.py` in the directory passed
```
