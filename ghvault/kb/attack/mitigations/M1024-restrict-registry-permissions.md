---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1024 - Restrict Registry Permissions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1024` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Restricting registry permissions involves configuring access control settings for sensitive registry keys and hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This mitigation can be implemented through the following measures:

Review and Adjust Permissions on Critical Keys

- Regularly review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access.
- Use tools like `icacls` or `PowerShell` to automate permission adjustments.

Enable Registry Auditing

- Enable auditing on sensitive keys to log access attempts.
- Use Event Viewer or SIEM solutions to analyze logs and detect suspicious activity.
- Example Audit Policy: `auditpol /set /subcategory:"Registry" /success:enable /failure:enable`

Protect Credential-Related Hives

- Limit access to hives like `SAM`,`SECURITY`, and `SYSTEM` to prevent credential dumping or other unauthorized access.
- Use LSA Protection to add an additional security layer for credential storage.

Restrict Registry Editor Usage

- Use Group Policy to restrict access to regedit.exe for non-administrative users.
- Block execution of registry editing tools on endpoints where they are unnecessary.

Deploy Baseline Configuration Tools

- Use tools like Microsoft Security Compliance Toolkit or CIS Benchmarks to apply and maintain secure registry configurations.

*Tools for Implementation* 

Registry Permission Tools:

- Registry Editor (regedit): Built-in tool to manage registry permissions.
- PowerShell: Automate permissions and manage keys. `Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "KeyName" -Value "Value"`
- icacls: Command-line tool to modify ACLs.

Monitoring Tools:

- Sysmon: Monitor and log registry events.
- Event Viewer: View registry access logs.

Policy Management Tools:

- Group Policy Management Console (GPMC): Enforce registry permissions via GPOs.
- Microsoft Endpoint Manager: Deploy configuration baselines for registry permissions.

## Source Verification

[source record](../../sources/mitre/restrict-registry-permissions.md)

## Evidence Excerpt

```text
created: '2019-06-06T20:58:59.577Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Restricting registry permissions involves configuring access control settings for sensitive registry keys and\
\ hives to ensure that only authorized users or processes can make modifications. By limiting access, organizations can\
\ prevent unauthorized changes that adversaries might use for persistence, privilege escalation, or defense evasion. This\
\ mitigation can be implemented through the following measures:\n\nReview and Adjust Permissions on Critical Keys\n\n- Regularly\
\ review permissions on keys such as `Run`, `RunOnce`, and `Services` to ensure only authorized users have write access.\n\
- Use tools like `icacls` or `PowerShell` to automate permission adjustments.\n\nEnable Registry Auditing\n\n- Enable auditing\
```
