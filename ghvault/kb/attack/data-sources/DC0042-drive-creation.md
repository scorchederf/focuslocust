---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0042 - Drive Creation

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

## Summary

The activity of assigning a new drive letter or creating a mount point for a data storage device, such as a USB, network share, or external hard drive, enabling access to its content on a host system. Examples: 

- USB Drive Insertion: A USB drive is plugged in and automatically assigned the letter `E:\` on a Windows machine.
- Network Drive Mapping: A network share `\\server\share` is mapped to the drive `Z:\`.
- Virtual Drive Creation: A virtual disk is mounted on `/mnt/virtualdrive` using an ISO image or a virtual hard disk (VHD).
- Cloud Storage Mounting: Google Drive is mounted as `G:\` on a Windows machine using a cloud sync tool.
- External Storage Integration: An external HDD or SSD is connected and assigned `/mnt/external` on a Linux system..

## Source Verification

[source record](../../sources/mitre/drive-creation.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The activity of assigning a new drive letter or creating a mount point for a data storage device, such as a\
\ USB, network share, or external hard drive, enabling access to its content on a host system. Examples: \n\n- USB Drive\
\ Insertion: A USB drive is plugged in and automatically assigned the letter `E:\\` on a Windows machine.\n- Network Drive\
\ Mapping: A network share `\\\\server\\share` is mapped to the drive `Z:\\`.\n- Virtual Drive Creation: A virtual disk\
\ is mounted on `/mnt/virtualdrive` using an ISO image or a virtual hard disk (VHD).\n- Cloud Storage Mounting: Google Drive\
\ is mounted as `G:\\` on a Windows machine using a cloud sync tool.\n- External Storage Integration: An external HDD or\
```
