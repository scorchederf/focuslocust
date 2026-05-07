---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1594
tags:
    - attack/domain/enterprise_attack
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1594-search-victim-owned-websites
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may search websites owned by the victim for information that can be used during targeting. Victim-owned websites may contain a variety of details, including names of departments/divisions, physical locations, and data about key employees such as names, roles, and contact info (ex: [[kb/mitre/attack/techniques/T1589.002-email-addresses|Email Addresses]]). These sites may also have details highlighting business operations and relationships.[^2] <br><br>Adversaries may search victim-owned websites to gather actionable information. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]] or [[kb/mitre/attack/techniques/T1596-search-open-technical-databases|Search Open Technical Databases]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1585-establish-accounts|Establish Accounts]] or [[kb/mitre/attack/techniques/T1586-compromise-accounts|Compromise Accounts]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1199-trusted-relationship|Trusted Relationship]] or [[kb/mitre/attack/techniques/T1566-phishing|Phishing]]).<br><br>In addition to manually browsing the website, adversaries may attempt to identify hidden directories or files that could contain additional sensitive information or vulnerable functionality. They may do this through automated activities such as [[kb/mitre/attack/techniques/T1595.003-wordlist-scanning|Wordlist Scanning]], as well as by leveraging files such as sitemap.xml and robots.txt.[^1] [^3]  

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

 [^1]: [Perez Sitemap XML 2023](https://medium.com/@adimenia/how-attackers-can-misuse-sitemaps-to-enumerate-users-and-discover-sensitive-information-361a5065857a)
 [^2]: [Comparitech Leak](https://www.comparitech.com/blog/vpn-privacy/350-million-customer-records-exposed-online/)
 [^3]: [Register Robots TXT 2015](https://www.theregister.com/2015/05/19/robotstxt/)
