---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0004
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0004-firmware-modification
---

## Description

Changes made to firmware, which may include its settings, configurations, or underlying data. This can encompass alterations to the Master Boot Record (MBR), Volume Boot Record (VBR), or other firmware components critical to system boot and functionality. Such modifications are often indicators of adversary activity, including malware persistence and system compromise. Examples: <br><br>- Changes to Master Boot Record (MBR): Modifying the MBR to load malicious code during the boot process.<br>- Changes to Volume Boot Record (VBR): Altering the VBR to redirect boot processes to malicious locations.<br>- Firmware Configuration Changes: Modifying BIOS/UEFI settings such as disabling Secure Boot.<br>- Firmware Image Tampering: Updating firmware with a malicious or unauthorized image.<br>- Logs or Errors Indicating Firmware Changes: Logs showing unauthorized firmware updates or checksum mismatches.<br><br>This data component can be collected through the following measures:<br><br>- BIOS/UEFI Logs: Enable and monitor BIOS/UEFI logs to capture settings changes or firmware updates.<br>- Firmware Integrity Monitoring: Use tools or firmware security features to detect changes to firmware components.<br>- Endpoint Detection and Response (EDR) Solutions: Many EDR platforms can detect abnormal firmware activity, such as changes to MBR/VBR or unauthorized firmware updates.<br>- File System Monitoring: Monitor changes to MBR/VBR-related files using tools like Sysmon or auditd.<br>    - Windows Example (Sysmon): Monitor Event ID 7 (Raw disk access).<br>    - Linux Example (auditd): `auditctl -w /dev/sda -p wa -k firmware_modification`<br>- Network Traffic Analysis: Capture firmware updates downloaded over the network, particularly from untrusted sources. Use network monitoring tools like Zeek or Wireshark to analyze firmware-related traffic.<br>- Secure Boot Logs: Collect and analyze Secure Boot logs for signs of tampering or unauthorized configurations. Example: Use PowerShell to retrieve Secure Boot settings on Windows: `Confirm-SecureBootUEFI`<br>- Vendor-Specific Firmware Tools: Many hardware vendors provide tools for firmware integrity checks.Examples:<br>    - Intel Platform Firmware Resilience (PFR).<br>    - Lenovo UEFI diagnostics.
