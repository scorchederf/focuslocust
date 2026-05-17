---
parsed_by: focuslocust
source: mitre
type: generated
---
# Trusted Developer Utilities Proxy Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1127` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1127 |
| name | Trusted Developer Utilities Proxy Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1127 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:39.262Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may take advantage of trusted developer utilities to proxy execution of malicious payloads. There
  are many utilities used for software development related tasks that can be used to execute code in various forms to assist
  in development, debugging, and reverse engineering.(Citation: engima0x3 DNX Bypass)(Citation: engima0x3 RCSI Bypass)(Citation:
  Exploit Monday WinDbg)(Citation: LOLBAS Tracker) These utilities may often be signed with legitimate certificates that allow
  them to execute on a system and proxy execution of malicious code through a trusted process that effectively bypasses application
  control solutions.


  Smart App Control is a feature of Windows that blocks applications it considers potentially malicious from running by verifying
  unsigned applications against a known safe list from a Microsoft cloud service before executing them.(Citation: Microsoft
  Smart App Control) However, adversaries may leverage "reputation hijacking" to abuse an operating system’s trust of safe,
  signed applications that support the execution of arbitrary code. By leveraging [Trusted Developer Utilities Proxy Execution](https://attack.mitre.org/techniques/T1127)
  to run their malicious code, adversaries may bypass Smart App Control protections.(Citation: Elastic Security Labs)'
external_references:
- external_id: T1127
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1127
- description: Graeber, M. (2016, August 15). Bypassing Application Whitelisting by using WinDbg/CDB as a Shellcode Runner.
    Retrieved November 17, 2024.
  source_name: Exploit Monday WinDbg
  url: https://web.archive.org/web/20160816135945/http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html
- description: Joe Desimone. (2024, August 5). Dismantling Smart App Control. Retrieved March 21, 2025.
  source_name: Elastic Security Labs
  url: https://www.elastic.co/security-labs/dismantling-smart-app-control
- description: LOLBAS. (n.d.). Tracker.exe. Retrieved July 31, 2019.
  source_name: LOLBAS Tracker
  url: https://lolbas-project.github.io/lolbas/OtherMSBinaries/Tracker/
- description: Microsoft. (n.d.). Smart App Control Frequently Asked Questions. Retrieved April 4, 2025.
  source_name: Microsoft Smart App Control
  url: https://support.microsoft.com/en-us/windows/smart-app-control-frequently-asked-questions-285ea03d-fa88-4d56-882e-6698afdb7003
- description: Nelson, M. (2016, November 21). Bypassing Application Whitelisting By Using rcsi.exe. Retrieved May 26, 2017.
  source_name: engima0x3 RCSI Bypass
  url: https://enigma0x3.net/2016/11/21/bypassing-application-whitelisting-by-using-rcsi-exe/
- description: Nelson, M. (2017, November 17). Bypassing Application Whitelisting By Using dnx.exe. Retrieved May 25, 2017.
  source_name: engima0x3 DNX Bypass
  url: https://enigma0x3.net/2016/11/17/bypassing-application-whitelisting-by-using-dnx-exe/
id: attack-pattern--ff25900d-76d5-449b-a351-8824e62fc81b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-04-15T22:45:17.637Z'
name: Trusted Developer Utilities Proxy Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Casey Smith
- Matthew Demaske, Adaptforward
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.0'
```
