---
parsed_by: focuslocust
source: mitre
type: generated
---
# Lua

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059.011` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lua](../../attack/techniques/T1059.011-lua.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059.011 |
| name | Lua |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059/011 |

## Preserved Source Material

```yaml
created: '2024-08-05T18:19:42.201Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse Lua commands and scripts for execution. Lua is a cross-platform scripting and programming
  language primarily designed for embedded use in applications. Lua can be executed on the command-line (through the stand-alone
  lua interpreter), via scripts (<code>.lua</code>), or from Lua-embedded programs (through the <code>struct lua_State</code>).(Citation:
  Lua main page)(Citation: Lua state)


  Lua scripts may be executed by adversaries for malicious purposes. Adversaries may incorporate, abuse, or replace existing
  Lua interpreters to allow for malicious Lua command execution at runtime.(Citation: PoetRat Lua)(Citation: Lua Proofpoint
  Sunseed)(Citation: Cyphort EvilBunny)(Citation: Kaspersky Lua)'
external_references:
- external_id: T1059.011
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059/011
- description: Global Research and Analysis Team. (2016, August 9). The ProjectSauron APT. Retrieved August 5, 2024.
  source_name: Kaspersky Lua
  url: https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07190154/The-ProjectSauron-APT_research_KL.pdf
- description: Lua. (2024, June 25). Getting started. Retrieved August 5, 2024.
  source_name: Lua main page
  url: https://www.lua.org/start.html
- description: Lua. (n.d.). lua_State. Retrieved August 5, 2024.
  source_name: Lua state
  url: https://pgl.yoyo.org/luai/i/lua_State
- description: 'Marschalek, Marion. (2014, December 16). EvilBunny: Malware Instrumented By Lua. Retrieved August 5, 2024.'
  source_name: Cyphort EvilBunny
  url: https://web.archive.org/web/20150311013500/http:/www.cyphort.com/evilbunny-malware-instrumented-lua/
- description: 'Mercer, Warren. (2020, October 6). PoetRAT: Malware targeting public and private sector in Azerbaijan evolves.
    Retrieved August 5, 2024.'
  source_name: PoetRat Lua
  url: https://blog.talosintelligence.com/poetrat-update/
- description: 'Raggi, Michael. Cass, Zydeca. The Proofpoint Threat Research Team.. (2022, March 1). Asylum Ambuscade: State
    Actor Uses Lua-based Sunseed Malware to Target European Governments and Refugee Movement. Retrieved August 5, 2024.'
  source_name: Lua Proofpoint Sunseed
  url: https://www.proofpoint.com/us/blog/threat-insight/asylum-ambuscade-state-actor-uses-compromised-private-ukrainian-military-emails
id: attack-pattern--afddee82-3385-4682-ad90-eeced33f2d07
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-04-15T19:58:57.854Z'
name: Lua
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
- Linux
- Network Devices
- Windows
- macOS
x_mitre_remote_support: false
x_mitre_version: '1.1'
```
