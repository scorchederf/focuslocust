---
parsed_by: focuslocust
source: mitre
type: generated
---
# GUI Input Capture

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1056.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [GUI Input Capture](../../attack/techniques/T1056.002-gui-input-capture.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1056.002 |
| name | GUI Input Capture |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1056/002 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:58:45.908Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may mimic common operating system GUI components to prompt users for credentials with a seemingly
  legitimate prompt. When programs are executed that need additional privileges than are present in the current user context,
  it is common for the operating system to prompt the user for proper credentials to authorize the elevated privileges for
  the task (ex: [Bypass User Account Control](https://attack.mitre.org/techniques/T1548/002)).


  Adversaries may mimic this functionality to prompt users for credentials with a seemingly legitimate prompt for a number
  of reasons that mimic normal usage, such as a fake installer requiring additional access or a fake malware removal suite.(Citation:
  OSX Malware Exploits MacKeeper) This type of prompt can be used to collect credentials via various languages such as [AppleScript](https://attack.mitre.org/techniques/T1059/002)(Citation:
  LogRhythm Do You Trust Oct 2014)(Citation: OSX Keydnap malware)(Citation: Spoofing credential dialogs) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).(Citation:
  LogRhythm Do You Trust Oct 2014)(Citation: Enigma Phishing for Credentials Jan 2015)(Citation: Spoofing credential dialogs)
  On Linux systems adversaries may launch dialog boxes prompting users for credentials from malicious shell scripts or the
  command line (i.e. [Unix Shell](https://attack.mitre.org/techniques/T1059/004)).(Citation: Spoofing credential dialogs)


  Adversaries may also mimic common software authentication requests, such as those from browsers or email clients. This may
  also be paired with user activity monitoring (i.e., [Browser Information Discovery](https://attack.mitre.org/techniques/T1217)
  and/or [Application Window Discovery](https://attack.mitre.org/techniques/T1010)) to spoof prompts when users are naturally
  accessing sensitive sites/data.'
external_references:
- external_id: T1056.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1056/002
- description: Foss, G. (2014, October 3). Do You Trust Your Computer?. Retrieved December 17, 2018.
  source_name: LogRhythm Do You Trust Oct 2014
  url: https://logrhythm.com/blog/do-you-trust-your-computer/
- description: Johann Rehberger. (2021, April 18). Spoofing credential dialogs on macOS Linux and Windows. Retrieved August
    19, 2021.
  source_name: Spoofing credential dialogs
  url: https://embracethered.com/blog/posts/2021/spoofing-credential-dialogs/
- description: Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July
    3, 2017.
  source_name: OSX Keydnap malware
  url: https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/
- description: 'Nelson, M. (2015, January 21). Phishing for Credentials: If you want it, just ask!. Retrieved December 17,
    2018.'
  source_name: Enigma Phishing for Credentials Jan 2015
  url: https://enigma0x3.net/2015/01/21/phishing-for-credentials-if-you-want-it-just-ask/
- description: Sergei Shevchenko. (2015, June 4). New Mac OS Malware Exploits Mackeeper. Retrieved July 3, 2017.
  source_name: OSX Malware Exploits MacKeeper
  url: https://baesystemsai.blogspot.com/2015/06/new-mac-os-malware-exploits-mackeeper.html
id: attack-pattern--a2029942-0a85-4947-b23c-ca434698171d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:10.643Z'
name: GUI Input Capture
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Matthew Molyett, @s1air, Cisco Talos
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.3'
```
