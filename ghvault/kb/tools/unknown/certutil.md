---
parsed_by: focuslocust
source: mitre
type: generated
---
# certutil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0160` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

certutil is a command-line utility that can be used to obtain certificate authority information and configure Certificate Services.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/certutil.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [certutil](https://attack.mitre.org/software/S0160) can be used to download files from a given URL.(Citation: TechNet Certutil)(Citation: LOLBAS Certutil) |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | [certutil](https://attack.mitre.org/software/S0160) has been used to decode binaries hidden inside certificate files as Base64 information.(Citation: Malwarebytes Targeted Attack against Saudi Arabia) |
| [T1553.004 - Install Root Certificate](../../attack/techniques/T1553.004-install-root-certificate.md) | explicit | source | [certutil](https://attack.mitre.org/software/S0160) can be used to install browser root certificates as a precursor to performing [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557) between connections to banking websites. Example command: <code>certutil -addstore -f -user ROOT ProgramData\cert512121.der</code>.(Citation: Palo Alto Retefe) |
| [T1560.001 - Archive via Utility](../../attack/techniques/T1560.001-archive-via-utility.md) | explicit | source | [certutil](https://attack.mitre.org/software/S0160) may be used to Base64 encode collected data.(Citation: TechNet Certutil)(Citation: LOLBAS Certutil) |

## Source Verification

[source record](../../sources/mitre/certutil.md)

## Evidence Excerpt

```text
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[certutil](https://attack.mitre.org/software/S0160) is a command-line utility that can be used to obtain certificate
authority information and configure Certificate Services. (Citation: TechNet Certutil)'
external_references:
- external_id: S0160
source_name: mitre-attack
url: https://attack.mitre.org/software/S0160
```
