---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1480 - Execution Guardrails

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1480` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against an intended target and reduces collateral damage from an adversary’s campaign. Values an adversary can provide about a target system or environment to use as guardrails may include specific network share names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.

Guardrails can be used to prevent exposure of capabilities in environments that are not intended to be compromised or operated within. This use of guardrails is distinct from typical Virtualization/Sandbox Evasion. While use of Virtualization/Sandbox Evasion may involve checking for known sandbox values and continuing with execution only if there is no match, the use of guardrails will involve checking for an expected target-specific value and only continuing with execution if there is such a match.

Adversaries may identify and block certain user-agents to evade defenses and narrow the scope of their attack to victims and platforms on which it will be most effective. A user-agent self-identifies data such as a user's software application, operating system, vendor, and version. Adversaries may check user-agents for operating system identification and then only serve malware for the exploitable software while ignoring all other operating systems.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can reject requests to phishing URLs if the User-Agent of the visitor doesn't match the allowlist REGEX filter for a specific lure.(Citation: Breakdev Evilginx 2.4 SEP 2020) |

## Source Verification

[source record](../../sources/mitre/execution-guardrails.md)

## Evidence Excerpt

```text
created: '2019-01-31T02:10:08.261Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use execution guardrails to constrain execution or actions based on adversary supplied and environment
specific conditions that are expected to be present on the target. Guardrails ensure that a payload only executes against
an intended target and reduces collateral damage from an adversary’s campaign.(Citation: FireEye Kevin Mandia Guardrails)
Values an adversary can provide about a target system or environment to use as guardrails may include specific network share
names, attached physical devices, files, joined Active Directory (AD) domains, and local/external IP addresses.(Citation:
FireEye Outlook Dec 2019)
```
