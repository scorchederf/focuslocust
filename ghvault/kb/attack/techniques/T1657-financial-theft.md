---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1657 - Financial Theft

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1657` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft, or other methods aimed at their own financial gain at the expense of the availability of these resources for victims. Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware, business email compromise (BEC) and fraud, "pig butchering," bank hacking, and exploiting cryptocurrency networks. 

Adversaries may Compromise Accounts to conduct unauthorized transfers of funds. In the case of business email compromise or email fraud, an adversary may utilize Impersonation of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial accounts controlled by an adversary. This creates the potential for multiple victims (i.e., compromised accounts as well as the ultimate monetary loss) in incidents involving financial theft.

Extortion by ransomware may occur, for example, when an adversary demands payment from a victim after Data Encrypted for Impact  and Exfiltration of data, followed by threatening to leak sensitive data to the public unless payment is made to the adversary. Adversaries may use dedicated leak sites to distribute victim data.

Due to the potentially immense business impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert attention from their true goals such as Data Destruction and business disruption.

## Source Verification

[source record](../../sources/mitre/financial-theft.md)

## Evidence Excerpt

```text
created: '2023-08-18T20:50:04.222Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft,\
\ or other methods aimed at their own financial gain at the expense of the availability of these resources for victims.\
\ Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,(Citation:\
\ FBI-ransomware) business email compromise (BEC) and fraud,(Citation: FBI-BEC) \"pig butchering,\"(Citation: wired-pig\
\ butchering) bank hacking,(Citation: DOJ-DPRK Heist) and exploiting cryptocurrency networks.(Citation: BBC-Ronin) \n\n\
Adversaries may [Compromise Accounts](https://attack.mitre.org/techniques/T1586) to conduct unauthorized transfers of funds.(Citation:\
```
