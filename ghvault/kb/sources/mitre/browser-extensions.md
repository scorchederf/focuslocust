---
parsed_by: focuslocust
source: mitre
type: generated
---
# Browser Extensions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1176.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Browser Extensions](../../attack/techniques/T1176.001-browser-extensions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1176.001 |
| name | Browser Extensions |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1176/001 |

## Preserved Source Material

```yaml
created: '2025-03-30T22:12:27.799Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may abuse internet browser extensions to establish persistent access to victim systems. Browser\
  \ extensions or plugins are small programs that can add functionality to and customize aspects of internet browsers. They\
  \ can be installed directly via a local file or custom URL or through a browser's app store - an official online platform\
  \ where users can browse, install, and manage extensions for a specific web browser. Extensions generally inherit the web\
  \ browser's permissions previously granted.(Citation: Wikipedia Browser Extension)(Citation: Chrome Extensions Definition)\
  \ \n \nMalicious extensions can be installed into a browser through malicious app store downloads masquerading as legitimate\
  \ extensions, through social engineering, or by an adversary that has already compromised a system. Security can be limited\
  \ on browser app stores, so it may not be difficult for malicious extensions to defeat automated scanners.(Citation: Malicious\
  \ Chrome Extension Numbers) Depending on the browser, adversaries may also manipulate an extension's update url to install\
  \ updates from an adversary-controlled server or manipulate the mobile configuration file to silently install additional\
  \ extensions. \n\nAdversaries may abuse how chromium-based browsers load extensions by modifying or replacing the Preferences\
  \ and/or Secure Preferences files to silently install malicious extensions. When the browser is not running, adversaries\
  \ can alter these files, ensuring the extension is loaded, granted desired permissions, and will persist in browser sessions.\
  \ This method does not require user consent and extensions are silently loaded in the background from disk or from the browser's\
  \ trusted store.(Citation: Pulsedive)\n  \nPrevious to macOS 11, adversaries could silently install browser extensions via\
  \ the command line using the <code>profiles</code> tool to install malicious <code>.mobileconfig</code> files. In macOS\
  \ 11+, the use of the <code>profiles</code> tool can no longer install configuration profiles; however, <code>.mobileconfig</code>\
  \ files can be planted and installed with user interaction.(Citation: xorrior chrome extensions macOS) \n \nOnce the extension\
  \ is installed, it can browse to websites in the background, steal all information that a user enters into a browser (including\
  \ credentials), and be used as an installer for a RAT for persistence.(Citation: Chrome Extension Crypto Miner)(Citation:\
  \ ICEBRG Chrome Extensions)(Citation: Banker Google Chrome Extension Steals Creds)(Citation: Catch All Chrome Extension)\
  \ \n\nThere have also been instances of botnets using a persistent backdoor through malicious Chrome extensions for [Command\
  \ and Control](https://attack.mitre.org/tactics/TA0011).(Citation: Stantinko Botnet)(Citation: Chrome Extension C2 Malware)\
  \ Adversaries may also use browser extensions to modify browser permissions and components, privacy settings, and other\
  \ security controls for [Stealth](https://attack.mitre.org/tactics/TA0005).(Citation: Browers FriarFox)(Citation: Browser\
  \ Adrozek) "
external_references:
- external_id: T1176.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1176/001
- description: '  Pulsedive Threat Research. (2025, March 21). Rilide - An Information Stealing Browser Extension. Retrieved
    September 22, 2025.'
  source_name: Pulsedive
  url: https://blog.pulsedive.com/rilide-an-information-stealing-browser-extension/
- description: Brinkmann, M. (2017, September 19). First Chrome extension with JavaScript Crypto Miner detected. Retrieved
    November 16, 2017.
  source_name: Chrome Extension Crypto Miner
  url: https://www.ghacks.net/2017/09/19/first-chrome-extension-with-javascript-crypto-miner-detected/
- description: Chris Ross. (2019, February 8). No Place Like Chrome. Retrieved April 27, 2021.
  source_name: xorrior chrome extensions macOS
  url: https://www.xorrior.com/No-Place-Like-Chrome/
- description: Chrome. (n.d.). What are Extensions?. Retrieved November 16, 2017.
  source_name: Chrome Extensions Definition
  url: https://developer.chrome.com/extensions
- description: De Tore, M., Warner, J. (2018, January 15). MALICIOUS CHROME EXTENSIONS ENABLE CRIMINALS TO IMPACT OVER HALF
    A MILLION USERS AND GLOBAL BUSINESSES. Retrieved January 17, 2018.
  source_name: ICEBRG Chrome Extensions
  url: https://www.icebrg.io/blog/malicious-chrome-extensions-enable-criminals-to-impact-over-half-a-million-users-and-global-businesses
- description: Jagpal, N., et al. (2015, August). Trends and Lessons from Three Years Fighting Malicious Extensions. Retrieved
    November 17, 2017.
  source_name: Malicious Chrome Extension Numbers
  url: https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43824.pdf
- description: 'Kjaer, M. (2016, July 18). Malware in the browser: how you might get hacked by a Chrome extension. Retrieved
    September 12, 2024.'
  source_name: Chrome Extension C2 Malware
  url: https://web.archive.org/web/20240608001937/https://kjaer.io/extension-malware/
- description: Marinho, R. (n.d.). "Catch-All" Google Chrome Malicious Extension Steals All Posted Data. Retrieved November
    16, 2017.
  source_name: Catch All Chrome Extension
  url: https://isc.sans.edu/forums/diary/CatchAll+Google+Chrome+Malicious+Extension+Steals+All+Posted+Data/22976/https:/threatpost.com/malicious-chrome-extension-steals-data-posted-to-any-website/128680/)
- description: Marinho, R. (n.d.). (Banker(GoogleChromeExtension)).targeting. Retrieved November 18, 2017.
  source_name: Banker Google Chrome Extension Steals Creds
  url: https://isc.sans.edu/forums/diary/BankerGoogleChromeExtensiontargetingBrazil/22722/
- description: Microsoft Threat Intelligence. (2020, December 10). Widespread malware campaign seeks to silently inject ads
    into search results, affects multiple browsers. Retrieved February 26, 2024.
  source_name: Browser Adrozek
  url: https://www.microsoft.com/en-us/security/blog/2020/12/10/widespread-malware-campaign-seeks-to-silently-inject-ads-into-search-results-affects-multiple-browsers/
- description: Raggi, Michael. Proofpoint Threat Research Team. (2021, February 25). TA413 Leverages New FriarFox Browser
    Extension to Target the Gmail Accounts of Global Tibetan Organizations. Retrieved November 17, 2024.
  source_name: Browers FriarFox
  url: https://www.proofpoint.com/uk/blog/threat-insight/ta413-leverages-new-friarfox-browser-extension-target-gmail-accounts-global
- description: 'Vachon, F., Faou, M. (2017, July 20). Stantinko: A massive adware campaign operating covertly since 2012.
    Retrieved November 16, 2017.'
  source_name: Stantinko Botnet
  url: https://www.welivesecurity.com/2017/07/20/stantinko-massive-adware-campaign-operating-covertly-since-2012/
- description: Wikipedia. (2017, October 8). Browser Extension. Retrieved January 11, 2018.
  source_name: Wikipedia Browser Extension
  url: https://en.wikipedia.org/wiki/Browser_extension
id: attack-pattern--278716b1-61ce-4a74-8d17-891d0c494101
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-09-22T17:00:42.545Z'
name: Browser Extensions
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Gordon Long, LegioX/Zoom, asaurusrex
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
- macOS
x_mitre_version: '1.1'
```
