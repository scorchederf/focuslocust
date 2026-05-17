---
parsed_by: focuslocust
source: mitre
type: generated
---
# Execution Prevention

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1038` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Execution Prevention](../../attack/mitigations/M1038-execution-prevention.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1038 |
| name | Execution Prevention |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1038 |

## Preserved Source Material

```yaml
created: '2019-06-11T16:35:25.488Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Prevent the execution of unauthorized or malicious code on systems by implementing application control, script\
  \ blocking, and other execution prevention mechanisms. This ensures that only trusted and authorized code is executed, reducing\
  \ the risk of malware and unauthorized actions. This mitigation can be implemented through the following measures:\n\nApplication\
  \ Control:\n\n- Use Case: Use tools like AppLocker or Windows Defender Application Control (WDAC) to create whitelists of\
  \ authorized applications and block unauthorized ones. On Linux, use tools like SELinux or AppArmor to define mandatory\
  \ access control policies for application execution.\n- Implementation: Allow only digitally signed or pre-approved applications\
  \ to execute on servers and endpoints. (e.g., `New-AppLockerPolicy -PolicyType Enforced -FilePath \"C:\\Policies\\AppLocker.xml\"\
  `) \n\n\nScript Blocking:\n\n- Use Case: Use script control mechanisms to block unauthorized execution of scripts, such\
  \ as PowerShell or JavaScript. Web Browsers: Use browser extensions or settings to block JavaScript execution from untrusted\
  \ sources.\n- Implementation: Configure PowerShell to enforce Constrained Language Mode for non-administrator users. (e.g.,\
  \ `Set-ExecutionPolicy AllSigned`) \n\nExecutable Blocking:\n\n- Use Case: Prevent execution of binaries from suspicious\
  \ locations, such as `%TEMP%` or `%APPDATA%` directories.\n- Implementation: Block execution of `.exe`, `.bat`, or `.ps1`\
  \ files from user-writable directories.\n\nDynamic Analysis Prevention:\n- Use Case: Use behavior-based execution prevention\
  \ tools to identify and block malicious activity in real time.\n- Implemenation: Employ EDR solutions that analyze runtime\
  \ behavior and block suspicious code execution."
external_references:
- external_id: M1038
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1038
id: course-of-action--47e0e9fe-96ce-4f65-8bb1-8be1feacb5db
modified: '2024-12-11T18:10:27.976Z'
name: Execution Prevention
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
x_mitre_version: '1.3'
```
