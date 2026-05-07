---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1686
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1686-disable-or-modify-system-firewall
tactic:
    - Defense Impairment
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may disable or modify host-based or network firewalls to impair defensive mechanisms and enable further action. Once an adversary has gathered sufficient privileges, they can tamper with firewall services, policies, or rule sets to remove restrictions on inbound or outbound traffic. For example, this may include turning off firewall profiles, altering existing rules to permit previously blocked ports or protocols, or adding new rules that create covert communication paths (e.g., adding a new firewall rule for a well-known protocol (such as RDP) using a non-traditional and potentially less securitized port.[^3] <br><br>Adversaries may disable or modify firewalls using different behaviors, depending on the platform. For example, in ESXi, firewall rules may be modified directly via the esxcli (e.g., via esxcli network firewall set) or via the vCenter user interface.[^1] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has modified local firewall rules on victim machines to enable a random, high-number listening port for subsequent access and C2 activity.[^1]  |
| [S0031](https://attack.mitre.org/software/S0031) | BACKSPACE | The "ZR" variant of BACKSPACE will check to see if known host-based firewalls are installed on the infected systems. BACKSPACE will attempt to establish a C2 channel, then will examine open windows to identify a pop-up from the firewall software and will simulate a mouse-click to allow the connection to proceed.[^1]  |
| [S0088](https://attack.mitre.org/software/S0088) | Kasidet | Kasidet has the ability to change firewall settings to allow a plug-in to be downloaded.[^1]  |
| [[kb/mitre/attack/software/S0108-netsh\|S0108]] | netsh | [[kb/mitre/attack/software/S0108-netsh\|netsh]] can be used to disable local firewall settings.[^1] [^2]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole has a command to disable routing and the Firewall on the victim’s machine.[^1]  |
| [S0336](https://attack.mitre.org/software/S0336) | NanoCore | NanoCore can modify the victim's firewall.[^1] [^2]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT has modified the firewall using [[kb/mitre/attack/software/S0108-netsh\|netsh]].[^1] 	 |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can disable the firewall by modifying the registry key `HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile`.[^1]   |
| [S0492](https://attack.mitre.org/software/S0492) | CookieMiner | CookieMiner has checked for the presence of "Little Snitch", macOS network monitoring and application firewall software, stopping and exiting if it is found.[^1]  |
| [S0531](https://attack.mitre.org/software/S0531) | Grandoreiro | Grandoreiro can block the Deibold Warsaw GAS Tecnologia security tool at the firewall level.[^1]  |
| [S1032](https://attack.mitre.org/software/S1032) | PyDCrypt | PyDCrypt has modified firewall rules to allow incoming SMB, NetBIOS, and RPC connections using `netsh.exe` on remote machines.[^1]  |
| [S1161](https://attack.mitre.org/software/S1161) | BPFDoor | BPFDoor starts a shell on a high TCP port starting at 42391 up to 43391, then changes the local `iptables` rules to redirect all packets from the attacker to the shell port.[^1]   |
| [S1178](https://attack.mitre.org/software/S1178) | ShrinkLocker | ShrinkLocker turns on the system firewall and deletes all of its rules during execution.[^1] [^2]  |
| [S1211](https://attack.mitre.org/software/S1211) | Hannotog | Hannotog can modify local firewall settings via `netsh` commands to open a listening UDP port.[^1]  |
| [S1223](https://attack.mitre.org/software/S1223) | THINCRUST | THINCRUST can use the Django python module "django.views.decorators.csrf” along with the decorator “csrf_exempt” within victim firewalls to disable cross-site request forgery protections.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Ensure proper user permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Ensure proper process and file permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Ensure proper Registry permissions are in place to prevent adversaries from disabling or modifying firewall settings. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Routinely check account role permissions to ensure only expected users and roles have permission to modify system firewalls. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1686.003-windows-host-firewall\|T1686.003]] | Windows Host Firewall |
| [[kb/mitre/attack/techniques/T1686.002-network-device-firewall\|T1686.002]] | Network Device Firewall |
| [[kb/mitre/attack/techniques/T1686.001-cloud-firewall\|T1686.001]] | Cloud Firewall |

 [^1]: [Broadcom ESXi Firewall](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/7-0/add-allowed-ip-addresses-for-an-esxi-host-by-using-the-vmware-host-client.html)
 [^2]: [Trellix Rnasomhouse 2024](https://www.trellix.com/en-au/blogs/research/ransomhouse-am-see/)
 [^3]: [change_rdp_port_conti](https://x.com/TheDFIRReport/status/1498657772254240768)
 [^4]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^5]: [Mandiant Fortinet Zero Day](https://www.mandiant.com/resources/blog/fortinet-malware-ecosystem)
 [^6]: [TechNet Netsh](https://technet.microsoft.com/library/bb490939.aspx)
 [^7]: [TechNet Netsh Firewall](https://technet.microsoft.com/en-us/library/cc771046(v=ws.10).aspx)
 [^8]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^9]: [Unit42 CookieMiner Jan 2019](https://unit42.paloaltonetworks.com/mac-malware-steals-cryptocurrency-exchanges-cookies/)
 [^10]: [Checkpoint MosesStaff Nov 2021](https://research.checkpoint.com/2021/mosesstaff-targeting-israeli-companies/)
 [^11]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
 [^12]: [Symantec Bilbug 2022](https://www.security.com/threat-intelligence/espionage-asia-governments-cert-authority)
 [^13]: [Sygnia VelvetAnt 2024A](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
 [^14]: [DigiTrust NanoCore Jan 2017](https://www.digitrustgroup.com/nanocore-not-your-average-rat/)
 [^15]: [PaloAlto NanoCore Feb 2016](https://researchcenter.paloaltonetworks.com/2016/02/nanocorerat-behind-an-increase-in-tax-themed-phishing-e-mails/)
 [^16]: [Talos ZxShell Oct 2014](https://blogs.cisco.com/security/talos/opening-zxshell)
 [^17]: [Sandfly BPFDoor 2022](https://sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/)
 [^18]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^19]: [Kaspersky ShrinkLocker 2024](https://securelist.com/ransomware-abuses-bitlocker/112643/)
 [^20]: [Splunk ShrinkLocker 2024](https://www.splunk.com/en_us/blog/security/shrinklocker-malware-abusing-bitlocker-to-lock-your-data.html)
 [^21]: [ESET Grandoreiro April 2020](https://www.welivesecurity.com/2020/04/28/grandoreiro-how-engorged-can-exe-get/)
