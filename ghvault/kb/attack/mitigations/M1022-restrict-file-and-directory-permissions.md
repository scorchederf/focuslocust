---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1022 - Restrict File and Directory Permissions

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

## Summary

Restricting file and directory permissions involves setting access controls at the file system level to limit which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system files.

Enforce Least Privilege Permissions:

- Remove unnecessary write permissions on sensitive files and directories.
- Use file ownership and groups to control access for specific roles.

Example (Windows): Right-click the shared folder → Properties → Security tab → Adjust permissions for NTFS ACLs.

Harden File Shares:

- Disable anonymous access to shared folders.
- Enforce NTFS permissions for shared folders on Windows.

Example: Set permissions to restrict write access to critical files, such as system executables (e.g., `/bin` or `/sbin` on Linux). Use tools like `chown` and `chmod` to assign file ownership and limit access.

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
- On Linux, monitor permissions using tools like `lsattr` or `auditd`.

## Source Verification

[source record](../../sources/mitre/restrict-file-and-directory-permissions.md)

## Evidence Excerpt

```text
created: '2019-06-06T20:54:49.964Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Restricting file and directory permissions involves setting access controls at the file system level to limit
which users, groups, or processes can read, write, or execute files. By configuring permissions appropriately, organizations
can reduce the attack surface for adversaries seeking to access sensitive data, plant malicious code, or tamper with system
files.
Enforce Least Privilege Permissions:
- Remove unnecessary write permissions on sensitive files and directories.
```
