---
parsed_by: focuslocust
source: commands
type: generated
---
# npm Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## npm

Tool page: [npm](../../tools/linux/npm.md)

### shell

```text
npm exec /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/npm` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '{"scripts": {"preinstall": "/bin/sh"}}' >package.json
npm -C . i
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/npm` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '{"scripts": {"xxx": "/bin/sh"}}' >package.json
npm -C . run xxx
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/npm` |
| Evidence | Function example preserved from source parser. |
