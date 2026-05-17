---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0059 - File Metadata

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0059` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: 

- File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows.
- Timestamps: Analyzing the creation, modification, and access timestamps of a file.
- File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation.
- File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows.
- File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds.
- File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.

## Source Verification

[source record](../../sources/mitre/file-metadata.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.273Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "contextual information about a file, including attributes such as the file's name, size, type, content (e.g.,\
\ signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides\
\ insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other\
\ anomalies. Examples: \n\n- File Ownership and Permissions: Checking the owner and permissions of a critical configuration\
\ file like /etc/passwd on Linux or C:\\Windows\\System32\\config\\SAM on Windows.\n- Timestamps: Analyzing the creation,\
\ modification, and access timestamps of a file.\n- File Content and Signatures: Extracting the headers of an executable\
```
