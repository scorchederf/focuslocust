---
parsed_by: focuslocust
source: mitre
type: generated
---
# Space after Filename

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1036.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Space after Filename](../../attack/techniques/T1036.006-space-after-filename.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1036.006 |
| name | Space after Filename |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1036/006 |

## Preserved Source Material

```yaml
created: '2020-02-10T20:47:10.082Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries can hide a program''s true filetype by changing the extension of a file. With certain file types
  (specifically this does not work with .app extensions), appending a space to the end of a filename will change how the file
  is processed by the operating system.


  For example, if there is a Mach-O executable file called <code>evil.bin</code>, when it is double clicked by a user, it
  will launch Terminal.app and execute. If this file is renamed to <code>evil.txt</code>, then when double clicked by a user,
  it will launch with the default text editing application (not executing the binary). However, if the file is renamed to
  <code>evil.txt </code> (note the space at the end), then when double clicked by a user, the true file type is determined
  by the OS and handled appropriately and the binary will be executed (Citation: Mac Backdoors are back).


  Adversaries can use this feature to trick users into double clicking benign-looking files of any format and ultimately executing
  something malicious.'
external_references:
- external_id: T1036.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1036/006
- description: Dan Goodin. (2016, July 6). After hiatus, in-the-wild Mac backdoors are suddenly back. Retrieved July 8, 2017.
  source_name: Mac Backdoors are back
  url: https://arstechnica.com/security/2016/07/after-hiatus-in-the-wild-mac-backdoors-are-suddenly-back/
id: attack-pattern--e51137a5-1cdc-499e-911a-abaedaa5ac86
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:41:09.462Z'
name: Space after Filename
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Erye Hernandez, Palo Alto Networks
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
x_mitre_version: '2.0'
```
