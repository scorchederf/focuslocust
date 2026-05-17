---
parsed_by: focuslocust
source: mitre
type: generated
---
# Embedded Payloads

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1027.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Embedded Payloads](../../attack/techniques/T1027.009-embedded-payloads.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1027.009 |
| name | Embedded Payloads |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1027/009 |

## Preserved Source Material

```yaml
created: '2022-09-30T18:50:14.351Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may embed payloads within other files to conceal malicious content from defenses. Otherwise seemingly\
  \ benign files (such as scripts and executables) may be abused to carry and obfuscate malicious payloads and content. In\
  \ some cases, embedded payloads may also enable adversaries to [Subvert Trust Controls](https://attack.mitre.org/techniques/T1553)\
  \ by not impacting execution controls such as digital signatures and notarization tickets.(Citation: Sentinel Labs) \n\n\
  Adversaries may embed payloads in various file formats to hide payloads.(Citation: Microsoft Learn) This is similar to [Steganography](https://attack.mitre.org/techniques/T1027/003),\
  \ though does not involve weaving malicious content into specific bytes and patterns related to legitimate digital media\
  \ formats.(Citation: GitHub PSImage) \n\nFor example, adversaries have been observed embedding payloads within or as an\
  \ overlay of an otherwise benign binary.(Citation: Securelist Dtrack2) Adversaries have also been observed nesting payloads\
  \ (such as executables and run-only scripts) inside a file of the same format.(Citation: SentinelLabs reversing run-only\
  \ applescripts 2021) \n\nEmbedded content may also be used as [Process Injection](https://attack.mitre.org/techniques/T1055)\
  \ payloads used to infect benign system processes.(Citation: Trend Micro) These embedded then injected payloads may be used\
  \ as part of the modules of malware designed to provide specific features such as encrypting C2 communications in support\
  \ of an orchestrator module. For example, an embedded module may be injected into default browsers, allowing adversaries\
  \ to then communicate via the network.(Citation: Malware Analysis Report ComRAT)"
external_references:
- external_id: T1027.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1027/009
- description: Barrett Adams . (n.d.). Invoke-PSImage . Retrieved September 30, 2022.
  source_name: GitHub PSImage
  url: https://github.com/peewpw/Invoke-PSImage
- description: 'CISA. (2020, October 29). Malware Analysis Report (AR20-303A) MAR-10310246-2.v1 – PowerShell Script: ComRAT.
    Retrieved September 30, 2022.'
  source_name: Malware Analysis Report ComRAT
  url: https://www.cisa.gov/uscert/ncas/analysis-reports/ar20-303a
- description: Karen Victor. (2020, May 18). Reflective Loading Runs Netwalker Fileless Ransomware. Retrieved September 30,
    2022.
  source_name: Trend Micro
  url: https://www.trendmicro.com/en_us/research/20/e/netwalker-fileless-ransomware-injected-via-reflective-loading.html
- description: KONSTANTIN ZYKOV. (2019, September 23). Hello! My name is Dtrack. Retrieved September 30, 2022.
  source_name: Securelist Dtrack2
  url: https://securelist.com/my-name-is-dtrack/93338/
- description: Microsoft. (2021, April 6). 2.5 ExtraData. Retrieved September 30, 2022.
  source_name: Microsoft Learn
  url: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/c41e062d-f764-4f13-bd4f-ea812ab9a4d1
- description: Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved
    September 29, 2022.
  source_name: SentinelLabs reversing run-only applescripts 2021
  url: https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/
- description: Phil Stokes. (2021, January 11). FADE DEAD | Adventures in Reversing Malicious Run-Only AppleScripts. Retrieved
    September 30, 2022.
  source_name: Sentinel Labs
  url: https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/
id: attack-pattern--0533ab23-3f7d-463f-9bd8-634d27e4dee1
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:18:17.938Z'
name: Embedded Payloads
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Nick Cairns, @grotezinfosec
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
