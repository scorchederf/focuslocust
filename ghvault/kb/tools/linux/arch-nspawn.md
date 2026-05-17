---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# arch-nspawn

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `arch-nspawn` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arch-nspawn` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for arch-nspawn covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/arch-nspawn.md)
- Source verification: [source record](../../sources/gtfobins/arch-nspawn.md)

## Aliases

- `arch-nspawn`

## Source Verification

[source record](../../sources/gtfobins/arch-nspawn.md)

## Evidence Excerpt

```text
_body: ''
_name: arch-nspawn
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arch-nspawn
functions:
shell:
- code: 'mkdir -p ./etc/
grep -oP "^CHROOT_VERSION=''\K[^'']+" /usr/share/devtools/lib/archroot.sh >.arch-chroot
touch ./etc/pacman.conf
```
