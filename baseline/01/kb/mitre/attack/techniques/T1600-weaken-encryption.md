---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1600
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/network_devices
mitre-attack: kb/mitre/attack/techniques/T1600-weaken-encryption
tactic:
    - Defense Impairment
platforms:
    - Network Devices
permissions required:
    - none
---

## Description

Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications.[^1] <br><br>Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.<br><br>Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as [[kb/mitre/attack/techniques/T1601-modify-system-image|Modify System Image]], [[kb/mitre/attack/techniques/T1600.001-reduce-key-space|Reduce Key Space]], and [[kb/mitre/attack/techniques/T1600.002-disable-crypto-hardware|Disable Crypto Hardware]], an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts.[^2] 

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1600.001-reduce-key-space\|T1600.001]] | Reduce Key Space |
| [[kb/mitre/attack/techniques/T1600.002-disable-crypto-hardware\|T1600.002]] | Disable Crypto Hardware |

 [^1]: [Cisco Synful Knock Evolution](https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices)
 [^2]: [Cisco Blog Legacy Device Attacks](https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954)
