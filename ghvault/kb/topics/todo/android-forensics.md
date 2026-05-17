---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Android Forensics

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-todo-android-forensics` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/todo/android-forensics.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

To start extracting data from an Android device it has to be unlocked. If it's locked you can:

## Preserved Body

```markdown
## Locked Device

To start extracting data from an Android device it has to be unlocked. If it's locked you can:

- Check if the device has debugging via USB activated.
- Check for a possible [smudge attack](https://www.usenix.org/legacy/event/woot10/tech/full_papers/Aviv.pdf)
- Try with [Brute-force](https://www.cultofmac.com/316532/this-brute-force-device-can-crack-any-iphones-pin-code/)

## Data Adquisition

Create an [android backup using adb](../mobile-pentesting/android-app-pentesting/adb-commands.md#backup) and extract it using [Android Backup Extractor](https://sourceforge.net/projects/adbextractor/): `java -jar abe.jar unpack file.backup file.tar`

### If root access or physical connection to JTAG interface

- `cat /proc/partitions` (search the path to the flash memory, generally the first entry is _mmcblk0_ and corresponds to the whole flash memory).
- `df /data` (Discover the block size of the system).
- dd if=/dev/block/mmcblk0 of=/sdcard/blk0.img bs=4096 (execute it with the information gathered from the block size).

### Memory

Use Linux Memory Extractor (LiME) to extract the RAM information. It's a kernel extension that should be loaded via adb.
```

## Source Verification

[source record](../../sources/hacktricks/android-forensics.md)

## Evidence Excerpt

```text
_body: '# Android Forensics
{{#include ../banners/hacktricks-training.md}}
## Locked Device
To start extracting data from an Android device it has to be unlocked. If it''s locked you can:
- Check if the device has debugging via USB activated.
- Check for a possible [smudge attack](https://www.usenix.org/legacy/event/woot10/tech/full_papers/Aviv.pdf)
- Try with [Brute-force](https://www.cultofmac.com/316532/this-brute-force-device-can-crack-any-iphones-pin-code/)
## Data Adquisition
```
