---
parsed_by: focuslocust
source: commands
type: generated
---
# Cdb Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Cdb.exe

Tool page: [Cdb.exe](../../tools/windows/cdb.exe.md)

### Local execution of assembly shellcode.

```text
cdb.exe -cf {PATH:.wds} -o notepad.exe
```

Description:

Launch 64-bit shellcode from the specified .wds file using cdb.exe.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Cdb.yml` |
| Evidence | Command preserved from source parser. |

### Run a shell command under a trusted Microsoft signed binary

```text
cdb.exe -pd -pn {process_name}
.shell {CMD}
```

Description:

Attaching to any process and executing shell commands.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Cdb.yml` |
| Evidence | Command preserved from source parser. |

### Run commands under a trusted Microsoft signed binary

```text
cdb.exe -c {PATH:.txt} "{CMD}"
```

Description:

Execute arbitrary commands and binaries using a debugging script (see Resources section for a sample file).

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Cdb.yml` |
| Evidence | Command preserved from source parser. |
