---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S1040
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1040-rclone
---

## Description

[[kb/mitre/attack/software/S1040-rclone|Rclone]] is a command line program for syncing files with cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA. [[kb/mitre/attack/software/S1040-rclone|Rclone]] has been used in a number of ransomware campaigns, including those associated with the Conti and DarkSide Ransomware-as-a-Service operations.[^4] [^3] [^1] [^5] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1030-data-transfer-size-limits\|T1030]] | Data Transfer Size Limits | The [[kb/mitre/attack/software/S1040-rclone\|Rclone]] "chunker" overlay supports splitting large files in smaller chunks during upload to circumvent size limits.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1048.002-exfiltration-over-asymmetric-encrypted-non-c2-protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | [[kb/mitre/attack/software/S1040-rclone\|Rclone]] can exfiltrate data over SFTP or HTTPS via WebDAV.[^1]  |
| [[kb/mitre/attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol | [[kb/mitre/attack/software/S1040-rclone\|Rclone]] can exfiltrate data over FTP or HTTP, including HTTP via WebDAV.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S1040-rclone\|Rclone]] can list files and directories with the `ls`, `lsd`, and `lsl` commands.[^1]  |
| [[kb/mitre/attack/techniques/T1560.001-archive-via-utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S1040-rclone\|Rclone]] can compress files using `gzip` prior to exfiltration.[^1]  |
| [[kb/mitre/attack/techniques/T1567.002-exfiltration-to-cloud-storage\|T1567.002]] | Exfiltration to Cloud Storage | [[kb/mitre/attack/software/S1040-rclone\|Rclone]] can exfiltrate data to cloud storage services such as Dropbox, Google Drive, Amazon S3, and MEGA.[^2] [^1]  |

 [^1]: [Detecting Rclone](https://research.nccgroup.com/2021/05/27/detecting-rclone-an-effective-tool-for-exfiltration/)
 [^2]: [DFIR Conti Bazar Nov 2021](https://thedfirreport.com/2021/11/29/continuing-the-bazar-ransomware-story/)
 [^3]: [Rclone Wars](https://redcanary.com/blog/rclone-mega-extortion/)
 [^4]: [Rclone](https://rclone.org)
 [^5]: [DarkSide Ransomware Gang](https://unit42.paloaltonetworks.com/darkside-ransomware/)
