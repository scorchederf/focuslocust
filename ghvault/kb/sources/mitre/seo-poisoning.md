---
parsed_by: focuslocust
source: mitre
type: generated
---
# SEO Poisoning

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1608.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SEO Poisoning](../../attack/techniques/T1608.006-seo-poisoning.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1608.006 |
| name | SEO Poisoning |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1608/006 |

## Preserved Source Material

```yaml
created: '2022-09-30T21:14:12.284Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may poison mechanisms that influence search engine optimization (SEO) to further lure staged capabilities
  towards potential victims. Search engines typically display results to users based on purchased ads as well as the site’s
  ranking/score/reputation calculated by their web crawlers and algorithms.(Citation: Atlas SEO)(Citation: MalwareBytes SEO)


  To help facilitate [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), adversaries may stage content that
  explicitly manipulates SEO rankings in order to promote sites hosting their malicious payloads (such as [Drive-by Target](https://attack.mitre.org/techniques/T1608/004))
  within search engines. Poisoning SEO rankings may involve various tricks, such as stuffing keywords (including in the form
  of hidden text) into compromised sites. These keywords could be related to the interests/browsing habits of the intended
  victim(s) as well as more broad, seasonably popular topics (e.g. elections, trending news).(Citation: ZScaler SEO)(Citation:
  Atlas SEO)


  In addition to internet search engines (such as Google), adversaries may also aim to manipulate specific in-site searches
  for developer platforms (such as GitHub) to deceive users towards [Supply Chain Compromise](https://attack.mitre.org/techniques/T1195)
  lures. In-site searches will rank search results according to their own algorithms and metrics such as popularity(Citation:
  Chexmarx-seo) which may be targeted and gamed by malicious actors.(Citation: Checkmarx-oss-seo)


  Adversaries may also purchase or plant incoming links to staged capabilities in order to boost the site’s calculated relevance
  and reputation.(Citation: MalwareBytes SEO)(Citation: DFIR Report Gootloader)


  SEO poisoning may also be combined with evasive redirects and other cloaking mechanisms (such as measuring mouse movements
  or serving content based on browser user agents, user language/localization settings, or HTTP headers) in order to feed
  SEO inputs while avoiding scrutiny from defenders.(Citation: ZScaler SEO)(Citation: Sophos Gootloader)'
external_references:
- external_id: T1608.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1608/006
- description: 'Arntz, P. (2018, May 29). SEO poisoning: Is it worth it?. Retrieved September 30, 2022.'
  source_name: MalwareBytes SEO
  url: https://www.malwarebytes.com/blog/news/2018/05/seo-poisoning-is-it-worth-it
- description: Atlas Cybersecurity. (2021, April 19). Threat Actors use Search-Engine-Optimization Tactics to Redirect Traffic
    and Install Malware. Retrieved September 30, 2022.
  source_name: Atlas SEO
  url: https://atlas-cybersecurity.com/cyber-threats/threat-actors-use-search-engine-optimization-tactics-to-redirect-traffic-and-install-malware/
- description: Szappanos, G. & Brandt, A. (2021, March 1). “Gootloader” expands its payload delivery options. Retrieved September
    30, 2022.
  source_name: Sophos Gootloader
  url: https://news.sophos.com/en-us/2021/03/01/gootloader-expands-its-payload-delivery-options/
- description: The DFIR Report. (2022, May 9). SEO Poisoning – A Gootloader Story. Retrieved September 30, 2022.
  source_name: DFIR Report Gootloader
  url: https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/
- description: Wang, J. (2018, October 17). Ubiquitous SEO Poisoning URLs. Retrieved September 30, 2022.
  source_name: ZScaler SEO
  url: https://www.zscaler.com/blogs/security-research/ubiquitous-seo-poisoning-urls-0
- description: 'Yehuda Gelb. (2023, November 30). The GitHub Black Market: Gaming the Star Ranking Game. Retrieved June 18,
    2024.'
  source_name: Chexmarx-seo
  url: https://zero.checkmarx.com/the-github-black-market-gaming-the-star-ranking-game-fc42f5913fb7
- description: Yehuda Gelb. (2024, April 10). New Technique to Trick Developers Detected in an Open Source Supply Chain Attack.
    Retrieved June 18, 2024.
  source_name: Checkmarx-oss-seo
  url: https://checkmarx.com/blog/new-technique-to-trick-developers-detected-in-an-open-source-supply-chain-attack/
id: attack-pattern--e5d550f3-2202-4634-85f2-4a200a1d49b3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-04-15T23:01:38.651Z'
name: SEO Poisoning
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Menachem Goldstein
- Vijay Lalwani
- Will Thomas, Equinix Threat Analysis Center (ETAC)
- Will Jolliffe
- Hiroki Nagahama, NEC Corporation
- Manikantan Srinivasan, NEC Corporation India
- Pooja Natarajan, NEC Corporation India
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.1'
```
