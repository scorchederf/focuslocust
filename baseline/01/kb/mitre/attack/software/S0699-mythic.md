---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0699
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0699-mythic
---

## Description

[[kb/mitre/attack/software/S0699-mythic|Mythic]] is an open source, cross-platform post-exploitation/command and control platform. [[kb/mitre/attack/software/S0699-mythic|Mythic]] is designed to "plug-n-play" with various agents and communication channels.[^2] [^3] [^4]  Deployed [[kb/mitre/attack/software/S0699-mythic|Mythic]] C2 servers have been observed as part of potentially malicious infrastructure.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1008-fallback-channels\|T1008]] | Fallback Channels | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] can use a list of C2 URLs as fallback mechanisms in case one IP or domain gets blocked.[^1] 	 |
| [[kb/mitre/attack/techniques/T1030-data-transfer-size-limits\|T1030]] | Data Transfer Size Limits | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports custom chunk sizes used to upload/download files.[^1] 	 |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports HTTP-based C2 profiles.[^1] 	 |
| [[kb/mitre/attack/techniques/T1071.002-file-transfer-protocols\|T1071.002]] | File Transfer Protocols | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports SMB-based peer-to-peer C2 profiles.[^1] 	 |
| [[kb/mitre/attack/techniques/T1071.004-dns\|T1071.004]] | DNS | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports DNS-based C2 profiles.[^1] 	 |
| [[kb/mitre/attack/techniques/T1090.001-internal-proxy\|T1090.001]] | Internal Proxy | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] can leverage a peer-to-peer C2 profile between agents.[^1] 		 |
| [[kb/mitre/attack/techniques/T1090.002-external-proxy\|T1090.002]] | External Proxy | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] can leverage a modified SOCKS5 proxy to tunnel egress C2 traffic.[^1]  |
| [[kb/mitre/attack/techniques/T1090.004-domain-fronting\|T1090.004]] | Domain Fronting | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports domain fronting via custom request headers.[^1] 	 |
| [[kb/mitre/attack/techniques/T1095-non-application-layer-protocol\|T1095]] | Non-Application Layer Protocol | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports WebSocket and TCP-based C2 profiles.[^1] 	 |
| [[kb/mitre/attack/techniques/T1119-automated-collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports scripting of file downloads from agents.[^1] 	 |
| [[kb/mitre/attack/techniques/T1132-data-encoding\|T1132]] | Data Encoding | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] provides various transform functions to encode and/or randomize C2 data.[^1] 	 |
| [[kb/mitre/attack/techniques/T1572-protocol-tunneling\|T1572]] | Protocol Tunneling | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] can use SOCKS proxies to tunnel traffic through another protocol.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0699-mythic\|Mythic]] supports SSL encrypted C2.[^1] 	 |

 [^1]: [RecordedFuture 2021 Ad Infra](https://go.recordedfuture.com/hubfs/reports/cta-2022-0118.pdf)
 [^2]: [Mythic Github](https://github.com/its-a-feature/Mythic)
 [^3]: [Mythic SpecterOps](https://posts.specterops.io/a-change-of-mythic-proportions-21debeb03617)
 [^4]: [Mythc Documentation](https://docs.mythic-c2.net/)
