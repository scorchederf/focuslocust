---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1584
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1584-compromise-infrastructure
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may compromise third-party infrastructure that can be used during targeting. Infrastructure solutions include physical or cloud servers, domains, network devices, and third-party web and DNS services. Instead of buying, leasing, or renting infrastructure an adversary may compromise infrastructure and use it during other phases of the adversary lifecycle.[^7] [^4] [^8] [^12]  Additionally, adversaries may compromise numerous machines to form a botnet they can leverage.<br><br>Use of compromised infrastructure allows adversaries to stage, launch, and execute operations. Compromised infrastructure can help adversary operations blend in with traffic that is seen as normal, such as contact with high reputation or trusted sites. For example, adversaries may leverage compromised infrastructure (potentially also in conjunction with [[kb/mitre/attack/techniques/T1588.004-digital-certificates|Digital Certificates]]) to further blend in and support staged information gathering and/or [[kb/mitre/attack/techniques/T1566-phishing|Phishing]] campaigns.[^3]  Adversaries may also compromise numerous machines to support [[kb/mitre/attack/techniques/T1090-proxy|Proxy]] and/or proxyware services or to form a botnet.[^1] [^2]  Additionally, adversaries may compromise infrastructure residing in close proximity to a target in order to gain [[kb/mitre/attack/tactics/TA0001-initial-access|Initial Access]] via [[kb/mitre/attack/techniques/T1669-wi-fi-networks|Wi-Fi Networks]].[^6] <br><br>By using compromised infrastructure, adversaries may enable follow-on malicious operations. Prior to targeting, adversaries may also compromise the infrastructure of other adversaries.[^9] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1584.008-network-devices\|T1584.008]] | Network Devices |
| [[kb/mitre/attack/techniques/T1584.003-virtual-private-server\|T1584.003]] | Virtual Private Server |
| [[kb/mitre/attack/techniques/T1584.005-botnet\|T1584.005]] | Botnet |
| [[kb/mitre/attack/techniques/T1584.006-web-services\|T1584.006]] | Web Services |
| [[kb/mitre/attack/techniques/T1584.002-dns-server\|T1584.002]] | DNS Server |
| [[kb/mitre/attack/techniques/T1584.007-serverless\|T1584.007]] | Serverless |
| [[kb/mitre/attack/techniques/T1584.004-server\|T1584.004]] | Server |
| [[kb/mitre/attack/techniques/T1584.001-domains\|T1584.001]] | Domains |

 [^1]: [amnesty_nso_pegasus](https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/)
 [^2]: [Sysdig Proxyjacking](https://sysdig.com/blog/proxyjacking-attackers-log4j-exploited/)
 [^3]: [FireEye DNS Hijack 2019](https://www.fireeye.com/blog/threat-research/2019/01/global-dns-hijacking-campaign-dns-record-manipulation-at-scale.html)
 [^4]: [ICANNDomainNameHijacking](https://www.icann.org/en/ssac/registration-services/documents/sac-007-domain-name-hijacking-incidents-threats-risks-and-remediation-12-07-2005-en)
 [^5]: [Koczwara Beacon Hunting Sep 2021](https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2)
 [^6]: [Nearest Neighbor Volexity](https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/)
 [^7]: [Mandiant APT1](https://www.fireeye.com/content/dam/fireeye-www/services/pdfs/mandiant-apt1-report.pdf)
 [^8]: [Talos DNSpionage Nov 2018](https://blog.talosintelligence.com/2018/11/dnspionage-campaign-targets-middle-east.html)
 [^9]: [NSA NCSC Turla OilRig](https://media.defense.gov/2019/Oct/18/2002197242/-1/-1/0/NSA_CSA_Turla_20191021%20ver%204%20-%20nsa.gov.pdf)
 [^10]: [Mandiant SCANdalous Jul 2020](https://cloud.google.com/blog/topics/threat-intelligence/scandalous-external-detection-using-network-scan-data-and-automation/)
 [^11]: [ThreatConnect Infrastructure Dec 2020](https://threatconnect.com/blog/infrastructure-research-hunting/)
 [^12]: [FireEye EPS Awakens Part 2](https://web.archive.org/web/20151226205946/https://www.fireeye.com/blog/threat-research/2015/12/the-eps-awakens-part-two.html)
