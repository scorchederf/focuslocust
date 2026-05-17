---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0061 - File Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0061` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware, or adversarial modifications). Examples: 

- Content Modifications: Changes to the content of a configuration file, such as modifying `/etc/ssh/sshd_config` on Linux or `C:\Windows\System32\drivers\etc\hosts` on Windows.
- Permission Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying NTFS permissions on Windows.
- Attribute Modifications: Changing a file's attributes to hidden, read-only, or system on Windows.
- Timestamp Manipulation: Adjusting a file's creation or modification timestamp using tools like `touch` in Linux or timestomping tools on Windows.
- Software or System File Changes: Modifying system files such as `boot.ini`, kernel modules, or application binaries.

## Source Verification

[source record](../../sources/mitre/file-modification.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These\
\ modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware,\
\ or adversarial modifications). Examples: \n\n- Content Modifications: Changes to the content of a configuration file,\
\ such as modifying `/etc/ssh/sshd_config` on Linux or `C:\\Windows\\System32\\drivers\\etc\\hosts` on Windows.\n- Permission\
\ Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying\
\ NTFS permissions on Windows.\n- Attribute Modifications: Changing a file's attributes to hidden, read-only, or system\
```
