---
parsed_by: focuslocust
source: commands
type: generated
---
# exiftool Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## exiftool

Tool page: [exiftool](../../tools/linux/exiftool.md)

### file-read

```text
exiftool -filename=/path/to/output-file /path/to/input-file
cat /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
exiftool -filename=/path/to/output-file /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
exiftool "-description<=/path/to/input-file --filename /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
exiftool "-description=DATA --filename /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
exiftool -description -W /path/to/output-file --filename /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
exiftool -if '...' /etc/passwd
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/exiftool` |
| Evidence | Function example preserved from source parser. |
