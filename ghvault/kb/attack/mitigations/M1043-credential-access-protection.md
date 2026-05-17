---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1043 - Credential Access Protection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1043` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Credential Access Protection focuses on implementing measures to prevent adversaries from obtaining credentials, such as passwords, hashes, tokens, or keys, that could be used for unauthorized access. This involves restricting access to credential storage mechanisms, hardening configurations to block credential dumping methods, and using monitoring tools to detect suspicious credential-related activity. This mitigation can be implemented through the following measures:

Restrict Access to Credential Storage:

- Use Case: Prevent adversaries from accessing the SAM (Security Account Manager) database on Windows systems.
- Implementation: Enforce least privilege principles and restrict administrative access to credential stores such as `C:\Windows\System32\config\SAM`.

Use Credential Guard:

- Use Case: Isolate LSASS (Local Security Authority Subsystem Service) memory to prevent credential dumping.
- Implementation: Enable Windows Defender Credential Guard on enterprise endpoints to isolate secrets and protect them from unauthorized access.

Monitor for Credential Dumping Tools:

- Use Case: Detect and block known tools like Mimikatz or Windows Credential Editor.
- Implementation: Flag suspicious process behavior related to credential dumping.

Disable Cached Credentials:

- Use Case: Prevent adversaries from exploiting cached credentials on endpoints.
- Implementation: Configure group policy to reduce or eliminate the use of cached credentials (e.g., set Interactive logon: Number of previous logons to cache to 0).

Enable Secure Boot and Memory Protections:

- Use Case: Prevent memory-based attacks used to extract credentials.
- Implementation: Configure Secure Boot and enforce hardware-based security features like DEP (Data Execution Prevention) and ASLR (Address Space Layout Randomization).

## Source Verification

[source record](../../sources/mitre/credential-access-protection.md)

## Evidence Excerpt

```text
created: '2019-06-11T16:47:12.859Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Credential Access Protection focuses on implementing measures to prevent adversaries from obtaining credentials,
such as passwords, hashes, tokens, or keys, that could be used for unauthorized access. This involves restricting access
to credential storage mechanisms, hardening configurations to block credential dumping methods, and using monitoring tools
to detect suspicious credential-related activity. This mitigation can be implemented through the following measures:
Restrict Access to Credential Storage:
- Use Case: Prevent adversaries from accessing the SAM (Security Account Manager) database on Windows systems.
```
