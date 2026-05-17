---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1037 - Boot or Logon Initialization Scripts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1037` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence. Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Source Verification

[source record](../../sources/mitre/boot-or-logon-initialization-scripts.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:38.910Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation:\
\ Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform\
\ administrative functions, which may often execute other programs or send information to an internal logging server. These\
\ scripts can vary based on operating system and whether applied locally or remotely.  \n\nAdversaries may use these scripts\
\ to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials\
\ or an administrator account may be necessary. \n\nAn adversary may also be able to escalate their privileges since some\
```
