---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1583
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1583-acquire-infrastructure
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting. A wide variety of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or cloud servers, domains, and third-party web services.[^6]  Some infrastructure providers offer free trial periods, enabling infrastructure acquisition at limited to no cost.[^4]  Additionally, botnets are available for rent or purchase.<br><br>Use of these infrastructure solutions allows adversaries to stage, launch, and execute operations. Solutions may help adversary operations blend in with traffic that is seen as normal, such as contacting third-party web services or acquiring infrastructure to support [[kb/mitre/attack/techniques/T1090-proxy|Proxy]], including from residential proxy services.[^1] [^3] [^2]  Depending on the implementation, adversaries may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can be rapidly provisioned, modified, and shut down.

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1583.007-serverless\|T1583.007]] | Serverless |
| [[kb/mitre/attack/techniques/T1583.008-malvertising\|T1583.008]] | Malvertising |
| [[kb/mitre/attack/techniques/T1583.002-dns-server\|T1583.002]] | DNS Server |
| [[kb/mitre/attack/techniques/T1583.005-botnet\|T1583.005]] | Botnet |
| [[kb/mitre/attack/techniques/T1583.001-domains\|T1583.001]] | Domains |
| [[kb/mitre/attack/techniques/T1583.004-server\|T1583.004]] | Server |
| [[kb/mitre/attack/techniques/T1583.003-virtual-private-server\|T1583.003]] | Virtual Private Server |
| [[kb/mitre/attack/techniques/T1583.006-web-services\|T1583.006]] | Web Services |

 [^1]: [amnesty_nso_pegasus](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
 [^2]: [Mandiant APT29 Microsoft 365 2022](https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft)
 [^3]: [FBI Proxies Credential Stuffing](https://www.ic3.gov/Media/News/2022/220818.pdf)
 [^4]: [Free Trial PurpleUrchin](https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/)
 [^5]: [Koczwara Beacon Hunting Sep 2021](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)
 [^6]: [TrendmicroHideoutsLease](https://documents.trendmicro.com/assets/wp/wp-criminal-hideouts-for-lease.pdf)
 [^7]: [Mandiant SCANdalous Jul 2020](https://cloud.google.com/blog/topics/threat-intelligence/scandalous-external-detection-using-network-scan-data-and-automation/)
 [^8]: [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
