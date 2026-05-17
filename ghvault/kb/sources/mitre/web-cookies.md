---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Cookies

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1606.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Cookies](../../attack/techniques/T1606.001-web-cookies.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1606.001 |
| name | Web Cookies |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1606/001 |

## Preserved Source Material

```yaml
created: '2020-12-17T02:14:34.178Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may forge web cookies that can be used to gain access to web applications or Internet services.
  Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies to authenticate
  and authorize user access.


  Adversaries may generate these cookies in order to gain access to web resources. This differs from [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539)
  and other similar behaviors in that the cookies are new and forged by the adversary, rather than stolen or intercepted from
  legitimate users. Most common web applications have standardized and documented cookie values that can be generated using
  provided tools or interfaces.(Citation: Pass The Cookie) The generation of web cookies often requires secret values, such
  as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004), or other cryptographic seed values.


  Once forged, adversaries may use these web cookies to access resources ([Web Session Cookie](https://attack.mitre.org/techniques/T1550/004)),
  which may bypass multi-factor and other authentication protection mechanisms.(Citation: Volexity SolarWinds)(Citation: Pass
  The Cookie)(Citation: Unit 42 Mac Crypto Cookies January 2019)'
external_references:
- external_id: T1606.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1606/001
- description: Cash, D. et al. (2020, December 14). Dark Halo Leverages SolarWinds Compromise to Breach Organizations. Retrieved
    December 29, 2020.
  source_name: Volexity SolarWinds
  url: https://www.volexity.com/blog/2020/12/14/dark-halo-leverages-solarwinds-compromise-to-breach-organizations/
- description: Chen, Y., Hu, W., Xu, Z., et. al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies.
    Retrieved October 14, 2019.
  source_name: Unit 42 Mac Crypto Cookies January 2019
  url: https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/
- description: Rehberger, J. (2018, December). Pivot to the Cloud using Pass the Cookie. Retrieved April 5, 2019.
  source_name: Pass The Cookie
  url: https://wunderwuzzi23.github.io/blog/passthecookie.html
id: attack-pattern--861b8fd2-57f3-4ee1-ab5d-c19c3b8c7a4a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:04.036Z'
name: Web Cookies
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jack Burns, HubSpot
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
x_mitre_version: '1.1'
```
