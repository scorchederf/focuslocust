---
parsed_by: focuslocust
source: mitre
type: generated
---
# Environment Variable Permissions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1039` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Environment Variable Permissions](../../attack/mitigations/M1039-environment-variable-permissions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1039 |
| name | Environment Variable Permissions |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1039 |

## Preserved Source Material

```yaml
created: '2019-06-11T16:40:14.543Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Restrict the modification of environment variables to authorized users and processes by enforcing strict permissions
  and policies. This ensures the integrity of environment variables, preventing adversaries from abusing or altering them
  for malicious purposes. This mitigation can be implemented through the following measures:


  Restrict Write Access:


  - Use Case: Set file system-level permissions to restrict access to environment variable configuration files (e.g., `.bashrc`,
  `.bash_profile`, `.zshrc`, `systemd` service files).

  - Implementation: Configure `/etc/environment` or `/etc/profile` on Linux systems to only allow root or administrators to
  modify the file.


  Secure Access Controls:


  - Use Case: Limit access to environment variable settings in application deployment tools or CI/CD pipelines to authorized
  personnel.

  - Implementation: Use role-based access control (RBAC) in tools like Jenkins or GitLab to ensure only specific users can
  modify environment variables.


  Restrict Process Scope:


  - Use Case: Configure policies to ensure environment variables are only accessible to the processes they are explicitly
  intended for.

  - Implementation: Use containerized environments like Docker to isolate environment variables to specific containers and
  ensure they are not inherited by other processes.


  Audit Environment Variable Changes:


  - Use Case: Enable logging for changes to critical environment variables.

  - Implementation: Use `auditd` on Linux to monitor changes to files like `/etc/environment` or application-specific environment
  files.'
external_references:
- external_id: M1039
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1039
id: course-of-action--609191bf-7d06-40e4-b1f8-9e11eb3ff8a6
modified: '2024-12-11T17:54:05.697Z'
name: Environment Variable Permissions
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
x_mitre_version: '1.1'
```
