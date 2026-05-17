---
parsed_by: focuslocust
source: mitre
type: generated
---
# Transport Agent

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1505.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Transport Agent](../../attack/techniques/T1505.002-transport-agent.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1505.002 |
| name | Transport Agent |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1505/002 |

## Preserved Source Material

```yaml
created: '2019-12-12T15:08:20.972Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse Microsoft transport agents to establish persistent access to systems. Microsoft Exchange\
  \ transport agents can operate on email messages passing through the transport pipeline to perform various tasks such as\
  \ filtering spam, filtering malicious attachments, journaling, or adding a corporate signature to the end of all outgoing\
  \ emails.(Citation: Microsoft TransportAgent Jun 2016)(Citation: ESET LightNeuron May 2019) Transport agents can be written\
  \ by application developers and then compiled to .NET assemblies that are subsequently registered with the Exchange server.\
  \ Transport agents will be invoked during a specified stage of email processing and carry out developer defined tasks. \n\
  \nAdversaries may register a malicious transport agent to provide a persistence mechanism in Exchange Server that can be\
  \ triggered by adversary-specified email events.(Citation: ESET LightNeuron May 2019) Though a malicious transport agent\
  \ may be invoked for all emails passing through the Exchange transport pipeline, the agent can be configured to only carry\
  \ out specific tasks in response to adversary defined criteria. For example, the transport agent may only carry out an action\
  \ like copying in-transit attachments and saving them for later exfiltration if the recipient email address matches an entry\
  \ on a list provided by the adversary. "
external_references:
- external_id: T1505.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1505/002
- description: Microsoft. (2016, June 1). Transport agents. Retrieved June 24, 2019.
  source_name: Microsoft TransportAgent Jun 2016
  url: https://docs.microsoft.com/en-us/exchange/transport-agents-exchange-2013-help
- description: 'Faou, M. (2019, May). Turla LightNeuron: One email away from remote code execution. Retrieved June 24, 2019.'
  source_name: ESET LightNeuron May 2019
  url: https://www.welivesecurity.com/wp-content/uploads/2019/05/ESET-LightNeuron.pdf
id: attack-pattern--35187df2-31ed-43b6-a1f5-2f1d3d58d3f1
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:38.001Z'
name: Transport Agent
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- ESET
- Christoffer Strömblad
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
x_mitre_version: '1.1'
```
