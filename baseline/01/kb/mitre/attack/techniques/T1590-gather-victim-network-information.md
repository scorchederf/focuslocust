---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1590
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1590-gather-victim-network-information
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.<br><br>Adversaries may gather this information in various ways, such as direct collection actions via [[kb/mitre/attack/techniques/T1595-active-scanning|Active Scanning]] or [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]]. Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: [[kb/mitre/attack/techniques/T1596-search-open-technical-databases|Search Open Technical Databases]]).[^3] [^2] [^1]  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1595-active-scanning|Active Scanning]] or [[kb/mitre/attack/techniques/T1593-search-open-websites-domains|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1583-acquire-infrastructure|Acquire Infrastructure]] or [[kb/mitre/attack/techniques/T1584-compromise-infrastructure|Compromise Infrastructure]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1199-trusted-relationship|Trusted Relationship]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1590.005-ip-addresses\|T1590.005]] | IP Addresses |
| [[kb/mitre/attack/techniques/T1590.002-dns\|T1590.002]] | DNS |
| [[kb/mitre/attack/techniques/T1590.004-network-topology\|T1590.004]] | Network Topology |
| [[kb/mitre/attack/techniques/T1590.003-network-trust-dependencies\|T1590.003]] | Network Trust Dependencies |
| [[kb/mitre/attack/techniques/T1590.006-network-security-appliances\|T1590.006]] | Network Security Appliances |
| [[kb/mitre/attack/techniques/T1590.001-domain-properties\|T1590.001]] | Domain Properties |

 [^1]: [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)
 [^2]: [DNS Dumpster](https://dnsdumpster.com/)
 [^3]: [WHOIS](https://who.is/)
