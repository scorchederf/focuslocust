---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1137
tags:
    - attack/domain/enterprise_attack
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/type/technique
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1137-office-application-startup
tactic:
    - Persistence
platforms:
    - Windows
    - Office Suite
permissions required:
    - none
---

## Description

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.<br><br>A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.[^4]  These persistence mechanisms can work within Outlook or be used through Office 365.[^2] 

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to prevent Office applications from creating child processes and from writing potentially malicious executable content to disk. [^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Follow Office macro security best practices suitable for your environment. Disable Office VBA macros from executing.<br><br>Disable Office add-ins. If they are required, follow best practices for securing them by requiring them to be signed and disabling user notification for allowing add-ins. For some add-ins types (WLL, VBA) additional mitigation is likely required as disabling add-ins in the Office Trust Center does not disable WLL nor does it prevent VBA code from executing. [^1]  |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | For the Outlook methods, blocking macros may be ineffective as the Visual Basic engine used for these features is separate from the macro scripting engine.[^1]  Microsoft has released patches to try to address each issue. Ensure KB3191938 which blocks Outlook Visual Basic and displays a malicious code warning, KB4011091 which disables custom forms by default, and KB4011162 which removes the legacy Home Page feature, are applied to systems.[^2]  |
| [[kb/mitre/attack/mitigations/M1054-software-configuration\|M1054]] | Software Configuration | For the Office Test method, create the Registry key used to execute it and set the permissions to "Read Control" to prevent easy access to the key without administrator permissions or requiring Privilege Escalation. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1137.006-add-ins\|T1137.006]] | Add-ins |
| [[kb/mitre/attack/techniques/T1137.005-outlook-rules\|T1137.005]] | Outlook Rules |
| [[kb/mitre/attack/techniques/T1137.001-office-template-macros\|T1137.001]] | Office Template Macros |
| [[kb/mitre/attack/techniques/T1137.003-outlook-forms\|T1137.003]] | Outlook Forms |
| [[kb/mitre/attack/techniques/T1137.004-outlook-home-page\|T1137.004]] | Outlook Home Page |
| [[kb/mitre/attack/techniques/T1137.002-office-test\|T1137.002]] | Office Test |

 [^1]: [Microsoft Detect Outlook Forms](https://docs.microsoft.com/en-us/office365/securitycompliance/detect-and-remediate-outlook-rules-forms-attack)
 [^2]: [TechNet O365 Outlook Rules](https://blogs.technet.microsoft.com/office365security/defending-against-rules-and-forms-injection/)
 [^3]: [CrowdStrike Outlook Forms](https://malware.news/t/using-outlook-forms-for-lateral-movement-and-persistence/13746)
 [^4]: [SensePost Ruler GitHub](https://github.com/sensepost/ruler)
 [^5]: [SensePost NotRuler](https://github.com/sensepost/notruler)
 [^6]: [Outlook Today Home Page](https://medium.com/@bwtech789/outlook-today-homepage-persistence-33ea9b505943)
 [^7]: [MRWLabs Office Persistence Add-ins](https://web.archive.org/web/20190526112859/https://labs.mwrinfosecurity.com/blog/add-in-opportunities-for-office-persistence/)
 [^8]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^9]: [SensePost Outlook Forms](https://sensepost.com/blog/2017/outlook-forms-and-shells/)
 [^10]: [SensePost Outlook Home Page](https://sensepost.com/blog/2017/outlook-home-page-another-ruler-vector/)
 [^11]: [Palo Alto Office Test Sofacy](https://researchcenter.paloaltonetworks.com/2016/07/unit42-technical-walkthrough-office-test-persistence-method-used-in-recent-sofacy-attacks/)
