---
parsed_by: focuslocust
source: commands
type: generated
---
# Odbcconf Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Odbcconf.exe

Tool page: [Odbcconf.exe](../../tools/windows/odbcconf.exe.md)

### Execute a DLL file using technique that can evade defensive counter measures

```text
odbcconf /a {REGSVR {PATH_ABSOLUTE:.dll}}
```

Description:

Execute DllRegisterServer from DLL specified.

Related ATT&CK:

- [T1218.008](../../attack/techniques/T1218.008-odbcconf.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Odbcconf.yml` |
| Evidence | Command preserved from source parser. |

### Execute dll file using technique that can evade defensive counter measures

```text
odbcconf INSTALLDRIVER "lolbas-project|Driver={PATH_ABSOLUTE:.dll}|APILevel=2"
odbcconf configsysdsn "lolbas-project" "DSN=lolbas-project"
```

Description:

Install a driver and load the DLL. Requires administrator privileges.

Related ATT&CK:

- [T1218.008](../../attack/techniques/T1218.008-odbcconf.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Odbcconf.yml` |
| Evidence | Command preserved from source parser. |

### Execute dll file using technique that can evade defensive counter measures

```text
odbcconf -f {PATH:.rsp}
```

Description:

Load DLL specified in target .RSP file. See the Code Sample section for an example .RSP file.

Related ATT&CK:

- [T1218.008](../../attack/techniques/T1218.008-odbcconf.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Odbcconf.yml` |
| Evidence | Command preserved from source parser. |
