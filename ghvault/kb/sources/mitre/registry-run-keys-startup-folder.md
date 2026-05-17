---
parsed_by: focuslocust
source: mitre
type: generated
---
# Registry Run Keys ／ Startup Folder

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.001 |
| name | Registry Run Keys ／ Startup Folder |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/001 |

## Preserved Source Material

```yaml
created: '2020-01-23T22:02:48.566Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may achieve persistence by adding a program to a startup folder or referencing it with a Registry
  run key. Adding an entry to the "run keys" in the Registry or startup folder will cause the program referenced to be executed
  when a user logs in.(Citation: Microsoft Run Key) These programs will be executed under the context of the user and will
  have the account''s associated permissions level.


  The following run keys are created by default on Windows systems:


  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run</code>

  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce</code>

  * <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run</code>

  * <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce</code>


  Run keys may exist under multiple hives.(Citation: Microsoft Wow6432Node 2018)(Citation: Malwarebytes Wow6432Node 2016)
  The <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnceEx</code> is also available but is not created
  by default on Windows Vista and newer. Registry run key entries can reference programs directly or list them as a dependency.(Citation:
  Microsoft Run Key) For example, it is possible to load a DLL at logon using a "Depend" key with RunOnceEx: <code>reg add
  HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnceEx\0001\Depend /v 1 /d "C:\temp\evil[.]dll"</code> (Citation: Oddvar
  Moe RunOnceEx Mar 2018)


  Placing a program within a startup folder will also cause that program to execute when a user logs in. There is a startup
  folder location for individual user accounts as well as a system-wide startup folder that will be checked regardless of
  which user account logs in. The startup folder path for the current user is <code>C:\Users\\[Username]\AppData\Roaming\Microsoft\Windows\Start
  Menu\Programs\Startup</code>. The startup folder path for all users is <code>C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp</code>.


  The following Registry keys can be used to set startup folder items for persistence:


  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders</code>

  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders</code>

  * <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders</code>

  * <code>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders</code>


  The following Registry keys can control automatic startup of services during boot:


  * <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce</code>

  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServicesOnce</code>

  * <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunServices</code>

  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunServices</code>


  Using policy settings to specify startup programs creates corresponding values in either of two Registry keys:


  * <code>HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run</code>

  * <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run</code>


  Programs listed in the load value of the registry key <code>HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows</code>
  run automatically for the currently logged-on user.


  By default, the multistring <code>BootExecute</code> value of the registry key <code>HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session
  Manager</code> is set to <code>autocheck autochk *</code>. This value causes Windows, at startup, to check the file-system
  integrity of the hard disks if the system has been shut down abnormally. Adversaries can add other programs or processes
  to this registry value which will automatically launch at boot.


  Adversaries can use these configuration locations to execute malware, such as remote access tools, to maintain persistence
  through system reboots. Adversaries may also use [Masquerading](https://attack.mitre.org/techniques/T1036) to make the Registry
  entries look as if they are associated with legitimate programs.'
external_references:
- external_id: T1547.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/001
- description: Arntz, P. (2016, March 30). Hiding in Plain Sight. Retrieved August 3, 2020.
  source_name: Malwarebytes Wow6432Node 2016
  url: https://blog.malwarebytes.com/cybercrime/2013/10/hiding-in-plain-sight/
- description: Microsoft. (2018, May 31). 32-bit and 64-bit Application Data in the Registry. Retrieved August 3, 2020.
  source_name: Microsoft Wow6432Node 2018
  url: https://docs.microsoft.com/en-us/windows/win32/sysinfo/32-bit-and-64-bit-application-data-in-the-registry
- description: Microsoft. (n.d.). Run and RunOnce Registry Keys. Retrieved September 12, 2024.
  source_name: Microsoft Run Key
  url: https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys
- description: Moe, O. (2018, March 21). Persistence using RunOnceEx - Hidden from Autoruns.exe. Retrieved June 29, 2018.
  source_name: Oddvar Moe RunOnceEx Mar 2018
  url: https://oddvar.moe/2018/03/21/persistence-using-runonceex-hidden-from-autoruns-exe/
- description: Russinovich, M. (2016, January 4). Autoruns for Windows v13.51. Retrieved June 6, 2016.
  source_name: TechNet Autoruns
  url: https://technet.microsoft.com/en-us/sysinternals/bb963902
id: attack-pattern--9efb1ea7-c37b-4595-9640-b7680cd84279
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:09.744Z'
name: Registry Run Keys / Startup Folder
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Oddvar Moe, @oddvarmoe
- Dray Agha, @Purp1eW0lf, Huntress Labs
- Harun Küßner
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.1'
```
