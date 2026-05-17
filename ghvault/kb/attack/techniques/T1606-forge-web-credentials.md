---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1606 - Forge Web Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1606` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may forge credential materials that can be used to gain access to web applications or Internet services. Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens, or other materials to authenticate and authorize user access.

Adversaries may generate these credential materials in order to gain access to web resources. This differs from Steal Web Session Cookie, Steal Application Access Token, and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted from legitimate users.

The generation of web credentials often requires secret values, such as passwords, Private Keys, or other cryptographic seed values. Adversaries may also forge tokens by taking advantage of features such as the `AssumeRole` and `GetFederationToken` APIs in AWS, which allow users to request temporary security credentials (i.e., Temporary Elevated Cloud Access), or the `zmprov gdpak` command in Zimbra, which generates a pre-authentication key that can be used to generate tokens for any user in the domain.

Once forged, adversaries may use these web credentials to access resources (ex: Use Alternate Authentication Material), which may bypass multi-factor and other authentication protection mechanisms.

## Source Verification

[source record](../../sources/mitre/forge-web-credentials.md)

## Evidence Excerpt

```text
created: '2020-12-17T02:13:46.247Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may forge credential materials that can be used to gain access to web applications or Internet services.
Web applications and services (hosted in cloud SaaS environments or on-premise servers) often use session cookies, tokens,
or other materials to authenticate and authorize user access.
Adversaries may generate these credential materials in order to gain access to web resources. This differs from [Steal Web
Session Cookie](https://attack.mitre.org/techniques/T1539), [Steal Application Access Token](https://attack.mitre.org/techniques/T1528),
and other similar behaviors in that the credentials are new and forged by the adversary, rather than stolen or intercepted
```
