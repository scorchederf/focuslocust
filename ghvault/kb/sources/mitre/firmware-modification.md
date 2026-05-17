---
parsed_by: focuslocust
source: mitre
type: generated
---
# Firmware Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Firmware Modification](../../attack/data-sources/DC0004-firmware-modification.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0004 |
| name | Firmware Modification |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0004 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to firmware, which may include its settings, configurations, or underlying data. This can encompass\
  \ alterations to the Master Boot Record (MBR), Volume Boot Record (VBR), or other firmware components critical to system\
  \ boot and functionality. Such modifications are often indicators of adversary activity, including malware persistence and\
  \ system compromise. Examples: \n\n- Changes to Master Boot Record (MBR): Modifying the MBR to load malicious code during\
  \ the boot process.\n- Changes to Volume Boot Record (VBR): Altering the VBR to redirect boot processes to malicious locations.\n\
  - Firmware Configuration Changes: Modifying BIOS/UEFI settings such as disabling Secure Boot.\n- Firmware Image Tampering:\
  \ Updating firmware with a malicious or unauthorized image.\n- Logs or Errors Indicating Firmware Changes: Logs showing\
  \ unauthorized firmware updates or checksum mismatches.\n\nThis data component can be collected through the following measures:\n\
  \n- BIOS/UEFI Logs: Enable and monitor BIOS/UEFI logs to capture settings changes or firmware updates.\n- Firmware Integrity\
  \ Monitoring: Use tools or firmware security features to detect changes to firmware components.\n- Endpoint Detection and\
  \ Response (EDR) Solutions: Many EDR platforms can detect abnormal firmware activity, such as changes to MBR/VBR or unauthorized\
  \ firmware updates.\n- File System Monitoring: Monitor changes to MBR/VBR-related files using tools like Sysmon or auditd.\n\
  \    - Windows Example (Sysmon): Monitor Event ID 7 (Raw disk access).\n    - Linux Example (auditd): `auditctl -w /dev/sda\
  \ -p wa -k firmware_modification`\n- Network Traffic Analysis: Capture firmware updates downloaded over the network, particularly\
  \ from untrusted sources. Use network monitoring tools like Zeek or Wireshark to analyze firmware-related traffic.\n- Secure\
  \ Boot Logs: Collect and analyze Secure Boot logs for signs of tampering or unauthorized configurations. Example: Use PowerShell\
  \ to retrieve Secure Boot settings on Windows: `Confirm-SecureBootUEFI`\n- Vendor-Specific Firmware Tools: Many hardware\
  \ vendors provide tools for firmware integrity checks.Examples:\n    - Intel Platform Firmware Resilience (PFR).\n    -\
  \ Lenovo UEFI diagnostics."
external_references:
- external_id: DC0004
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0004
id: x-mitre-data-component--b9d031bb-d150-4fc6-8025-688201bf3ffd
modified: '2025-10-21T15:14:38.020Z'
name: Firmware Modification
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- ics-attack
- enterprise-attack
x_mitre_log_sources:
- channel: None
  name: Firmware
- channel: Image Upgrade / Configuration Change
  name: networkdevice:syslog
- channel: Boot image path or firmware configuration variable modified outside of maintenance windows
  name: networkdevice:config
- channel: Firmware integrity validation failed or boot configuration tampered
  name: WinEventLog:Microsoft-Windows-Kernel-Boot
- channel: write access to /dev/mem or /sys/firmware/efi/efivars
  name: auditd:SYSCALL
- channel: boot failure events or SMC validation errors
  name: macos:unifiedlog
- channel: Firmware update initiated or bootloader tampering detected
  name: networkdevice:firmware
- channel: Log entries indicating ROMMON image upgrade commands (boot system, upgrade rom-monitor)
  name: networkdevice:config
- channel: Boot variable modified to point to non-standard or unsigned image
  name: networkdevice:config
- channel: Firmware integrity verification failures or mismatches against expected UEFI/firmware image baselines
  name: 'firmware:integrity '
- channel: 'ioctl/write: Direct firmware update or device memory manipulation syscalls'
  name: auditd:SYSCALL
- channel: Unexpected firmware-level errors or abnormal S.M.A.R.T. log entries
  name: firmware:smart
- channel: Firmware update events or kernel extension (kext) loads not signed by Apple
  name: macos:unifiedlog
- channel: Baseline mismatch or unexpected EFI module detected during integrity checks
  name: firmware:integrity
- channel: Unexpected changes in EFI or NVRAM variables controlling hardware boot state
  name: macos:osquery
- channel: Custom firmware or routing changes
  name: networkdevice:syslog
- channel: Raw disk I/O operations bypassing NTFS APIs
  name: etw:Microsoft-Windows-Kernel-Storage
- channel: Debug or memory access commands indicating attempts to alter OS instructions in memory
  name: firmware:runtime
- channel: Boot information log showing image loaded from TFTP server instead of local storage
  name: networkdevice:syslog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
