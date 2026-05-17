---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS AppleFS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-applefs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-applefs.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS AppleFS](../../topics/macos-hardening/macos-applefs.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-applefs |
| name | macOS AppleFS |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-security-and-privilege-escalation/macos-applefs.md |

## Preserved Source Material

````yaml
_body: "# macOS AppleFS\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Apple Propietary File System (APFS)\n\n\
  **Apple File System (APFS)** is a modern file system designed to supersede the Hierarchical File System Plus (HFS+). Its\
  \ development was driven by the need for **improved performance, security, and efficiency**.\n\nSome notable features of\
  \ APFS include:\n\n1. **Space Sharing**: APFS allows multiple volumes to **share the same underlying free storage** on a\
  \ single physical device. This enables more efficient space utilization as the volumes can dynamically grow and shrink without\
  \ the need for manual resizing or repartitioning.\n   1. This means, compared with traditional partitions in file disks,\
  \ **that in APFS different partitions (volumes) shares all the disk space**, while a regular partition usually had a fixed\
  \ size.\n2. **Snapshots**: APFS supports **creating snapshots**, which are **read-only**, point-in-time instances of the\
  \ file system. Snapshots enable efficient backups and easy system rollbacks, as they consume minimal additional storage\
  \ and can be quickly created or reverted.\n3. **Clones**: APFS can **create file or directory clones that share the same\
  \ storage** as the original until either the clone or the original file is modified. This feature provides an efficient\
  \ way to create copies of files or directories without duplicating the storage space.\n4. **Encryption**: APFS **natively\
  \ supports full-disk encryption** as well as per-file and per-directory encryption, enhancing data security across different\
  \ use cases.\n5. **Crash Protection**: APFS uses a **copy-on-write metadata scheme that ensures file system consistency**\
  \ even in cases of sudden power loss or system crashes, reducing the risk of data corruption.\n\nOverall, APFS offers a\
  \ more modern, flexible, and efficient file system for Apple devices, with a focus on improved performance, reliability,\
  \ and security.\n\n```bash\ndiskutil list # Get overview of the APFS volumes\n```\n\n## Firmlinks\n\nThe `Data` volume is\
  \ mounted in **`/System/Volumes/Data`** (you can check this with `diskutil apfs list`).\n\nThe list of firmlinks can be\
  \ found in the **`/usr/share/firmlinks`** file.\n\n```bash\n\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: macos-hardening/macos-security-and-privilege-escalation/macos-applefs.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-applefs.md
````
