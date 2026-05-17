---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1222 - File and Directory Permissions Modification

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1222` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access protected files. File and directory permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions. File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform which actions (read, write, execute, etc.).

Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or elevated permissions depending on the file or directory’s existing permissions. This may enable malicious activity such as modifying, replacing, or deleting specific files or directories. Specific file and directory modifications may be a required step for many techniques, such as establishing Persistence via Accessibility Features, Boot or Logon Initialization Scripts, Unix Shell Configuration Modification, or tainting/hijacking other instrumental binary/configuration files via Hijack Execution Flow.

Adversaries may also change permissions of symbolic links. For example, malware (particularly ransomware) may modify symbolic links and associated settings to enable access to files from local shortcuts with remote paths.

## Source Verification

[source record](../../sources/mitre/file-and-directory-permissions-modification.md)

## Evidence Excerpt

```text
created: '2018-10-17T00:14:20.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify file or directory permissions/attributes to evade access control lists (ACLs) and access
protected files.(Citation: Hybrid Analysis Icacls1 June 2018)(Citation: Hybrid Analysis Icacls2 May 2018) File and directory
permissions are commonly managed by ACLs configured by the file or directory owner, or users with the appropriate permissions.
File and directory ACL implementations vary by platform, but generally explicitly designate which users or groups can perform
which actions (read, write, execute, etc.).
Modifications may include changing specific access rights, which may require taking ownership of a file or directory and/or
```
