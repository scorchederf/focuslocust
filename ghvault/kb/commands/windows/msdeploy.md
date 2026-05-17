---
parsed_by: focuslocust
source: commands
type: generated
---
# Msdeploy Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Msdeploy.exe

Tool page: [Msdeploy.exe](../../tools/windows/msdeploy.exe.md)

### Local execution of batch file using msdeploy.exe.

```text
msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
```

Description:

Launch .bat file via msdeploy.exe.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msdeploy.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of batch file using msdeploy.exe.

```text
msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}"
```

Description:

Launch .bat file via msdeploy.exe.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msdeploy.yml` |
| Evidence | Command preserved from source parser. |

### Copy file.

```text
msdeploy.exe -verb:sync -source:filePath={PATH_ABSOLUTE:.source.ext} -dest:filePath={PATH_ABSOLUTE:.dest.ext}
```

Description:

Copy file from source to destination.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msdeploy.yml` |
| Evidence | Command preserved from source parser. |
