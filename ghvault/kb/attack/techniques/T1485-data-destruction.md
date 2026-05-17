---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1485 - Data Destruction

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1485` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic techniques through overwriting files or data on local and remote drives. Common operating system file deletion commands such as <code>del</code> and <code>rm</code> often only remove pointers to files without wiping the contents of the files themselves, making the files recoverable by proper forensic methodology. This behavior is distinct from Disk Content Wipe and Disk Structure Wipe because individual files are destroyed rather than sections of a storage disk or the disk's logical structure.

Adversaries may attempt to overwrite files and directories with randomly generated data to make it irrecoverable. In some cases politically oriented image files have been used to overwrite data.

To maximize impact on the target organization in operations where network-wide availability interruption is the goal, malware designed for destroying data may have worm-like features to propagate across a network by leveraging additional techniques like Valid Accounts, OS Credential Dumping, and SMB/Windows Admin Shares..

In cloud environments, adversaries may leverage access to delete cloud storage objects, machine images, database instances, and other infrastructure crucial to operations to damage an organization or their customers. Similarly, they may delete virtual machines from on-prem virtualized environments.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Cipher.exe](../../tools/windows/cipher.exe.md) | explicit | source | Command metadata lists T1485: cipher /w:{PATH_ABSOLUTE:folder} |
| [Fsutil.exe](../../tools/windows/fsutil.exe.md) | explicit | source | Command metadata lists T1485: fsutil.exe usn deletejournal /d c: |
| [RawDisk](../../tools/unknown/rawdisk.md) | explicit | source | [RawDisk](https://attack.mitre.org/software/S0364) was used in [Shamoon](https://attack.mitre.org/software/S0140) to write to protected system locations such as the MBR and disk partitions in an effort to destroy data.(Citation: Palo Alto Shamoon Nov 2016)(Citation: Unit 42 Shamoon3 2018) |
| [SDelete](../../tools/unknown/sdelete.md) | explicit | source | [SDelete](https://attack.mitre.org/software/S0195) deletes data in a way that makes it unrecoverable.(Citation: Microsoft SDelete July 2016) |

## Source Verification

[source record](../../sources/mitre/data-destruction.md)

## Evidence Excerpt

```text
created: '2019-03-14T18:47:17.701Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may destroy data and files on specific systems or in large numbers on a network to interrupt availability
to systems, services, and network resources. Data destruction is likely to render stored data irrecoverable by forensic
techniques through overwriting files or data on local and remote drives.(Citation: Symantec Shamoon 2012)(Citation: FireEye
Shamoon Nov 2016)(Citation: Palo Alto Shamoon Nov 2016)(Citation: Kaspersky StoneDrill 2017)(Citation: Unit 42 Shamoon3
2018)(Citation: Talos Olympic Destroyer 2018) Common operating system file deletion commands such as <code>del</code> and
<code>rm</code> often only remove pointers to files without wiping the contents of the files themselves, making the files
```
