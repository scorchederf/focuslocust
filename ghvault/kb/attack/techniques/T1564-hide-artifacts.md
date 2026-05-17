---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1564 - Hide Artifacts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems may have features to hide various artifacts, such as important system files and administrative task execution, to avoid disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.

Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are isolated from common security instrumentation, such as through the use of virtualization technology.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [DeviceCredentialDeployment.exe](../../tools/windows/devicecredentialdeployment.exe.md) | explicit | source | Command metadata lists T1564: DeviceCredentialDeployment |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can modify file attributes to hide the file.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [msxsl.exe](../../tools/windows/msxsl.exe.md) | explicit | source | Command metadata lists T1564: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name |

## Source Verification

[source record](../../sources/mitre/hide-artifacts.md)

## Evidence Excerpt

```text
created: '2020-02-26T17:41:25.933Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to hide artifacts associated with their behaviors to evade detection. Operating systems
may have features to hide various artifacts, such as important system files and administrative task execution, to avoid
disrupting user work environments and prevent users from changing files or features on the system. Adversaries may abuse
these features to hide artifacts such as files, directories, user accounts, or other system activity to evade detection.(Citation:
Sofacy Komplex Trojan)(Citation: Cybereason OSX Pirrit)(Citation: MalwareBytes ADS July 2015)
Adversaries may also attempt to hide artifacts associated with malicious behavior by creating computing regions that are
```
