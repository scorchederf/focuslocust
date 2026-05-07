---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0046
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0046-drive-modification
---

## Description

The alteration of a drive letter, mount point, or other attributes of a data storage device, which could involve reassignment, renaming, permissions changes, or other modifications. Examples: <br><br>- Drive Letter Reassignment: A USB drive previously assigned `E:\` is reassigned to `D:\` on a Windows machine.<br>- Mount Point Change: On a Linux system, a mounted storage device at `/mnt/external` is moved to `/mnt/storage`.<br>- Drive Permission Changes: A shared drive's permissions are modified to allow write access for unauthorized users or processes.<br>- Renaming of a Drive: A network drive labeled "HR_Share" is renamed to "Shared_Resources."<br>- Modification of Cloud-Integrated Drives: A cloud storage mount such as Google Drive is modified to sync only specific folders.<br><br>This data component can be collected through the following measures:<br><br>Windows Event Logs<br><br>- Relevant Events:<br>    - Event ID 98: Indicates changes to a volume (e.g., drive letter reassignment).<br>    - Event ID 1006: Logs permission modifications or changes to removable storage.<br>- Configuration: Enable "Storage Operational Logs" in the Event Viewer:<br>`Applications and Services Logs > Microsoft > Windows > Storage-Tiering > Operational`<br><br>Linux System Logs<br><br>- Auditd Configuration: Add audit rules to track changes to mounted drives: `auditctl -w /mnt/ -p w -k drive_modification`<br>- Command-Line Monitoring: Use `dmesg` or `journalctl` to observe drive modifications.<br><br>macOS System Logs<br><br>- Unified Logs: Collect mount or drive modification events: `log show --info | grep "Volume modified"`<br>- Command-Line Monitoring: Use `diskutil` to track changes:<br><br>Endpoint Detection and Response (EDR) Tools<br><br>- Configure policies in EDR solutions to monitor and log changes to drive configurations or attributes.<br><br>SIEM Tools<br><br>- Aggregate logs from multiple systems into a centralized platform like Splunk to correlate events and alert on suspicious drive modification activities.<br>
