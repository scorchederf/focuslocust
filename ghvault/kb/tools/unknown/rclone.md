---
parsed_by: focuslocust
source: mitre
type: generated
---
# Rclone

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1040` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Rclone is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. Rclone has been used in a number of ransomware campaigns, including those associated with the Conti and DarkSide Ransomware-as-a-Service operations.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/rclone.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1030 - Data Transfer Size Limits](../../attack/techniques/T1030-data-transfer-size-limits.md) | explicit | source | The [Rclone](https://attack.mitre.org/software/S1040) "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.(Citation: Rclone)(Citation: DFIR Conti Bazar Nov 2021) |
| [T1048.002 - Exfiltration Over Asymmetric Encrypted Non-C2 Protocol](../../attack/techniques/T1048.002-exfiltration-over-asymmetric-encrypted-non-c2-protocol.md) | explicit | source | [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data over SFTP or HTTPS via WebDAV.(Citation: Rclone) |
| [T1048.003 - Exfiltration Over Unencrypted Non-C2 Protocol](../../attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol.md) | explicit | source | [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data over FTP or HTTP, including HTTP via WebDAV.(Citation: Rclone) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Rclone](https://attack.mitre.org/software/S1040) can list files and directories with the `ls`, `lsd`, and `lsl` commands.(Citation: Rclone) |
| [T1560.001 - Archive via Utility](../../attack/techniques/T1560.001-archive-via-utility.md) | explicit | source | [Rclone](https://attack.mitre.org/software/S1040) can compress files using `gzip` prior to exfiltration.(Citation: Rclone) |
| [T1567.002 - Exfiltration to Cloud Storage](../../attack/techniques/T1567.002-exfiltration-to-cloud-storage.md) | explicit | source | [Rclone](https://attack.mitre.org/software/S1040) can exfiltrate data to cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA.(Citation: Rclone)(Citation: DFIR Conti Bazar Nov 2021) |

## Source Verification

[source record](../../sources/mitre/rclone.md)

## Evidence Excerpt

```text
created: '2022-08-30T13:02:36.422Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Rclone](https://attack.mitre.org/software/S1040) is a command line program for syncing files with cloud storage
services such as Dropbox, Google Drive, Amazon S3, and MEGA. [Rclone](https://attack.mitre.org/software/S1040) has been
used in a number of ransomware campaigns, including those associated with the [Conti](https://attack.mitre.org/software/S0575)
and DarkSide Ransomware-as-a-Service operations.(Citation: Rclone)(Citation: Rclone Wars)(Citation: Detecting Rclone)(Citation:
DarkSide Ransomware Gang)(Citation: DFIR Conti Bazar Nov 2021)'
external_references:
```
