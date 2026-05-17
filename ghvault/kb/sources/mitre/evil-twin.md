---
parsed_by: focuslocust
source: mitre
type: generated
---
# Evil Twin

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1557.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Evil Twin](../../attack/techniques/T1557.004-evil-twin.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1557.004 |
| name | Evil Twin |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1557/004 |

## Preserved Source Material

```yaml
created: '2024-09-17T14:27:40.947Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may host seemingly genuine Wi-Fi access points to deceive users into connecting to malicious networks\
  \ as a way of supporting follow-on behaviors such as [Network Sniffing](https://attack.mitre.org/techniques/T1040), [Transmitted\
  \ Data Manipulation](https://attack.mitre.org/techniques/T1565/002), or [Input Capture](https://attack.mitre.org/techniques/T1056).(Citation:\
  \ Australia ‘Evil Twin’)\n\nBy using a Service Set Identifier (SSID) of a legitimate Wi-Fi network, fraudulent Wi-Fi access\
  \ points may trick devices or users into connecting to malicious Wi-Fi networks.(Citation: Kaspersky evil twin)(Citation:\
  \ medium evil twin)  Adversaries may provide a stronger signal strength or block access to Wi-Fi access points to coerce\
  \ or entice victim devices into connecting to malicious networks.(Citation: specter ops evil twin)  A Wi-Fi Pineapple –\
  \ a network security auditing and penetration testing tool – may be deployed in Evil Twin attacks for ease of use and broader\
  \ range. Custom certificates may be used in an attempt to intercept HTTPS traffic. \n\nSimilarly, adversaries may also listen\
  \ for client devices sending probe requests for known or previously connected networks (Preferred Network Lists or PNLs).\
  \ When a malicious access point receives a probe request, adversaries can respond with the same SSID to imitate the trusted,\
  \ known network.(Citation: specter ops evil twin)  Victim devices are led to believe the responding access point is from\
  \ their PNL and initiate a connection to the fraudulent network.\n\nUpon logging into the malicious Wi-Fi access point,\
  \ a user may be directed to a fake login page or captive portal webpage to capture the victim’s credentials. Once a user\
  \ is logged into the fraudulent Wi-Fi network, the adversary may able to monitor network activity, manipulate data, or steal\
  \ additional credentials. Locations with high concentrations of public Wi-Fi access, such as airports, coffee shops, or\
  \ libraries, may be targets for adversaries to set up illegitimate Wi-Fi access points. "
external_references:
- external_id: T1557.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1557/004
- description: AO Kaspersky Lab. (n.d.). Evil twin attacks and how to prevent them. Retrieved September 17, 2024.
  source_name: Kaspersky evil twin
  url: https://usa.kaspersky.com/resource-center/preemptive-safety/evil-twin-attacks
- description: Gihan, Kavishka. (2021, August 8). Wireless Security— Evil Twin Attack. Retrieved September 17, 2024.
  source_name: medium evil twin
  url: https://kavigihan.medium.com/wireless-security-evil-twin-attack-d3842f4aef59
- description: Ryan, Gabriel. (2019, October 28). Modern Wireless Tradecraft Pt I — Basic Rogue AP Theory — Evil Twin and
    Karma Attacks. Retrieved September 17, 2024.
  source_name: specter ops evil twin
  url: https://posts.specterops.io/modern-wireless-attacks-pt-i-basic-rogue-ap-theory-evil-twin-and-karma-attacks-35a8571550ee
- description: Toulas, Bill. (2024, July 1). Australian charged for ‘Evil Twin’ WiFi attack on plane. Retrieved September
    17, 2024.
  source_name: Australia ‘Evil Twin’
  url: https://www.bleepingcomputer.com/news/security/australian-charged-for-evil-twin-wifi-attack-on-plane/
id: attack-pattern--48b836c6-e4ca-435a-82a3-29c03e5b492e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-04-15T19:58:27.842Z'
name: Evil Twin
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Menachem Goldstein
- DeFord L. Smith
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '1.1'
```
