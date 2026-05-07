---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0633
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0633-sliver
---

## Description

[[kb/mitre/attack/software/S0633-sliver|Sliver]] is an open source, cross-platform, red team command and control (C2) framework written in Golang. [[kb/mitre/attack/software/S0633-sliver|Sliver]] includes its own package manager, "armory," for staging and downloading additional tools and payloads to the primary C2 framework.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1001.002-steganography\|T1001.002]] | Steganography | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can encode binary data into a .PNG file for C2 communication.[^1]  |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has a built-in `procdump` command allowing for retrieval of memory from processes such as `lsass.exe` for credential harvesting.[^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has the ability to gather network configuration information.[^1]  |
| [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] obfuscates configuration and other static files using native Go libraries such as `garble` and `gobfuscate` to inhibit configuration analysis and static detection.[^1]  |
| [[kb/mitre/attack/techniques/T1027.004-compile-after-delivery\|T1027.004]] | Compile After Delivery | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] includes functionality to retrieve source code and compile locally prior to execution in victim environments.[^1]  |
| [[kb/mitre/attack/techniques/T1027.013-encrypted-encoded-file\|T1027.013]] | Encrypted/Encoded File | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can encrypt strings at compile time.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can exfiltrate files from the victim using the `download` command.[^1]  |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can collect network connection information.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.[^4] [^2] [^3] [^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has built-in functionality to launch a Powershell command prompt.[^1]  |
| [[kb/mitre/attack/techniques/T1071-application-layer-protocol\|T1071]] | Application Layer Protocol | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can utilize the Wireguard VPN protocol for command and control.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols |  [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has the ability to support C2 communications over HTTP and HTTPS.[^5] [^3] [^1] [^2] [^4]  |
| [[kb/mitre/attack/techniques/T1071.004-dns\|T1071.004]] | DNS | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can support C2 communications over DNS.[^5] [^3] [^1] [^2] [^4]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can enumerate files on a target system.[^1]  |
| [[kb/mitre/attack/techniques/T1090.001-internal-proxy\|T1090.001]] | Internal Proxy | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has a built-in SOCKS5 proxying capability allowing for [[kb/mitre/attack/software/S0633-sliver\|Sliver]] clients to proxy network traffic through other clients within a victim network.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can download additional content and files from the [[kb/mitre/attack/software/S0633-sliver\|Sliver]] server to the client residing on the victim machine using the `upload` command.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can take screenshots of the victim’s active display.[^1]  |
| [[kb/mitre/attack/techniques/T1132.001-standard-encoding\|T1132.001]] | Standard Encoding | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can use standard encoding techniques like gzip and hex to ASCII to encode the C2 communication payload.[^1]  |
| [[kb/mitre/attack/techniques/T1134-access-token-manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] has the ability to manipulate user tokens on targeted Windows systems.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can leverage multiple techniques to bypass User Account Control (UAC) on Windows systems.[^1]  |
| [[kb/mitre/attack/techniques/T1558.001-golden-ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] incorporates the [[kb/mitre/attack/software/S1071-rubeus\|Rubeus]] framework to allow for Kerberos ticket manipulation, specifically for forging Kerberos Golden Tickets.[^1]  |
| [[kb/mitre/attack/techniques/T1573.001-symmetric-cryptography\|T1573.001]] | Symmetric Cryptography | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can use AES-GCM-256 to encrypt a session key for C2 message exchange.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can use mutual TLS and RSA  cryptography to exchange a session key.[^5] [^3] [^1] [^2] [^4]  |

 [^1]: [Cybereason Sliver Undated](https://www.cybereason.com/blog/sliver-c2-leveraged-by-many-threat-actors)
 [^2]: [Bishop Fox Sliver Framework August 2019](https://labs.bishopfox.com/tech-blog/sliver)
 [^3]: [Microsoft Sliver 2022](https://www.microsoft.com/en-us/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/)
 [^4]: [GitHub Sliver C2](https://github.com/BishopFox/sliver/)
 [^5]: [GitHub Sliver File System August 2021](https://github.com/BishopFox/sliver/tree/master/client/command/filesystem)
 [^6]: [GitHub Sliver HTTP](https://github.com/BishopFox/sliver/wiki/HTTP(S)-C2)
 [^7]: [GitHub Sliver C2 DNS](https://github.com/BishopFox/sliver/wiki/DNS-C2)
 [^8]: [Cybersecurity Advisory SVR TTP May 2021](https://www.ncsc.gov.uk/files/Advisory-further-TTPs-associated-with-SVR-cyber-actors.pdf)
 [^9]: [GitHub Sliver Encryption](https://github.com/BishopFox/sliver/wiki/Transport-Encryption)
 [^10]: [GitHub Sliver Ifconfig](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/network/ifconfig.go)
 [^11]: [GitHub Sliver Screen](https://github.com/BishopFox/sliver/blob/master/implant/sliver/screen/screenshot_windows.go)
 [^12]: [GitHub Sliver Upload](https://github.com/BishopFox/sliver/blob/ea329226636ab8e470086a17f13aa8d330baad22/client/command/filesystem/upload.go)
 [^13]: [GitHub Sliver Download](https://github.com/BishopFox/sliver/blob/7489c69962b52b09ed377d73d142266564845297/client/command/filesystem/download.go)
 [^14]: [GitHub Sliver Netstat](https://github.com/BishopFox/sliver/tree/58a56a077f0813bb312f9fa4df7453b510c3a73b/implant/sliver/netstat)
