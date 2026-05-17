---
parsed_by: focuslocust
source: mitre
type: generated
---
# JavaScript

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059.007` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [JavaScript](../../attack/techniques/T1059.007-javascript.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1059.007 |
| name | JavaScript |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1059/007 |

## Preserved Source Material

```yaml
created: '2020-06-23T19:12:24.924Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse various implementations of JavaScript for execution. JavaScript (JS) is a platform-independent
  scripting language (compiled just-in-time at runtime) commonly associated with scripts in webpages, though JS can be executed
  in runtime environments outside the browser.(Citation: NodeJS)


  JScript is the Microsoft implementation of the same scripting standard. JScript is interpreted via the Windows Script engine
  and thus integrated with many components of Windows such as the [Component Object Model](https://attack.mitre.org/techniques/T1559/001)
  and Internet Explorer HTML Application (HTA) pages.(Citation: JScrip May 2018)(Citation: Microsoft JScript 2007)(Citation:
  Microsoft Windows Scripts)


  JavaScript for Automation (JXA) is a macOS scripting language based on JavaScript, included as part of Apple’s Open Scripting
  Architecture (OSA), that was introduced in OSX 10.10. Apple’s OSA provides scripting capabilities to control applications,
  interface with the operating system, and bridge access into the rest of Apple’s internal APIs. As of OSX 10.10, OSA only
  supports two languages, JXA and [AppleScript](https://attack.mitre.org/techniques/T1059/002). Scripts can be executed via
  the command line utility <code>osascript</code>, they can be compiled into applications or script files via <code>osacompile</code>,
  and they can be compiled and executed in memory of other programs by leveraging the OSAKit Framework.(Citation: Apple About
  Mac Scripting 2016)(Citation: SpecterOps JXA 2020)(Citation: SentinelOne macOS Red Team)(Citation: Red Canary Silver Sparrow
  Feb2021)(Citation: MDSec macOS JXA and VSCode)


  Adversaries may abuse various implementations of JavaScript to execute various behaviors. Common uses include hosting malicious
  scripts on websites as part of a [Drive-by Compromise](https://attack.mitre.org/techniques/T1189) or downloading and executing
  these script files as secondary payloads. Since these payloads are text-based, it is also very common for adversaries to
  obfuscate their content as part of [Obfuscated Files or Information](https://attack.mitre.org/techniques/T1027).'
external_references:
- external_id: T1059.007
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1059/007
- description: Apple. (2016, June 13). About Mac Scripting. Retrieved April 14, 2021.
  source_name: Apple About Mac Scripting 2016
  url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/index.html
- description: Dominic Chell. (2021, January 1). macOS Post-Exploitation Shenanigans with VSCode Extensions. Retrieved April
    20, 2021.
  source_name: MDSec macOS JXA and VSCode
  url: https://www.mdsec.co.uk/2021/01/macos-post-exploitation-shenanigans-with-vscode-extensions/
- description: Microsoft. (2007, August 15). The World of JScript, JavaScript, ECMAScript …. Retrieved June 23, 2020.
  source_name: Microsoft JScript 2007
  url: https://docs.microsoft.com/archive/blogs/gauravseth/the-world-of-jscript-javascript-ecmascript
- description: Microsoft. (2017, January 18). Windows Script Interfaces. Retrieved June 23, 2020.
  source_name: Microsoft Windows Scripts
  url: https://docs.microsoft.com/scripting/winscript/windows-script-interfaces
- description: Microsoft. (2018, May 31). Translating to JScript. Retrieved June 23, 2020.
  source_name: JScrip May 2018
  url: https://docs.microsoft.com/windows/win32/com/translating-to-jscript
- description: OpenJS Foundation. (n.d.). Node.js. Retrieved June 23, 2020.
  source_name: NodeJS
  url: https://nodejs.org/
- description: 'Phil Stokes. (2019, December 5). macOS Red Team: Calling Apple APIs Without Building Binaries. Retrieved July
    17, 2020.'
  source_name: SentinelOne macOS Red Team
  url: https://www.sentinelone.com/blog/macos-red-team-calling-apple-apis-without-building-binaries/
- description: Pitt, L. (2020, August 6). Persistent JXA. Retrieved April 14, 2021.
  source_name: SpecterOps JXA 2020
  url: https://posts.specterops.io/persistent-jxa-66e1c3cd1cf5
- description: 'Tony Lambert. (2021, February 18). Clipping Silver Sparrow’s wings: Outing macOS malware before it takes flight.
    Retrieved April 20, 2021.'
  source_name: Red Canary Silver Sparrow Feb2021
  url: https://redcanary.com/blog/clipping-silver-sparrows-wings/
id: attack-pattern--0f4a0c76-ab2d-4cb0-85d3-3f0efb8cba0d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: execution
modified: '2025-10-24T17:48:24.217Z'
name: JavaScript
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Cody Thomas, SpecterOps
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_remote_support: false
x_mitre_version: '2.2'
```
