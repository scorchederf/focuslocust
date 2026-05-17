---
parsed_by: focuslocust
source: mitre
type: generated
---
# Driver Load

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0079` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Driver Load](../../attack/data-sources/DC0079-driver-load.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | DC0079 |
| name | Driver Load |
| type | data-source |
| source | mitre |
| url | https://attack.mitre.org/datacomponents/DC0079 |

## Preserved Source Material

```yaml
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The process of attaching a driver, which is a software component that allows the operating system and applications\
  \ to interact with hardware devices, to either user-mode or kernel-mode of a system. This can include benign actions (e.g.,\
  \ hardware drivers) or malicious behavior (e.g., rootkits or unsigned drivers). Examples: \n\n- Legitimate Driver Loading:\
  \ A new graphics driver from a vendor like NVIDIA or AMD is loaded into the system.\n- Unsigned Driver Loading: A driver\
  \ without a valid digital signature is loaded into the kernel.\n- Rootkit Installation: A malicious rootkit driver is loaded\
  \ to manipulate kernel-mode processes.\n- Anti-Virus or EDR Driver Loading: An Endpoint Detection and Response (EDR) solution\
  \ loads its driver to monitor system activities.\n- Driver Misuse: A legitimate driver is loaded and exploited to execute\
  \ malicious actions, such as using vulnerable drivers for bypassing defenses (e.g., Bring Your Own Vulnerable Driver (BYOVD)\
  \ attacks)."
external_references:
- external_id: DC0079
  source_name: mitre-attack
  url: https://attack.mitre.org/datacomponents/DC0079
id: x-mitre-data-component--3551476e-14f5-4e48-a518-e82135329e03
modified: '2025-11-12T22:03:39.105Z'
name: Driver Load
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: x-mitre-data-component
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_log_sources:
- channel: EventCode=6
  name: WinEventLog:Sysmon
- channel: dmesg or syslog for module loads
  name: linux:syslog
- channel: Driver load events or firmware load failures for hardware devices
  name: linux:syslog
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '2.0'
```
