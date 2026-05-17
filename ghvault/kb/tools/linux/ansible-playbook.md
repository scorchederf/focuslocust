---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# ansible-playbook

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `ansible-playbook` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ansible-playbook` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for ansible-playbook covering shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/ansible-playbook.md)
- Source verification: [source record](../../sources/gtfobins/ansible-playbook.md)

## Aliases

- `ansible-playbook`

## Source Verification

[source record](../../sources/gtfobins/ansible-playbook.md)

## Evidence Excerpt

```text
_body: ''
_name: ansible-playbook
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ansible-playbook
functions:
shell:
- code: 'echo ''[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]'' >/path/to/temp-file
ansible-playbook /path/to/temp-file'
contexts:
```
