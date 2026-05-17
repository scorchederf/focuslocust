---
parsed_by: focuslocust
source: mitre
type: generated
---
# Gather Victim Identity Information

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1589` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Gather Victim Identity Information](../../attack/techniques/T1589-gather-victim-identity-information.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1589 |
| name | Gather Victim Identity Information |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1589 |

## Preserved Source Material

```yaml
created: '2020-10-02T14:54:59.263Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather information about the victim''s identity that can be used during targeting. Information
  about identities may include a variety of details, including personal data (ex: employee names, email addresses, security
  question responses, etc.) as well as sensitive details such as credentials or multi-factor authentication (MFA) configurations.


  Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598).
  Information about users could also be enumerated via other active means (i.e. [Active Scanning](https://attack.mitre.org/techniques/T1595))
  such as probing and analyzing responses from authentication services that may reveal valid usernames in a system or permitted
  MFA /methods associated with those usernames.(Citation: GrimBlog UsernameEnum)(Citation: Obsidian SSPR Abuse 2023) Information
  about victims may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001)
  or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: OPM Leak)(Citation: Register Deloitte)(Citation:
  Register Uber)(Citation: Detectify Slack Tokens)(Citation: Forbes GitHub Creds)(Citation: GitHub truffleHog)(Citation: GitHub
  Gitrob)(Citation: CNET Leaks)


  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)
  or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise
  Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)
  or [Valid Accounts](https://attack.mitre.org/techniques/T1078)).'
external_references:
- external_id: T1589
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1589
- description: Cybersecurity Resource Center. (n.d.). CYBERSECURITY INCIDENTS. Retrieved September 16, 2024.
  source_name: OPM Leak
  url: https://web.archive.org/web/20230602111604/https://www.opm.gov/cybersecurity/cybersecurity-incidents/
- description: Detectify. (2016, April 28). Slack bot token leakage exposing business critical information. Retrieved November
    17, 2024.
  source_name: Detectify Slack Tokens
  url: https://labs.detectify.com/writeups/slack-bot-token-leakage-exposing-business-critical-information/
- description: Dylan Ayrey. (2016, December 31). truffleHog. Retrieved October 19, 2020.
  source_name: GitHub truffleHog
  url: https://github.com/dxa4481/truffleHog
- description: GrimHacker. (2017, July 24). Office365 ActiveSync Username Enumeration. Retrieved December 9, 2021.
  source_name: GrimBlog UsernameEnum
  url: https://grimhacker.com/2017/07/24/office365-activesync-username-enumeration/
- description: McCarthy, K. (2015, February 28). FORK ME! Uber hauls GitHub into court to find who hacked database of 50,000
    drivers. Retrieved October 19, 2020.
  source_name: Register Uber
  url: https://www.theregister.com/2015/02/28/uber_subpoenas_github_for_hacker_details/
- description: 'Michael Henriksen. (2018, June 9). Gitrob: Putting the Open Source in OSINT. Retrieved October 19, 2020.'
  source_name: GitHub Gitrob
  url: https://github.com/michenriksen/gitrob
- description: Ng, A. (2019, January 17). Massive breach leaks 773 million email addresses, 21 million passwords. Retrieved
    October 20, 2020.
  source_name: CNET Leaks
  url: https://www.cnet.com/news/massive-breach-leaks-773-million-emails-21-million-passwords/
- description: 'Noah Corradin and Shuyang Wang. (2023, August 1). Behind The Breach: Self-Service Password Reset (SSPR) Abuse
    in Azure AD. Retrieved March 28, 2024.'
  source_name: Obsidian SSPR Abuse 2023
  url: https://www.obsidiansecurity.com/blog/behind-the-breach-self-service-password-reset-azure-ad/
- description: Sandvik, R. (2014, January 14). Attackers Scrape GitHub For Cloud Service Credentials, Hijack Account To Mine
    Virtual Currency. Retrieved October 19, 2020.
  source_name: Forbes GitHub Creds
  url: https://www.forbes.com/sites/runasandvik/2014/01/14/attackers-scrape-github-for-cloud-service-credentials-hijack-account-to-mine-virtual-currency/#242c479d3196
- description: 'Thomson, I. (2017, September 26). Deloitte is a sitting duck: Key systems with RDP open, VPN and proxy ''login
    details leaked''. Retrieved October 19, 2020.'
  source_name: Register Deloitte
  url: https://www.theregister.com/2017/09/26/deloitte_leak_github_and_google/
id: attack-pattern--5282dd9a-d26d-4e16-88b7-7c0f4553daf4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:47.303Z'
name: Gather Victim Identity Information
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Jannie Li, Microsoft Threat Intelligence Center (MSTIC)
- Obsidian Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.3'
```
