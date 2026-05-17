---
parsed_by: focuslocust
source: mitre
type: generated
---
# Hidden Window

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hidden Window](../../attack/techniques/T1564.003-hidden-window.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.003 |
| name | Hidden Window |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/003 |

## Preserved Source Material

```yaml
created: '2020-03-13T20:26:49.433Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use hidden windows to conceal malicious activity from the plain sight of users. In some cases,\
  \ windows that would typically be displayed when an application carries out an operation can be hidden. This may be utilized\
  \ by system administrators to avoid disrupting user work environments when carrying out administrative tasks. \n\nAdversaries\
  \ may abuse these functionalities to hide otherwise visible windows from users so as not to alert the user to adversary\
  \ activity on the system.(Citation: Antiquated Mac Malware)\n\nOn macOS, the configurations for how applications run are\
  \ listed in property list (plist) files. One of the tags in these files can be <code>apple.awt.UIElement</code>, which allows\
  \ for Java applications to prevent the application's icon from appearing in the Dock. A common use for this is when applications\
  \ run in the system tray, but don't also want to show up in the Dock.\n\nSimilarly, on Windows there are a variety of features\
  \ in scripting languages, such as [PowerShell](https://attack.mitre.org/techniques/T1059/001), Jscript, and [Visual Basic](https://attack.mitre.org/techniques/T1059/005)\
  \ to make windows hidden. One example of this is <code>powershell.exe -WindowStyle Hidden</code>.(Citation: PowerShell About\
  \ 2019)\n\nThe Windows Registry can also be edited to hide application windows from the current user. For example, by setting\
  \ the `WindowPosition` subkey in the `HKEY_CURRENT_USER\\Console\\%SystemRoot%_System32_WindowsPowerShell_v1.0_PowerShell.exe`\
  \ Registry key to a maximum value, PowerShell windows will open off screen and be hidden.(Citation: Cantoris Computing)\n\
  \nIn addition, Windows supports the `CreateDesktop()` API that can create a hidden desktop window with its own corresponding\
  \ <code>explorer.exe</code> process.(Citation: Hidden VNC)(Citation: Anatomy of an hVNC Attack)  All applications running\
  \ on the hidden desktop window, such as a hidden VNC (hVNC) session,(Citation: Hidden VNC) will be invisible to other desktops\
  \ windows.\n\nAdversaries may also leverage cmd.exe(Citation: Cybereason - Hidden Malicious Remote Access) as a parent process,\
  \ and then utilize a LOLBin, such as DeviceCredentialDeployment.exe,(Citation: LOLBAS Project GitHub Device Cred Dep)(Citation:\
  \ SecureList BlueNoroff Device Cred Dev) to hide windows."
external_references:
- external_id: T1564.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/003
- description: Cantoris. (2016, July 22). PowerShell Malware. Retrieved December 12, 2024.
  source_name: Cantoris Computing
  url: https://cantoriscomputing.wordpress.com/2016/07/22/powershell-malware/
- description: 'Cybereason Security Services Team. (n.d.). Behind Closed Doors: The Rise of Hidden Malicious Remote Access.
    Retrieved July 22, 2025.'
  source_name: Cybereason - Hidden Malicious Remote Access
  url: https://www.cybereason.com/blog/behind-closed-doors-the-rise-of-hidden-malicious-remote-access
- description: Elliot Killick. (n.d.). /DeviceCredentialDeployment.exe. Retrieved July 22, 2025.
  source_name: LOLBAS Project GitHub Device Cred Dep
  url: https://lolbas-project.github.io/lolbas/Binaries/DeviceCredentialDeployment/
- description: Hutchins, Marcus. (2015, September 13). Hidden VNC for Beginners. Retrieved November 28, 2023.
  source_name: Hidden VNC
  url: https://www.malwaretech.com/2015/09/hidden-vnc-for-beginners.html
- description: Keshet, Lior. Kessem, Limor. (2017, January 25). Anatomy of an hVNC Attack. Retrieved November 28, 2023.
  source_name: Anatomy of an hVNC Attack
  url: https://securityintelligence.com/anatomy-of-an-hvnc-attack/
- description: Seongsu Park. (2022, December 27). BlueNoroff introduces new methods bypassing MoTW. Retrieved July 22, 2025.
  source_name: SecureList BlueNoroff Device Cred Dev
  url: https://securelist.com/bluenoroff-methods-bypass-motw/108383/
- description: Thomas Reed. (2017, January 18). New Mac backdoor using antiquated code. Retrieved July 5, 2017.
  source_name: Antiquated Mac Malware
  url: https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/
- description: Wheeler, S. et al.. (2019, May 1). About PowerShell.exe. Retrieved October 11, 2019.
  source_name: PowerShell About 2019
  url: https://docs.microsoft.com/en-us/powershell/module/Microsoft.PowerShell.Core/About/about_PowerShell_exe?view=powershell-5.1
id: attack-pattern--cbb66055-0325-4111-aca0-40547b6ad5b0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:23:51.965Z'
name: Hidden Window
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Liran Ravich, CardinalOps
- Mark Tsipershtein
- Travis Smith, Tripwire
- Vijay Lalwani
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
