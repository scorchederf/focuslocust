---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exclusive Control

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1668` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exclusive Control](../../attack/techniques/T1668-exclusive-control.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1668 |
| name | Exclusive Control |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1668 |

## Preserved Source Material

```yaml
created: '2025-01-31T15:22:39.317Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries who successfully compromise a system may attempt to maintain persistence by “closing the door” behind\
  \ them  – in other words, by preventing other threat actors from initially accessing or maintaining a foothold on the same\
  \ system. \n\nFor example, adversaries may patch a vulnerable, compromised system(Citation: Mandiant-iab-control)(Citation:\
  \ CERT AT Fortinent Ransomware 2025) to prevent other threat actors from leveraging that vulnerability in the future. They\
  \ may “close the door” in other ways, such as disabling vulnerable services(Citation: sophos-multiple-attackers), stripping\
  \ privileges from accounts(Citation: aquasec-postgres-processes), or removing other malware already on the compromised device.(Citation:\
  \ fsecure-netsky)\n\nHindering other threat actors may allow an adversary to maintain sole access to a compromised system\
  \ or network. This prevents the threat actor from needing to compete with or even being removed themselves by other threat\
  \ actors. It also reduces the “noise” in the environment, lowering the possibility of being caught and evicted by defenders.\
  \ Finally, in the case of [Resource Hijacking](https://attack.mitre.org/techniques/T1496), leveraging a compromised device’s\
  \ full power allows the threat actor to maximize profit.(Citation: sophos-multiple-attackers)"
external_references:
- external_id: T1668
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1668
- description: 'Assaf Morag. (2024, August 19). PG_MEM: A Malware Hidden in the Postgres Processes. Retrieved January 31,
    2025.'
  source_name: aquasec-postgres-processes
  url: https://www.aquasec.com/blog/pg_mem-a-malware-hidden-in-the-postgres-processes/
- description: CERT Austria. (2025, March 20). Ransomware-Gruppen nutzen weiterhin kritische Fortinet-Schwachstellen - Warnung
    vor gepatchten, aber bereits kompromittierten Geräten. Retrieved March 31, 2025.
  source_name: CERT AT Fortinent Ransomware 2025
  url: https://www.cert.at/de/warnungen/2025/3/ransomware-gruppen-nutzen-weiterhin-kritische-fortinet-schwachstellen-warnung-vor-gepatchten-aber-bereits-kompromittierten-geraten
- description: F-Secure. (2004). Worm:W32/NetSky.H. Retrieved January 31, 2025.
  source_name: fsecure-netsky
  url: https://www.f-secure.com/v-descs/netsky-h.shtml
- description: Matt Wixey. (2022, August 9). Multiple attackers increase pressure on victims, complicate incident response.
    Retrieved January 31, 2025.
  source_name: sophos-multiple-attackers
  url: https://news.sophos.com/en-us/2022/08/09/multiple-attackers-increase-pressure-on-victims-complicate-incident-response/#:~:text=While%20some%20threat%20actors%20are%20interdependent%20%28e.g.%2C%20IABs,vulnerabilities%20or%20disabling%20vulnerable%20services%20after%20gaining%20access
- description: Michael Raggi, Adam Aprahamian, Dan Kelly, Mathew Potaczek, Marcin Siedlarz, Austin Larsen. (2024, March 21).
    Bringing Access Back — Initial Access Brokers Exploit F5 BIG-IP (CVE-2023-46747) and ScreenConnect. Retrieved January
    31, 2025.
  source_name: Mandiant-iab-control
  url: https://cloud.google.com/blog/topics/threat-intelligence/initial-access-brokers-exploit-f5-screenconnect
id: attack-pattern--dff263cc-328e-42b4-afbc-1fee8b6a8913
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-04-15T19:59:14.622Z'
name: Exclusive Control
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
