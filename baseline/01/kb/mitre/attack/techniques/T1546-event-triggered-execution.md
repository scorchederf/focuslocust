---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1546
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/iaas
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/saas
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1546-event-triggered-execution
tactic:
    - Persistence
    - Privilege Escalation
platforms:
    - Linux
    - macOS
    - Windows
    - SaaS
    - IaaS
    - Office Suite
permissions required:
    - none
---

## Description

Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.[^4] [^5] [^2] <br><br>Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.[^1] [^6] [^3] <br><br>Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges. 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET's `dfhsebxzod` module searches for `.xcodeproj` directories within the user’s home folder and subdirectories. For each match, it locates the corresponding `project.pbxproj` file and embeds an encoded payload into a build rule, target configuration, or project setting. The payload is later executed during the build process.[^1] [^2]  |
| [[kb/mitre/attack/software/S1091-pacu\|S1091]] | Pacu | [[kb/mitre/attack/software/S1091-pacu\|Pacu]] can set up S3 bucket notifications to trigger a malicious Lambda function when a CloudFormation template is uploaded to the bucket. It can also create Lambda functions that trigger upon the creation of users, roles, and groups.[^1]  |
| [S1164](https://attack.mitre.org/software/S1164) | UPSTYLE | UPSTYLE creates a `.pth` file beginning with the text `import` so that any time another process or script attempts to reference the modified item the malicious code will also run.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Manage the creation, modification, use, and permissions associated to privileged accounts, including SYSTEM and root. |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Perform regular software updates to mitigate exploitation risk. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1546.013-powershell-profile\|T1546.013]] | PowerShell Profile |
| [[kb/mitre/attack/techniques/T1546.006-lc-load-dylib-addition\|T1546.006]] | LC_LOAD_DYLIB Addition |
| [[kb/mitre/attack/techniques/T1546.011-application-shimming\|T1546.011]] | Application Shimming |
| [[kb/mitre/attack/techniques/T1546.005-trap\|T1546.005]] | Trap |
| [[kb/mitre/attack/techniques/T1546.012-image-file-execution-options-injection\|T1546.012]] | Image File Execution Options Injection |
| [[kb/mitre/attack/techniques/T1546.008-accessibility-features\|T1546.008]] | Accessibility Features |
| [[kb/mitre/attack/techniques/T1546.009-appcert-dlls\|T1546.009]] | AppCert DLLs |
| [[kb/mitre/attack/techniques/T1546.003-windows-management-instrumentation-event-subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription |
| [[kb/mitre/attack/techniques/T1546.001-change-default-file-association\|T1546.001]] | Change Default File Association |
| [[kb/mitre/attack/techniques/T1546.014-emond\|T1546.014]] | Emond |
| [[kb/mitre/attack/techniques/T1546.004-unix-shell-configuration-modification\|T1546.004]] | Unix Shell Configuration Modification |
| [[kb/mitre/attack/techniques/T1546.015-component-object-model-hijacking\|T1546.015]] | Component Object Model Hijacking |
| [[kb/mitre/attack/techniques/T1546.018-python-startup-hooks\|T1546.018]] | Python Startup Hooks |
| [[kb/mitre/attack/techniques/T1546.010-appinit-dlls\|T1546.010]] | AppInit DLLs |
| [[kb/mitre/attack/techniques/T1546.002-screensaver\|T1546.002]] | Screensaver |
| [[kb/mitre/attack/techniques/T1546.016-installer-packages\|T1546.016]] | Installer Packages |
| [[kb/mitre/attack/techniques/T1546.017-udev-rules\|T1546.017]] | Udev Rules |
| [[kb/mitre/attack/techniques/T1546.007-netsh-helper-dll\|T1546.007]] | Netsh Helper DLL |

 [^1]: [FireEye WMI 2015](https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/wp-windows-management-instrumentation.pdf)
 [^2]: [Microsoft DART Case Report 001](https://www.microsoft.com/security/blog/2020/03/09/real-life-cybercrime-stories-dart-microsoft-detection-and-response-team)
 [^3]: [amnesia malware](https://researchcenter.paloaltonetworks.com/2017/04/unit42-new-iotlinux-malware-targets-dvrs-forms-botnet/)
 [^4]: [Backdooring an AWS account](https://medium.com/daniel-grzelak/backdooring-an-aws-account-da007d36f8f9)
 [^5]: [Varonis Power Automate Data Exfiltration](https://www.varonis.com/blog/power-automate-data-exfiltration)
 [^6]: [Malware Persistence on OS X](https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf)
 [^7]: [GitHub Pacu](https://github.com/RhinoSecurityLabs/pacu)
 [^8]: [Volexity UPSTYLE 2024](https://www.volexity.com/blog/2024/04/12/zero-day-exploitation-of-unauthenticated-remote-code-execution-vulnerability-in-globalprotect-cve-2024-3400/)
 [^9]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
 [^10]: [April 2021 TrendMicro XCSSET](https://www.trendmicro.com/en_us/research/21/d/xcsset-quickly-adapts-to-macos-11-and-m1-based-macs.html)
