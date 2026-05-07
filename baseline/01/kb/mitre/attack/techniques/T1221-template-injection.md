---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1221
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1221-template-injection
tactic:
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may create or modify references in user document templates to conceal malicious code or force authentication attempts. For example, Microsoft’s Office Open XML (OOXML) specification defines an XML-based format for Office documents (.docx, xlsx, .pptx) to replace older binary formats (.doc, .xls, .ppt). OOXML files are packed together ZIP archives compromised of various XML files, referred to as parts, containing properties that collectively define how a document is rendered.[^5] <br><br>Properties within parts may reference shared public resources accessed via online URLs. For example, template properties may reference a file, serving as a pre-formatted document blueprint, that is fetched when the document is loaded.<br><br>Adversaries may abuse these templates to initially conceal malicious code to be executed via user documents. Template references injected into a document may enable malicious payloads to be fetched and executed when the document is loaded.[^9]  These documents can be delivered via other techniques such as [[kb/mitre/attack/techniques/T1566-phishing|Phishing]] and/or [[kb/mitre/attack/techniques/T1080-taint-shared-content|Taint Shared Content]] and may evade static detections since no typical indicators (VBA macro, script, etc.) are present until after the malicious payload is fetched.[^3]  Examples have been seen in the wild where template injection was used to load malicious code containing an exploit.[^8] <br><br>Adversaries may also modify the `*\template` control word within an .rtf file to similarly conceal then download malicious code. This legitimate control word value is intended to be a file destination of a template file resource that is retrieved and loaded when an .rtf file is opened. However, adversaries may alter the bytes of an existing .rtf file to insert a template control word field to include a URL resource of a malicious payload.[^7] [^6] <br><br>This technique may also enable [[kb/mitre/attack/techniques/T1187-forced-authentication|Forced Authentication]] by injecting a SMB/HTTPS (or other credential prompting) URL and triggering an authentication attempt.[^4] [^1] [^2] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes changed the template target of the settings.xml file embedded in the Word document and populated that field with the downloaded URL of the next payload.[^1]   |
| [S0670](https://attack.mitre.org/software/S0670) | WarzoneRAT | WarzoneRAT has been install via template injection through a malicious DLL embedded within a template RTF in a Word document.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1017-user-training\|M1017]] | User Training | Train users to identify social engineering techniques and spearphishing emails that could be used to deliver malicious documents. |
| [[kb/mitre/attack/mitigations/M1031-network-intrusion-prevention\|M1031]] | Network Intrusion Prevention | Network/Host intrusion prevention systems, antivirus, and detonation chambers can be employed to prevent documents from fetching and/or executing malicious payloads.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Consider disabling Microsoft Office macros/active content to prevent the execution of malicious payloads in documents [^1] , though this setting may not mitigate the [[kb/mitre/attack/techniques/T1187-forced-authentication\|Forced Authentication]] use for this technique. |
| [[kb/mitre/attack/mitigations/M1049-antivirus-antimalware\|M1049]] | Antivirus/Antimalware | Network/Host intrusion prevention systems, antivirus, and detonation chambers can be employed to prevent documents from fetching and/or executing malicious payloads.[^1]  |

 [^1]: [Talos Template Injection July 2017](https://blog.talosintelligence.com/2017/07/template-injection.html)
 [^2]: [ryhanson phishery SEPT 2016](https://github.com/ryhanson/phishery)
 [^3]: [Redxorblue Remote Template Injection](http://blog.redxorblue.com/2018/07/executing-macros-from-docx-with-remote.html)
 [^4]: [Anomali Template Injection MAR 2018](https://forum.anomali.com/t/credential-harvesting-and-malicious-file-delivery-using-microsoft-office-template-injection/2104)
 [^5]: [Microsoft Open XML July 2017](https://docs.microsoft.com/previous-versions/office/developer/office-2007/aa338205(v=office.12))
 [^6]: [Ciberseguridad Decoding malicious RTF files](https://ciberseguridad.blog/decodificando-ficheros-rtf-maliciosos/)
 [^7]: [Proofpoint RTF Injection](https://www.proofpoint.com/us/blog/threat-insight/injection-new-black-novel-rtf-template-inject-technique-poised-widespread)
 [^8]: [MalwareBytes Template Injection OCT 2017](https://blog.malwarebytes.com/threat-analysis/2017/10/decoy-microsoft-word-document-delivers-malware-through-rat/)
 [^9]: [SANS Brian Wiltse Template Injection](https://www.sans.org/reading-room/whitepapers/testing/template-injection-attacks-bypassing-security-controls-living-land-38780)
 [^10]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^11]: [Microsoft Disable Macros](https://support.office.com/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6)
 [^12]: [Uptycs Confucius APT Jan 2021](https://www.uptycs.com/blog/confucius-apt-deploys-warzone-rat)
