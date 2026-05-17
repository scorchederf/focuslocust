---
parsed_by: focuslocust
source: mitre
type: generated
---
# Malicious Copy and Paste

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1204.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Malicious Copy and Paste](../../attack/techniques/T1204.004-malicious-copy-and-paste.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1204.004 |
| name | Malicious Copy and Paste |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1204/004 |

## Preserved Source Material

```yaml
created: '2025-03-18T12:57:50.188Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may rely upon a user copying and pasting code in order to gain execution. Users may be subjected
  to social engineering to get them to copy and paste code directly into a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059).
  One such strategy is "ClickFix," in which adversaries present users with seemingly helpful solutions—such as prompts to
  fix errors or complete CAPTCHAs—that instead instruct the user to copy and paste malicious code.


  Malicious websites, such as those used in [Drive-by Compromise](https://attack.mitre.org/techniques/T1189), may present
  fake error messages or CAPTCHA prompts that instruct users to open a terminal or the Windows Run Dialog box and execute
  an arbitrary command. These commands may be obfuscated using encoding or other techniques to conceal malicious intent. Once
  executed, the adversary will typically be able to establish a foothold on the victim''s machine.(Citation: CloudSEK Lumma
  Stealer 2024)(Citation: Sekoia ClickFake 2025)(Citation: Reliaquest CAPTCHA 2024)(Citation: AhnLab LummaC2 2025)


  Adversaries may also leverage phishing emails for this purpose. When a user attempts to open an attachment, they may be
  presented with a fake error and offered a malicious command to paste as a solution, consistent with the "ClickFix" strategy.(Citation:
  Proofpoint ClickFix 2024)(Citation: AhnLab Malicioys Copy Paste 2024)


  Tricking a user into executing a command themselves may help to bypass email filtering, browser sandboxing, or other mitigations
  designed to protect users against malicious downloaded files. '
external_references:
- external_id: T1204.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1204/004
- description: AhnLab SEcurity intelligence Center. (2024, May 23). Warning Against Phishing Emails Prompting Execution of
    Commands via Paste (CTRL+V). Retrieved April 23, 2025.
  source_name: AhnLab Malicioys Copy Paste 2024
  url: https://asec.ahnlab.com/en/73952/
- description: AhnLab SEcurity intelligence Center. (2025, January 8). Infostealer LummaC2 Spreading Through Fake CAPTCHA
    Verification Page. Retrieved April 23, 2025.
  source_name: AhnLab LummaC2 2025
  url: https://asec.ahnlab.com/en/85699/
- description: 'Alex Capraro. (2024, December 17). Using CAPTCHA for Compromise: Hackers Flip the Script. Retrieved March
    18, 2025.'
  source_name: Reliaquest CAPTCHA 2024
  url: https://www.reliaquest.com/blog/using-captcha-for-compromise/
- description: 'Amaury G., Coline Chavane, Felix Aimé and Sekoia TDR. (2025, March 31). From Contagious to ClickFake Interview:
    Lazarus leveraging the ClickFix tactic. Retrieved April 1, 2025.'
  source_name: Sekoia ClickFake 2025
  url: https://blog.sekoia.io/clickfake-interview-campaign-by-lazarus/
- description: 'CloudSEK TRIAD. (2024, September 19). Unmasking the Danger: Lumma Stealer Malware Exploits Fake CAPTCHA Pages.
    Retrieved March 18, 2025.'
  source_name: CloudSEK Lumma Stealer 2024
  url: https://www.cloudsek.com/blog/unmasking-the-danger-lumma-stealer-malware-exploits-fake-captcha-pages
- description: 'Tommy Madjar, Selena Larson and The Proofpoint Threat Research Team. (2024, November 18). Security Brief:
    ClickFix Social Engineering Technique Floods Threat Landscape. Retrieved March 18, 2025.'
  source_name: Proofpoint ClickFix 2024
  url: https://www.proofpoint.com/us/blog/threat-insight/security-brief-clickfix-social-engineering-technique-floods-threat-landscape
id: attack-pattern--e261a979-f354-41a8-963e-6cadac27c4bf
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2026-03-27T20:05:57.921Z'
name: Malicious Copy and Paste
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Ale Houspanossian
- Fernando Bacchin
- Gabriel Currie
- Harikrishnan Muthu, Cyble
- Menachem Goldstein
- ReliaQuest
- SeungYoul Yoo, AhnLab
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_remote_support: false
x_mitre_version: '1.1'
```
