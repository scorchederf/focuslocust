---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1201 - Password Policy Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1201` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to access detailed information about the password policy used within an enterprise network or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through Brute Force. This information may help the adversary to create a list of common passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length should be 8, then not trying passwords such as 'pass123'; not checking for more than 3-4 passwords per account if the lockout is set to 6 as to not lock out accounts).

Password policies can be set and discovered on Windows, Linux, and macOS systems via various command shell utilities such as <code>net accounts (/domain)</code>, <code>Get-ADDefaultDomainPasswordPolicy</code>, <code>chage -l <username></code>, <code>cat /etc/pam.d/common-password</code>, and <code>pwpolicy getaccountpolicies</code>  . Adversaries may also leverage a Network Device CLI on network devices to discover password policy information (e.g. <code>show aaa</code>, <code>show aaa common-criteria policy all</code>).

Password policies can be discovered in cloud environments using available APIs such as <code>GetAccountPasswordPolicy</code> in AWS .

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover the password policies applied to the target system.(Citation: CME Github September 2018) |
| [Net](../../tools/unknown/net.md) | explicit | source | The <code>net accounts</code> and <code>net accounts /domain</code> commands with [Net](https://attack.mitre.org/software/S0039) can be used to obtain password policy information.(Citation: Savill 1999) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use <code>Get-PassPol</code> to enumerate the domain password policy.(Citation: GitHub PoshC2) |

## Source Verification

[source record](../../sources/mitre/password-policy-discovery.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to access detailed information about the password policy used within an enterprise network
or cloud environment. Password policies are a way to enforce complex passwords that are difficult to guess or crack through
[Brute Force](https://attack.mitre.org/techniques/T1110). This information may help the adversary to create a list of common
passwords and launch dictionary and/or brute force attacks which adheres to the policy (e.g. if the minimum password length
should be 8, then not trying passwords such as ''pass123''; not checking for more than 3-4 passwords per account if the
lockout is set to 6 as to not lock out accounts).
```
