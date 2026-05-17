---
parsed_by: focuslocust
source: mitre
type: generated
---
# Hidden Users

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hidden Users](../../attack/techniques/T1564.002-hidden-users.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.002 |
| name | Hidden Users |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/002 |

## Preserved Source Material

```yaml
created: '2020-03-13T20:12:40.876Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use hidden users to hide the presence of user accounts they create or modify. Administrators\
  \ may want to hide users when there are many user accounts on a given system or if they want to hide their administrative\
  \ or other management accounts from other users. \n\nIn macOS, adversaries can create or modify a user to be hidden through\
  \ manipulating plist files, folder attributes, and user attributes. To prevent a user from being shown on the login screen\
  \ and in System Preferences, adversaries can set the userID to be under 500 and set the key value <code>Hide500Users</code>\
  \ to <code>TRUE</code> in the <code>/Library/Preferences/com.apple.loginwindow</code> plist file.(Citation: Cybereason OSX\
  \ Pirrit) Every user has a userID associated with it. When the <code>Hide500Users</code> key value is set to <code>TRUE</code>,\
  \ users with a userID under 500 do not appear on the login screen and in System Preferences. Using the command line, adversaries\
  \ can use the <code>dscl</code> utility to create hidden user accounts by setting the <code>IsHidden</code> attribute to\
  \ <code>1</code>. Adversaries can also hide a user’s home folder by changing the <code>chflags</code> to hidden.(Citation:\
  \ Apple Support Hide a User Account) \n\nAdversaries may similarly hide user accounts in Windows. Adversaries can set the\
  \ <code>HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList</code> Registry key value\
  \ to <code>0</code> for a specific user to prevent that user from being listed on the logon screen.(Citation: FireEye SMOKEDHAM\
  \ June 2021)(Citation: US-CERT TA18-074A)\n\nOn Linux systems, adversaries may hide user accounts from the login screen,\
  \ also referred to as the greeter. The method an adversary may use depends on which Display Manager the distribution is\
  \ currently using. For example, on an Ubuntu system using the GNOME Display Manger (GDM), accounts may be hidden from the\
  \ greeter using the <code>gsettings</code> command (ex: <code>sudo -u gdm gsettings set org.gnome.login-screen disable-user-list\
  \ true</code>).(Citation: Hide GDM User Accounts) Display Managers are not anchored to specific distributions and may be\
  \ changed by a user or adversary."
external_references:
- external_id: T1564.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/002
- description: Amit Serper. (2016). Cybereason Lab Analysis OSX.Pirrit. Retrieved December 10, 2021.
  source_name: Cybereason OSX Pirrit
  url: https://cdn2.hubspot.net/hubfs/3354902/Content%20PDFs/Cybereason-Lab-Analysis-OSX-Pirrit-4-6-16.pdf
- description: Apple. (2020, November 30). Hide a user account in macOS. Retrieved December 10, 2021.
  source_name: Apple Support Hide a User Account
  url: https://support.apple.com/en-us/HT203998
- description: FireEye. (2021, June 16). Smoking Out a DARKSIDE Affiliate’s Supply Chain Software Compromise. Retrieved September
    22, 2021.
  source_name: FireEye SMOKEDHAM June 2021
  url: https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html
- description: Ji Mingkui. (2021, June 17). How to Hide All The User Accounts in Ubuntu 20.04, 21.04 Login Screen. Retrieved
    March 15, 2022.
  source_name: Hide GDM User Accounts
  url: https://ubuntuhandbook.org/index.php/2021/06/hide-user-accounts-ubuntu-20-04-login-screen/
- description: 'US-CERT. (2018, March 16). Alert (TA18-074A): Russian Government Cyber Activity Targeting Energy and Other
    Critical Infrastructure Sectors. Retrieved June 6, 2018.'
  source_name: US-CERT TA18-074A
  url: https://www.us-cert.gov/ncas/alerts/TA18-074A
id: attack-pattern--8c4aef43-48d5-49aa-b2af-c0cd58d30c3d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:23:44.205Z'
name: Hidden Users
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Omkar Gudhate
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
