---
parsed_by: focuslocust
source: mitre
type: generated
---
# Event Triggered Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Event Triggered Execution](../../attack/techniques/T1546-event-triggered-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1546 |
| name | Event Triggered Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1546 |

## Preserved Source Material

```yaml
created: '2020-01-22T21:04:23.285Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution
  based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other
  user activity such as running specific applications/binaries. Cloud environments may also support various functions and
  services that monitor and can be invoked in response to specific cloud events.(Citation: Backdooring an AWS account)(Citation:
  Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001)


  Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing
  malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious
  content that will be executed whenever the event trigger is invoked.(Citation: FireEye WMI 2015)(Citation: Malware Persistence
  on OS X)(Citation: amnesia malware)


  Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary
  may be able to abuse these triggered execution mechanisms to escalate their privileges. '
external_references:
- external_id: T1546
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1546
- description: Ballenthin, W., et al. (2015). Windows Management Instrumentation (WMI) Offense, Defense, and Forensics. Retrieved
    March 30, 2016.
  source_name: FireEye WMI 2015
  url: https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf
- description: Berk Veral. (2020, March 9). Real-life cybercrime stories from DART, the Microsoft Detection and Response Team.
    Retrieved May 27, 2022.
  source_name: Microsoft DART Case Report 001
  url: https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team
- description: Claud Xiao, Cong Zheng, Yanhui Jia. (2017, April 6). New IoT/Linux Malware Targets DVRs, Forms Botnet. Retrieved
    February 19, 2018.
  source_name: amnesia malware
  url: https://researchcenter.paloaltonetworks.com/2017/04/unit42-new-iotlinux-malware-targets-dvrs-forms-botnet/
- description: Daniel Grzelak. (2016, July 9). Backdooring an AWS account. Retrieved May 27, 2022.
  source_name: Backdooring an AWS account
  url: https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9
- description: Eric Saraga. (2022, February 2). Using Power Automate for Covert Data Exfiltration in Microsoft 365. Retrieved
    May 27, 2022.
  source_name: Varonis Power Automate Data Exfiltration
  url: https://www.varonis.com/blog/power-automate-data-exfiltration
- description: Patrick Wardle. (2015). Malware Persistence on OS X Yosemite. Retrieved July 10, 2017.
  source_name: Malware Persistence on OS X
  url: https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf
id: attack-pattern--b6301b64-ef57-4cce-bb0b-77026f14a8db
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:15.866Z'
name: Event Triggered Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
- SaaS
- IaaS
- Office Suite
x_mitre_version: '1.4'
```
