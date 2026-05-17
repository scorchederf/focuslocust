---
parsed_by: focuslocust
source: mitre
type: generated
---
# Keylogging

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1056.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Keylogging](../../attack/techniques/T1056.001-keylogging.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1056.001 |
| name | Keylogging |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1056/001 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:58:11.791Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may log user keystrokes to intercept credentials as the user types them. Keylogging is likely to
  be used to acquire credentials for new access opportunities when [OS Credential Dumping](https://attack.mitre.org/techniques/T1003)
  efforts are not effective, and may require an adversary to intercept keystrokes on a system for a substantial period of
  time before credentials can be successfully captured. In order to increase the likelihood of capturing credentials quickly,
  an adversary may also perform actions such as clearing browser cookies to force users to reauthenticate to systems.(Citation:
  Talos Kimsuky Nov 2021)


  Keylogging is the most prevalent type of input capture, with many different ways of intercepting keystrokes.(Citation: Adventures
  of a Keystroke) Some methods include:


  * Hooking API callbacks used for processing keystrokes. Unlike [Credential API Hooking](https://attack.mitre.org/techniques/T1056/004),
  this focuses solely on API functions intended for processing keystroke data.

  * Reading raw keystroke data from the hardware buffer.

  * Windows Registry modifications.

  * Custom drivers.

  * [Modify System Image](https://attack.mitre.org/techniques/T1601) may provide adversaries with hooks into the operating
  system of network devices to read raw keystrokes for login sessions.(Citation: Cisco Blog Legacy Device Attacks) '
external_references:
- external_id: T1056.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1056/001
- description: An, J and Malhotra, A. (2021, November 10). North Korean attackers use malicious blogs to deliver malware to
    high-profile South Korean targets. Retrieved December 29, 2021.
  source_name: Talos Kimsuky Nov 2021
  url: https://blog.talosintelligence.com/2021/11/kimsuky-abuses-blogs-delivers-malware.html
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
- description: 'Tinaztepe,  E. (n.d.). The Adventures of a Keystroke:  An in-depth look into keyloggers on Windows. Retrieved
    April 27, 2016.'
  source_name: Adventures of a Keystroke
  url: http://opensecuritytraining.info/Keylogging_files/The%20Adventures%20of%20a%20Keystroke.pdf
id: attack-pattern--09a60ea3-a8d1-4ae5-976e-5783248b72a4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:21.756Z'
name: Keylogging
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- TruKno
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.3'
```
