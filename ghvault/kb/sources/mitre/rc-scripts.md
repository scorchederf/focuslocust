---
parsed_by: focuslocust
source: mitre
type: generated
---
# RC Scripts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1037.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [RC Scripts](../../attack/techniques/T1037.004-rc-scripts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1037.004 |
| name | RC Scripts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1037/004 |

## Preserved Source Material

```yaml
created: '2020-01-15T16:25:22.260Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may establish persistence by modifying RC scripts, which are executed during a Unix-like system’s
  startup. These files allow system administrators to map and start custom services at startup for different run levels. RC
  scripts require root privileges to modify.


  Adversaries may establish persistence by adding a malicious binary path or shell commands to <code>rc.local</code>, <code>rc.common</code>,
  and other RC scripts specific to the Unix-like distribution.(Citation: IranThreats Kittens Dec 2017)(Citation: Intezer HiddenWasp
  Map 2019) Upon reboot, the system executes the script''s contents as root, resulting in persistence.


  Adversary abuse of RC scripts is especially effective for lightweight Unix-like distributions using the root user as default,
  such as ESXi hypervisors, IoT, or embedded systems.(Citation: intezer-kaiji-malware) As ESXi servers store most system files
  in memory and therefore discard changes on shutdown, leveraging `/etc/rc.local.d/local.sh` is one of the few mechanisms
  for enabling persistence across reboots.(Citation: Juniper Networks ESXi Backdoor 2022)


  Several Unix-like systems have moved to Systemd and deprecated the use of RC scripts. This is now a deprecated mechanism
  in macOS in favor of Launchd.(Citation: Apple Developer Doco Archive Launchd)(Citation: Startup Items) This technique can
  be used on Mac OS X Panther v10.3 and earlier versions which still execute the RC scripts.(Citation: Methods of Mac Malware
  Persistence) To maintain backwards compatibility some systems, such as Ubuntu, will execute the RC scripts if they exist
  with the correct file permissions.(Citation: Ubuntu Manpage systemd rc)'
external_references:
- external_id: T1037.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1037/004
- description: Apple. (2016, September 13). Daemons and Services Programming Guide - Creating Launch Daemons and Agents. Retrieved
    February 24, 2021.
  source_name: Apple Developer Doco Archive Launchd
  url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html
- description: Apple. (2016, September 13). Startup Items. Retrieved July 11, 2017.
  source_name: Startup Items
  url: https://developer.apple.com/library/content/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html
- description: Asher Langton. (2022, December 9). A Custom Python Backdoor for VMWare ESXi Servers. Retrieved March 26, 2025.
  source_name: Juniper Networks ESXi Backdoor 2022
  url: https://blogs.juniper.net/en-us/threat-research/a-custom-python-backdoor-for-vmware-esxi-servers
- description: Canonical Ltd.. (n.d.). systemd-rc-local-generator - Compatibility generator for starting /etc/rc.local and        /usr/sbin/halt.local
    during boot and shutdown. Retrieved February 23, 2021.
  source_name: Ubuntu Manpage systemd rc
  url: http://manpages.ubuntu.com/manpages/bionic/man8/systemd-rc-local-generator.8.html
- description: Iran Threats . (2017, December 5). Flying Kitten to Rocket Kitten, A Case of Ambiguity and Shared Code. Retrieved
    May 28, 2020.
  source_name: IranThreats Kittens Dec 2017
  url: https://iranthreats.github.io/resources/attribution-flying-rocket-kitten/
- description: Patrick Wardle. (2014, September). Methods of Malware Persistence on Mac OS X. Retrieved July 5, 2017.
  source_name: Methods of Mac Malware Persistence
  url: https://www.virusbulletin.com/uploads/pdf/conference/vb2014/VB2014-Wardle.pdf
- description: 'Paul Litvak. (2020, May 4). Kaiji: New Chinese Linux malware turning to Golang. Retrieved December 17, 2020.'
  source_name: intezer-kaiji-malware
  url: https://www.intezer.com/blog/research/kaiji-new-chinese-linux-malware-turning-to-golang/
- description: Sanmillan, I. (2019, May 29). HiddenWasp Malware Stings Targeted Linux Systems. Retrieved June 24, 2019.
  source_name: Intezer HiddenWasp Map 2019
  url: https://www.intezer.com/blog-hiddenwasp-malware-targeting-linux-systems/
id: attack-pattern--dca670cf-eeec-438f-8185-fd959d9ef211
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:28.955Z'
name: RC Scripts
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- macOS
- Linux
- Network Devices
- ESXi
x_mitre_version: '2.2'
```
