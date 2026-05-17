---
parsed_by: focuslocust
source: mitre
type: generated
---
# Kernel Modules and Extensions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kernel Modules and Extensions](../../attack/techniques/T1547.006-kernel-modules-and-extensions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.006 |
| name | Kernel Modules and Extensions |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/006 |

## Preserved Source Material

```yaml
created: '2020-01-24T17:42:23.339Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify the kernel to automatically execute programs on system boot. Loadable Kernel Modules
  (LKMs) are pieces of code that can be loaded and unloaded into the kernel upon demand. They extend the functionality of
  the kernel without the need to reboot the system. For example, one type of module is the device driver, which allows the
  kernel to access hardware connected to the system.(Citation: Linux Kernel Programming) 


  When used maliciously, LKMs can be a type of kernel-mode [Rootkit](https://attack.mitre.org/techniques/T1014) that run with
  the highest operating system privilege (Ring 0).(Citation: Linux Kernel Module Programming Guide) Common features of LKM
  based rootkits include: hiding itself, selective hiding of files, processes and network activity, as well as log tampering,
  providing authenticated backdoors, and enabling root access to non-privileged users.(Citation: iDefense Rootkit Overview)


  Kernel extensions, also called kext, are used in macOS to load functionality onto a system similar to LKMs for Linux. Since
  the kernel is responsible for enforcing security and the kernel extensions run as apart of the kernel, kexts are not governed
  by macOS security policies. Kexts are loaded and unloaded through <code>kextload</code> and <code>kextunload</code> commands.
  Kexts need to be signed with a developer ID that is granted privileges by Apple allowing it to sign Kernel extensions. Developers
  without these privileges may still sign kexts but they will not load unless SIP is disabled. If SIP is enabled, the kext
  signature is verified before being added to the AuxKC.(Citation: System and kernel extensions in macOS)


  Since macOS Catalina 10.15, kernel extensions have been deprecated in favor of System Extensions. However, kexts are still
  allowed as "Legacy System Extensions" since there is no System Extension for Kernel Programming Interfaces.(Citation: Apple
  Kernel Extension Deprecation)


  Adversaries can use LKMs and kexts to conduct [Persistence](https://attack.mitre.org/tactics/TA0003) and/or [Privilege Escalation](https://attack.mitre.org/tactics/TA0004)
  on a system. Examples have been found in the wild, and there are some relevant open source projects as well.(Citation: Volatility
  Phalanx2)(Citation: CrowdStrike Linux Rootkit)(Citation: GitHub Reptile)(Citation: GitHub Diamorphine)(Citation: RSAC 2015
  San Francisco Patrick Wardle)(Citation: Synack Secure Kernel Extension Broken)(Citation: Securelist Ventir)(Citation: Trend
  Micro Skidmap)'
external_references:
- external_id: T1547.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/006
- description: Apple. (2019, May 3). Configuration Profile Reference. Retrieved September 23, 2021.
  source_name: Apple Developer Configuration Profile
  url: https://developer.apple.com/business/documentation/Configuration-Profile-Reference.pdf
- description: Apple. (n.d.). Deprecated Kernel Extensions and System Extension Alternatives. Retrieved November 4, 2020.
  source_name: Apple Kernel Extension Deprecation
  url: https://developer.apple.com/support/kernel-extensions/
- description: Apple. (n.d.). System and kernel extensions in macOS. Retrieved March 31, 2022.
  source_name: System and kernel extensions in macOS
  url: https://support.apple.com/guide/deployment/system-and-kernel-extensions-in-macos-depa5fb8376f/web
- description: Augusto, I. (2018, March 8). Reptile - LMK Linux rootkit. Retrieved April 9, 2018.
  source_name: GitHub Reptile
  url: https://github.com/f0rb1dd3n/Reptile
- description: 'Case, A. (2012, October 10). Phalanx 2 Revealed: Using Volatility to Analyze an Advanced Linux Rootkit. Retrieved
    April 9, 2018.'
  source_name: Volatility Phalanx2
  url: https://volatility-labs.blogspot.com/2012/10/phalanx-2-revealed-using-volatility-to.html
- description: Chuvakin, A. (2003, February). An Overview of Rootkits. Retrieved September 12, 2024.
  source_name: iDefense Rootkit Overview
  url: https://www.megasecurity.org/papers/Rootkits.pdf
- description: Henderson, B. (2006, September 24). How To Insert And Remove LKMs. Retrieved November 17, 2024.
  source_name: Linux Loadable Kernel Module Insert and Remove LKMs
  url: https://tldp.org/HOWTO/Module-HOWTO/x197.html
- description: Kurtz, G. (2012, November 19). HTTP iframe Injecting Linux Rootkit. Retrieved December 21, 2017.
  source_name: CrowdStrike Linux Rootkit
  url: https://www.crowdstrike.com/blog/http-iframe-injecting-linux-rootkit/
- description: Mello, V. (2018, March 8). Diamorphine - LMK rootkit for Linux Kernels 2.6.x/3.x/4.x (x86 and x86_64). Retrieved
    April 9, 2018.
  source_name: GitHub Diamorphine
  url: https://github.com/m0nad/Diamorphine
- description: 'Mikhail, K. (2014, October 16). The Ventir Trojan: assemble your MacOS spy. Retrieved April 6, 2018.'
  source_name: Securelist Ventir
  url: https://securelist.com/the-ventir-trojan-assemble-your-macos-spy/67267/
- description: Pikeralpha. (2017, August 29). User Approved Kernel Extension Loading…. Retrieved September 23, 2021.
  source_name: User Approved Kernel Extension Pike’s
  url: https://pikeralpha.wordpress.com/2017/08/29/user-approved-kernel-extension-loading/
- description: Pomerantz, O., Salzman, P. (2003, April 4). Modules vs Programs. Retrieved November 17, 2024.
  source_name: Linux Kernel Module Programming Guide
  url: https://tldp.org/LDP/lkmpg/2.4/html/x437.html
- description: Pomerantz, O., Salzman, P.. (2003, April 4). The Linux Kernel Module Programming Guide. Retrieved April 6,
    2018.
  source_name: Linux Kernel Programming
  url: https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf
- description: Remillano, A., Urbanec, J. (2019, September 19). Skidmap Linux Malware Uses Rootkit Capabilities to Hide Cryptocurrency-Mining
    Payload. Retrieved June 4, 2020.
  source_name: Trend Micro Skidmap
  url: https://blog.trendmicro.com/trendlabs-security-intelligence/skidmap-linux-malware-uses-rootkit-capabilities-to-hide-cryptocurrency-mining-payload/
- description: Richard Purves. (2017, November 9). MDM and the Kextpocalypse . Retrieved September 23, 2021.
  source_name: Purves Kextpocalypse 2
  url: https://richard-purves.com/2017/11/09/mdm-and-the-kextpocalypse-2/
- description: Wardle, P. (2015, April). Malware Persistence on OS X Yosemite. Retrieved April 6, 2018.
  source_name: RSAC 2015 San Francisco Patrick Wardle
  url: https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf
- description: Wardle, P. (2017, September 8). High Sierra’s ‘Secure Kernel Extension Loading’ is Broken. Retrieved November
    17, 2024.
  source_name: Synack Secure Kernel Extension Broken
  url: https://objective-see.org/blog/blog_0x21.html
- description: Wikipedia. (2018, March 17). Loadable kernel module. Retrieved April 9, 2018.
  source_name: Wikipedia Loadable Kernel Module
  url: https://en.wikipedia.org/wiki/Loadable_kernel_module#Linux
id: attack-pattern--a1b52199-c8c5-438a-9ded-656f1d0888c6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:10.550Z'
name: Kernel Modules and Extensions
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Wayne Silva, F-Secure Countercept
- Anastasios Pingios
- Jeremy Galloway
- Red Canary
- Eric Kaiser @ideologysec
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
- Linux
x_mitre_version: '1.4'
```
