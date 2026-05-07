---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1596
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/reconnaissance
    - attack/type/technique
    - platform/pre
mitre-attack: kb/mitre/attack/techniques/T1596-search-open-technical-databases
tactic:
    - Reconnaissance
platforms:
    - PRE
permissions required:
    - none
---

## Description

Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans.[^4] [^2] [^1] [^3] [^6] [^7] [^5] <br><br>Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[kb/mitre/attack/techniques/T1598-phishing-for-information|Phishing for Information]] or [[kb/mitre/attack/techniques/T1593-search-open-websites-domains|Search Open Websites/Domains]]), establishing operational resources (ex: [[kb/mitre/attack/techniques/T1583-acquire-infrastructure|Acquire Infrastructure]] or [[kb/mitre/attack/techniques/T1584-compromise-infrastructure|Compromise Infrastructure]]), and/or initial access (ex: [[kb/mitre/attack/techniques/T1133-external-remote-services|External Remote Services]] or [[kb/mitre/attack/techniques/T1199-trusted-relationship|Trusted Relationship]]).

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1056-pre-compromise\|M1056]] | Pre-compromise | This technique cannot be easily mitigated with preventive controls since it is based on behaviors performed outside of the scope of enterprise defenses and controls. Efforts should focus on minimizing the amount and sensitivity of data available to external parties. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1596.003-digital-certificates\|T1596.003]] | Digital Certificates |
| [[kb/mitre/attack/techniques/T1596.002-whois\|T1596.002]] | WHOIS |
| [[kb/mitre/attack/techniques/T1596.001-dns-passive-dns\|T1596.001]] | DNS／Passive DNS |
| [[kb/mitre/attack/techniques/T1596.004-cdns\|T1596.004]] | CDNs |
| [[kb/mitre/attack/techniques/T1596.005-scan-databases\|T1596.005]] | Scan Databases |

 [^1]: [Circl Passive DNS](https://www.circl.lu/services/passive-dns/)
 [^2]: [DNS Dumpster](https://dnsdumpster.com/)
 [^3]: [Medium SSL Cert](https://medium.com/@menakajain/export-download-ssl-certificate-from-server-site-url-bcfc41ea46a2)
 [^4]: [WHOIS](https://who.is/)
 [^5]: [Shodan](https://shodan.io)
 [^6]: [SSLShopper Lookup](https://www.sslshopper.com/ssl-checker.html)
 [^7]: [DigitalShadows CDN](https://www.digitalshadows.com/blog-and-research/content-delivery-networks-cdns-can-leave-you-exposed-how-you-might-be-affected-and-what-you-can-do-about-it/)
