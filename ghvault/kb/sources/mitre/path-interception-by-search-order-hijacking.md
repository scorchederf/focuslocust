---
parsed_by: focuslocust
source: mitre
type: generated
---
# Path Interception by Search Order Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.008` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Path Interception by Search Order Hijacking](../../attack/techniques/T1574.008-path-interception-by-search-order-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.008 |
| name | Path Interception by Search Order Hijacking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/008 |

## Preserved Source Material

```yaml
created: '2020-03-13T17:48:58.999Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may execute their own malicious payloads by hijacking the search order used to load other programs.
  Because some programs do not call other programs using the full path, adversaries may place their own file in the directory
  where the calling program is located, causing the operating system to launch their malicious software at the request of
  the calling program.


  Search order hijacking occurs when an adversary abuses the order in which Windows searches for programs that are not given
  a path. Unlike [DLL](https://attack.mitre.org/techniques/T1574/001) search order hijacking, the search order differs depending
  on the method that is used to execute the program. (Citation: Microsoft CreateProcess) (Citation: Windows NT Command Shell)
  (Citation: Microsoft WinExec) However, it is common for Windows to search in the directory of the initiating program before
  searching through the Windows system directory. An adversary who finds a program vulnerable to search order hijacking (i.e.,
  a program that does not specify the path to an executable) may take advantage of this vulnerability by creating a program
  named after the improperly specified program and placing it within the initiating program''s directory.


  For example, "example.exe" runs "cmd.exe" with the command-line argument <code>net user</code>. An adversary may place a
  program called "net.exe" within the same directory as example.exe, "net.exe" will be run instead of the Windows system utility
  net. In addition, if an adversary places a program called "net.com" in the same directory as "net.exe", then <code>cmd.exe
  /C net user</code> will execute "net.com" instead of "net.exe" due to the order of executable extensions defined under PATHEXT.
  (Citation: Microsoft Environment Property)


  Search order hijacking is also a common practice for hijacking DLL loads and is covered in [DLL](https://attack.mitre.org/techniques/T1574/001).'
external_references:
- external_id: T1574.008
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/008
- description: Microsoft. (2011, October 24). Environment Property. Retrieved July 27, 2016.
  source_name: Microsoft Environment Property
  url: https://docs.microsoft.com/en-us/previous-versions//fd7hxfdd(v=vs.85)?redirectedfrom=MSDN
- description: Microsoft. (n.d.). CreateProcess function. Retrieved September 12, 2024.
  source_name: Microsoft CreateProcess
  url: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa
- description: Microsoft. (n.d.). WinExec function. Retrieved September 12, 2024.
  source_name: Microsoft WinExec
  url: https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-winexec
- description: Tim Hill. (2014, February 2). The Windows NT Command Shell. Retrieved December 5, 2014.
  source_name: Windows NT Command Shell
  url: https://docs.microsoft.com/en-us/previous-versions//cc723564(v=technet.10)?redirectedfrom=MSDN#XSLTsection127121120120
id: attack-pattern--58af3705-8740-4c68-9329-ec015a7013c2
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T23:01:48.263Z'
name: Path Interception by Search Order Hijacking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Stefan Kanthak
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
