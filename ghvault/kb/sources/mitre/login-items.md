---
parsed_by: focuslocust
source: mitre
type: generated
---
# Login Items

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1547.015` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Login Items](../../attack/techniques/T1547.015-login-items.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1547.015 |
| name | Login Items |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1547/015 |

## Preserved Source Material

```yaml
created: '2021-10-05T21:26:15.081Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may add login items to execute upon user login to gain persistence or escalate privileges. Login
  items are applications, documents, folders, or server connections that are automatically launched when a user logs in.(Citation:
  Open Login Items Apple) Login items can be added via a shared file list or Service Management Framework.(Citation: Adding
  Login Items) Shared file list login items can be set using scripting languages such as [AppleScript](https://attack.mitre.org/techniques/T1059/002),
  whereas the Service Management Framework uses the API call <code>SMLoginItemSetEnabled</code>.


  Login items installed using the Service Management Framework leverage <code>launchd</code>, are not visible in the System
  Preferences, and can only be removed by the application that created them.(Citation: Adding Login Items)(Citation: SMLoginItemSetEnabled
  Schroeder 2013) Login items created using a shared file list are visible in System Preferences, can hide the application
  when it launches, and are executed through LaunchServices, not launchd, to open applications, documents, or URLs without
  using Finder.(Citation: Launch Services Apple Developer) Users and applications use login items to configure their user
  environment to launch commonly used services or applications, such as email, chat, and music applications.


  Adversaries can utilize [AppleScript](https://attack.mitre.org/techniques/T1059/002) and [Native API](https://attack.mitre.org/techniques/T1106)
  calls to create a login item to spawn malicious executables.(Citation: ELC Running at startup) Prior to version 10.5 on
  macOS, adversaries can add login items by using [AppleScript](https://attack.mitre.org/techniques/T1059/002) to send an
  Apple events to the “System Events” process, which has an AppleScript dictionary for manipulating login items.(Citation:
  Login Items AE) Adversaries can use a command such as <code>tell application “System Events” to make login item at end with
  properties /path/to/executable</code>.(Citation: Startup Items Eclectic)(Citation: hexed osx.dok analysis 2019)(Citation:
  Add List Remove Login Items Apple Script) This command adds the path of the malicious executable to the login item file
  list located in <code>~/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm</code>.(Citation:
  Startup Items Eclectic) Adversaries can also use login items to launch executables that can be used to control the victim
  system remotely or as a means to gain privilege escalation by prompting for user credentials.(Citation: objsee mac malware
  2017)(Citation: CheckPoint Dok)(Citation: objsee netwire backdoor 2019)'
external_references:
- external_id: T1547.015
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1547/015
- description: Apple. (2016, September 13). Adding Login Items. Retrieved July 11, 2017.
  source_name: Adding Login Items
  url: https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLoginItems.html
- description: Apple. (2018, June 4). Launch Services Keys. Retrieved October 5, 2021.
  source_name: Launch Service Keys Developer Apple
  url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW1
- description: Apple. (n.d.). Launch Services. Retrieved October 5, 2021.
  source_name: Launch Services Apple Developer
  url: https://developer.apple.com/documentation/coreservices/launch_services
- description: Apple. (n.d.). Login Items AE. Retrieved October 4, 2021.
  source_name: Login Items AE
  url: https://developer.apple.com/library/archive/samplecode/LoginItemsAE/Introduction/Intro.html#//apple_ref/doc/uid/DTS10003788
- description: Apple. (n.d.). Open items automatically when you log in on Mac. Retrieved October 1, 2021.
  source_name: Open Login Items Apple
  url: https://support.apple.com/guide/mac-help/open-items-automatically-when-you-log-in-mh15189/mac
- description: fluffybunny. (2019, July 9). OSX.Dok Analysis. Retrieved November 17, 2024.
  source_name: hexed osx.dok analysis 2019
  url: https://web.archive.org/web/20221007144948/http://www.hexed.in/2019/07/osxdok-analysis.html
- description: 'hoakley. (2018, May 22). Running at startup: when to use a Login Item or a LaunchAgent/LaunchDaemon. Retrieved
    October 5, 2021.'
  source_name: ELC Running at startup
  url: https://eclecticlight.co/2018/05/22/running-at-startup-when-to-use-a-login-item-or-a-launchagent-launchdaemon/
- description: hoakley. (2021, September 16). How to run an app or tool at startup. Retrieved October 5, 2021.
  source_name: Startup Items Eclectic
  url: https://eclecticlight.co/2021/09/16/how-to-run-an-app-or-tool-at-startup/
- description: 'kaloprominat. (2013, July 30). macos: manage add list remove login items apple script. Retrieved October 5,
    2021.'
  source_name: Add List Remove Login Items Apple Script
  url: https://gist.github.com/kaloprominat/6111584
- description: Ofer Caspi. (2017, May 4). OSX Malware is Catching Up, and it wants to Read Your HTTPS Traffic. Retrieved October
    5, 2021.
  source_name: CheckPoint Dok
  url: https://blog.checkpoint.com/2017/04/27/osx-malware-catching-wants-read-https-traffic/
- description: Patrick Wardle. (2018, July 23). Block Blocking Login Items. Retrieved October 1, 2021.
  source_name: objsee block blocking login items
  url: https://objective-see.com/blog/blog_0x31.html
- description: Patrick Wardle. (2019, June 20). Burned by Fire(fox). Retrieved October 1, 2021.
  source_name: objsee netwire backdoor 2019
  url: https://objective-see.com/blog/blog_0x44.html
- description: Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.
  source_name: objsee mac malware 2017
  url: https://objective-see.com/blog/blog_0x25.html
- description: Stokes, Phil. (2019, June 17). HOW MALWARE PERSISTS ON MACOS. Retrieved September 10, 2019.
  source_name: sentinelone macos persist Jun 2019
  url: https://www.sentinelone.com/blog/how-malware-persists-on-macos/
- description: Tim Schroeder. (2013, April 21). SMLoginItemSetEnabled Demystified. Retrieved November 17, 2024.
  source_name: SMLoginItemSetEnabled Schroeder 2013
  url: https://web.archive.org/web/20160216034946/https://blog.timschroeder.net/2013/04/21/smloginitemsetenabled-demystified/
id: attack-pattern--84601337-6a55-4ad7-9c35-79e0d1ea2ab3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:03.355Z'
name: Login Items
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
x_mitre_version: '1.1'
```
