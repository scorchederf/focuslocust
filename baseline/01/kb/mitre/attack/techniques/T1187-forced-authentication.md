---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1187
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/credential_access
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1187-forced-authentication
tactic:
    - Credential Access
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may gather credential material by invoking or forcing a user to automatically provide authentication information through a mechanism in which they can intercept.<br><br>The Server Message Block (SMB) protocol is commonly used in Windows networks for authentication and communication between systems for access to resources and file sharing. When a Windows system attempts to connect to an SMB resource it will automatically attempt to authenticate and send credential information for the current user to the remote system.[^9]  This behavior is typical in enterprise environments so that users do not need to enter credentials to access network resources.<br><br>Web Distributed Authoring and Versioning (WebDAV) is also typically used by Windows systems as a backup protocol when SMB is blocked or fails. WebDAV is an extension of HTTP and will typically operate over TCP ports 80 and 443.[^6] [^4] <br><br>Adversaries may take advantage of this behavior to gain access to user account hashes through forced SMB/WebDAV authentication. An adversary can send an attachment to a user through spearphishing that contains a resource link to an external server controlled by the adversary  (i.e. [[kb/mitre/attack/techniques/T1221-template-injection|Template Injection]]), or place a specially crafted file on navigation path for privileged accounts (e.g. .SCF file placed on desktop) or on a publicly accessible share to be accessed by victim(s). When the user's system accesses the untrusted resource, it will attempt authentication and send information, including the user's hashed credentials, over SMB to the adversary-controlled server.[^3]  With access to the credential hash, an adversary can perform off-line [[kb/mitre/attack/techniques/T1110-brute-force|Brute Force]] cracking to gain access to plaintext credentials.[^2] <br><br>There are several different ways this can occur.[^5]  Some specifics from in-the-wild use include:<br><br>* A spearphishing attachment containing a document with a resource that is automatically loaded when the document is opened (i.e. [[kb/mitre/attack/techniques/T1221-template-injection|Template Injection]]). The document can include, for example, a request similar to `file[:]//[remote address]/Normal.dotm` to trigger the SMB request.[^8] <br>* A modified .LNK or .SCF file with the icon filename pointing to an external reference such as `\\[remote address]\pic.png` that will force the system to load the resource when the icon is rendered to repeatedly gather credentials.[^8] <br><br>Alternatively, by leveraging the `EfsRpcOpenFileRaw` function, an adversary can send SMB requests to a remote system's MS-EFSRPC interface and force the victim computer to initiate an authentication procedure and share its authentication details. The Encrypting File System Remote Protocol (EFSRPC) is a protocol used in Windows networks for maintenance and management operations on encrypted data that is stored remotely to be accessed over a network. Utilization of `EfsRpcOpenFileRaw` function in EFSRPC is used to open an encrypted object on the server for backup or restore. Adversaries can collect this data and abuse it as part of a NTLM relay attack to gain access to remote systems on the same internal network.[^1] [^7] <br><br>

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0634](https://attack.mitre.org/software/S0634) | EnvyScout | EnvyScout can use protocol handlers to coax the operating system to send NTLMv2 authentication responses to attacker-controlled infrastructure.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1027-password-policies\|M1027]] | Password Policies | Use strong passwords to increase the difficulty of credential hashes from being cracked if they are obtained. |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | <br>Block SMB traffic from exiting an enterprise network with egress filtering or by blocking TCP ports 139, 445 and UDP port 137. Filter or block WebDAV protocol traffic from exiting the network. If access to external resources over SMB and WebDAV is necessary, then traffic should be tightly limited with allowlisting. [^1]  [^2]  |

 [^1]: [Rapid7](https://www.rapid7.com/blog/post/2021/08/03/petitpotam-novel-attack-chain-can-fully-compromise-windows-domains-running-ad-cs/)
 [^2]: [Cylance Redirect to SMB](https://www.cylance.com/content/dam/cylance/pdfs/white_papers/RedirectToSMB.pdf)
 [^3]: [GitHub Hashjacking](https://github.com/hob0/hashjacking)
 [^4]: [Microsoft Managing WebDAV Security](https://web.archive.org/web/20100210125749/https://www.microsoft.com/technet/prodtechnol/WindowsServer2003/Library/IIS/4beddb35-0cba-424c-8b9b-a5832ad8e208.mspx)
 [^5]: [Osanda Stealing NetNTLM Hashes](https://osandamalith.com/2017/03/24/places-of-interest-in-stealing-netntlm-hashes/)
 [^6]: [Didier Stevens WebDAV Traffic](https://blog.didierstevens.com/2017/11/13/webdav-traffic-to-malicious-sites/)
 [^7]: [GitHub](https://github.com/topotam/PetitPotam)
 [^8]: [US-CERT APT Energy Oct 2017](https://www.us-cert.gov/ncas/alerts/TA17-293A)
 [^9]: [Wikipedia Server Message Block](https://en.wikipedia.org/wiki/Server_Message_Block)
 [^10]: [US-CERT SMB Security](https://www.us-cert.gov/ncas/current-activity/2017/01/16/SMB-Security-Best-Practices)
 [^11]: [MSTIC Nobelium Toolset May 2021](https://www.microsoft.com/security/blog/2021/05/28/breaking-down-nobeliums-latest-early-stage-toolset/)
