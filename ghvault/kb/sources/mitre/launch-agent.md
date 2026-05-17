---
parsed_by: focuslocust
source: mitre
type: generated
---
# Launch Agent

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1543.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Launch Agent](../../attack/techniques/T1543.001-launch-agent.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1543.001 |
| name | Launch Agent |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1543/001 |

## Preserved Source Material

```yaml
created: '2020-01-17T16:10:58.592Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may create or modify launch agents to repeatedly execute malicious payloads as part of persistence.\
  \ When a user logs in, a per-user launchd process is started which loads the parameters for each launch-on-demand user agent\
  \ from the property list (.plist) file found in <code>/System/Library/LaunchAgents</code>, <code>/Library/LaunchAgents</code>,\
  \ and <code>~/Library/LaunchAgents</code>.(Citation: AppleDocs Launch Agent Daemons)(Citation: OSX Keydnap malware) (Citation:\
  \ Antiquated Mac Malware) Property list files use the <code>Label</code>, <code>ProgramArguments </code>, and <code>RunAtLoad</code>\
  \ keys to identify the Launch Agent's name, executable location, and execution time.(Citation: OSX.Dok Malware) Launch Agents\
  \ are often installed to perform updates to programs, launch user specified programs at login, or to conduct other developer\
  \ tasks.\n\n Launch Agents can also be executed using the [Launchctl](https://attack.mitre.org/techniques/T1569/001) command.\n\
  \ \nAdversaries may install a new Launch Agent that executes at login by placing a .plist file into the appropriate folders\
  \ with the <code>RunAtLoad</code> or <code>KeepAlive</code> keys set to <code>true</code>.(Citation: Sofacy Komplex Trojan)(Citation:\
  \ Methods of Mac Malware Persistence) The Launch Agent name may be disguised by using a name from the related operating\
  \ system or benign software. Launch Agents are created with user level privileges and execute with user level permissions.(Citation:\
  \ OSX Malware Detection)(Citation: OceanLotus for OS X) "
external_references:
- external_id: T1543.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1543/001
- description: Apple. (n.d.). Creating Launch Daemons and Agents. Retrieved July 10, 2017.
  source_name: AppleDocs Launch Agent Daemons
  url: https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html
- description: Dani Creus, Tyler Halfpop, Robert Falcone. (2016, September 26). Sofacy's 'Komplex' OS X Trojan. Retrieved
    July 8, 2017.
  source_name: Sofacy Komplex Trojan
  url: https://researchcenter.paloaltonetworks.com/2016/09/unit42-sofacys-komplex-os-x-trojan/
- description: Eddie Lee. (2016, February 17). OceanLotus for OS X - an Application Bundle Pretending to be an Adobe Flash
    Update. Retrieved July 5, 2017.
  source_name: OceanLotus for OS X
  url: https://www.alienvault.com/blogs/labs-research/oceanlotus-for-os-x-an-application-bundle-pretending-to-be-an-adobe-flash-update
- description: Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July
    3, 2017.
  source_name: OSX Keydnap malware
  url: https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/
- description: Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.
  source_name: Methods of Mac Malware Persistence
  url: https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf
- description: 'Patrick Wardle. (2016, February 29). Let''s Play Doctor: Practical OS X Malware Detection & Analysis. Retrieved
    November 17, 2024.'
  source_name: OSX Malware Detection
  url: https://papers.put.as/papers/macosx/2016/RSA_OSX_Malware.pdf
- description: Thomas Reed. (2017, January 18). New Mac backdoor using antiquated code. Retrieved July 5, 2017.
  source_name: Antiquated Mac Malware
  url: https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/
- description: Thomas Reed. (2017, July 7). New OSX.Dok malware intercepts web traffic. Retrieved July 10, 2017.
  source_name: OSX.Dok Malware
  url: https://blog.malwarebytes.com/threat-analysis/2017/04/new-osx-dok-malware-intercepts-web-traffic/
id: attack-pattern--d10cbd34-42e3-45c0-84d2-535a09849584
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:25.367Z'
name: Launch Agent
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Antonio Piazza, @antman1p
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '1.5'
```
