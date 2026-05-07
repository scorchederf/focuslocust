---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1597
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1597-search-closed-sources
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may search and gather information about victims from closed (e.g., paid, private, or otherwise not freely available) sources that can be used during targeting. Information about victims may be available for purchase from reputable private sources and databases, such as paid subscriptions to feeds of technical/threat intelligence data. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.[^1] <br><br>Adversaries may search in different closed databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]] or [[kb/mitre/attack/techniques/T1593-search-open-websites-domains|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1587-develop-capabilities|Develop Capabilities]] or [[kb/mitre/attack/techniques/T1588-obtain-capabilities|Obtain Capabilities]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1133-external-remote-services|External Remote Services]] or [[kb/mitre/attack/techniques/T1078-valid-accounts|Valid Accounts]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1597.002-purchase-technical-data\|T1597.002]] | Purchase Technical Data |
| [[kb/mitre/attack/techniques/T1597.001-threat-intel-vendors\|T1597.001]] | Threat Intel Vendors |

 [^1]: [ZDNET Selling Data](https://www.zdnet.com/article/a-hacker-group-is-selling-more-than-73-million-user-records-on-the-dark-web/)
