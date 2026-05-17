---
parsed_by: focuslocust
source: mitre
type: generated
---
# M1028 - Operating System Configuration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `mitigation` |
| Record ID | `M1028` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: 

Disable Unused Features:

- Turn off SMBv1, LLMNR, and NetBIOS where not needed.
- Disable remote registry and unnecessary services.

Enforce OS-level Protections:

- Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows.
- Use AppArmor or SELinux on Linux for mandatory access controls.

Secure Access Settings:

- Enable User Account Control (UAC) for Windows.
- Restrict root/sudo access on Linux/macOS and enforce strong permissions using sudoers files.

File System Hardening:

- Implement least-privilege access for critical files and system directories.
- Audit permissions regularly using tools like icacls (Windows) or getfacl/chmod (Linux/macOS).

Secure Remote Access:

- Restrict RDP, SSH, and VNC to authorized IPs using firewall rules.
- Enable NLA for RDP and enforce strong password/lockout policies.

Harden Boot Configurations:

- Enable Secure Boot and enforce UEFI/BIOS password protection.
- Use BitLocker or LUKS to encrypt boot drives.

Regular Audits:

- Periodically audit OS configurations using tools like CIS Benchmarks or SCAP tools.

*Tools for Implementation*

Windows:

- Microsoft Group Policy Objects (GPO): Centrally enforce OS security settings.
- Windows Defender Exploit Guard: Built-in OS protection against exploits.
- CIS-CAT Pro: Audit Windows security configurations based on CIS Benchmarks.

Linux/macOS:

- AppArmor/SELinux: Enforce mandatory access controls.
- Lynis: Perform comprehensive security audits.
- SCAP Security Guide: Automate configuration hardening using Security Content Automation Protocol.

Cross-Platform:

- Ansible or Chef/Puppet: Automate configuration hardening at scale.
- OpenSCAP: Perform compliance and configuration checks.

## Source Verification

[source record](../../sources/mitre/operating-system-configuration.md)

## Evidence Excerpt

```text
created: '2019-06-06T21:16:18.709Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Operating System Configuration involves adjusting system settings and hardening the default configurations of\
\ an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations\
\ address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques.\
\ This mitigation can be implemented through the following measures: \n\nDisable Unused Features:\n\n- Turn off SMBv1, LLMNR,\
\ and NetBIOS where not needed.\n- Disable remote registry and unnecessary services.\n\nEnforce OS-level Protections:\n\n\
- Enable Data Execution Prevention (DEP), Address Space Layout Randomization (ASLR), and Control Flow Guard (CFG) on Windows.\n\
```
