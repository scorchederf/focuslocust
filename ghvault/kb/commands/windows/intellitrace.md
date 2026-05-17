---
parsed_by: focuslocust
source: commands
type: generated
---
# IntelliTrace Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## IntelliTrace.exe

Tool page: [IntelliTrace.exe](../../tools/windows/intellitrace.exe.md)

### Executes an executable under a trusted microsoft signed binary.

```text
IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe"
```

Description:

Launches an executable via Visual Studio command line utility.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/IntelliTrace.yml` |
| Evidence | Command preserved from source parser. |
