---
parsed_by: focuslocust
source: mitre
type: generated
---
# Clear Network Connection History and Configurations

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1070.007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Clear Network Connection History and Configurations](../../attack/techniques/T1070.007-clear-network-connection-history-and-configurations.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1070.007 |
| name | Clear Network Connection History and Configurations |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1070/007 |

## Preserved Source Material

```yaml
created: '2022-06-15T18:00:04.219Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may clear or remove evidence of malicious network connections in order to clean up traces of their
  operations. Configuration settings as well as various artifacts that highlight connection history may be created on a system
  and/or in application logs from behaviors that require network connections, such as [Remote Services](https://attack.mitre.org/techniques/T1021)
  or [External Remote Services](https://attack.mitre.org/techniques/T1133). Defenders may use these artifacts to monitor or
  otherwise analyze network connections created by adversaries.


  Network connection history may be stored in various locations. For example, RDP connection history may be stored in Windows
  Registry values under (Citation: Microsoft RDP Removal):


  * <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default</code>

  * <code>HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Servers</code>


  Windows may also store information about recent RDP connections in files such as <code>C:\Users\\%username%\Documents\Default.rdp</code>
  and `C:\Users\%username%\AppData\Local\Microsoft\Terminal

  Server Client\Cache\`.(Citation: Moran RDPieces) Similarly, macOS and Linux hosts may store information highlighting connection
  history in system logs (such as those stored in `/Library/Logs` and/or `/var/log/`).(Citation: Apple Culprit Access)(Citation:
  FreeDesktop Journal)(Citation: Apple Unified Log Analysis Remote Login and Screen Sharing)


  Malicious network connections may also require changes to third-party applications or network configuration settings, such
  as [Disable or Modify System Firewall](https://attack.mitre.org/techniques/T1686) or tampering to enable [Proxy](https://attack.mitre.org/techniques/T1090).
  Adversaries may delete or modify this data to conceal indicators and/or impede defensive analysis.'
external_references:
- external_id: T1070.007
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1070/007
- description: freedesktop.org. (n.d.). systemd-journald.service. Retrieved June 15, 2022.
  source_name: FreeDesktop Journal
  url: https://www.freedesktop.org/software/systemd/man/systemd-journald.service.html
- description: Microsoft. (2021, September 24). How to remove entries from the Remote Desktop Connection Computer box. Retrieved
    June 15, 2022.
  source_name: Microsoft RDP Removal
  url: https://docs.microsoft.com/troubleshoot/windows-server/remote/remove-entries-from-remote-desktop-connection-computer
- description: Moran, B. (2020, November 18). Putting Together the RDPieces. Retrieved October 17, 2022.
  source_name: Moran RDPieces
  url: https://www.osdfcon.org/presentations/2020/Brian-Moran_Putting-Together-the-RDPieces.pdf
- description: rjben. (2012, May 30). How do you find the culprit when unauthorized access to a computer is a problem?. Retrieved
    August 3, 2022.
  source_name: Apple Culprit Access
  url: https://discussions.apple.com/thread/3991574
- description: 'Sarah Edwards. (2020, April 30). Analysis of Apple Unified Logs: Quarantine Edition [Entry 6] – Working From
    Home? Remote Logins. Retrieved August 19, 2021.'
  source_name: Apple Unified Log Analysis Remote Login and Screen Sharing
  url: https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins
id: attack-pattern--3975dbb5-0e1e-4f5b-bae1-cf2ab84b46dc
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-16T19:27:07.242Z'
name: Clear Network Connection History and Configurations
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- CrowdStrike Falcon OverWatch
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- Network Devices
x_mitre_version: '2.0'
```
