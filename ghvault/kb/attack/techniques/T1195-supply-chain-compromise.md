---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1195 - Supply Chain Compromise

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1195` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.

Supply chain compromise can take place at any stage of the supply chain including:

* Manipulation of development tools
* Manipulation of a development environment
* Manipulation of source code repositories (public or private)
* Manipulation of source code in open-source dependencies
* Manipulation of software update/distribution mechanisms
* Compromised/infected system images (removable media infected at the factory) 
* Replacement of legitimate software with modified versions
* Sales of modified/counterfeit products to legitimate distributors
* Shipment interdiction

While supply chain compromise can impact any component of hardware or software, adversaries looking to gain execution have often focused on malicious additions to legitimate software in software distribution or update channels. Adversaries may limit targeting to a desired victim set or distribute malicious software to a broad set of consumers but only follow up with specific victims. Popular open-source projects that are used as dependencies in many applications may also be targeted as a means to add malicious code to users of the dependency.

In some cases, adversaries may conduct “second-order” supply chain compromises by leveraging the access gained from an initial supply chain compromise to further compromise a software component. This may allow the threat actor to spread to even more victims.

## Source Verification

[source record](../../sources/mitre/supply-chain-compromise.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may manipulate products or product delivery mechanisms prior to receipt by a final consumer for\
\ the purpose of data or system compromise.\n\nSupply chain compromise can take place at any stage of the supply chain including:\n\
\n* Manipulation of development tools\n* Manipulation of a development environment\n* Manipulation of source code repositories\
\ (public or private)\n* Manipulation of source code in open-source dependencies\n* Manipulation of software update/distribution\
\ mechanisms\n* Compromised/infected system images (removable media infected at the factory)(Citation: IBM Storwize)(Citation:\
\ Schneider Electric USB Malware) \n* Replacement of legitimate software with modified versions\n* Sales of modified/counterfeit\
```
