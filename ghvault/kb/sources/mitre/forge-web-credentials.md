---
parsed_by: focuslocust
source: mitre
type: generated
---
# Forge Web Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1606` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Forge Web Credentials](../../attack/techniques/T1606-forge-web-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1606 |
| name | Forge Web Credentials |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1606 |

## Preserved Source Material

```yaml
created: '2020-12-17T02:13:46.247Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may forge credential materials that can be used to gain access to web applications or Internet services.
  Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens,
  or other materials to authenticate and authorize user access.


  Adversaries may generate these credential materials in order to gain access to web resources. This differs from [Steal Web
  Session Cookie](https://attack.mitre.org/techniques/T1539), [Steal Application Access Token](https://attack.mitre.org/techniques/T1528),
  and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted
  from legitimate users.


  The generation of web credentials often requires secret values, such as passwords, [Private Keys](https://attack.mitre.org/techniques/T1552/004),
  or other cryptographic seed values.(Citation: GitHub AWS-ADFS-Credential-Generator) Adversaries may also forge tokens by
  taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request
  temporary security credentials (i.e., [Temporary Elevated Cloud Access](https://attack.mitre.org/techniques/T1548/005)),
  or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for
  any user in the domain.(Citation: AWS Temporary Security Credentials)(Citation: Zimbra Preauth)


  Once forged, adversaries may use these web credentials to access resources (ex: [Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550)),
  which may bypass multi-factor and other authentication protection mechanisms.(Citation: Pass The Cookie)(Citation: Unit
  42 Mac Crypto Cookies January 2019)(Citation: Microsoft SolarWinds Customer Guidance)  '
external_references:
- external_id: T1606
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1606
- description: AWS. (n.d.). Requesting temporary security credentials. Retrieved April 1, 2022.
  source_name: AWS Temporary Security Credentials
  url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html
- description: Chen, Y., Hu, W., Xu, Z., et. al. (2019, January 31). Mac Malware Steals Cryptocurrency Exchanges’ Cookies.
    Retrieved October 14, 2019.
  source_name: Unit 42 Mac Crypto Cookies January 2019
  url: https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/
- description: Damian Hickey. (2017, January 28). AWS-ADFS-Credential-Generator. Retrieved September 27, 2024.
  source_name: GitHub AWS-ADFS-Credential-Generator
  url: https://github.com/pvanbuijtene/aws-adfs-credential-generator
- description: MSRC. (2020, December 13). Customer Guidance on Recent Nation-State Cyber Attacks. Retrieved December 17, 2020.
  source_name: Microsoft SolarWinds Customer Guidance
  url: https://msrc-blog.microsoft.com/2020/12/13/customer-guidance-on-recent-nation-state-cyber-attacks/
- description: Rehberger, J. (2018, December). Pivot to the Cloud using Pass the Cookie. Retrieved April 5, 2019.
  source_name: Pass The Cookie
  url: https://wunderwuzzi23.github.io/blog/passthecookie.html
- description: Zimbra. (2023, March 16). Preauth. Retrieved May 31, 2023.
  source_name: Zimbra Preauth
  url: https://wiki.zimbra.com/wiki/Preauth
id: attack-pattern--94cb00a4-b295-4d06-aa2b-5653b9c1be9c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:07.201Z'
name: Forge Web Credentials
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Dylan Silva, AWS Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- SaaS
- Windows
- macOS
- Linux
- IaaS
- Office Suite
- Identity Provider
x_mitre_version: '1.5'
```
