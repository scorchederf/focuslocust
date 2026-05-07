---
parsed_by: focuslocust
source: mitre
type: data-source
aliases:
    - DC0074
tags:
    - attack/domain/enterprise_attack
    - attack/type/data_source
mitre-attack: kb/mitre/attack/data-sources/DC0074-driver-metadata
---

## Description

to contextual data about a driver, including its attributes, functionality, and activity. This can involve details such as the driver's origin, integrity, cryptographic signature, issues reported during its use, and runtime behavior. Examples include metadata captured during driver integrity checks, hash validation, or error reporting. Examples: <br><br>- Driver Signature Validation: A driver is validated to ensure it is signed by a trusted Certificate Authority (CA).<br>- Driver Hash Verification: The hash of a driver is compared to a known good hash stored in a database.<br>- Driver Compatibility Issues: A driver error is logged due to compatibility issues with a particular version of the operating system.<br>- Vulnerable Driver Identification: Metadata indicates the driver version is outdated or contains a known vulnerability.<br>- Monitoring Driver Integrity: Drivers are monitored for any unauthorized modifications to their binary or associated files.<br><br>This data component can be collected through the following measures:<br><br>Windows<br><br>- Windows Event Logs:<br>    - Event ID 3000-3006: Logs metadata about driver signature validation.<br>    - Event ID 2000-2011 (Windows Defender Application Control): Tracks driver integrity and policy enforcement.<br>- Sysmon Logs: Configure Sysmon to capture driver loading metadata (Event ID 6).<br>- Driver Verifier: Use Driver Verifier to collect diagnostic and performance data about drivers, including stability and compatibility metrics.<br>- PowerShell: Use commands to retrieve metadata about installed drivers:<br>`Get-WindowsDriver -Online | Select-Object Driver, ProviderName, Version`<br><br>Linux<br><br>- Auditd: Configure audit rules to monitor driver interactions and collect metadata: `auditctl -w /lib/modules/ -p rwxa -k driver_metadata`<br>- dmesg: Use `dmesg` to extract kernel logs with driver metadata: `dmesg | grep "module"`<br>- lsmod and modinfo: Commands to list loaded modules and retrieve metadata about drivers: `lsmod` | `modinfo <module_name>`<br><br>macOS<br><br>- Unified Logs: Collect metadata from system logs about kernel extensions (kexts): `log show --predicate 'eventMessage contains "kext load"' --info`<br>- kextstat: Command to retrieve information about loaded kernel extensions: `kextstat`<br><br>SIEM Tools<br><br>- Ingest Driver Metadata: Collect driver metadata logs from Sysmon, Auditd, or macOS logs into SIEMs like Splunk or Elastic.<br><br>Vulnerability Management Tools<br><br>- Use these tools to collect metadata about vulnerable drivers across enterprise systems.
