---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0061
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0061-file-modification
---

## Description

Changes made to a file, including updates to its contents, metadata, access permissions, or attributes. These modifications may indicate legitimate activity (e.g., software updates) or unauthorized changes (e.g., tampering, ransomware, or adversarial modifications). Examples: <br><br>- Content Modifications: Changes to the content of a configuration file, such as modifying `/etc/ssh/sshd_config` on Linux or `C:\Windows\System32\drivers\etc\hosts` on Windows.<br>- Permission Changes: Altering file permissions to allow broader access, such as changing a file from `644` to `777` on Linux or modifying NTFS permissions on Windows.<br>- Attribute Modifications: Changing a file's attributes to hidden, read-only, or system on Windows.<br>- Timestamp Manipulation: Adjusting a file's creation or modification timestamp using tools like `touch` in Linux or timestomping tools on Windows.<br>- Software or System File Changes: Modifying system files such as `boot.ini`, kernel modules, or application binaries.
