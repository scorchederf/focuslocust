---
parsed_by: focuslocust
source: mitre
type: generated
---
# Drive Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0054` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Drive Access](../../attack/data-sources/DC0054-drive-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0054 |
| name | Drive Access |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0054 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive.\
  \ This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing\
  \ files within an assigned drive letter (e.g., `C:\\`, `/mnt/drive`) or mount point. Examples: \n\n- Removable Drive Insertion:\
  \ A USB drive is inserted, assigned the letter `F:\\`, and files are accessed.\n- Network Drive Mounting: A network share\
  \ `\\\\server\\share` is mapped to the drive `Z:\\`.\n- External Hard Drive Access: An external drive is connected, mounted\
  \ at `/mnt/backup`, and accessed for copying files.\n- System Volume Access: The system volume `C:\\` is accessed for modifications\
  \ to critical files.\n- Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts."
external_references:
- external_id: DC0054
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0054
id: x-mitre-data-component--73ff2dcc-24b1-4368-b9dc-706dd9e68354
modified: '2025-11-12T22:03:39.105Z'
name: Drive Access
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: EventCode=9
  name: WinEventLog:Sysmon
- channel: open/write syscalls on /dev/sd* or /dev/nvme*
  name: auditd:SYSCALL
- channel: write syscalls to /dev/sd* targeting offset 0
  name: auditd:SYSCALL
- channel: open/write syscalls to block devices (/dev/sd*, /dev/nvme*)
  name: auditd:SYSCALL
- channel: mount/umount or file copy logs
  name: linux:syslog
- channel: open/read/mount operations
  name: fs:fsusage
- channel: hardware_events
  name: linux:osquery
- channel: usb_devices
  name: macos:osquery
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
