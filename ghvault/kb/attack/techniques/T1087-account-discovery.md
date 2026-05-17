---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1087 - Account Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1087` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., Valid Accounts).

Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential misconfigurations that leak account names and roles or permissions in the targeted environment.

For examples, cloud environments typically provide easily accessible interfaces to obtain user lists. On hosts, adversaries can use default PowerShell and other command line functionality to identify accounts. Information about email addresses and accounts may also be extracted by searching an infected system’s files.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all non-privileged and privileged accounts available on the machine.(Citation: FOX-IT May 2016 Mofang) |

## Source Verification

[source record](../../sources/mitre/account-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:06.988Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of valid accounts, usernames, or email addresses on a system or within
a compromised environment. This information can help adversaries determine which accounts exist, which can aid in follow-on
behavior such as brute-forcing, spear-phishing attacks, or account takeovers (e.g., [Valid Accounts](https://attack.mitre.org/techniques/T1078)).
Adversaries may use several methods to enumerate accounts, including abuse of existing tools, built-in commands, and potential
misconfigurations that leak account names and roles or permissions in the targeted environment.
For examples, cloud environments typically provide easily accessible interfaces to obtain user lists.(Citation: AWS List
```
