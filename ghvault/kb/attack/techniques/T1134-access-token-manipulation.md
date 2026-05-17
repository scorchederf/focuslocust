---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1134 - Access Token Manipulation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1134` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may modify access tokens to operate under a different user or system security context to perform actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to someone other than the user that started the process. When this occurs, the process also takes on the security context associated with the new token.

An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token stealing. These token can then be applied to an existing process (i.e. Token Impersonation/Theft) or used to spawn a new process (i.e. Create Process with Token). An adversary must already be in a privileged user context (i.e. administrator) to steal a token. However, adversaries commonly use token stealing to elevate their security context from the administrator level to the SYSTEM level. An adversary can then use a token to authenticate to a remote system as the account for that token if the account has appropriate permissions on the remote system.

Any standard user can use the <code>runas</code> command, and the Windows API functions, to create impersonation tokens; it does not require access to an administrator account. There are also other mechanisms, such as Active Directory fields, that can be used to modify access tokens.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can use [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-TokenManipulation</code> to manipulate access tokens.(Citation: Github PowerShell Empire) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can use Invoke-TokenManipulation for manipulating tokens.(Citation: GitHub PoshC2) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-TokenManipulation</code> Exfiltration module can be used to manipulate tokens.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) has the ability to manipulate user tokens on targeted Windows systems.(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2) |

## Source Verification

[source record](../../sources/mitre/access-token-manipulation.md)

## Evidence Excerpt

```text
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify access tokens to operate under a different user or system security context to perform
actions and bypass access controls. Windows uses access tokens to determine the ownership of a running process. A user can
manipulate access tokens to make a running process appear as though it is the child of a different process or belongs to
someone other than the user that started the process. When this occurs, the process also takes on the security context associated
with the new token.
An adversary can use built-in Windows API functions to copy access tokens from existing processes; this is known as token
```
