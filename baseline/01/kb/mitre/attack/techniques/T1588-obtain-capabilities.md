---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1588
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1588-obtain-capabilities
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may buy and/or steal capabilities that can be used during targeting. Rather than developing their own capabilities in-house, adversaries may purchase, freely download, or steal them. Activities may include the acquisition of malware, software (including licenses), exploits, certificates, and information relating to vulnerabilities. Adversaries may obtain capabilities to support their operations throughout numerous phases of the adversary lifecycle.<br><br>In addition to downloading free malware, software, and exploits from the internet, adversaries may purchase these capabilities from third-party entities. Third-party entities can include technology companies that specialize in malware and exploits, criminal marketplaces, or from individuals.[^7] [^1] <br><br>In addition to purchasing capabilities, adversaries may steal capabilities from third-party entities (including other adversaries). This can include stealing software licenses, malware, SSL/TLS and code-signing certificates, or raiding closed databases of vulnerabilities or exploits.[^3] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1588.007-artificial-intelligence\|T1588.007]] | Artificial Intelligence |
| [[kb/mitre/attack/techniques/T1588.004-digital-certificates\|T1588.004]] | Digital Certificates |
| [[kb/mitre/attack/techniques/T1588.006-vulnerabilities\|T1588.006]] | Vulnerabilities |
| [[kb/mitre/attack/techniques/T1588.001-malware\|T1588.001]] | Malware |
| [[kb/mitre/attack/techniques/T1588.002-tool\|T1588.002]] | Tool |
| [[kb/mitre/attack/techniques/T1588.003-code-signing-certificates\|T1588.003]] | Code Signing Certificates |
| [[kb/mitre/attack/techniques/T1588.005-exploits\|T1588.005]] | Exploits |

 [^1]: [PegasusCitizenLab](https://citizenlab.ca/2016/08/million-dollar-dissident-iphone-zero-day-nso-group-uae/)
 [^2]: [FireEyeSupplyChain](https://www.mandiant.com/resources/supply-chain-analysis-from-quartermaster-to-sunshop)
 [^3]: [DiginotarCompromise](https://threatpost.com/final-report-diginotar-hack-shows-total-compromise-ca-servers-103112/77170/)
 [^4]: [Recorded Future Beacon Certificates](https://www.recordedfuture.com/research/cobalt-strike-servers)
 [^5]: [Splunk Kovar Certificates 2017](https://www.splunk.com/en_us/blog/security/tall-tales-of-hunting-with-tls-ssl-certificates.html)
 [^6]: [Analyzing CS Dec 2020](https://www.randhome.io/blog/2020/12/20/analyzing-cobalt-strike-for-fun-and-profit/)
 [^7]: [NationsBuying](https://www.nytimes.com/2013/07/14/world/europe/nations-buying-as-hackers-sell-computer-flaws.html)
