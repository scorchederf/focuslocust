---
parsed_by: focuslocust
source: mitre
type: generated
---
# Brute Ratel C4

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1063` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Brute Ratel C4 is a commercial red-teaming and adversarial attack simulation tool that first appeared in December 2020. Brute Ratel C4 was specifically designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September 2022, a cracked version of Brute Ratel C4 was leaked in the cybercriminal underground, leading to its use by threat actors.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/brute-ratel-c4.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to upload files from a compromised system.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1021 - Remote Services](../../attack/techniques/T1021-remote-services.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use RPC for lateral movement.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1021.002 - SMB／Windows Admin Shares](../../attack/techniques/T1021.002-smb-windows-admin-shares.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use SMB to pivot in compromised networks.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022)(Citation: Dark Vortex Brute Ratel C4) |
| [T1021.006 - Windows Remote Management](../../attack/techniques/T1021.006-windows-remote-management.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WinRM for pivoting.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used encrypted payload files and maintains an encrypted configuration structure in memory.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |
| [T1027.007 - Dynamic API Resolution](../../attack/techniques/T1027.007-dynamic-api-resolution.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call and dynamically resolve hashed APIs.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1036.005 - Match Legitimate Resource Name or Location](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used a payload file named OneDrive.update to appear benign.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1036.008 - Masquerade File Type](../../attack/techniques/T1036.008-masquerade-file-type.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used Microsoft Word icons to hide malicious LNK files.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can conduct port scanning against targeted systems.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use WMI to move laterally.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1055.002 - Portable Executable Injection](../../attack/techniques/T1055.002-portable-executable-injection.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has injected [Latrodectus](https://attack.mitre.org/software/S1160) into the Explorer.exe process on comrpomised hosts.(Citation: Rapid7 Fake W2 July 2024) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can enumerate all processes and locate specific process IDs (PIDs).(Citation: Palo Alto Brute Ratel July 2022) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use cmd.exe for execution.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use `net group` for discovery on targeted domains.(Citation: Trend Micro Black Basta October 2022) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use HTTPS and HTTPS for C2 communication.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [T1071.004 - DNS](../../attack/techniques/T1071.004-dns.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries, `net group "Domain Admins" /domain` and `net user /domain` for discovery.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [T1095 - Non-Application Layer Protocol](../../attack/techniques/T1095-non-application-layer-protocol.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to use TCP for external C2.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1102 - Web Service](../../attack/techniques/T1102-web-service.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use legitimate websites for external C2 channels including Slack, Discord, and MS Teams.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) can download files to compromised hosts.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Rapid7 Fake W2 July 2024) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call multiple Windows APIs for execution, to share memory, and defense evasion.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can take screenshots on compromised hosts.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to deobfuscate its payload prior to execution.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1204.002 - Malicious File](../../attack/techniques/T1204.002-malicious-file.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has gained execution through users opening malicious documents.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use LDAP queries and `nltest /domain_trusts` for domain trust discovery.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [T1497.003 - Time Based Checks](../../attack/techniques/T1497.003-time-based-checks.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call `NtDelayExecution` to pause execution.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |
| [T1518.001 - Security Software Discovery](../../attack/techniques/T1518.001-security-software-discovery.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can detect EDR userland hooks.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1558.003 - Kerberoasting](../../attack/techniques/T1558.003-kerberoasting.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can decode Kerberos 5 tickets and convert it to hashcat format for subsequent cracking.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) can create Windows system services for execution.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1572 - Protocol Tunneling](../../attack/techniques/T1572-protocol-tunneling.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can use DNS over HTTPS for C2.(Citation: Palo Alto Brute Ratel July 2022)(Citation: Trend Micro Black Basta October 2022) |
| [T1574.001 - DLL](../../attack/techniques/T1574.001-dll.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used search order hijacking to load a malicious payload DLL as a dependency to a benign application packaged in the same ISO.(Citation: Palo Alto Brute Ratel July 2022) [Brute Ratel C4](https://attack.mitre.org/software/S1063) has loaded a malicious DLL by spoofing the name of the legitimate Version.DLL and placing it in the same folder as the digitally-signed Microsoft binary OneDriveUpdater.exe.(Citation: Palo Alto Brute Ratel July 2022) |
| [T1620 - Reflective Code Loading](../../attack/techniques/T1620-reflective-code-loading.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used reflective loading to execute malicious DLLs.(Citation: MDSec Brute Ratel August 2022) |
| [T1685 - Disable or Modify Tools](../../attack/techniques/T1685-disable-or-modify-tools.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to hide memory artifacts and to patch Event Tracing for Windows (ETW) and the Anti Malware Scan Interface (AMSI).(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |

## Source Verification

[source record](../../sources/mitre/brute-ratel-c4.md)

## Evidence Excerpt

```text
created: '2023-02-07T20:26:58.792Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Brute Ratel C4](https://attack.mitre.org/software/S1063) is a commercial red-teaming and adversarial attack
simulation tool that first appeared in December 2020. [Brute Ratel C4](https://attack.mitre.org/software/S1063) was specifically
designed to avoid detection by endpoint detection and response (EDR) and antivirus (AV) capabilities, and deploys agents
called badgers to enable arbitrary command execution for lateral movement, privilege escalation, and persistence. In September
2022, a cracked version of [Brute Ratel C4](https://attack.mitre.org/software/S1063) was leaked in the cybercriminal underground,
leading to its use by threat actors.(Citation: Dark Vortex Brute Ratel C4)(Citation: Palo Alto Brute Ratel July 2022)(Citation:
```
