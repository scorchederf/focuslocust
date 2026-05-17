---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1669 - Wi-Fi Networks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1669` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may gain initial access to target systems by connecting to wireless networks. They may accomplish this by exploiting open Wi-Fi networks used by target devices or by accessing secured Wi-Fi networks — requiring Valid Accounts — belonging to a target organization. Establishing a connection to a Wi-Fi access point requires a certain level of proximity to both discover and maintain a stable network connection. 

Adversaries may establish a wireless connection through various methods, such as by physically positioning themselves near a Wi-Fi network to conduct close access operations. To bypass the need for physical proximity, adversaries may attempt to remotely compromise nearby third-party systems that have both wired and wireless network connections available (i.e., dual-homed systems). These third-party compromised devices can then serve as a bridge to connect to a target’s Wi-Fi network.

Once an initial wireless connection is achieved, adversaries may leverage this access for follow-on activities in the victim network or further targeting of specific devices on the network. Adversaries may perform Network Sniffing or Adversary-in-the-Middle activities for Credential Access or Discovery.

## Source Verification

[source record](../../sources/mitre/wi-fi-networks.md)

## Evidence Excerpt

```text
created: '2025-02-25T15:49:33.963Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may gain initial access to target systems by connecting to wireless networks. They may accomplish\
\ this by exploiting open Wi-Fi networks used by target devices or by accessing secured Wi-Fi networks — requiring [Valid\
\ Accounts](https://attack.mitre.org/techniques/T1078) — belonging to a target organization.(Citation: DOJ GRU Charges 2018)(Citation:\
\ Nearest Neighbor Volexity) Establishing a connection to a Wi-Fi access point requires a certain level of proximity to\
\ both discover and maintain a stable network connection. \n\nAdversaries may establish a wireless connection through various\
\ methods, such as by physically positioning themselves near a Wi-Fi network to conduct close access operations. To bypass\
```
