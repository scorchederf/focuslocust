---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1586 - Compromise Accounts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1586` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may compromise accounts with services that can be used during targeting. For operations incorporating social engineering, the utilization of an online persona may be important. Rather than creating and cultivating accounts (i.e. Establish Accounts), adversaries may compromise existing accounts. Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge of, the compromised persona. 

A variety of methods exist for compromising accounts, such as gathering credentials via Phishing for Information, purchasing credentials from third-party sites, brute forcing credentials (ex: password reuse from breach credential dumps), or paying employees, suppliers or business partners for access to credentials. Prior to compromising accounts, adversaries may conduct Reconnaissance to inform decisions about which accounts to compromise to further their operation.

Personas may exist on a single site or across multiple sites (ex: Facebook, LinkedIn, Twitter, Google, etc.). Compromised accounts may require additional development, this could include filling out or modifying profile information, further developing social networks, or incorporating photos.

Adversaries may directly leverage compromised email accounts for Phishing for Information or Phishing.

## Source Verification

[source record](../../sources/mitre/compromise-accounts.md)

## Evidence Excerpt

```text
created: '2020-10-01T01:17:15.965Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may compromise accounts with services that can be used during targeting. For operations incorporating\
\ social engineering, the utilization of an online persona may be important. Rather than creating and cultivating accounts\
\ (i.e. [Establish Accounts](https://attack.mitre.org/techniques/T1585)), adversaries may compromise existing accounts.\
\ Utilizing an existing persona may engender a level of trust in a potential victim if they have a relationship, or knowledge\
\ of, the compromised persona. \n\nA variety of methods exist for compromising accounts, such as gathering credentials via\
\ [Phishing for Information](https://attack.mitre.org/techniques/T1598), purchasing credentials from third-party sites,\
```
