---
parsed_by: focuslocust
source: commands
type: generated
---
# ansible-playbook Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ansible-playbook

Tool page: [ansible-playbook](../../tools/linux/ansible-playbook.md)

### shell

```text
echo '[{hosts: localhost, tasks: [shell: /bin/sh </dev/tty >/dev/tty 2>/dev/tty]}]' >/path/to/temp-file
ansible-playbook /path/to/temp-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ansible-playbook` |
| Evidence | Function example preserved from source parser. |
