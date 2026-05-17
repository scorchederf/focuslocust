---
parsed_by: focuslocust
source: mitre
type: generated
---
# Resource Forking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.009` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Resource Forking](../../attack/techniques/T1564.009-resource-forking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.009 |
| name | Resource Forking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/009 |

## Preserved Source Material

```yaml
created: '2021-10-12T20:02:31.866Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse resource forks to hide malicious code or executables to evade detection and bypass security
  applications. A resource fork provides applications a structured way to store resources such as thumbnail images, menu definitions,
  icons, dialog boxes, and code.(Citation: macOS Hierarchical File System Overview) Usage of a resource fork is identifiable
  when displaying a file’s extended attributes, using <code>ls -l@</code> or <code>xattr -l</code> commands. Resource forks
  have been deprecated and replaced with the application bundle structure. Non-localized resources are placed at the top level
  directory of an application bundle, while localized resources are placed in the <code>/Resources</code> folder.(Citation:
  Resource and Data Forks)(Citation: ELC Extended Attributes)


  Adversaries can use resource forks to hide malicious data that may otherwise be stored directly in files. Adversaries can
  execute content with an attached resource fork, at a specified offset, that is moved to an executable location then invoked.
  Resource fork content may also be obfuscated/encrypted until execution.(Citation: sentinellabs resource named fork 2020)(Citation:
  tau bundlore erika noerenberg 2020)'
external_references:
- external_id: T1564.009
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/009
- description: 'Erika Noerenberg. (2020, June 29). TAU Threat Analysis: Bundlore (macOS) mm-install-macos. Retrieved October
    12, 2021.'
  source_name: tau bundlore erika noerenberg 2020
  url: https://blogs.vmware.com/security/2020/06/tau-threat-analysis-bundlore-macos-mm-install-macos.html
- description: Flylib. (n.d.). Identifying Resource and Data Forks. Retrieved October 12, 2021.
  source_name: Resource and Data Forks
  url: https://flylib.com/books/en/4.395.1.192/1/
- description: 'Howard Oakley. (2020, October 24). There''s more to files than data: Extended Attributes. Retrieved October
    12, 2021.'
  source_name: ELC Extended Attributes
  url: https://eclecticlight.co/2020/10/24/theres-more-to-files-than-data-extended-attributes/
- description: Phil Stokes. (2020, November 5). Resourceful macOS Malware Hides in Named Fork. Retrieved October 12, 2021.
  source_name: sentinellabs resource named fork 2020
  url: https://www.sentinelone.com/labs/resourceful-macos-malware-hides-in-named-fork/
- description: Tenon. (n.d.). Retrieved October 12, 2021.
  source_name: macOS Hierarchical File System Overview
  url: http://tenon.com/products/codebuilder/User_Guide/6_File_Systems.html#anchor520553
id: attack-pattern--b22e5153-ac28-4cc6-865c-2054e36285cb
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:25:32.891Z'
name: Resource Forking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Ivan Sinyakov
- Jaron Bradley @jbradley89
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '2.0'
```
