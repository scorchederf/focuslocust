---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# check_by_ssh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `check-by-ssh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_by_ssh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for check_by_ssh covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/check-by-ssh.md)
- Source verification: [source record](../../sources/gtfobins/check-by-ssh.md)

## Aliases

- `check-by-ssh`
- `check_by_ssh`

## Source Verification

[source record](../../sources/gtfobins/check-by-ssh.md)

## Evidence Excerpt

```text
_body: ''
_name: check_by_ssh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_by_ssh
comment: This is the `check_by_ssh` Nagios plugin, available e.g. in `/usr/lib/nagios/plugins/`.
functions:
shell:
- code: check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C x
comment: The shell will only last 10 seconds.
```
