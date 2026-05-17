---
parsed_by: focuslocust
source: mitre
type: generated
---
# Credential API Hooking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1056.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credential API Hooking](../../attack/techniques/T1056.004-credential-api-hooking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1056.004 |
| name | Credential API Hooking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1056/004 |

## Preserved Source Material

```yaml
created: '2020-02-11T19:01:15.930Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may hook into Windows application programming interface (API) functions and Linux system functions\
  \ to collect user credentials. Malicious hooking mechanisms may capture API or function calls that include parameters that\
  \ reveal user authentication credentials.(Citation: Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017) Unlike [Keylogging](https://attack.mitre.org/techniques/T1056/001),\
  \ this technique focuses specifically on API functions that include parameters that reveal user credentials. \n\nIn Windows,\
  \ hooking involves redirecting calls to these functions and can be implemented via:\n\n* **Hooks procedures**, which intercept\
  \ and execute designated code in response to events such as messages, keystrokes, and mouse inputs.(Citation: Microsoft\
  \ Hook Overview)(Citation: Elastic Process Injection July 2017)\n* **Import address table (IAT) hooking**, which use modifications\
  \ to a process’s IAT, where pointers to imported API functions are stored.(Citation: Elastic Process Injection July 2017)(Citation:\
  \ Adlice Software IAT Hooks Oct 2014)(Citation: MWRInfoSecurity Dynamic Hooking 2015)\n* **Inline hooking**, which overwrites\
  \ the first bytes in an API function to redirect code flow.(Citation: Elastic Process Injection July 2017)(Citation: HighTech\
  \ Bridge Inline Hooking Sept 2011)(Citation: MWRInfoSecurity Dynamic Hooking 2015)\n\nIn Linux and macOS, adversaries may\
  \ hook into system functions via the `LD_PRELOAD` (Linux) or `DYLD_INSERT_LIBRARIES` (macOS) environment variables, which\
  \ enables loading shared libraries into a program’s address space. For example, an adversary may capture credentials by\
  \ hooking into the `libc read` function leveraged by SSH or SCP.(Citation: Intezer Symbiote 2022)"
external_references:
- external_id: T1056.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1056/004
- description: 'Eye of Ra. (2017, June 27). Windows Keylogger Part 2: Defense against user-land. Retrieved December 12, 2017.'
  source_name: EyeofRa Detecting Hooking June 2017
  url: https://eyeofrablog.wordpress.com/2017/06/27/windows-keylogger-part-2-defense-against-user-land/
- description: Felici, M. (2006, December 6). Any application-defined hook procedure on my machine?. Retrieved December 12,
    2017.
  source_name: Zairon Hooking Dec 2006
  url: https://zairon.wordpress.com/2006/12/06/any-application-defined-hook-procedure-on-my-machine/
- description: GMER. (n.d.). GMER. Retrieved December 12, 2017.
  source_name: GMER Rootkits
  url: http://www.gmer.net/
- description: 'Hillman, M. (2015, August 8). Dynamic Hooking Techniques: User Mode. Retrieved December 20, 2017.'
  source_name: MWRInfoSecurity Dynamic Hooking 2015
  url: https://www.mwrinfosecurity.com/our-thinking/dynamic-hooking-techniques-user-mode/
- description: 'Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending
    Process Injection Techniques. Retrieved December 7, 2017.'
  source_name: Elastic Process Injection July 2017
  url: https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process
- description: 'Joakim Kennedy and The BlackBerry Threat Research & Intelligence Team. (2022, June 9). Symbiote Deep-Dive:
    Analysis of a New, Nearly-Impossible-to-Detect Linux Threat. Retrieved March 24, 2025.'
  source_name: Intezer Symbiote 2022
  url: https://intezer.com/blog/research/new-linux-threat-symbiote/
- description: Mariani, B. (2011, September 6). Inline Hooking in Windows. Retrieved November 17, 2024.
  source_name: HighTech Bridge Inline Hooking Sept 2011
  url: https://www.scribd.com/document/68671361/Inline-Hooking-in-Windows
- description: Microsoft. (2017, September 15). TrojanSpy:Win32/Ursnif.gen!I. Retrieved December 18, 2017.
  source_name: Microsoft TrojanSpy:Win32/Ursnif.gen!I Sept 2017
  url: https://www.microsoft.com/en-us/wdsi/threats/malware-encyclopedia-description?Name=TrojanSpy:Win32/Ursnif.gen!I&threatId=-2147336918
- description: Microsoft. (n.d.). Hooks Overview. Retrieved December 12, 2017.
  source_name: Microsoft Hook Overview
  url: https://msdn.microsoft.com/library/windows/desktop/ms644959.aspx
- description: Microsoft. (n.d.). Taking a Snapshot and Viewing Processes. Retrieved December 12, 2017.
  source_name: Microsoft Process Snapshot
  url: https://msdn.microsoft.com/library/windows/desktop/ms686701.aspx
- description: Prekas, G. (2011, July 11). Winhook. Retrieved December 12, 2017.
  source_name: PreKageo Winhook Jul 2011
  url: https://github.com/prekageo/winhook
- description: Satiro, J. (2011, September 14). GetHooks. Retrieved December 12, 2017.
  source_name: Jay GetHooks Sept 2011
  url: https://github.com/jay/gethooks
- description: Stack Exchange - Security. (2012, July 31). What are the methods to find hooked functions and APIs?. Retrieved
    December 12, 2017.
  source_name: StackExchange Hooks Jul 2012
  url: https://security.stackexchange.com/questions/17904/what-are-the-methods-to-find-hooked-functions-and-apis
- description: 'Tigzy. (2014, October 15). Userland Rootkits: Part 1, IAT hooks. Retrieved December 12, 2017.'
  source_name: Adlice Software IAT Hooks Oct 2014
  url: https://www.adlice.com/userland-rootkits-part-1-iat-hooks/
- description: Volatility Labs. (2012, September 24). MoVP 3.1 Detecting Malware Hooks in the Windows GUI Subsystem. Retrieved
    December 12, 2017.
  source_name: Volatility Detecting Hooks Sept 2012
  url: https://volatility-labs.blogspot.com/2012/09/movp-31-detecting-malware-hooks-in.html
id: attack-pattern--f5946b5e-9408-485f-a7f7-b5efc88909b6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:49:37.119Z'
name: Credential API Hooking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- Linux
- macOS
x_mitre_version: '1.2'
```
