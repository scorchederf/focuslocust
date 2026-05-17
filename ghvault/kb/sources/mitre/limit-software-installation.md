---
parsed_by: focuslocust
source: mitre
type: generated
---
# Limit Software Installation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1033` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Limit Software Installation](../../attack/mitigations/M1033-limit-software-installation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1033 |
| name | Limit Software Installation |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1033 |

## Preserved Source Material

```yaml
created: '2019-06-11T16:26:52.202Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Prevent users or groups from installing unauthorized or unapproved software to reduce the risk of introducing
  malicious or vulnerable applications. This can be achieved through allowlists, software restriction policies, endpoint management
  tools, and least privilege access principles. This mitigation can be implemented through the following measures:


  Application Whitelisting


  - Implement Microsoft AppLocker or Windows Defender Application Control (WDAC) to create and enforce allowlists for approved
  software.

  - Whitelist applications based on file hash, path, or digital signatures.


  Restrict User Permissions


  - Remove local administrator rights for all non-IT users.

  - Use Role-Based Access Control (RBAC) to restrict installation permissions to privileged accounts only.


  Software Restriction Policies (SRP)


  - Use GPO to configure SRP to deny execution of binaries from directories such as `%AppData%`, `%Temp%`, and external drives.

  - Restrict specific file types (`.exe`, `.bat`, `.msi`, `.js`, `.vbs`) to trusted directories only.


  Endpoint Management Solutions


  - Deploy tools like Microsoft Intune, SCCM, or Jamf for centralized software management.

  - Maintain a list of approved software, versions, and updates across the enterprise.


  Monitor Software Installation Events


  - Enable logging of software installation events and monitor Windows Event ID 4688 and Event ID 11707 for software installs.

  - Use SIEM or EDR tools to alert on attempts to install unapproved software.


  Implement Software Inventory Management


  - Use tools like OSQuery or Wazuh to scan for unauthorized software on endpoints and servers.

  - Conduct regular audits to detect and remove unapproved software.


  *Tools for Implementation*


  Application Whitelisting:


  - Microsoft AppLocker

  - Windows Defender Application Control (WDAC)


  Endpoint Management:


  - Microsoft Intune

  - SCCM (System Center Configuration Manager)

  - Jamf Pro (macOS)

  - Puppet or Ansible for automation


  Software Restriction Policies:


  - Group Policy Object (GPO)

  - Microsoft Software Restriction Policies (SRP)


  Monitoring and Logging:


  - Splunk

  - OSQuery

  - Wazuh (open-source SIEM and XDR)

  - EDRs


  Inventory Management and Auditing:


  - OSQuery

  - Wazuh'
external_references:
- external_id: M1033
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1033
id: course-of-action--23843cff-f7b9-4659-a7b7-713ef347f547
modified: '2024-12-18T16:17:46.153Z'
name: Limit Software Installation
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
