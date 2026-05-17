---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1135 - Network Share Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1135` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol.   Net can be used to query a remote system for available shared drives using the <code>net view \\\\remotesystem</code> command. It can also be used to query shared drives on the local system using <code>net share</code>. For macOS, the <code>sharing -l</code> command lists all shared points used for smb services.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can enumerate the shared folders and associated permissions for a targeted network.(Citation: CME Github September 2018) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can find shared drives on the local system.(Citation: Github PowerShell Empire) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can scan local network for open SMB.(Citation: Github Koadic) |
| [Net](../../tools/unknown/net.md) | explicit | source | The <code>net view \\remotesystem</code> and <code>net share</code> commands in [Net](https://attack.mitre.org/software/S0039) can be used to find shared drives and directories on remote and local systems respectively.(Citation: Savill 1999) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can list local and remote shared drives and folders over SMB.(Citation: GitHub Pupy) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate shares on a compromised host.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/network-share-discovery.md)

## Evidence Excerpt

```text
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information\
\ to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often\
\ contain shared network drives and folders that enable users to access file directories on various systems across a network.\
\ \n\nFile sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation:\
\ TechNet Shared Folder) [Net](https://attack.mitre.org/software/S0039) can be used to query a remote system for available\
\ shared drives using the <code>net view \\\\\\\\remotesystem</code> command. It can also be used to query shared drives\
```
