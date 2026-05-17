---
parsed_by: focuslocust
source: mitre
type: generated
---
# Python Startup Hooks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546.018` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Python Startup Hooks](../../attack/techniques/T1546.018-python-startup-hooks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1546.018 |
| name | Python Startup Hooks |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1546/018 |

## Preserved Source Material

```yaml
created: '2025-05-22T19:20:46.740Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may achieve persistence by leveraging Python’s startup mechanisms, including path configuration
  (`.pth`) files and the `sitecustomize.py` or `usercustomize.py` modules. These files are automatically processed during
  the initialization of the Python interpreter, allowing for the execution of arbitrary code whenever Python is invoked.(Citation:
  Volexity GlobalProtect CVE 2024)


  Path configuration files are designed to extend Python’s module search paths through the use of import statements. If a
  `.pth` file is placed in Python''s `site-packages` or `dist-packages` directories, any lines beginning with `import` will
  be executed automatically on Python invocation.(Citation: DFIR Python Persistence 2025) Similarly, if `sitecustomize.py`
  or `usercustomize.py` is present in the Python path, these files will be imported during interpreter startup, and any code
  they contain will be executed.(Citation: Python Site Configuration Hook)


  Adversaries may abuse these mechanisms to establish persistence on systems where Python is widely used (e.g., for automation
  or scripting in production environments).  '
external_references:
- external_id: T1546.018
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1546/018
- description: Python. (n.d.). site — Site-specific configuration hook. Retrieved May 22, 2025.
  source_name: Python Site Configuration Hook
  url: https://docs.python.org/3/library/site.html
- description: Stephan Berger. (2025, January 14). Analysis of Python's .pth files as a persistence mechanism. Retrieved May
    22, 2025.
  source_name: DFIR Python Persistence 2025
  url: https://dfir.ch/posts/publish_python_pth_extension/
- description: Volexity Threat Research. (2024, April 12). Zero-Day Exploitation of Unauthenticated Remote Code Execution
    Vulnerability in GlobalProtect (CVE-2024-3400). Retrieved May 22, 2025.
  source_name: Volexity GlobalProtect CVE 2024
  url: https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/
id: attack-pattern--c5087385-9b7c-4488-9923-d9e370bf08df
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-21T02:35:20.850Z'
name: Python Startup Hooks
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Ruben Groenewoud (@RFGroenewoud)
- Pyae Heinn Kyaw, CSIRT @ Salesforce
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.0'
```
