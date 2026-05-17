---
parsed_by: focuslocust
source: mitre
type: generated
---
# Parent PID Spoofing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1134.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Parent PID Spoofing](../../attack/techniques/T1134.004-parent-pid-spoofing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1134.004 |
| name | Parent PID Spoofing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1134/004 |

## Preserved Source Material

```yaml
created: '2020-02-18T18:22:41.448Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may spoof the parent process identifier (PPID) of a new process to evade process-monitoring defenses
  or to elevate privileges. New processes are typically spawned directly from their parent, or calling, process unless explicitly
  specified. One way of explicitly assigning the PPID of a new process is via the <code>CreateProcess</code> API call, which
  supports a parameter that defines the PPID to use.(Citation: DidierStevens SelectMyParent Nov 2009) This functionality is
  used by Windows features such as User Account Control (UAC) to correctly set the PPID after a requested elevated process
  is spawned by SYSTEM (typically via <code>svchost.exe</code> or <code>consent.exe</code>) rather than the current user context.(Citation:
  Microsoft UAC Nov 2018)


  Adversaries may abuse these mechanisms to evade defenses, such as those blocking processes spawning directly from Office
  documents, and analysis targeting unusual/potentially malicious parent-child process relationships, such as spoofing the
  PPID of [PowerShell](https://attack.mitre.org/techniques/T1059/001)/[Rundll32](https://attack.mitre.org/techniques/T1218/011)
  to be <code>explorer.exe</code> rather than an Office document delivered as part of [Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001).(Citation:
  CounterCept PPID Spoofing Dec 2018) This spoofing could be executed via [Visual Basic](https://attack.mitre.org/techniques/T1059/005)
  within a malicious Office document or any code that can perform [Native API](https://attack.mitre.org/techniques/T1106).(Citation:
  CTD PPID Spoofing Macro Mar 2019)(Citation: CounterCept PPID Spoofing Dec 2018)


  Explicitly assigning the PPID may also enable elevated privileges given appropriate access rights to the parent process.
  For example, an adversary in a privileged user context (i.e. administrator) may spawn a new process and assign the parent
  as a process running as SYSTEM (such as <code>lsass.exe</code>), causing the new process to be elevated via the inherited
  access token.(Citation: XPNSec PPID Nov 2017)'
external_references:
- external_id: T1134.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1134/004
- description: Chester, A. (2017, November 20). Alternative methods of becoming SYSTEM. Retrieved June 4, 2019.
  source_name: XPNSec PPID Nov 2017
  url: https://blog.xpnsec.com/becoming-system/
- description: Loh, I. (2018, December 21). Detecting Parent PID Spoofing. Retrieved June 3, 2019.
  source_name: CounterCept PPID Spoofing Dec 2018
  url: https://web.archive.org/web/20200726110643/https://blog.f-secure.com/detecting-parent-pid-spoofing/
- description: Montemayor, D. et al.. (2018, November 15). How User Account Control works. Retrieved June 3, 2019.
  source_name: Microsoft UAC Nov 2018
  url: https://docs.microsoft.com/windows/security/identity-protection/user-account-control/how-user-account-control-works
- description: 'Stevens, D. (2009, November 22). Quickpost: SelectMyParent or Playing With the Windows Process Tree. Retrieved
    June 3, 2019.'
  source_name: DidierStevens SelectMyParent Nov 2009
  url: https://blog.didierstevens.com/2009/11/22/quickpost-selectmyparent-or-playing-with-the-windows-process-tree/
- description: Tafani-Dereeper, C. (2019, March 12). Building an Office macro to spoof parent processes and command line arguments.
    Retrieved June 3, 2019.
  source_name: CTD PPID Spoofing Macro Mar 2019
  url: https://blog.christophetd.fr/building-an-office-macro-to-spoof-process-parent-and-command-line/
id: attack-pattern--93591901-3172-4e94-abf8-6034ab26f44a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:54:42.976Z'
name: Parent PID Spoofing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Wayne Silva, F-Secure Countercept
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
