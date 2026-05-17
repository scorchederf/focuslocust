---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1671 - Cloud Application Integration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1671` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt an existing integration to achieve malicious ends.

OAuth is an open standard that allows users to authorize applications to access their information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications to improve their workflow and achieve tasks.  

Leveraging application integrations may allow adversaries to persist in an environment – for example, by granting consent to an application from a high-privileged adversary-controlled account in order to maintain access to its data, even in the event of losing access to the account. In some cases, integrations may remain valid even after the original consenting user account is disabled. Application integrations may also allow adversaries to bypass multi-factor authentication requirements through the use of Application Access Tokens. Finally, they may enable persistent Automated Exfiltration over time.

Creating or adding a new application may require the adversary to create a dedicated Cloud Account for the application and assign it Additional Cloud Roles – for example, in Microsoft 365 environments, an application can only access resources via an associated service principal.

## Source Verification

[source record](../../sources/mitre/cloud-application-integration.md)

## Evidence Excerpt

```text
created: '2025-03-20T22:21:59.326Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may achieve persistence by leveraging OAuth application integrations in a software-as-a-service\
\ environment. Adversaries may create a custom application, add a legitimate application into the environment, or even co-opt\
\ an existing integration to achieve malicious ends.(Citation: Push Security SaaS Persistence 2022)(Citation: SaaS Attacks\
\ GitHub Evil Twin Integrations)\n\nOAuth is an open standard that allows users to authorize applications to access their\
\ information on their behalf. In a SaaS environment such as Microsoft 365 or Google Workspace, users may integrate applications\
\ to improve their workflow and achieve tasks.  \n\nLeveraging application integrations may allow adversaries to persist\
```
