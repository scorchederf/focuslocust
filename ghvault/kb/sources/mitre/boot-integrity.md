---
parsed_by: focuslocust
source: mitre
type: generated
---
# Boot Integrity

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1046` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Boot Integrity](../../attack/mitigations/M1046-boot-integrity.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | M1046 |
| name | Boot Integrity |
| type | mitigation |
| source | mitre |
| url | https://attack.mitre.org/mitigations/M1046 |

## Preserved Source Material

```yaml
created: '2019-06-11T17:02:36.984Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Boot Integrity ensures that a system starts securely by verifying the integrity of its boot process, operating
  system, and associated components. This mitigation focuses on leveraging secure boot mechanisms, hardware-rooted trust,
  and runtime integrity checks to prevent tampering during the boot sequence. It is designed to thwart adversaries attempting
  to modify system firmware, bootloaders, or critical OS components. This mitigation can be implemented through the following
  measures:


  Implementation of Secure Boot:


  - Implementation: Enable UEFI Secure Boot on all systems and configure it to allow only signed bootloaders and operating
  systems.

  - Use Case: An adversary attempts to replace the system’s bootloader with a malicious version to gain persistence. Secure
  Boot prevents the untrusted bootloader from executing, halting the attack.


  Utilization of TPMs:


  - Implementation: Configure systems to use TPM-based attestation for boot integrity, ensuring that any modification to the
  firmware, bootloader, or OS is detected.

  - Use Case: A compromised firmware component alters the boot sequence. The TPM detects the change and triggers an alert,
  allowing the organization to respond before further damage.


  Enable Bootloader Passwords:


  - Implementation: Protect BIOS/UEFI settings with a strong password and limit physical access to devices.

  - Use Case: An attacker with physical access attempts to disable Secure Boot or modify the boot sequence. The password prevents
  unauthorized changes.


  Runtime Integrity Monitoring:


  - Implementation: Deploy solutions to verify the integrity of critical files and processes after boot.

  - Use Case: A malware infection modifies kernel modules post-boot. Runtime integrity monitoring detects the modification
  and prevents the malicious module from loading.'
external_references:
- external_id: M1046
  source_name: mitre-attack
  url: https://attack.mitre.org/mitigations/M1046
id: course-of-action--7da0387c-ba92-4553-b291-b636ee42b2eb
modified: '2024-12-10T18:48:36.517Z'
name: Boot Integrity
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: course-of-action
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_version: '1.1'
```
