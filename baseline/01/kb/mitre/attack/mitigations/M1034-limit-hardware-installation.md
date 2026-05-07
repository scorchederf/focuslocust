---
generated_by: focuslocust
source: mitre
type: mitigation
aliases:
    - M1034
tags:
    - attack/domain/enterprise_attack
    - attack/type/mitigation
mitre-attack: kb/mitre/attack/mitigations/M1034-limit-hardware-installation
---

## Description

Prevent unauthorized users or groups from installing or using hardware, such as external drives, peripheral devices, or unapproved internal hardware components, by enforcing hardware usage policies and technical controls. This includes disabling USB ports, restricting driver installation, and implementing endpoint security tools to monitor and block unapproved devices. This mitigation can be implemented through the following measures:<br><br>Disable USB Ports and Hardware Installation Policies:<br><br>- Use Group Policy Objects (GPO) to disable USB mass storage devices:<br>     - Navigate to Computer Configuration > Administrative Templates > System > Removable Storage Access.<br>     - Deny write and read access to USB devices.<br>- Whitelist approved devices using unique serial numbers via Windows Device Installation Policies.<br><br>Deploy Endpoint Protection and Device Control Solutions:<br><br>- Use tools like Microsoft Defender for Endpoint, Symantec Endpoint Protection, or Tanium to monitor and block unauthorized hardware.<br>- Implement device control policies to allow specific hardware types (e.g., keyboards, mice) and block others.<br><br>Harden BIOS/UEFI and System Firmware:<br><br>- Set strong passwords for BIOS/UEFI access.<br>- Enable Secure Boot to prevent rogue hardware components from loading unauthorized firmware.<br><br>Restrict Peripheral Devices and Drivers:<br><br>- Use Windows Device Manager Policies to block installation of unapproved drivers.<br>- Monitor hardware installation attempts through endpoint monitoring tools.<br><br>Disable Bluetooth and Wireless Hardware:<br><br>- Use GPO or MDM tools to disable Bluetooth and Wi-Fi interfaces across systems.<br>- Restrict hardware pairing to approved devices only.<br><br>Logging and Monitoring:<br><br>- Enable logging for hardware installation events in Windows Event Logs (Event ID 20001 for Device Setup Manager).<br>- Use SIEM solutions (e.g., Splunk, Elastic Stack) to detect unauthorized hardware installation activities.<br><br>*Tools for Implementation*<br><br>USB and Device Control:<br><br>- Microsoft Group Policy Objects (GPO)<br>- Microsoft Defender for Endpoint<br>- Symantec Endpoint Protection<br>- McAfee Device Control<br><br>Endpoint Monitoring:<br><br>- EDRs<br>- OSSEC (open-source host-based IDS)<br><br>Hardware Whitelisting:<br><br>- BitLocker for external drives (Windows)<br>- Windows Device Installation Policies<br>- Device Control <br><br>BIOS/UEFI Security:<br><br>- Secure Boot (Windows/Linux)<br>Firmware management tools like Dell Command Update or HP Sure Start

## Techniques Addressed by Mitigation
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1052-exfiltration-over-physical-medium\|T1052]] | Exfiltration Over Physical Medium | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/techniques/T1052.001-exfiltration-over-usb\|T1052.001]] | Exfiltration over USB | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/techniques/T1091-replication-through-removable-media\|T1091]] | Replication Through Removable Media | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/techniques/T1200-hardware-additions\|T1200]] | Hardware Additions | Block unknown devices and accessories by endpoint security configuration and monitoring agent. |
| [[kb/mitre/attack/techniques/T1219-remote-access-tools\|T1219]] | Remote Access Tools | Block the use of IP-based KVM devices within the network if they are not required.  |
| [[kb/mitre/attack/techniques/T1219.003-remote-access-hardware\|T1219.003]] | Remote Access Hardware | Block the use of IP-based KVM devices within the network if they are not required.  |
| [[kb/mitre/attack/techniques/T1674-input-injection\|T1674]] | Input Injection | Limit the use of USB devices and removable media within a network. |
