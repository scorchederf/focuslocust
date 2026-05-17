---
parsed_by: focuslocust
source: mitre
type: generated
---
# Software

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1592.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Software](../../attack/techniques/T1592.002-software.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1592.002 |
| name | Software |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1592/002 |

## Preserved Source Material

```yaml
created: '2020-10-02T16:42:17.482Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather information about the victim''s host software that can be used during targeting. Information
  about installed software may include a variety of details such as types and versions on specific hosts, as well as the presence
  of additional components that might be indicative of added defensive protections (ex: antivirus, SIEMs, etc.).


  Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595)
  (ex: listening ports, server banners, user agent strings) or [Phishing for Information](https://attack.mitre.org/techniques/T1598).
  Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation:
  ATT ScanBox) Information about the installed software may also be exposed to adversaries via online or other accessible
  data sets (ex: job postings, network maps, assessment reports, resumes, or purchase invoices). Additionally, adversaries
  may analyze metadata from victim-owned files (e.g., PDFs, DOCs, images, and sound files hosted on victim-owned websites)
  to extract information about the software and hardware used to create or process those files. Metadata may reveal software
  versions, configurations, or timestamps that indicate outdated or vulnerable software. This information can be cross-referenced
  with known CVEs to identify potential vectors for exploitation in future operations.(Citation: Outpost24)


  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)
  or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex:
  [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)),
  and/or for initial access (ex: [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195) or [External Remote
  Services](https://attack.mitre.org/techniques/T1133)).'
external_references:
- external_id: T1592.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1592/002
- description: 'Blasco, J. (2014, August 28). Scanbox: A Reconnaissance Framework Used with Watering Hole Attacks. Retrieved
    October 19, 2020.'
  source_name: ATT ScanBox
  url: https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks
- description: Stijn Vande Casteele. (2025, March 31). How to analyze metadata and hide it from hackers. Retrieved July 2,
    2025.
  source_name: Outpost24
  url: https://outpost24.com/blog/metadata-hackers-best-friend/
- description: 'ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved
    October 12, 2021.'
  source_name: ThreatConnect Infrastructure Dec 2020
  url: https://threatconnect.com/blog/infrastructure-research-hunting/
id: attack-pattern--baf60e1a-afe5-4d31-830f-1b1ba2351884
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:17.631Z'
name: Software
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Michal Biesiada
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.2'
```
