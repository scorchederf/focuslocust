---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sshfs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sshfs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sshfs covering command, download, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sshfs.md)
- Source verification: [source record](../../sources/gtfobins/sshfs.md)

## Aliases

- `sshfs`

## Source Verification

[source record](../../sources/gtfobins/sshfs.md)

## Evidence Excerpt

```text
_body: ''
_name: sshfs
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs
functions:
command:
- blind: true
code: 'sshfs -o ssh_command=/path/to/command x: /path/to/dir/'
contexts:
```
