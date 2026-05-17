---
parsed_by: focuslocust
source: commands
type: generated
---
# Reg Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Reg.exe

Tool page: [Reg.exe](../../tools/windows/reg.exe.md)

### Hide/plant registry information in Alternate data stream for later use

```text
reg export HKLM\SOFTWARE\Microsoft\Evilreg {PATH_ABSOLUTE}:evilreg.reg
```

Description:

Export the target Registry key and save it to the specified .REG file within an Alternate data stream.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reg.yml` |
| Evidence | Command preserved from source parser. |

### Dump credentials from the Security Account Manager (SAM)

```text
reg save HKLM\SECURITY {PATH_ABSOLUTE:.1.bak} && reg save HKLM\SYSTEM {PATH_ABSOLUTE:.2.bak} && reg save HKLM\SAM {PATH_ABSOLUTE:.3.bak}
```

Description:

Dump registry hives (SAM, SYSTEM, SECURITY) to retrieve password hashes and key material

Related ATT&CK:

- [T1003.002](../../attack/techniques/T1003.002-security-account-manager.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reg.yml` |
| Evidence | Command preserved from source parser. |
