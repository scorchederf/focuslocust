---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0054 - Drive Access

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

## Summary

Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive. This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing files within an assigned drive letter (e.g., `C:\`, `/mnt/drive`) or mount point. Examples: 

- Removable Drive Insertion: A USB drive is inserted, assigned the letter `F:\`, and files are accessed.
- Network Drive Mounting: A network share `\\server\share` is mapped to the drive `Z:\`.
- External Hard Drive Access: An external drive is connected, mounted at `/mnt/backup`, and accessed for copying files.
- System Volume Access: The system volume `C:\` is accessed for modifications to critical files.
- Cloud-Synced Drives: Cloud storage drives like OneDrive or Google Drive are accessed via local mounts.

## Source Verification

[source record](../../sources/mitre/drive-access.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Refers to the act of accessing a data storage device, such as a hard drive, SSD, USB, or network-mounted drive.\
\ This data component logs the opening or mounting of drives, capturing activities such as reading, writing, or executing\
\ files within an assigned drive letter (e.g., `C:\\`, `/mnt/drive`) or mount point. Examples: \n\n- Removable Drive Insertion:\
\ A USB drive is inserted, assigned the letter `F:\\`, and files are accessed.\n- Network Drive Mounting: A network share\
\ `\\\\server\\share` is mapped to the drive `Z:\\`.\n- External Hard Drive Access: An external drive is connected, mounted\
\ at `/mnt/backup`, and accessed for copying files.\n- System Volume Access: The system volume `C:\\` is accessed for modifications\
```
