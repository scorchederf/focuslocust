---
parsed_by: focuslocust
source: mitre
type: generated
---
# LaZagne

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0349` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

LaZagne is a post-exploitation, open-source tool used to recover stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. LaZagne is publicly available on GitHub.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/lazagne.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from memory to obtain account and password information.(Citation: GitHub LaZagne Dec 2018) |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from LSA secrets to obtain account and password information.(Citation: GitHub LaZagne Dec 2018) |
| [T1003.005 - Cached Domain Credentials](../../attack/techniques/T1003.005-cached-domain-credentials.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can perform credential dumping from MSCache to obtain account and password information.(Citation: GitHub LaZagne Dec 2018) |
| [T1003.007 - Proc Filesystem](../../attack/techniques/T1003.007-proc-filesystem.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can use the `<PID>/maps` and `<PID>/mem` files to identify regex patterns to dump cleartext passwords from the browser's process memory.(Citation: GitHub LaZagne Dec 2018)(Citation: Picus Labs Proc cump 2022) |
| [T1003.008 - ／etc／passwd and ／etc／shadow](../../attack/techniques/T1003.008-etc-passwd-and-etc-shadow.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credential information from /etc/shadow using the shadow.py module.(Citation: GitHub LaZagne Dec 2018) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from chats, databases, mail, and WiFi.(Citation: GitHub LaZagne Dec 2018) |
| [T1555 - Credentials from Password Stores](../../attack/techniques/T1555-credentials-from-password-stores.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from databases, mail, and WiFi across multiple platforms.(Citation: GitHub LaZagne Dec 2018) |
| [T1555.001 - Keychain](../../attack/techniques/T1555.001-keychain.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from macOS Keychains.(Citation: GitHub LaZagne Dec 2018)	 |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from web browsers such as Google Chrome, Internet Explorer, and Firefox.(Citation: GitHub LaZagne Dec 2018) |
| [T1555.004 - Windows Credential Manager](../../attack/techniques/T1555.004-windows-credential-manager.md) | explicit | source | [LaZagne](https://attack.mitre.org/software/S0349) can obtain credentials from Vault files.(Citation: GitHub LaZagne Dec 2018)	 |

## Source Verification

[source record](../../sources/mitre/lazagne.md)

## Evidence Excerpt

```text
created: '2019-01-30T16:44:59.887Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[LaZagne](https://attack.mitre.org/software/S0349) is a post-exploitation, open-source tool used to recover
stored passwords on a system. It has modules for Windows, Linux, and OSX, but is mainly focused on Windows systems. [LaZagne](https://attack.mitre.org/software/S0349)
is publicly available on GitHub.(Citation: GitHub LaZagne Dec 2018)'
external_references:
- external_id: S0349
source_name: mitre-attack
```
