---
parsed_by: focuslocust
source: mitre
type: generated
---
# Hide Infrastructure

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1665` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hide Infrastructure](../../attack/techniques/T1665-hide-infrastructure.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1665 |
| name | Hide Infrastructure |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1665 |

## Preserved Source Material

```yaml
created: '2024-02-13T17:00:00.175Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure.
  This can be accomplished by identifying and filtering traffic from defensive tools,(Citation: TA571) masking malicious domains
  to obfuscate the true destination from both automated scanning tools and security researchers,(Citation: Schema-abuse)(Citation:
  Facad1ng)(Citation: Browser-updates) and otherwise hiding malicious artifacts to delay discovery and prolong the effectiveness
  of adversary infrastructure that could otherwise be identified, blocked, or taken down entirely.


  C2 networks may include the use of [Proxy](https://attack.mitre.org/techniques/T1090) or VPNs to disguise IP addresses,
  which can allow adversaries to blend in with normal network traffic and bypass conditional access policies or anti-abuse
  protections. For example, an adversary may use a virtual private cloud to spoof their IP address to closer align with a
  victim''s IP address ranges. This may also bypass security measures relying on geolocation of the source IP address.(Citation:
  sysdig)(Citation: Orange Residential Proxies)


  Adversaries may also attempt to filter network traffic in order to evade defensive tools in numerous ways, including blocking/redirecting
  common incident responder or security appliance user agents.(Citation: mod_rewrite)(Citation: SocGholish-update) Filtering
  traffic based on IP and geo-fencing may also avoid automated sandboxing or researcher activity (i.e., [Virtualization/Sandbox
  Evasion](https://attack.mitre.org/techniques/T1497)).(Citation: TA571)(Citation: mod_rewrite)


  Hiding C2 infrastructure may also be supported by [Resource Development](https://attack.mitre.org/tactics/TA0042) activities
  such as [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) and [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584).
  For example, using widely trusted hosting services or domains such as prominent URL shortening providers or marketing services
  for C2 networks may enable adversaries to present benign content that later redirects victims to malicious web pages or
  infrastructure once specific conditions are met.(Citation: StarBlizzard)(Citation: QR-cofense)'
external_references:
- external_id: T1665
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1665
- description: Andrew Northern. (2022, November 22). SocGholish, a very real threat from a very fake update. Retrieved February
    13, 2024.
  source_name: SocGholish-update
  url: https://www.proofpoint.com/us/blog/threat-insight/part-1-socgholish-very-real-threat-very-fake-update
- description: Axel F, Selena Larson. (2023, October 30).  TA571 Delivers IcedID Forked Loader. Retrieved February 13, 2024.
  source_name: TA571
  url: https://www.proofpoint.com/us/blog/threat-insight/security-brief-ta571-delivers-icedid-forked-loader
- description: Bluescreenofjeff.com. (2015, April 12). Combatting Incident Responders with Apache mod_rewrite. Retrieved February
    13, 2024.
  source_name: mod_rewrite
  url: https://bluescreenofjeff.com/2016-04-12-combatting-incident-responders-with-apache-mod_rewrite/
- description: Dusty Miller. (2023, October 17). Are You Sure Your Browser is Up to Date? The Current Landscape of Fake Browser
    Updates . Retrieved February 13, 2024.
  source_name: Browser-updates
  url: https://www.proofpoint.com/us/blog/threat-insight/are-you-sure-your-browser-date-current-landscape-fake-browser-updates
- description: Microsoft Threat Intelligence. (2023, December 7). Star Blizzard increases sophistication and evasion in ongoing
    attacks. Retrieved February 13, 2024.
  source_name: StarBlizzard
  url: https://www.microsoft.com/en-us/security/blog/2023/12/07/star-blizzard-increases-sophistication-and-evasion-in-ongoing-attacks/
- description: Nathaniel Raymond. (2023, August 16). Major Energy Company Targeted in Large QR Code Phishing Campaign. Retrieved
    February 13, 2024.
  source_name: QR-cofense
  url: https://cofense.com/blog/major-energy-company-targeted-in-large-qr-code-campaign/
- description: 'Nick Simonian. (2023, May 22). Don''t @ Me: URL Obfuscation Through Schema Abuse. Retrieved February 13, 2024.'
  source_name: Schema-abuse
  url: https://www.mandiant.com/resources/blog/url-obfuscation-schema-abuse
- description: Orange Cyberdefense. (2024, March 14). Unveiling the depths of residential proxies providers. Retrieved April
    11, 2024.
  source_name: Orange Residential Proxies
  url: https://www.orangecyberdefense.com/global/blog/research/residential-proxies
- description: Spyboy. (2023). Facad1ng. Retrieved February 13, 2024.
  source_name: Facad1ng
  url: https://github.com/spyboy-productions/Facad1ng
- description: Sysdig. (2023). Sysdig Global Cloud Threat Report. Retrieved March 1, 2024.
  source_name: sysdig
  url: https://sysdig.com/content/c/pf-2023-global-cloud-threat-report?x=u_WFRi&xs=524303#page=1
id: attack-pattern--eb897572-8979-4242-a089-56f294f4c91d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: command-and-control
modified: '2025-10-22T03:57:22.646Z'
name: Hide Infrastructure
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Diyar Saadi Ali
- Eliav Livneh
- Hen Porcilan
- Matt Mullins
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.2'
```
