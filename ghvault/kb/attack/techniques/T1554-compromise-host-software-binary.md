---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1554 - Compromise Host Software Binary

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1554` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients, FTP clients, email clients, web browsers, and many other user or server applications.

Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may also modify a software binary such as an SSH client in order to persistently collect credentials during logins (i.e., Modify Authentication Process).

An adversary may also modify an existing binary by patching in malicious functionality (e.g., IAT Hooking/Entry point patching) prior to the binary’s legitimate execution. For example, an adversary may modify the entry point of a binary to point to malicious code patched in by the adversary before resuming normal execution flow.

After modifying a binary, an adversary may attempt to impair defenses by preventing it from updating (e.g., via the `yum-versionlock` command or `versionlock.list` file in Linux systems that use the yum package manager).

## Source Verification

[source record](../../sources/mitre/compromise-host-software-binary.md)

## Evidence Excerpt

```text
created: '2020-02-11T18:18:34.279Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may modify host software binaries to establish persistent access to systems. Software binaries/executables
provide a wide range of system commands or services, programs, and libraries. Common software binaries are SSH clients,
FTP clients, email clients, web browsers, and many other user or server applications.
Adversaries may establish persistence though modifications to host software binaries. For example, an adversary may replace
or otherwise infect a legitimate application binary (or support files) with a backdoor. Since these binaries may be routinely
executed by applications or the user, the adversary can leverage this for persistent access to the host. An adversary may
```
