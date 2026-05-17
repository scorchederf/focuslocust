---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1111 - Multi-Factor Authentication Interception

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1111` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may target multi-factor authentication (MFA) mechanisms, (i.e., smart cards, token generators, etc.) to gain access to credentials that can be used to access systems, services, and network resources. Use of MFA is recommended and provides a higher level of security than usernames and passwords alone, but organizations should be aware of techniques that could be used to intercept and bypass these security mechanisms. 

If a smart card is used for multi-factor authentication, then a keylogger will need to be used to obtain the password associated with a smart card during normal use. With both an inserted card and access to the smart card password, an adversary can connect to a network resource using the infected system to proxy the authentication with the inserted hardware token. 

Adversaries may also employ a keylogger to similarly target other hardware tokens, such as RSA SecurID. Capturing token input (including a user's personal identification code) may provide temporary access (i.e. replay the one-time passcode until the next value rollover) as well as possibly enabling adversaries to reliably predict future authentication values (given access to both the algorithm and any seed values used to generate appended temporary codes). 

Other methods of MFA may be intercepted and used by an adversary to authenticate. It is common for one-time codes to be sent via out-of-band communications (email, SMS). If the device and/or service is not secured, then it may be vulnerable to interception. Service providers can also be targeted: for example, an adversary may compromise an SMS messaging service in order to steal MFA codes sent to users’ phones.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [evilginx2](../../tools/unknown/evilginx2.md) | explicit | source | [evilginx2](https://attack.mitre.org/software/S9003) can intercept authentication tokens to enable bypass of non-phishing resistant forms of MFA.(Citation: Evilginx 2 July 2018) |

## Source Verification

[source record](../../sources/mitre/multi-factor-authentication-interception.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:23.195Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may target multi-factor authentication (MFA) mechanisms, (i.e., smart cards, token generators, etc.)\
\ to gain access to credentials that can be used to access systems, services, and network resources. Use of MFA is recommended\
\ and provides a higher level of security than usernames and passwords alone, but organizations should be aware of techniques\
\ that could be used to intercept and bypass these security mechanisms. \n\nIf a smart card is used for multi-factor authentication,\
\ then a keylogger will need to be used to obtain the password associated with a smart card during normal use. With both\
\ an inserted card and access to the smart card password, an adversary can connect to a network resource using the infected\
```
