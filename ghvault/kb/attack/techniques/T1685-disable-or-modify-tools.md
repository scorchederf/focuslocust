---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1685 - Disable or Modify Tools

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1685` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments. 

In addition to directly targeting tools, adversaries may block or manipulate indicators and telemetry used for detection. This includes maliciously disabling or redirecting sensors such as Event Tracing for Windows (ETW), modifying event log configurations (e.g., redirecting Security logs), or interfering with logging pipelines and forwarding mechanisms (e.g., SIEM ingestion).

More advanced techniques include leveraging legitimate drivers or debugging mechanisms to render tools non-functional, bypassing anti-tampering protections, and targeting specific defenses such as Sysmon or cloud monitoring agents. Adversaries may also disrupt broader defensive operations, including update mechanisms, logging infrastructure (e.g., syslog), or event aggregation, further degrading an organization’s ability to detect and respond to malicious activity.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI).(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |
| [DCRAT](../../tools/unknown/dcrat.md) | explicit | source | [DCRAT](https://attack.mitre.org/software/S9017) can patch Microsoft’s Antimalware Scan Interface (AMSI) to evade detection.(Citation: Zscaler BlindEagle DEC 2025) |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can patch Antimalware Scan Interface (AMSI), Windows Lockdown Policy (WLDP), as well as exit-related [Native API](https://attack.mitre.org/techniques/T1106) functions to avoid process termination.(Citation: Donut Github)	 |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a feature to disable Windows Task Manager.(Citation: Imminent Unit42 Dec2019)	 |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692)'s `amsiPatch.py` module can disable Antimalware Scan Interface (AMSI) functions.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/disable-or-modify-tools.md)

## Evidence Excerpt

```text
created: '2026-04-14T22:53:26.949Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may disable, degrade, or tamper with security tools or applications (e.g., endpoint detection and\
\ response (EDR) tools, intrusion detection systems (IDS), antivirus, logging agents, sensors, etc.) to impair or reduce\
\ visibility of defensive capabilities. This may include stopping specific services, killing processes, modifying or deleting\
\ tool configuration files and Registry keys, or preventing tools from updating. This may also include impairing defenses\
\ more broadly by disrupting preventative, detection, and response mechanisms across host, network, and cloud environments.(Citation:\
\ SCADAfence_ransomware) \n\nIn addition to directly targeting tools, adversaries may block or manipulate indicators and\
```
