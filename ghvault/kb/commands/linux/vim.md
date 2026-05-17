---
parsed_by: focuslocust
source: commands
type: generated
---
# vim Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## vim

Tool page: [vim](../../tools/linux/vim.md)

### file-read

```text
vim -c ':redir! >/path/to/output-file | echo "DATA" | redir END | q'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
vim -c ':py ...'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
vim -c ':lua ...'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
vim
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/vim` |
| Evidence | Function example preserved from source parser. |
