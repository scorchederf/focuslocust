---
parsed_by: focuslocust
source: mitre
type: generated
---
# Environmental Keying

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1480.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Environmental Keying](../../attack/techniques/T1480.001-environmental-keying.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1480.001 |
| name | Environmental Keying |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1480/001 |

## Preserved Source Material

```yaml
created: '2020-06-23T22:28:28.041Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may environmentally key payloads or other features of malware to evade defenses and constraint execution
  to a specific target environment. Environmental keying uses cryptography to constrain execution or actions based on adversary
  supplied environment specific conditions that are expected to be present on the target. Environmental keying is an implementation
  of [Execution Guardrails](https://attack.mitre.org/techniques/T1480) that utilizes cryptographic techniques for deriving
  encryption/decryption keys from specific types of values in a given computing environment.(Citation: EK Clueless Agents)


  Values can be derived from target-specific elements and used to generate a decryption key for an encrypted payload. Target-specific
  values can be derived from specific network shares, physical devices, software/software versions, files, joined AD domains,
  system time, and local/external IP addresses.(Citation: Kaspersky Gauss Whitepaper)(Citation: Proofpoint Router Malvertising)(Citation:
  EK Impeding Malware Analysis)(Citation: Environmental Keyed HTA) By generating the decryption keys from target-specific
  environmental values, environmental keying can make sandbox detection, anti-virus detection, crowdsourcing of information,
  and reverse engineering difficult.(Citation: Kaspersky Gauss Whitepaper) These difficulties can slow down the incident response
  process and help adversaries hide their tactics, techniques, and procedures (TTPs).


  Similar to [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027), adversaries may use environmental
  keying to help protect their TTPs and evade detection. Environmental keying may be used to deliver an encrypted payload
  to the target that will use target-specific values to decrypt the payload before execution.(Citation: Kaspersky Gauss Whitepaper)(Citation:
  EK Impeding Malware Analysis)(Citation: Environmental Keyed HTA)(Citation: Demiguise Guardrail Router Logo) By utilizing
  target-specific values to decrypt the payload the adversary can avoid packaging the decryption key with the payload or sending
  it over a potentially monitored network connection. Depending on the technique for gathering target-specific values, reverse
  engineering of the encrypted payload can be exceptionally difficult.(Citation: Kaspersky Gauss Whitepaper) This can be used
  to prevent exposure of capabilities in environments that are not intended to be compromised or operated within.


  Like other [Execution Guardrails](https://attack.mitre.org/techniques/T1480), environmental keying can be used to prevent
  exposure of capabilities in environments that are not intended to be compromised or operated within. This activity is distinct
  from typical [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497). While use of [Virtualization/Sandbox
  Evasion](https://attack.mitre.org/techniques/T1497) may involve checking for known sandbox values and continuing with execution
  only if there is no match, the use of environmental keying will involve checking for an expected target-specific value that
  must match for decryption and subsequent execution to be successful.'
external_references:
- external_id: T1480.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1480/001
- description: Kafeine. (2016, December 13). Home Routers Under Attack via Malvertising on Windows, Android Devices. Retrieved
    January 16, 2019.
  source_name: Proofpoint Router Malvertising
  url: https://www.proofpoint.com/us/threat-insight/post/home-routers-under-attack-malvertising-windows-android-devices
- description: 'Kaspersky Lab. (2012, August). Gauss: Abnormal Distribution. Retrieved January 17, 2019.'
  source_name: Kaspersky Gauss Whitepaper
  url: https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20134940/kaspersky-lab-gauss.pdf
- description: Riordan, J., Schneier, B. (1998, June 18). Environmental Key Generation towards Clueless Agents. Retrieved
    January 18, 2019.
  source_name: EK Clueless Agents
  url: https://www.schneier.com/academic/paperfiles/paper-clueless-agents.pdf
- description: Song, C., et al. (2012, August 7). Impeding Automated Malware Analysis with Environment-sensitive Malware.
    Retrieved January 18, 2019.
  source_name: EK Impeding Malware Analysis
  url: https://pdfs.semanticscholar.org/2721/3d206bc3c1e8c229fb4820b6af09e7f975da.pdf
- description: 'Warren, R. (2017, August 2). Demiguise: virginkey.js. Retrieved January 17, 2019.'
  source_name: Demiguise Guardrail Router Logo
  url: https://github.com/nccgroup/demiguise/blob/master/examples/virginkey.js
- description: Warren, R. (2017, August 8). Smuggling HTA files in Internet Explorer/Edge. Retrieved November 17, 2024.
  source_name: Environmental Keyed HTA
  url: http://web.archive.org/web/20200608093807/https://www.nccgroup.com/uk/about-us/newsroom-and-events/blogs/2017/august/smuggling-hta-files-in-internet-exploreredge/
id: attack-pattern--f244b8dd-af6c-4391-a497-fc03627ce995
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:07:10.470Z'
name: Environmental Keying
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Nick Carr, Mandiant
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
- macOS
x_mitre_version: '2.0'
```
