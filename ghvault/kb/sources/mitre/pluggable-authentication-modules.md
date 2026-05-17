---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pluggable Authentication Modules

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pluggable Authentication Modules](../../attack/techniques/T1556.003-pluggable-authentication-modules.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1556.003 |
| name | Pluggable Authentication Modules |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1556/003 |

## Preserved Source Material

```yaml
created: '2020-06-26T04:01:09.648Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify pluggable authentication modules (PAM) to access user credentials or enable otherwise
  unwarranted access to accounts. PAM is a modular system of configuration files, libraries, and executable files which guide
  authentication for many services. The most common authentication module is <code>pam_unix.so</code>, which retrieves, sets,
  and verifies account authentication information in <code>/etc/passwd</code> and <code>/etc/shadow</code>.(Citation: Apple
  PAM)(Citation: Man Pam_Unix)(Citation: Red Hat PAM)


  Adversaries may modify components of the PAM system to create backdoors. PAM components, such as <code>pam_unix.so</code>,
  can be patched to accept arbitrary adversary supplied values as legitimate credentials.(Citation: PAM Backdoor)


  Malicious modifications to the PAM system may also be abused to steal credentials. Adversaries may infect PAM resources
  with code to harvest user credentials, since the values exchanged with PAM components may be plain-text since PAM does not
  store passwords.(Citation: PAM Creds)(Citation: Apple PAM)'
external_references:
- external_id: T1556.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1556/003
- description: Apple. (2011, May 11). PAM - Pluggable Authentication Modules. Retrieved June 25, 2020.
  source_name: Apple PAM
  url: https://opensource.apple.com/source/dovecot/dovecot-239/dovecot/doc/wiki/PasswordDatabase.PAM.txt
- description: die.net. (n.d.). pam_unix(8) - Linux man page. Retrieved June 25, 2020.
  source_name: Man Pam_Unix
  url: https://linux.die.net/man/8/pam_unix
- description: Fernández, J. M. (2018, June 27). Exfiltrating credentials via PAM backdoors & DNS requests. Retrieved November
    17, 2024.
  source_name: PAM Creds
  url: https://web.archive.org/web/20240303094335/https://x-c3ll.github.io/posts/PAM-backdoor-DNS/
- description: Red Hat. (n.d.). CHAPTER 2. USING PLUGGABLE AUTHENTICATION MODULES (PAM). Retrieved June 25, 2020.
  source_name: Red Hat PAM
  url: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/managing_smart_cards/pluggable_authentication_modules
- description: zephrax. (2018, August 3). linux-pam-backdoor. Retrieved June 25, 2020.
  source_name: PAM Backdoor
  url: https://github.com/zephrax/linux-pam-backdoor
id: attack-pattern--06c00069-771a-4d57-8ef5-d3718c1a8771
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2026-04-16T20:07:53.037Z'
name: Pluggable Authentication Modules
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- George Allen, VMware Carbon Black
- Scott Knight, @sdotknight, VMware Carbon Black
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
x_mitre_version: '3.0'
```
