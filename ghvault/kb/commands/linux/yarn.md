---
parsed_by: focuslocust
source: commands
type: generated
---
# yarn Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## yarn

Tool page: [yarn](../../tools/linux/yarn.md)

### shell

```text
yarn exec /bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yarn` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '{"scripts": {"preinstall": "/bin/sh"}}' >package.json
yarn --cwd .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yarn` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo '{"scripts": {"xxx": "/bin/sh"}}' >package.json
yarn --cwd . xxx
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/yarn` |
| Evidence | Function example preserved from source parser. |
