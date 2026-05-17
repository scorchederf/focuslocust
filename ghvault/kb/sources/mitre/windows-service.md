---
parsed_by: focuslocust
source: mitre
type: generated
---
# Windows Service

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1543.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows Service](../../attack/techniques/T1543.003-windows-service.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1543.003 |
| name | Windows Service |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1543/003 |

## Preserved Source Material

```yaml
created: '2020-01-17T19:13:50.402Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persistence.\
  \ When Windows boots up, it starts programs or applications called services that perform background system functions.(Citation:\
  \ TechNet Services) Windows service configuration information, including the file path to the service's executable or recovery\
  \ programs/commands, is stored in the Windows Registry.\n\nAdversaries may install a new service or modify an existing service\
  \ to execute at startup in order to persist on a system. Service configurations can be set or modified using system utilities\
  \ (such as sc.exe), by directly modifying the Registry, or by interacting directly with the Windows API. \n\nAdversaries\
  \ may also use services to install and execute malicious drivers. For example, after dropping a driver file (ex: `.sys`)\
  \ to disk, the payload can be loaded and registered via [Native API](https://attack.mitre.org/techniques/T1106) functions\
  \ such as `CreateServiceW()` (or manually via functions such as `ZwLoadDriver()` and `ZwSetValueKey()`), by creating the\
  \ required service Registry values (i.e. [Modify Registry](https://attack.mitre.org/techniques/T1112)), or by using command-line\
  \ utilities such as `PnPUtil.exe`.(Citation: Symantec W.32 Stuxnet Dossier)(Citation: Crowdstrike DriveSlayer February 2022)(Citation:\
  \ Unit42 AcidBox June 2020) Adversaries may leverage these drivers as [Rootkit](https://attack.mitre.org/techniques/T1014)s\
  \ to hide the presence of malicious activity on a system. Adversaries may also load a signed yet vulnerable driver onto\
  \ a compromised machine (known as \"Bring Your Own Vulnerable Driver\" (BYOVD)) as part of [Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068).(Citation:\
  \ ESET InvisiMole June 2020)(Citation: Unit42 AcidBox June 2020)\n\nServices may be created with administrator privileges\
  \ but are executed under SYSTEM privileges, so an adversary may also use a service to escalate privileges. Adversaries may\
  \ also directly start services through [Service Execution](https://attack.mitre.org/techniques/T1569/002).\n\nTo make detection\
  \ analysis more challenging, malicious services may also incorporate [Masquerade Task or Service](https://attack.mitre.org/techniques/T1036/004)\
  \ (ex: using a service and/or payload name related to a legitimate OS or benign software component). Adversaries may also\
  \ create ‘hidden’ services (i.e., [Hide Artifacts](https://attack.mitre.org/techniques/T1564)), for example by using the\
  \ `sc sdset` command to set service permissions via the Service Descriptor Definition Language (SDDL). This may hide a Windows\
  \ service from the view of standard service enumeration methods such as `Get-Service`, `sc query`, and `services.exe`.(Citation:\
  \ SANS 1)(Citation: SANS 2)"
external_references:
- external_id: T1543.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1543/003
- description: Hardy, T. & Hall, J. (2018, February 15). Use Windows Event Forwarding to help with intrusion detection. Retrieved
    August 7, 2018.
  source_name: Microsoft Windows Event Forwarding FEB 2018
  url: https://docs.microsoft.com/windows/security/threat-protection/use-windows-event-forwarding-to-assist-in-intrusion-detection
- description: 'Hromcova, Z. and Cherpanov, A. (2020, June). INVISIMOLE: THE HIDDEN PART OF THE STORY. Retrieved July 16,
    2020.'
  source_name: ESET InvisiMole June 2020
  url: https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf
- description: Joshua Wright. (2020, October 13). Retrieved March 22, 2024.
  source_name: SANS 1
  url: https://www.sans.org/blog/red-team-tactics-hiding-windows-services/
- description: Joshua Wright. (2020, October 14). Retrieved March 22, 2024.
  source_name: SANS 2
  url: https://www.sans.org/blog/defense-spotlight-finding-hidden-windows-services/
- description: Microsoft. (n.d.). Services. Retrieved June 7, 2016.
  source_name: TechNet Services
  url: https://technet.microsoft.com/en-us/library/cc772408.aspx
- description: 'Miroshnikov, A. & Hall, J. (2017, April 18). 4697(S): A service was installed in the system. Retrieved August
    7, 2018.'
  source_name: Microsoft 4697 APR 2017
  url: https://docs.microsoft.com/windows/security/threat-protection/auditing/event-4697
- description: Nicolas Falliere, Liam O. Murchu, Eric Chien. (2011, February). W32.Stuxnet Dossier. Retrieved December 7,
    2020.
  source_name: Symantec W.32 Stuxnet Dossier
  url: https://www.wired.com/images_blogs/threatlevel/2010/11/w32_stuxnet_dossier.pdf
- description: 'Reichel, D. and Idrizovic, E. (2020, June 17). AcidBox: Rare Malware Repurposing Turla Group Exploit Targeted
    Russian Organizations. Retrieved March 16, 2021.'
  source_name: Unit42 AcidBox June 2020
  url: https://unit42.paloaltonetworks.com/acidbox-rare-malware/
- description: Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.
  source_name: TechNet Autoruns
  url: https://technet.microsoft.com/en-us/sysinternals/bb963902
- description: Thomas, W. et al. (2022, February 25). CrowdStrike Falcon Protects from New Wiper Malware Used in Ukraine Cyberattacks.
    Retrieved March 25, 2022.
  source_name: Crowdstrike DriveSlayer February 2022
  url: https://www.crowdstrike.com/blog/how-crowdstrike-falcon-protects-against-wiper-malware-used-in-ukraine-attacks/
id: attack-pattern--2959d63f-73fd-46a1-abd2-109d7dcede32
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-23T18:48:07.774Z'
name: Windows Service
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Matthew Demaske, Adaptforward
- Pedro Harrison
- Mayuresh Dani, Qualys
- Wietze Beukema @Wietze
- Akshat Pradhan, Qualys
- Wirapong Petshagun
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.6'
```
