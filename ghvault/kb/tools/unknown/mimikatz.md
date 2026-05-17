---
parsed_by: focuslocust
source: mitre
type: generated
---
# Mimikatz

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Mimikatz is a credential dumper capable of obtaining plaintext Windows account logins and passwords, along with many other features that make it useful for testing the security of networks.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/mimikatz.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSASS Memory.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools) |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the SAM table.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools) |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the LSA.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools) |
| [T1003.006 - DCSync](../../attack/techniques/T1003.006-dcsync.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DCSync/NetSync.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020) |
| [T1098 - Account Manipulation](../../attack/techniques/T1098-account-manipulation.md) | explicit | source | The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper has been extended to include Skeleton Key domain controller authentication bypass functionality. The <code>LSADUMP::ChangeNTLM</code> and <code>LSADUMP::SetNTLM</code> modules can also manipulate the password hash of an account without knowing the clear text value.(Citation: Adsecurity Mimikatz Guide)(Citation: Metcalf 2015) |
| [T1134.005 - SID-History Injection](../../attack/techniques/T1134.005-sid-history-injection.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)'s <code>MISC::AddSid</code> module can append any SID or user/group account to a user's SID-History. [Mimikatz](https://attack.mitre.org/software/S0002) also utilizes [SID-History Injection](https://attack.mitre.org/techniques/T1134/005) to expand the scope of other components such as generated Kerberos Golden Tickets and DCSync beyond a single domain.(Citation: Adsecurity Mimikatz Guide)(Citation: AdSecurity Kerberos GT Aug 2015) |
| [T1207 - Rogue Domain Controller](../../attack/techniques/T1207-rogue-domain-controller.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)’s <code>LSADUMP::DCShadow</code> module can be used to make AD updates by temporarily setting a computer to be a DC.(Citation: Deply Mimikatz)(Citation: Adsecurity Mimikatz Guide) |
| [T1547.005 - Security Support Provider](../../attack/techniques/T1547.005-security-support-provider.md) | explicit | source | The [Mimikatz](https://attack.mitre.org/software/S0002) credential dumper contains an implementation of an SSP.(Citation: Deply Mimikatz) |
| [T1550.002 - Pass the Hash](../../attack/techniques/T1550.002-pass-the-hash.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)'s <code>SEKURLSA::Pth</code> module can impersonate a user, with only a password hash, to execute arbitrary commands.(Citation: Adsecurity Mimikatz Guide)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020) |
| [T1550.003 - Pass the Ticket](../../attack/techniques/T1550.003-pass-the-ticket.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)’s <code>LSADUMP::DCSync</code> and <code>KERBEROS::PTT</code> modules implement the three steps required to extract the krbtgt account hash and create/use Kerberos tickets.(Citation: Adsecurity Mimikatz Guide)(Citation: AdSecurity Kerberos GT Aug 2015)(Citation: Harmj0y DCSync Sept 2015)(Citation: NCSC Joint Report Public Tools) |
| [T1552.004 - Private Keys](../../attack/techniques/T1552.004-private-keys.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)'s <code>CRYPTO::Extract</code> module can extract keys by interacting with Windows cryptographic application programming interface (API) functions.(Citation: Adsecurity Mimikatz Guide) |
| [T1555 - Credentials from Password Stores](../../attack/techniques/T1555-credentials-from-password-stores.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from the credential vault and DPAPI.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)(Citation: Cobalt Strike Manual 4.3 November 2020)	 |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) performs credential dumping to obtain account and password information useful in gaining access to additional systems and enterprise network resources. It contains functionality to acquire information about credentials in many ways, including from DPAPI.(Citation: Deply Mimikatz)(Citation: GitHub Mimikatz lsadump Module)(Citation: Directory Services Internals DPAPI Backup Keys Oct 2015)(Citation: NCSC Joint Report Public Tools)	 |
| [T1555.004 - Windows Credential Manager](../../attack/techniques/T1555.004-windows-credential-manager.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002) contains functionality to acquire credentials from the Windows Credential Manager.(Citation: Delpy Mimikatz Crendential Manager) |
| [T1558.001 - Golden Ticket](../../attack/techniques/T1558.001-golden-ticket.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)'s kerberos module can create golden tickets.(Citation: GitHub Mimikatz kerberos Module)(Citation: Cobalt Strike Manual 4.3 November 2020) |
| [T1558.002 - Silver Ticket](../../attack/techniques/T1558.002-silver-ticket.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)'s kerberos module can create silver tickets.(Citation: GitHub Mimikatz kerberos Module) |
| [T1649 - Steal or Forge Authentication Certificates](../../attack/techniques/T1649-steal-or-forge-authentication-certificates.md) | explicit | source | [Mimikatz](https://attack.mitre.org/software/S0002)'s `CRYPTO` module can create and export various types of authentication certificates.(Citation: Adsecurity Mimikatz Guide) |

## Source Verification

[source record](../../sources/mitre/mimikatz.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:11.544Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Mimikatz](https://attack.mitre.org/software/S0002) is a credential dumper capable of obtaining plaintext Windows
account logins and passwords, along with many other features that make it useful for testing the security of networks. (Citation:
Deply Mimikatz) (Citation: Adsecurity Mimikatz Guide)'
external_references:
- external_id: S0002
source_name: mitre-attack
```
