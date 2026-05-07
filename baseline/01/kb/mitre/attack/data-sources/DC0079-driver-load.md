---
generated_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0079
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0079-driver-load
---

## Description

The process of attaching a driver, which is a software component that allows the operating system and applications to interact with hardware devices, to either user-mode or kernel-mode of a system. This can include benign actions (e.g., hardware drivers) or malicious behavior (e.g., rootkits or unsigned drivers). Examples: <br><br>- Legitimate Driver Loading: A new graphics driver from a vendor like NVIDIA or AMD is loaded into the system.<br>- Unsigned Driver Loading: A driver without a valid digital signature is loaded into the kernel.<br>- Rootkit Installation: A malicious rootkit driver is loaded to manipulate kernel-mode processes.<br>- Anti-Virus or EDR Driver Loading: An Endpoint Detection and Response (EDR) solution loads its driver to monitor system activities.<br>- Driver Misuse: A legitimate driver is loaded and exploited to execute malicious actions, such as using vulnerable drivers for bypassing defenses (e.g., Bring Your Own Vulnerable Driver (BYOVD) attacks).
