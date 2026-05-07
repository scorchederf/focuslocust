---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0059
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0059-file-metadata
---

## Description

contextual information about a file, including attributes such as the file's name, size, type, content (e.g., signatures, headers, media), user/owner, permissions, timestamps, and other related properties. File metadata provides insights into a file's characteristics and can be used to detect malicious activity, unauthorized modifications, or other anomalies. Examples: <br><br>- File Ownership and Permissions: Checking the owner and permissions of a critical configuration file like /etc/passwd on Linux or C:\Windows\System32\config\SAM on Windows.<br>- Timestamps: Analyzing the creation, modification, and access timestamps of a file.<br>- File Content and Signatures: Extracting the headers of an executable file to verify its signature or detect packing/obfuscation.<br>- File Attributes: Analyzing attributes like hidden, system, or read-only flags in Windows.<br>- File Hashes: Generating MD5, SHA-1, or SHA-256 hashes of files to compare against threat intelligence feeds.<br>- File Location: Monitoring files located in unusual directories or paths, such as temporary or user folders.
