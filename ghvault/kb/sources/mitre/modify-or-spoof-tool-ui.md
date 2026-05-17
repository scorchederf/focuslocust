---
parsed_by: focuslocust
source: mitre
type: generated
---
# Modify or Spoof Tool UI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Modify or Spoof Tool UI](../../attack/techniques/T1685.003-modify-or-spoof-tool-ui.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1685.003 |
| name | Modify or Spoof Tool UI |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1685/003 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:02.938Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may spoof or manipulate security tool user interfaces (UIs) to falsely indicate tools are functioning\
  \ normally and delay detection and response. \n\nAdversaries may present misleading or falsified security tool interfaces\
  \ (UIs) that display normal or healthy status indicators, even when underlying security tools have been disabled, degraded,\
  \ or otherwise tampered with. Security tools typically provide visibility into system health, alerting, and operational\
  \ status; by misrepresenting this information, adversaries can undermine defender trust in these signals and obscure the\
  \ true security posture of the system. \n\nThis behavior is often used in conjunction with efforts to disable or modify\
  \ tools, where adversaries first impair the functionality of defenses (e.g., EDR, logging agents) and then replace or mimic\
  \ their interfaces to conceal the loss of visibility. By maintaining the appearance of normal operations, such as showing\
  \ active protection, successful updates, or absence of threats, adversaries can delay investigation and response, enabling\
  \ continued malicious activity. \n\nFor example, adversaries may display a fake Windows Security interface or system tray\
  \ icon indicating a “protected” or “healthy” state after disabling Windows Defender or related services.(Citation: BlackBasta)"
external_references:
- external_id: T1685.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1685/003
- description: Antonio Cocomazzi and Antonio Pirozzi. (2022, November 3). Black Basta Ransomware | Attacks Deploy Custom EDR
    Evasion Tools Tied to FIN7 Threat Actor. Retrieved March 14, 2023.
  source_name: BlackBasta
  url: https://www.sentinelone.com/labs/black-basta-ransomware-attacks-deploy-custom-edr-evasion-tools-tied-to-fin7-threat-actor/
id: attack-pattern--0ff4bd68-aebb-4039-9e00-9f92c705edf4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:44:20.156Z'
name: Modify or Spoof Tool UI
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
