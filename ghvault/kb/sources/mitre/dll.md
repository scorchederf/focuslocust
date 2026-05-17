---
parsed_by: focuslocust
source: mitre
type: generated
---
# DLL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1574.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DLL](../../attack/techniques/T1574.001-dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1574.001 |
| name | DLL |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1574/001 |

## Preserved Source Material

```yaml
created: '2020-03-13T18:11:08.357Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse dynamic-link library files (DLLs) in order to achieve persistence, escalate privileges,
  and evade defenses. DLLs are libraries that contain code and data that can be simultaneously utilized by multiple programs.
  While DLLs are not malicious by nature, they can be abused through mechanisms such as side-loading, hijacking search order,
  and phantom DLL hijacking.(Citation: unit 42)


  Specific ways DLLs are abused by adversaries include:


  ### DLL Sideloading

  Adversaries may execute their own malicious payloads by side-loading DLLs. Side-loading involves hijacking which DLL a program
  loads by planting and then invoking a legitimate application that executes their payload(s).


  Side-loading positions both the victim application and malicious payload(s) alongside each other. Adversaries likely use
  side-loading as a means of masking actions they perform under a legitimate, trusted, and potentially elevated system or
  software process. Benign executables used to side-load payloads may not be flagged during delivery and/or execution. Adversary
  payloads may also be encrypted/packed or otherwise obfuscated until loaded into the memory of the trusted process.


  Adversaries may also side-load other packages, such as BPLs (Borland Package Library).(Citation: kroll bpl)


  Adversaries may chain DLL sideloading multiple times to fragment functionality hindering analysis. Adversaries using multiple
  DLL files can split the loader functions across different DLLs, with a main DLL loading the separated export functions.
  (Citation: Virus Bulletin) Spreading loader functions across multiple DLLs makes analysis harder, since all files must be
  collected to fully understand the malware’s behavior.  Another method implements a “loader-for-a-loader”, where a malicious
  DLL’s sole role is to load a second DLL (or a chain of DLLs) that contain the real payload. (Citation: Sophos)


  ### DLL Search Order Hijacking

  Adversaries may execute their own malicious payloads by hijacking the search order that Windows uses to load DLLs. This
  search order is a sequence of special and standard search locations that a program checks when loading a DLL. An adversary
  can plant a trojan DLL in a directory that will be prioritized by the DLL search order over the location of a legitimate
  library. This will cause Windows to load the malicious DLL when it is called for by the victim program.(Citation: unit 42)


  ### DLL Redirection

  Adversaries may directly modify the search order via DLL redirection, which after being enabled (in the Registry or via
  the creation of a redirection file) may cause a program to load a DLL from a different location.(Citation: Microsoft redirection)(Citation:
  Microsoft - manifests/assembly)


  ### Phantom DLL Hijacking

  Adversaries may leverage phantom DLL hijacking by targeting references to non-existent DLL files. They may be able to load
  their own malicious DLL by planting it with the correct name in the location of the missing module.(Citation: Hexacorn DLL
  Hijacking)(Citation: Hijack DLLs CrowdStrike)


  ### DLL Substitution

  Adversaries may target existing, valid DLL files and substitute them with their own malicious DLLs, planting them with the
  same name and in the same location as the valid DLL file.(Citation: Wietze Beukema DLL Hijacking)


  Programs that fall victim to DLL hijacking may appear to behave normally because malicious DLLs may be configured to also
  load the legitimate DLLs they were meant to replace, evading defenses.


  Remote DLL hijacking can occur when a program sets its current directory to a remote location, such as a Web share, before
  loading a DLL.(Citation: dll pre load owasp)(Citation: microsoft remote preloading)


  If a valid DLL is configured to run at a higher privilege level, then the adversary-controlled DLL that is loaded will also
  be executed at the higher level. In this case, the technique could be used for privilege escalation.'
external_references:
- external_id: T1574.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1574/001
- description: ' falcon.overwatch.team. (2022, December 30). 4 Ways Adversaries Hijack DLLs — and How CrowdStrike Falcon OverWatch
    Fights Back. Retrieved January 30, 2025.'
  source_name: Hijack DLLs CrowdStrike
  url: https://www.crowdstrike.com/en-us/blog/4-ways-adversaries-hijack-dlls/
- description: Dave Truman. (2024, June 24). Novel Technique Combination Used In IDATLOADER Distribution. Retrieved January
    30, 2025.
  source_name: kroll bpl
  url: https://www.kroll.com/en/insights/publications/cyber/idatloader-distribution
- description: Gabor Szappanos. (2023, May 3). A doubled “Dragon Breath” adds new air to DLL sideloading attacks. Retrieved
    October 3, 2025.
  source_name: Sophos
  url: https://news.sophos.com/en-us/2023/05/03/doubled-dll-sideloading-dragon-breath/
- description: Hexacorn. (2013, December 8). Beyond good ol’ Run key, Part 5. Retrieved August 14, 2024.
  source_name: Hexacorn DLL Hijacking
  url: https://www.hexacorn.com/blog/2013/12/08/beyond-good-ol-run-key-part-5/
- description: 'Microsoft. (2014, May 13). Microsoft Security Advisory 2269637: Insecure Library Loading Could Allow Remote
    Code Execution. Retrieved January 30, 2025.'
  source_name: microsoft remote preloading
  url: https://learn.microsoft.com/en-us/security-updates/securityadvisories/2010/2269637
- description: Microsoft. (2021, January 7). Manifests. Retrieved January 30, 2025.
  source_name: Microsoft - manifests/assembly
  url: https://learn.microsoft.com/en-us/windows/win32/sbscs/manifests?redirectedfrom=MSDN
- description: Microsoft. (2023, October 12). Dynamic-link library redirection. Retrieved January 30, 2025.
  source_name: Microsoft redirection
  url: https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-redirection?redirectedfrom=MSDN
- description: OWASP. (n.d.). Binary Planting. Retrieved January 30, 2025.
  source_name: dll pre load owasp
  url: https://owasp.org/www-community/attacks/Binary_planting
- description: 'Suguru Ishimaru, Hajime Yanagishita, Yusuke Niwa. (2023, October 5). Unveiling activities of Tropic Trooper
    2023: deep analysis of Xiangoop Loader and EntryShell payload. Retrieved October 3, 2025.'
  source_name: Virus Bulletin
  url: https://www.virusbulletin.com/conference/vb2023/abstracts/unveiling-activities-tropic-trooper-2023-deep-analysis-xiangoop-loader-and-entryshell-payload/
- description: 'Tom Fakterman, Chen Erlich, & Assaf Dahan. (2024, February 22). Intruders in the Library: Exploring DLL Hijacking.
    Retrieved January 30, 2025.'
  source_name: unit 42
  url: https://unit42.paloaltonetworks.com/dll-hijacking-techniques/
- description: Wietze Beukema. (2020, June 22). Hijacking DLLs in Windows. Retrieved April 8, 2025.
  source_name: Wietze Beukema DLL Hijacking
  url: https://www.wietzebeukema.nl/blog/hijacking-dlls-in-windows
id: attack-pattern--2fee9321-3e71-4cf4-af24-d4d40d355b34
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T22:57:22.515Z'
name: DLL
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Ami Holeston, CrowdStrike
- Hajime Yanagishita, Macnica, Inc.
- Marina Liang
- Stefan Kanthak
- Suguru Ishimaru, ITOCHU Cyber & Intelligence Inc.
- Travis Smith, Tripwire
- Wietze Beukema @Wietze
- Will Alexander, CrowdStrike
- Yusuke Niwa, ITOCHU Cyber & Intelligence Inc.
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '3.0'
```
