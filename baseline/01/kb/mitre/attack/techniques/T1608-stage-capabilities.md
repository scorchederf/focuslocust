---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1608
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/resource_development
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1608-stage-capabilities
tactic:
    - Resource Development
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may upload, install, or otherwise set up capabilities that can be used during targeting. To support their operations, an adversary may need to take capabilities they developed ([[kb/mitre/attack/techniques/T1587-develop-capabilities|Develop Capabilities]]) or obtained ([[kb/mitre/attack/techniques/T1588-obtain-capabilities|Obtain Capabilities]]) and stage them on infrastructure under their control. These capabilities may be staged on infrastructure that was previously purchased/rented by the adversary ([[kb/mitre/attack/techniques/T1583-acquire-infrastructure|Acquire Infrastructure]]) or was otherwise compromised by them ([[kb/mitre/attack/techniques/T1584-compromise-infrastructure|Compromise Infrastructure]]). Capabilities may also be staged on web services, such as GitHub or Pastebin, or on Platform-as-a-Service (PaaS) offerings that enable users to easily provision applications.[^1] [^8] [^7] [^2] [^3] <br><br>Staging of capabilities can aid the adversary in a number of initial access and post-compromise behaviors, including (but not limited to):<br><br>* Staging web resources necessary to conduct [[kb/mitre/attack/techniques/T1189-drive-by-compromise|Drive-by Compromise]] when a user browses to a site.[^9] [^6] [^4] <br>* Staging web resources for a link target to be used with spearphishing.[^10] [^11] <br>* Uploading malware or tools to a location accessible to a victim network to enable [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer|Ingress Tool Transfer]].[^1] <br>* Installing a previously acquired SSL/TLS certificate to use to encrypt command and control traffic (ex: [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography|Asymmetric Cryptography]] with [[kb/mitre/attack/techniques/T1071.001-web-protocols|Web Protocols]]).[^5] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1608.004-drive-by-target\|T1608.004]] | Drive-by Target |
| [[kb/mitre/attack/techniques/T1608.001-upload-malware\|T1608.001]] | Upload Malware |
| [[kb/mitre/attack/techniques/T1608.002-upload-tool\|T1608.002]] | Upload Tool |
| [[kb/mitre/attack/techniques/T1608.005-link-target\|T1608.005]] | Link Target |
| [[kb/mitre/attack/techniques/T1608.003-install-digital-certificate\|T1608.003]] | Install Digital Certificate |
| [[kb/mitre/attack/techniques/T1608.006-seo-poisoning\|T1608.006]] | SEO Poisoning |

 [^1]: [Volexity Ocean Lotus November 2020](https://www.volexity.com/blog/2020/11/06/oceanlotus-extending-cyber-espionage-operations-through-fake-websites/)
 [^2]: [Netskope GCP Redirection](https://www.netskope.com/blog/targeted-attacks-abusing-google-cloud-platform-open-redirection)
 [^3]: [Netskope Cloud Phishing](https://www.netskope.com/blog/a-big-catch-cloud-phishing-from-google-app-engine-and-azure-app-service)
 [^4]: [ATT ScanBox](https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks)
 [^5]: [DigiCert Install SSL Cert](https://www.digicert.com/kb/ssl-certificate-installation.htm)
 [^6]: [Gallagher 2015](http://arstechnica.com/security/2015/08/newly-discovered-chinese-hacking-group-hacked-100-websites-to-use-as-watering-holes/)
 [^7]: [Malwarebytes Heroku Skimmers](https://www.malwarebytes.com/blog/news/2019/12/theres-an-app-for-that-web-skimmers-found-on-paas-heroku)
 [^8]: [Dragos Heroku Watering Hole](https://www.dragos.com/blog/industry-news/a-new-water-watering-hole/)
 [^9]: [FireEye CFR Watering Hole 2012](https://web.archive.org/web/20201024230407/https://www.fireeye.com/blog/threat-research/2012/12/council-foreign-relations-water-hole-attack-details.html)
 [^10]: [Malwarebytes Silent Librarian October 2020](https://blog.malwarebytes.com/malwarebytes-news/2020/10/silent-librarian-apt-phishing-attack/)
 [^11]: [Proofpoint TA407 September 2019](https://www.proofpoint.com/us/threat-insight/post/threat-actor-profile-ta407-silent-librarian)
