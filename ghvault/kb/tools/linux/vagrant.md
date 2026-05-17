---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# vagrant

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `vagrant` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vagrant` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for vagrant covering inherit.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/vagrant.md)
- Source verification: [source record](../../sources/gtfobins/vagrant.md)

## Aliases

- `vagrant`

## Source Verification

[source record](../../sources/gtfobins/vagrant.md)

## Evidence Excerpt

```text
_body: ''
_name: vagrant
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vagrant
functions:
inherit:
- code: 'echo ''...'' >Vagrantfile
vagrant up'
comment: This allows to run Ruby code (`...`).
```
