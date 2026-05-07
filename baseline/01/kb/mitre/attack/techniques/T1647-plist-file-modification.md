---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1647
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/defense_impairment
    - attack/type/technique
    - platform/macos
mitre-attack: kb/mitre/attack/techniques/T1647-plist-file-modification
tactic:
    - Defense Impairment
platforms:
    - macOS
permissions required:
    - none
---

## Description

Adversaries may modify property list files (plist files) to enable other malicious activity, while also potentially evading and bypassing system defenses. macOS applications use plist files, such as the `info.plist` file, to store properties and configuration settings that inform the operating system how to handle the application at runtime. Plist files are structured metadata in key-value pairs formatted in XML based on Apple's Core Foundation DTD. Plist files can be saved in text or binary format.[^2]  <br><br>Adversaries can modify key-value pairs in plist files to influence system behaviors, such as hiding the execution of an application (i.e. [[kb/mitre/attack/techniques/T1564.003-hidden-window|Hidden Window]]) or running additional commands for persistence (ex: [[kb/mitre/attack/techniques/T1543.001-launch-agent|Launch Agent]]/[[kb/mitre/attack/techniques/T1543.004-launch-daemon|Launch Daemon]] or [[kb/mitre/attack/techniques/T1547.007-re-opened-applications|Re-opened Applications]]).<br><br>For example, adversaries can add a malicious application path to the `~/Library/Preferences/com.apple.dock.plist` file, which controls apps that appear in the Dock. Adversaries can also modify the `LSUIElement` key in an application’s `info.plist` file  to run the app in the background. Adversaries can also insert key-value pairs to insert environment variables, such as `LSEnvironment`, to enable persistence via [[kb/mitre/attack/techniques/T1574.006-dynamic-linker-hijacking|Dynamic Linker Hijacking]].[^3] [^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | In older versions, XCSSET uses the `plutil` command to modify the `LSUIElement`, `DFBundleDisplayName`, and `CFBundleIdentifier` keys in the `/Contents/Info.plist` file to change how XCSSET is visible on the system. In later versions, XCSSET leverages a third-party notarized `dockutil` tool to modify the `.plist` file responsible for presenting applications to the user in the Dock and LaunchPad to point to a malicious application.[^1] [^2]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | <br>Cuckoo Stealer can create and populate property list (plist) files to enable execution.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1013-application-developer-guidance\|M1013]] | Application Developer Guidance | Ensure applications are using Apple's developer guidance which enables hardened runtime.[^1]  |

 [^1]: [eset_osx_flashback](https://www.welivesecurity.com/wp-content/uploads/200x/white-papers/osx_flashback.pdf)
 [^2]: [fileinfo plist file description](https://fileinfo.com/extension/plist)
 [^3]: [wardle chp2 persistence](https://taomm.org/PDFs/vol1/CH%200x02%20Persistence.pdf)
 [^4]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^5]: [SentinelOne Cuckoo Stealer May 2024](https://www.sentinelone.com/blog/macos-cuckoo-stealer-ensuring-detection-and-defense-as-new-samples-rapidly-emerge/)
 [^6]: [Apple Developer Doco Hardened Runtime](https://developer.apple.com/documentation/security/hardened_runtime)
 [^7]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^8]: [Microsoft March 2025 XCSSET](https://www.microsoft.com/en-us/security/blog/2025/03/11/new-xcsset-malware-adds-new-obfuscation-persistence-techniques-to-infect-xcode-projects/)
