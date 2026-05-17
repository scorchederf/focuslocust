---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1546 - Event Triggered Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1546` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.

Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Pacu](../../tools/unknown/pacu.md) | explicit | source | [Pacu](https://attack.mitre.org/software/S1091) can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.(Citation: GitHub Pacu) |

## Source Verification

[source record](../../sources/mitre/event-triggered-execution.md)

## Evidence Excerpt

```text
created: '2020-01-22T21:04:23.285Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution
based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other
user activity such as running specific applications/binaries. Cloud environments may also support various functions and
services that monitor and can be invoked in response to specific cloud events.(Citation: Backdooring an AWS account)(Citation:
Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001)
Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing
```
