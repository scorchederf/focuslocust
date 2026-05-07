---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1048
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/exfiltration
    - attack/type/technique
    - platform/esxi
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol
tactic:
    - Exfiltration
platforms:
    - ESXi
    - IaaS
    - Linux
    - macOS
    - Network Devices
    - Office Suite
    - SaaS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server.  <br><br>Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. <br><br>[[kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol|Exfiltration Over Alternative Protocol]] can be done using various common operating system utilities such as [[kb/mitre/attack/software/S0039-net|Net]]/SMB or FTP.[^2]  On macOS and Linux `curl` may be used to invoke protocols such as HTTP/S or FTP/S to exfiltrate data from a system.[^3] <br><br>Many IaaS and SaaS platforms (such as Microsoft Exchange, Microsoft SharePoint, GitHub, and AWS S3) support the direct download of files, emails, source code, and other sensitive information via the web console or [[kb/mitre/attack/techniques/T1059.009-cloud-api|Cloud API]].

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq connects to a predefined domain on port 443 to exfil gathered information.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has used a .NET tool named dog.exe to exiltrate information over an e-mail account.[^1]  |
| [S0482](https://attack.mitre.org/software/S0482) | Bundlore | Bundlore uses the `curl -s -L -o` command to exfiltrate archived data to a URL.[^1]  |
| [S0503](https://attack.mitre.org/software/S0503) | FrameworkPOS | FrameworkPOS can use DNS tunneling for exfiltration of credit card data.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes has exfiltrated its collected data from the infected machine to the C2, sometimes using the MIME protocol.[^1]   |
| [S0641](https://attack.mitre.org/software/S0641) | Kobalos | Kobalos can exfiltrate credentials over the network via UDP.[^1]  |
| [[kb/mitre/attack/software/S0677-aadinternals\|S0677]] | AADInternals | [[kb/mitre/attack/software/S0677-aadinternals\|AADInternals]] can directly download cloud user data such as OneDrive files.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Configure user permissions groups and roles for access to cloud storage.[^3]  Implement strict Identity and Access Management (IAM) controls to prevent access to storage solutions except for the applications, users, and services that require access.[^1]  Ensure that temporary access tokens are issued rather than permanent credentials, especially when access is being granted to entities outside of the internal security boundary.[^2]  |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Use access control lists on cloud storage systems and objects.  |
| [[kb/mitre/attack/mitigations/M1030-network-segmentation\|M1030]] | Network Segmentation | Follow best practices for network firewall configurations to allow only necessary ports and traffic to enter and exit the network.[^1]  |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network intrusion detection and prevention systems that use network signatures to identify traffic for specific adversary command and control infrastructure and malware can be used to mitigate activity at the network level. |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Enforce proxies and use dedicated servers for services such as DNS and only allow those systems to communicate over respective ports/protocols, instead of all systems within a network. Cloud service providers support IP-based restrictions when accessing cloud resources. Consider using IP allowlisting along with user account management to ensure that data access is restricted not only to valid users but only from expected IP ranges to mitigate the use of stolen credentials to access data. |
| [[kb/mitre/attack/mitigations/M1057-data-loss-prevention\|M1057]] | Data Loss Prevention | Data loss prevention can detect and block sensitive data being uploaded via web browsers. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1048.001-exfiltration-over-symmetric-encrypted-non-c2-protocol\|T1048.001]] | Exfiltration Over Symmetric Encrypted Non-C2 Protocol |
| [[kb/mitre/attack/techniques/T1048.002-exfiltration-over-asymmetric-encrypted-non-c2-protocol\|T1048.002]] | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol |
| [[kb/mitre/attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol\|T1048.003]] | Exfiltration Over Unencrypted Non-C2 Protocol |

 [^1]: [University of Birmingham C2](https://arxiv.org/ftp/arxiv/papers/1408/1408.1136.pdf)
 [^2]: [Palo Alto OilRig Oct 2016](http://researchcenter.paloaltonetworks.com/2016/10/unit42-oilrig-malware-campaign-updates-toolset-and-expands-targets/)
 [^3]: [20 macOS Common Tools and Techniques](https://labs.sentinelone.com/20-common-tools-techniques-used-by-macos-threat-actors-malware/)
 [^4]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^5]: [TechNet Firewall Design](https://technet.microsoft.com/en-us/library/cc700828.aspx)
 [^6]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^7]: [SentinelOne FrameworkPOS September 2019](https://labs.sentinelone.com/fin6-frameworkpos-point-of-sale-malware-analysis-internals-2/)
 [^8]: [ESET Kobalos Jan 2021](https://www.welivesecurity.com/wp-content/uploads/2021/01/ESET_Kobalos.pdf)
 [^9]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^10]: [Amazon S3 Security, 2019](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/)
 [^11]: [Amazon  AWS Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
 [^12]: [Microsoft Azure Storage Security, 2019](https://docs.microsoft.com/en-us/azure/storage/common/storage-security-guide)
 [^13]: [AADInternals Documentation](https://o365blog.com/aadinternals)
