---
parsed_by: focuslocust
source: mitre
type: generated
---
# Drive Creation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0042` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Drive Creation](../../attack/data-sources/DC0042-drive-creation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0042 |
| name | Drive Creation |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0042 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The activity of assigning a new drive letter or creating a mount point for a data storage device, such as a\
  \ USB, network share, or external hard drive, enabling access to its content on a host system. Examples: \n\n- USB Drive\
  \ Insertion: A USB drive is plugged in and automatically assigned the letter `E:\\` on a Windows machine.\n- Network Drive\
  \ Mapping: A network share `\\\\server\\share` is mapped to the drive `Z:\\`.\n- Virtual Drive Creation: A virtual disk\
  \ is mounted on `/mnt/virtualdrive` using an ISO image or a virtual hard disk (VHD).\n- Cloud Storage Mounting: Google Drive\
  \ is mounted as `G:\\` on a Windows machine using a cloud sync tool.\n- External Storage Integration: An external HDD or\
  \ SSD is connected and assigned `/mnt/external` on a Linux system.."
external_references:
- external_id: DC0042
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0042
id: x-mitre-data-component--3d6e6b3b-4aa8-40e1-8c47-91db0f313d9f
modified: '2025-11-12T22:03:39.105Z'
name: Drive Creation
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
  name: Drive
- channel: Kernel-PnP 410/400 device install, disk added
  name: WinEventLog:System
- channel: mknod,open,openat
  name: auditd:SYSCALL
- channel: 'mounted|appeared|DA: disk* attached'
  name: macos:unifiedlog
- channel: EventCode=1006
  name: WinEventLog:System
- channel: Removable media mount notification
  name: auditd:SYSCALL
- channel: com.apple.diskarbitration
  name: macos:unifiedlog
- channel: EventCode=1006, 10001
  name: WinEventLog:System
- channel: device event logs
  name: auditd:SYSCALL
- channel: mount_events
  name: linux:osquery
- channel: Volume Mount + File Read
  name: macos:unifiedlog
- channel: EventCode=2003
  name: WinEventLog:System
- channel: udev events or drive enumeration involving TinyPilot paths or device classes
  name: auditd:SYSCALL
- channel: Device attach logs containing TinyPilot/PiKVM identifiers
  name: linux:syslog
- channel: Hardware enumeration events via IOKit or USBMuxd showing TinyPilot or unknown keyboard/mouse
  name: macos:unifiedlog
- channel: Kernel Device Events - USB Block Devices
  name: auditd:SYSCALL
- channel: mount_events
  name: maos:osquery
- channel: Volume Mount + Process Trace + File Read
  name: macos:unifiedlog
- channel: udisks2 or udevd logs
  name: journald:systemd
- channel: log stream --predicate 'eventMessage contains "USBMSC"'
  name: macos:unifiedlog
- channel: New HID device enumeration with type 'keyboard' followed by immediate input injection
  name: linux:syslog
- channel: New IOUSB keyboard/HID device enumerated with suspicious attributes
  name: macos:unifiedlog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
