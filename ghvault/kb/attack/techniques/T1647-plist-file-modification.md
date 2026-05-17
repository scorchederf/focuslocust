---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1647 - Plist File Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1647` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the <code>info.plist</code> file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format. 

Adversaries can modify key-value pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. Hidden Window) or running additional commands for persistence (ex: Launch Agent/Launch Daemon or Re-opened Applications).

For example, adversaries can add a malicious application path to the `~/Library/Preferences/com.apple.dock.plist` file, which controls apps that appear in the Dock. Adversaries can also modify the <code>LSUIElement</code> key in an application’s <code>info.plist</code> file  to run the app in the background. Adversaries can also insert key-value pairs to insert environment variables, such as <code>LSEnvironment</code>, to enable persistence via Dynamic Linker Hijacking.

## Source Verification

[source record](../../sources/mitre/plist-file-modification.md)

## Evidence Excerpt

```text
created: '2022-04-09T15:06:32.458Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially\
\ evading and bypassing system defenses. macOS applications use plist files, such as the <code>info.plist</code> file, to\
\ store properties and configuration settings that inform the operating system how to handle the application at runtime.\
\ Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files\
\ can be saved in text or binary format.(Citation: fileinfo plist file description) \n\nAdversaries can modify key-value\
\ pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. [Hidden Window](https://attack.mitre.org/techniques/T1564/003))\
```
