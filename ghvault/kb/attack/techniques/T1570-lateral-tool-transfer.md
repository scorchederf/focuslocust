---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1570 - Lateral Tool Transfer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1570` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into the victim environment (i.e., Ingress Tool Transfer) files may then be copied from one system to another to stage adversary tools or other files over the course of an operation.

Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols such as file sharing over SMB/Windows Admin Shares to connected network shares or with authenticated connections via Remote Desktop Protocol.

Files can also be transferred using native or otherwise present tools on the victim system, such as scp, rsync, curl, sftp, and ftp. In some cases, adversaries may be able to leverage Web Services such as Dropbox or OneDrive to copy files from one machine to another via shared, automatically synced folders.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [BITSAdmin](../../tools/unknown/bitsadmin.md) | explicit | source | [BITSAdmin](https://attack.mitre.org/software/S0190) can be used to create [BITS Jobs](https://attack.mitre.org/techniques/T1197) to upload and/or download files from SMB file servers.(Citation: Microsoft About BITS) |
| [Expand](../../tools/unknown/expand.md) | explicit | source | [Expand](https://attack.mitre.org/software/S0361) can be used to download or upload a file over a network share.(Citation: LOLBAS Expand) |
| [Impacket](../../tools/unknown/impacket.md) | explicit | source | [Impacket](https://attack.mitre.org/software/S0357) has used its `wmiexec` command, leveraging Windows Management Instrumentation, to remotely stage and execute payloads in victim networks.(Citation: Sygnia VelvetAnt 2024A) |
| [PsExec](../../tools/unknown/psexec.md) | explicit | source | [PsExec](https://attack.mitre.org/software/S0029) can be used to download or upload a file over a network share.(Citation: PsExec Russinovich) |
| [cmd](../../tools/unknown/cmd.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to copy files to/from a remotely connected internal system.(Citation: TechNet Copy) |
| [esentutl](../../tools/unknown/esentutl.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to copy files to/from a remote share.(Citation: LOLBAS Esentutl) |
| [ftp](../../tools/unknown/ftp.md) | explicit | source | [ftp](https://attack.mitre.org/software/S0095) may be abused by adversaries to transfer tools or files between systems within a compromised environment.(Citation: Microsoft FTP)(Citation: Linux FTP) |

## Source Verification

[source record](../../sources/mitre/lateral-tool-transfer.md)

## Evidence Excerpt

```text
created: '2020-03-11T21:01:00.959Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may transfer tools or other files between systems in a compromised environment. Once brought into
the victim environment (i.e., [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) files may then be copied
from one system to another to stage adversary tools or other files over the course of an operation.
Adversaries may copy files between internal victim systems to support lateral movement using inherent file sharing protocols
such as file sharing over [SMB/Windows Admin Shares](https://attack.mitre.org/techniques/T1021/002) to connected network
shares or with authenticated connections via [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001).(Citation:
```
