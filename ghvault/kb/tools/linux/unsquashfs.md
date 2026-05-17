---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# unsquashfs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `unsquashfs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unsquashfs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for unsquashfs covering privilege-escalation.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/unsquashfs.md)
- Source verification: [source record](../../sources/gtfobins/unsquashfs.md)

## Aliases

- `unsquashfs`

## Source Verification

[source record](../../sources/gtfobins/unsquashfs.md)

## Evidence Excerpt

````text
_body: ''
_name: unsquashfs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/unsquashfs
comment: '`unsquashfs` preserve the SUID bit when extracting the file system. For example, prepare an archive beforehand with
the following commands as root:
```
cp /bin/sh .
chmod +s sh
````
