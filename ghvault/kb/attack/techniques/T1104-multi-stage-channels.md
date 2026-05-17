---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1104 - Multi-Stage Channels

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1104` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.

The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or Fallback Channels in case the original first-stage communication path is discovered and blocked.

## Source Verification

[source record](../../sources/mitre/multi-stage-channels.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:15.935Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create multiple stages for command and control that are employed under different conditions
or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.
Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have
automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access
tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second
stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and
```
