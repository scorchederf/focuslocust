---
parsed_by: focuslocust
source: commands
type: generated
---
# adplus Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## adplus.exe

Tool page: [adplus.exe](../../tools/windows/adplus.exe.md)

### Create memory dump and parse it offline

```text
adplus.exe -hang -pn lsass.exe -o {PATH_ABSOLUTE:folder} -quiet
```

Description:

Creates a memory dump of the lsass process

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml` |
| Evidence | Command preserved from source parser. |

### Run commands under a trusted Microsoft signed binary

```text
adplus.exe -c {PATH:.xml}
```

Description:

Execute arbitrary commands using adplus config file (see Resources section for a sample file).

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml` |
| Evidence | Command preserved from source parser. |

### Run commands under a trusted Microsoft signed binary

```text
adplus.exe -c {PATH:.xml}
```

Description:

Dump process memory using adplus config file (see Resources section for a sample file).

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml` |
| Evidence | Command preserved from source parser. |

### Run commands under a trusted Microsoft signed binary

```text
adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe}
```

Description:

Execute arbitrary commands and binaries from the context of adplus. Note that providing an output directory via '-o' is required.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml` |
| Evidence | Command preserved from source parser. |
