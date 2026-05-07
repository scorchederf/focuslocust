---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0054
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0054-drive-access
---

## Description

Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive. This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing files within an assigned drive letter (e.g., `C:\`, `/mnt/drive`) or mount point. Examples: <br><br>- Removable Drive Insertion: A USB drive is inserted, assigned the letter `F:\`, and files are accessed.<br>- Network Drive Mounting: A network share `\\server\share` is mapped to the drive `Z:\`.<br>- External Hard Drive Access: An external drive is connected, mounted at `/mnt/backup`, and accessed for copying files.<br>- System Volume Access: The system volume `C:\` is accessed for modifications to critical files.<br>- Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts.
