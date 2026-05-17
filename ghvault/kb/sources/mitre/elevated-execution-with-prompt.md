---
parsed_by: focuslocust
source: mitre
type: generated
---
# Elevated Execution with Prompt

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1548.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Elevated Execution with Prompt](../../attack/techniques/T1548.004-elevated-execution-with-prompt.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1548.004 |
| name | Elevated Execution with Prompt |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1548/004 |

## Preserved Source Material

```yaml
created: '2020-01-30T14:40:20.187Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may leverage the <code>AuthorizationExecuteWithPrivileges</code> API to escalate privileges by prompting\
  \ the user for credentials.(Citation: AppleDocs AuthorizationExecuteWithPrivileges) The purpose of this API is to give application\
  \ developers an easy way to perform operations with root privileges, such as for application installation or updating. This\
  \ API does not validate that the program requesting root privileges comes from a reputable source or has been maliciously\
  \ modified. \n\nAlthough this API is deprecated, it still fully functions in the latest releases of macOS. When calling\
  \ this API, the user will be prompted to enter their credentials but no checks on the origin or integrity of the program\
  \ are made. The program calling the API may also load world writable files which can be modified to perform malicious behavior\
  \ with elevated privileges.\n\nAdversaries may abuse <code>AuthorizationExecuteWithPrivileges</code> to obtain root privileges\
  \ in order to install malicious software on victims and install persistence mechanisms.(Citation: Death by 1000 installers;\
  \ it's all broken!)(Citation: Carbon Black Shlayer Feb 2019)(Citation: OSX Coldroot RAT) This technique may be combined\
  \ with [Masquerading](https://attack.mitre.org/techniques/T1036) to trick the user into granting escalated privileges to\
  \ malicious code.(Citation: Death by 1000 installers; it's all broken!)(Citation: Carbon Black Shlayer Feb 2019) This technique\
  \ has also been shown to work by modifying legitimate programs present on the machine that make use of this API.(Citation:\
  \ Death by 1000 installers; it's all broken!)"
external_references:
- external_id: T1548.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1548/004
- description: Apple. (n.d.). Apple Developer Documentation - AuthorizationExecuteWithPrivileges. Retrieved August 8, 2019.
  source_name: AppleDocs AuthorizationExecuteWithPrivileges
  url: https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg
- description: Carbon Black Threat Analysis Unit. (2019, February 12). New macOS Malware Variant of Shlayer (OSX) Discovered.
    Retrieved August 8, 2019.
  source_name: Carbon Black Shlayer Feb 2019
  url: https://blogs.vmware.com/security/2020/02/vmware-carbon-black-tau-threat-analysis-shlayer-macos.html
- description: Patrick Wardle. (2017). Death by 1000 installers; it's all broken!. Retrieved August 8, 2019.
  source_name: Death by 1000 installers; it's all broken!
  url: https://speakerdeck.com/patrickwardle/defcon-2017-death-by-1000-installers-its-all-broken?slide=8
- description: Patrick Wardle. (2018, February 17). Tearing Apart the Undetected (OSX)Coldroot RAT. Retrieved August 8, 2019.
  source_name: OSX Coldroot RAT
  url: https://objective-see.com/blog/blog_0x2A.html
id: attack-pattern--b84903f0-c7d5-435d-a69e-de47cc3578c0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:51:53.527Z'
name: Elevated Execution with Prompt
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Jimmy Astle, @AstleJimmy, Carbon Black
- Erika Noerenberg, @gutterchurl, Carbon Black
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '2.0'
```
