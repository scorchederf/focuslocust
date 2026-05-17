---
parsed_by: focuslocust
source: mitre
type: generated
---
# Invoke-PSImage

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0231` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Invoke-PSImage](../../tools/unknown/invoke-psimage.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | S0231 |
| name | Invoke-PSImage |
| type | tool |
| source | mitre |
| url | https://attack.mitre.org/software/S0231 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Invoke-PSImage](https://attack.mitre.org/software/S0231) takes a PowerShell script and embeds the bytes of
  the script into the pixels of a PNG image. It generates a one liner for executing either from a file of from the web. Example
  of usage is embedding the PowerShell code from the Invoke-Mimikatz module and embed it into an image file. By calling the
  image file from a macro for example, the macro will download the picture and execute the PowerShell code, which in this
  case will dump the passwords. (Citation: GitHub Invoke-PSImage)'
external_references:
- external_id: S0231
  source_name: mitre-attack
  url: https://attack.mitre.org/software/S0231
- description: Adams, B. (2017, December 17). Invoke-PSImage. Retrieved April 10, 2018.
  source_name: GitHub Invoke-PSImage
  url: https://github.com/peewpw/Invoke-PSImage
id: tool--b52d6583-14a2-4ddc-8527-87fd2142558f
modified: '2025-04-16T20:38:55.222Z'
name: Invoke-PSImage
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: tool
x_mitre_aliases:
- Invoke-PSImage
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
