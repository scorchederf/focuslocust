---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1133 - External Remote Services

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1133` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gateways that manage connections and credential authentication for these services. Services such as Windows Remote Management and VNC can also be used externally.

Access to Valid Accounts to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network. Access to remote services may be used as a redundant or persistent access mechanism during an operation.

Access may also be gained through an exposed service that doesn’t require authentication. In containerized environments, this may include an exposed Docker API, Kubernetes API server, kubelet, or web application such as the Kubernetes dashboard.

Adversaries may also establish persistence on network by configuring a Tor hidden service on a compromised system. Adversaries may utilize the tool `ShadowLink` to facilitate the installation and configuration of the Tor hidden service. Tor hidden service is then accessible via the Tor network because `ShadowLink` sets up a .onion address on the compromised system. `ShadowLink` may be used to forward any inbound connections to RDP, allowing the adversaries to have remote access. Adversaries may get `ShadowLink` to persist on a system by masquerading it as an MS Defender application.

## Source Verification

[source record](../../sources/mitre/external-remote-services.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:44.421Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may leverage external-facing remote services to initially access and/or persist within a network.
Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network
resources from external locations. There are often remote service gateways that manage connections and credential authentication
for these services. Services such as [Windows Remote Management](https://attack.mitre.org/techniques/T1021/006) and [VNC](https://attack.mitre.org/techniques/T1021/005)
can also be used externally.(Citation: MacOS VNC software for Remote Desktop)
Access to [Valid Accounts](https://attack.mitre.org/techniques/T1078) to use the service is often a requirement, which could
```
