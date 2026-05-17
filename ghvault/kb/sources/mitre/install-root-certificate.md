---
parsed_by: focuslocust
source: mitre
type: generated
---
# Install Root Certificate

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1553.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Install Root Certificate](../../attack/techniques/T1553.004-install-root-certificate.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1553.004 |
| name | Install Root Certificate |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1553/004 |

## Preserved Source Material

```yaml
created: '2020-02-21T21:05:32.844Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary
  controlled web servers. Root certificates are used in public key cryptography to identify a root certificate authority (CA).
  When a root certificate is installed, the system or application will trust certificates in the root''s chain of trust that
  have been signed by the root certificate.(Citation: Wikipedia Root Certificate) Certificates are commonly used for establishing
  secure TLS/SSL communications within a web browser. When a user attempts to browse a website that presents a certificate
  that is not trusted an error message will be displayed to warn the user of the security risk. Depending on the security
  settings, the browser may not allow the user to establish a connection to the website.


  Installation of a root certificate on a compromised system would give an adversary a way to degrade the security of that
  system. Adversaries have used this technique to avoid security warnings prompting users when compromised systems connect
  over HTTPS to adversary controlled web servers that spoof legitimate websites in order to collect login credentials.(Citation:
  Operation Emmental)


  Atypical root certificates have also been pre-installed on systems by the manufacturer or in the software supply chain and
  were used in conjunction with malware/adware to provide [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557)
  capability for intercepting information transmitted over secure TLS/SSL communications.(Citation: Kaspersky Superfish)


  Root certificates (and their associated chains) can also be cloned and reinstalled. Cloned certificate chains will carry
  many of the same metadata characteristics of the source and can be used to sign malicious code that may then bypass signature
  validation tools (ex: Sysinternals, antivirus, etc.) used to block execution and/or uncover artifacts of Persistence.(Citation:
  SpectorOps Code Signing Dec 2017)


  In macOS, the Ay MaMi malware uses <code>/usr/bin/security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain
  /path/to/malicious/cert</code> to install a malicious certificate as a trusted root certificate into the system keychain.(Citation:
  objective-see ay mami 2018)'
external_references:
- external_id: T1553.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1553/004
- description: 'botconf eu. (2014, December 31). David Sancho - Finding Holes in Banking 2FA: Operation Emmental. Retrieved
    January 4, 2024.'
  source_name: Operation Emmental
  url: https://www.youtube.com/watch?v=gchKFumYHWc
- description: Graeber, M. (2017, December 22). Code Signing Certificate Cloning Attacks and Defenses. Retrieved April 3,
    2018.
  source_name: SpectorOps Code Signing Dec 2017
  url: https://posts.specterops.io/code-signing-certificate-cloning-attacks-and-defenses-6f98657fc6ec
- description: 'Onuma. (2015, February 24). Superfish: Adware Preinstalled on Lenovo Laptops. Retrieved February 20, 2017.'
  source_name: Kaspersky Superfish
  url: https://www.kaspersky.com/blog/lenovo-pc-with-adware-superfish-preinstalled/7712/
- description: Patrick Wardle. (2018, January 11). Ay MaMi. Retrieved March 19, 2018.
  source_name: objective-see ay mami 2018
  url: https://objective-see.com/blog/blog_0x26.html
- description: Wikipedia. (2016, December 6). Root certificate. Retrieved February 20, 2017.
  source_name: Wikipedia Root Certificate
  url: https://en.wikipedia.org/wiki/Root_certificate
id: attack-pattern--c615231b-f253-4f58-9d47-d5b4cbdb6839
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:52.931Z'
name: Install Root Certificate
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Itzik Kotler, SafeBreach
- Matt Graeber, @mattifestation, SpecterOps
- Red Canary
- Travis Smith, Tripwire
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
