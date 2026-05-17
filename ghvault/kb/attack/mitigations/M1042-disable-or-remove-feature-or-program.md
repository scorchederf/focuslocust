---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1042 - Disable or Remove Feature or Program

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1042` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 

Remove Legacy Software:

- Use Case: Disable or remove older versions of software that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash).
- Implementation: A company removes Flash Player from all employee systems after it has reached its end-of-life date.

Disable Unused Features:

- Use Case: Turn off unnecessary operating system features like SMBv1, Telnet, or RDP if they are not required.
- Implementation: Disable SMBv1 in a Windows environment to mitigate vulnerabilities like EternalBlue.

Control Applications Installed by Users:

- Use Case: Prevent users from installing unauthorized software via group policies or other management tools.
- Implementation: Block user installations of unauthorized file-sharing applications (e.g., BitTorrent clients) in an enterprise environment.

Remove Unnecessary Services:

- Use Case: Identify and disable unnecessary default services running on endpoints, servers, or network devices.
- Implementation: Disable unused administrative shares (e.g., C$, ADMIN$) on workstations.

Restrict Add-ons and Plugins:

- Use Case: Remove or disable browser plugins and add-ons that are not needed for business purposes.
- Implementation: Disable Java and ActiveX plugins in web browsers to prevent drive-by attacks.

## Source Verification

[source record](../../sources/mitre/disable-or-remove-feature-or-program.md)

## Evidence Excerpt

```text
created: '2019-06-11T16:45:19.740Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack\
\ surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or\
\ that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented\
\ through the following measures: \n\nRemove Legacy Software:\n\n- Use Case: Disable or remove older versions of software\
\ that no longer receive updates or security patches (e.g., legacy Java, Adobe Flash).\n- Implementation: A company removes\
\ Flash Player from all employee systems after it has reached its end-of-life date.\n\nDisable Unused Features:\n\n- Use\
```
