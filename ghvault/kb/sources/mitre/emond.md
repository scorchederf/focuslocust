---
parsed_by: focuslocust
source: mitre
type: generated
---
# Emond

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546.014` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Emond](../../attack/techniques/T1546.014-emond.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1546.014 |
| name | Emond |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1546/014 |

## Preserved Source Material

```yaml
created: '2020-01-24T15:15:13.426Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gain persistence and elevate privileges by executing malicious content triggered by the Event
  Monitor Daemon (emond). Emond is a [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) that accepts events from
  various services, runs them through a simple rules engine, and takes action. The emond binary at <code>/sbin/emond</code>
  will load any rules from the <code>/etc/emond.d/rules/</code> directory and take action once an explicitly defined event
  takes place.


  The rule files are in the plist format and define the name, event type, and action to take. Some examples of event types
  include system startup and user authentication. Examples of actions are to run a system command or send an email. The emond
  service will not launch if there is no file present in the QueueDirectories path <code>/private/var/db/emondClients</code>,
  specified in the [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) configuration file at<code>/System/Library/LaunchDaemons/com.apple.emond.plist</code>.(Citation:
  xorrior emond Jan 2018)(Citation: magnusviri emond Apr 2016)(Citation: sentinelone macos persist Jun 2019)


  Adversaries may abuse this service by writing a rule to execute commands when a defined event occurs, such as system start
  up or user authentication.(Citation: xorrior emond Jan 2018)(Citation: magnusviri emond Apr 2016)(Citation: sentinelone
  macos persist Jun 2019) Adversaries may also be able to escalate privileges from administrator to root as the emond service
  is executed with root privileges by the [Launch Daemon](https://attack.mitre.org/techniques/T1543/004) service.'
external_references:
- external_id: T1546.014
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1546/014
- description: Reynolds, James. (2016, April 7). What is emond?. Retrieved September 10, 2019.
  source_name: magnusviri emond Apr 2016
  url: http://www.magnusviri.com/Mac/what-is-emond.html
- description: Ross, Chris. (2018, January 17). Leveraging Emond on macOS For Persistence. Retrieved September 10, 2019.
  source_name: xorrior emond Jan 2018
  url: https://www.xorrior.com/emond-persistence/
- description: Stokes, Phil. (2019, June 17). HOW MALWARE PERSISTS ON MACOS. Retrieved September 10, 2019.
  source_name: sentinelone macos persist Jun 2019
  url: https://www.sentinelone.com/blog/how-malware-persists-on-macos/
id: attack-pattern--9c45eaa3-8604-4780-8988-b5074dbb9ecd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:08.766Z'
name: Emond
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Ivan Sinyakov
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '1.1'
```
