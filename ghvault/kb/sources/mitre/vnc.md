---
parsed_by: focuslocust
source: mitre
type: generated
---
# VNC

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1021.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [VNC](../../attack/techniques/T1021.005-vnc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1021.005 |
| name | VNC |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1021/005 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:28:44.950Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use [Valid Accounts](https://attack.mitre.org/techniques/T1078) to remotely control machines
  using Virtual Network Computing (VNC).  VNC is a platform-independent desktop sharing system that uses the RFB (“remote
  framebuffer”) protocol to enable users to remotely control another computer’s display by relaying the screen, mouse, and
  keyboard inputs over the network.(Citation: The Remote Framebuffer Protocol)


  VNC differs from [Remote Desktop Protocol](https://attack.mitre.org/techniques/T1021/001) as VNC is screen-sharing software
  rather than resource-sharing software. By default, VNC uses the system''s authentication, but it can be configured to use
  credentials specific to VNC.(Citation: MacOS VNC software for Remote Desktop)(Citation: VNC Authentication)


  Adversaries may abuse VNC to perform malicious actions as the logged-on user such as opening documents, downloading files,
  and running arbitrary commands. An adversary could use VNC to remotely control and monitor a system to collect data and
  information to pivot to other systems within the network. Specific VNC libraries/implementations have also been susceptible
  to brute force attacks and memory usage exploitation.(Citation: Hijacking VNC)(Citation: macOS root VNC login without authentication)(Citation:
  VNC Vulnerabilities)(Citation: Offensive Security VNC Authentication Check)(Citation: Attacking VNC Servers PentestLab)(Citation:
  Havana authentication bug)'
external_references:
- external_id: T1021.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1021/005
- description: Administrator, Penetration Testing Lab. (2012, October 30). Attacking VNC Servers. Retrieved October 6, 2021.
  source_name: Attacking VNC Servers PentestLab
  url: https://pentestlab.blog/2012/10/30/attacking-vnc-servers/
- description: Apple Support. (n.d.). Set up a computer running VNC software for Remote Desktop. Retrieved August 18, 2021.
  source_name: MacOS VNC software for Remote Desktop
  url: https://support.apple.com/guide/remote-desktop/set-up-a-computer-running-vnc-software-apdbed09830/mac
- description: Jay Pipes. (2013, December 23). Security Breach! Tenant A is seeing the VNC Consoles of Tenant B!. Retrieved
    September 12, 2024.
  source_name: Havana authentication bug
  url: https://lists.openstack.org/pipermail/openstack/2013-December/004138.html
- description: Nick Miles. (2017, November 30). Detecting macOS High Sierra root account without authentication. Retrieved
    September 20, 2021.
  source_name: macOS root VNC login without authentication
  url: https://www.tenable.com/blog/detecting-macos-high-sierra-root-account-without-authentication
- description: Offensive Security. (n.d.). VNC Authentication. Retrieved October 6, 2021.
  source_name: Offensive Security VNC Authentication Check
  url: https://www.offensive-security.com/metasploit-unleashed/vnc-authentication/
- description: Pascal Nowack. (n.d.). Retrieved September 21, 2021.
  source_name: Gnome Remote Desktop grd-settings
  url: https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/blob/9aa9181e/src/grd-settings.c#L207
- description: Pascal Nowack. (n.d.). Retrieved September 21, 2021.
  source_name: Gnome Remote Desktop gschema
  url: https://gitlab.gnome.org/GNOME/gnome-remote-desktop/-/blob/9aa9181e/src/org.gnome.desktop.remote-desktop.gschema.xml.in
- description: 'Sarah Edwards. (2020, April 30). Analysis of Apple Unified Logs: Quarantine Edition [Entry 6] – Working From
    Home? Remote Logins. Retrieved August 19, 2021.'
  source_name: Apple Unified Log Analysis Remote Login and Screen Sharing
  url: https://sarah-edwards-xzkc.squarespace.com/blog/2020/4/30/analysis-of-apple-unified-logs-quarantine-edition-entry-6-working-from-home-remote-logins
- description: Sergiu Gatlan. (2019, November 22). Dozens of VNC Vulnerabilities Found in Linux, Windows Solutions. Retrieved
    September 20, 2021.
  source_name: VNC Vulnerabilities
  url: https://www.bleepingcomputer.com/news/security/dozens-of-vnc-vulnerabilities-found-in-linux-windows-solutions/
- description: T. Richardson, J. Levine, RealVNC Ltd.. (2011, March). The Remote Framebuffer Protocol. Retrieved September
    20, 2021.
  source_name: The Remote Framebuffer Protocol
  url: https://datatracker.ietf.org/doc/html/rfc6143#section-7.2.2
- description: Tegan. (2019, August 15). Setting up System Authentication. Retrieved September 20, 2021.
  source_name: VNC Authentication
  url: https://help.realvnc.com/hc/en-us/articles/360002250097-Setting-up-System-Authentication
- description: 'Z3RO. (2019, March 10). Day 70: Hijacking VNC (Enum, Brute, Access and Crack). Retrieved September 20, 2021.'
  source_name: Hijacking VNC
  url: https://int0x33.medium.com/day-70-hijacking-vnc-enum-brute-access-and-crack-d3d18a4601cc
id: attack-pattern--01327cde-66c4-4123-bf34-5f258d59457b
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: lateral-movement
modified: '2025-10-24T17:48:19.567Z'
name: VNC
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
- Linux
- Windows
- macOS
x_mitre_version: '1.2'
```
