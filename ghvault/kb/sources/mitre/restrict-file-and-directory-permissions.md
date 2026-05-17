---
parsed_by: focuslocust
source: mitre
type: generated
---
# Restrict File and Directory Permissions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1022` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Restrict File and Directory Permissions](../../attack/mitigations/M1022-restrict-file-and-directory-permissions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1022 |
| name | Restrict File and Directory Permissions |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1022 |

## Preserved Source Material

```yaml
created: '2019-06-06T20:54:49.964Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Restricting file and directory permissions involves setting access controls at the file system level to limit
  which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations
  can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system
  files.


  Enforce Least Privilege Permissions:


  - Remove unnecessary write permissions on sensitive files and directories.

  - Use file ownership and groups to control access for specific roles.


  Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs.


  Harden File Shares:


  - Disable anonymous access to shared folders.

  - Enforce NTFS permissions for shared folders on Windows.


  Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin`
  on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access.


  On Linux, apply:

  `chmod 750 /etc/sensitive.conf`

  `chown root:admin /etc/sensitive.conf`


  File Integrity Monitoring (FIM):


  - Use tools like Tripwire, Wazuh, or OSSEC to monitor changes to critical file permissions.


  Audit File System Access:


  - Enable auditing to track permission changes or unauthorized access attempts.

  - Use auditd (Linux) or Event Viewer (Windows) to log activities.


  Restrict Startup Directories:


  - Configure permissions to prevent unauthorized writes to directories like `C:\ProgramData\Microsoft\Windows\Start Menu`.


  Example: Restrict write access to critical directories like `/etc/`, `/usr/local/`, and Windows directories such as `C:\Windows\System32`.


  - On Windows, use icacls to modify permissions: `icacls "C:\Windows\System32" /inheritance:r /grant:r SYSTEM:(OI)(CI)F`

  - On Linux, monitor permissions using tools like `lsattr` or `auditd`.'
external_references:
- external_id: M1022
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1022
id: course-of-action--987988f0-cf86-4680-a875-2f6456ab2448
modified: '2024-12-18T19:18:58.856Z'
name: Restrict File and Directory Permissions
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.2'
```
