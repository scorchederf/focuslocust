---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1591
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1591-gather-victim-org-information
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.<br><br>Adversaries may gather this information in various ways, such as direct elicitation via [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]]. Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: [[kb/mitre/attack/techniques/T1593.001-social-media|Social Media]] or [[kb/mitre/attack/techniques/T1594-search-victim-owned-websites|Search Victim-Owned Websites]]).[^1] [^2]  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]] or [[kb/mitre/attack/techniques/T1593-search-open-websites-domains|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1585-establish-accounts|Establish Accounts]] or [[kb/mitre/attack/techniques/T1586-compromise-accounts|Compromise Accounts]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1566-phishing|Phishing]] or [[kb/mitre/attack/techniques/T1199-trusted-relationship|Trusted Relationship]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1591.003-identify-business-tempo\|T1591.003]] | Identify Business Tempo |
| [[kb/mitre/attack/techniques/T1591.002-business-relationships\|T1591.002]] | Business Relationships |
| [[kb/mitre/attack/techniques/T1591.004-identify-roles\|T1591.004]] | Identify Roles |
| [[kb/mitre/attack/techniques/T1591.001-determine-physical-locations\|T1591.001]] | Determine Physical Locations |

 [^1]: [ThreatPost Broadvoice Leak](https://threatpost.com/broadvoice-leaks-350m-records-voicemail-transcripts/160158/)
 [^2]: [SEC EDGAR Search](https://www.sec.gov/edgar/search/)
