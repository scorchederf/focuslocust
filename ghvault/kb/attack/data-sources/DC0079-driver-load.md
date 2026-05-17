---
parsed_by: focuslocust
source: mitre
type: generated
---
# DC0079 - Driver Load

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `data-source` |
| Record ID | `DC0079` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The process of attaching a driver, which is a software component that allows the operating system and applications to interact with hardware devices, to either user-mode or kernel-mode of a system. This can include benign actions (e.g., hardware drivers) or malicious behavior (e.g., rootkits or unsigned drivers). Examples: 

- Legitimate Driver Loading: A new graphics driver from a vendor like NVIDIA or AMD is loaded into the system.
- Unsigned Driver Loading: A driver without a valid digital signature is loaded into the kernel.
- Rootkit Installation: A malicious rootkit driver is loaded to manipulate kernel-mode processes.
- Anti-Virus or EDR Driver Loading: An Endpoint Detection and Response (EDR) solution loads its driver to monitor system activities.
- Driver Misuse: A legitimate driver is loaded and exploited to execute malicious actions, such as using vulnerable drivers for bypassing defenses (e.g., Bring Your Own Vulnerable Driver (BYOVD) attacks).

## Source Verification

[source record](../../sources/mitre/driver-load.md)

## Evidence Excerpt

```text
created: '2021-10-20T15:05:19.274Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The process of attaching a driver, which is a software component that allows the operating system and applications\
\ to interact with hardware devices, to either user-mode or kernel-mode of a system. This can include benign actions (e.g.,\
\ hardware drivers) or malicious behavior (e.g., rootkits or unsigned drivers). Examples: \n\n- Legitimate Driver Loading:\
\ A new graphics driver from a vendor like NVIDIA or AMD is loaded into the system.\n- Unsigned Driver Loading: A driver\
\ without a valid digital signature is loaded into the kernel.\n- Rootkit Installation: A malicious rootkit driver is loaded\
\ to manipulate kernel-mode processes.\n- Anti-Virus or EDR Driver Loading: An Endpoint Detection and Response (EDR) solution\
```
