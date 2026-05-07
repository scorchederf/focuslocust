---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1207
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1207-rogue-domain-controller
tactic:
    - Defense Impairment
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC. [^1]  Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain object, including credentials and keys.<br><br>Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema, which requires Administrator privileges (either Domain or local to the DC) or the KRBTGT hash. [^2] <br><br>This technique may bypass system logging and security monitors such as security information and event management (SIEM) products (since actions taken on a rogue DC may not be reported to these sensors). [^1]  The technique may also be used to alter and delete replication and other associated metadata to obstruct forensic analysis. Adversaries may also utilize this technique to perform [[kb/mitre/attack/techniques/T1134.005-sid-history-injection|SID-History Injection]] and/or manipulate AD objects (such as accounts, access control lists, schemas) to establish backdoors for Persistence. [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0002-mimikatz\|S0002]] | Mimikatz | [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]]’s `LSADUMP::DCShadow` module can be used to make AD updates by temporarily setting a computer to be a DC.[^1] [^2]  |

 [^1]: [DCShadow Blog](https://www.dcshadow.com/)
 [^2]: [Adsecurity Mimikatz Guide](https://adsecurity.org/?page_id=1821)
 [^3]: [Deply Mimikatz](https://github.com/gentilkiwi/mimikatz)
