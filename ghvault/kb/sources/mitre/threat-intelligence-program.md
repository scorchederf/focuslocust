---
parsed_by: focuslocust
source: mitre
type: generated
---
# Threat Intelligence Program

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1019` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Threat Intelligence Program](../../attack/mitigations/M1019-threat-intelligence-program.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1019 |
| name | Threat Intelligence Program |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1019 |

## Preserved Source Material

```yaml
created: '2019-06-06T19:55:50.927Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'A Threat Intelligence Program enables organizations to proactively identify, analyze, and act on cyber threats
  by leveraging internal and external data sources. The program supports decision-making processes, prioritizes defenses,
  and improves incident response by delivering actionable intelligence tailored to the organization''s risk profile and operational
  environment. This mitigation can be implemented through the following measures:


  Establish a Threat Intelligence Team:


  - Form a dedicated team or assign responsibility to existing security personnel to collect, analyze, and act on threat intelligence.


  Define Intelligence Requirements:


  - Identify the organization’s critical assets and focus intelligence gathering efforts on threats targeting these assets.


  Leverage Internal and External Data Sources:


  - Collect intelligence from internal sources such as logs, incidents, and alerts.

  Subscribe to external threat intelligence feeds, participate in ISACs, and monitor open-source intelligence (OSINT).


  Implement Tools for Automation:


  - Use threat intelligence platforms (TIPs) to automate the collection, enrichment, and dissemination of threat data.

  - Integrate threat intelligence with SIEMs to correlate IOCs with internal events.


  Analyze and Act on Intelligence:


  - Use frameworks like MITRE ATT&CK to map intelligence to adversary TTPs.

  - Prioritize defensive measures, such as patching vulnerabilities or deploying IOCs, based on analyzed threats.


  Share and Collaborate:


  - Share intelligence with industry peers through ISACs or threat-sharing platforms to enhance collective defense.


  Evaluate and Update the Program:


  - Regularly assess the effectiveness of the threat intelligence program.

  - Update intelligence priorities and capabilities as new threats emerge.


  *Tools for Implementation*


  Threat Intelligence Platforms (TIPs):


  - OpenCTI: An open-source platform for structuring and sharing threat intelligence.

  - MISP: A threat intelligence sharing platform for sharing structured threat data.


  Threat Intelligence Feeds:


  - Open Threat Exchange (OTX): Provides free access to a large repository of threat intelligence.

  - CIRCL OSINT Feed: A free source for IOCs and threat information.


  Automation and Enrichment Tools:


  - TheHive: An open-source incident response platform with threat intelligence integration.

  - Yeti: A platform for managing and structuring knowledge about threats.


  Analysis Frameworks:


  - MITRE ATT&CK Navigator: A tool for mapping threat intelligence to adversary behaviors.

  - Cuckoo Sandbox: Analyzes malware to extract behavioral indicators.


  Community and Collaboration Tools:


  - ISAC Memberships: Join industry-specific ISACs for intelligence sharing.

  - Slack/Discord Channels: Participate in threat intelligence communities for real-time collaboration.'
external_references:
- external_id: M1019
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1019
id: course-of-action--874c0166-e407-45c2-a1d9-e4e3a6570fd8
modified: '2024-12-24T14:05:21.946Z'
name: Threat Intelligence Program
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
