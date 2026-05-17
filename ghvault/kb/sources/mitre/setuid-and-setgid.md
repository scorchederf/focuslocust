---
parsed_by: focuslocust
source: mitre
type: generated
---
# Setuid and Setgid

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1548.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Setuid and Setgid](../../attack/techniques/T1548.001-setuid-and-setgid.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1548.001 |
| name | Setuid and Setgid |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1548/001 |

## Preserved Source Material

```yaml
created: '2020-01-30T14:11:41.212Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may abuse configurations where an application has the setuid or setgid bits set in order to get
  code running in a different (and possibly more privileged) user’s context. On Linux or macOS, when the setuid or setgid
  bits are set for an application binary, the application will run with the privileges of the owning user or group respectively.(Citation:
  setuid man page) Normally an application is run in the current user’s context, regardless of which user or group owns the
  application. However, there are instances where programs need to be executed in an elevated context to function properly,
  but the user running them may not have the specific required privileges.


  Instead of creating an entry in the sudoers file, which must be done by root, any user can specify the setuid or setgid
  flag to be set for their own applications (i.e. [Linux and Mac Permissions](https://attack.mitre.org/techniques/T1222/002)).
  The <code>chmod</code> command can set these bits with bitmasking, <code>chmod 4777 [file]</code> or via shorthand naming,
  <code>chmod u+s [file]</code>. This will enable the setuid bit. To enable the setgid bit, <code>chmod 2775</code> and <code>chmod
  g+s</code> can be used.


  Adversaries can use this mechanism on their own malware to make sure they''re able to execute in elevated contexts in the
  future.(Citation: OSX Keydnap malware) This abuse is often part of a "shell escape" or other actions to bypass an execution
  environment with restricted permissions.


  Alternatively, adversaries may choose to find and target vulnerable binaries with the setuid or setgid bits already enabled
  (i.e. [File and Directory Discovery](https://attack.mitre.org/techniques/T1083)). The setuid and setguid bits are indicated
  with an "s" instead of an "x" when viewing a file''s attributes via <code>ls -l</code>. The <code>find</code> command can
  also be used to search for such files. For example, <code>find / -perm +4000 2>/dev/null</code> can be used to find files
  with setuid set and <code>find / -perm +2000 2>/dev/null</code> may be used for setgid. Binaries that have these bits set
  may then be abused by adversaries.(Citation: GTFOBins Suid)'
external_references:
- external_id: T1548.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1548/001
- description: Emilio Pinna, Andrea Cardaci. (n.d.). GTFOBins. Retrieved January 28, 2022.
  source_name: GTFOBins Suid
  url: https://gtfobins.github.io/#+suid
- description: Marc-Etienne M.Leveille. (2016, July 6). New OSX/Keydnap malware is hungry for credentials. Retrieved July
    3, 2017.
  source_name: OSX Keydnap malware
  url: https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/
- description: Michael Kerrisk. (2017, September 15). Linux Programmer's Manual. Retrieved September 21, 2018.
  source_name: setuid man page
  url: http://man7.org/linux/man-pages/man2/setuid.2.html
id: attack-pattern--6831414d-bb70-42b7-8030-d4e06b2660c9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2026-04-15T19:52:13.675Z'
name: Setuid and Setgid
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
- Linux
- macOS
x_mitre_version: '2.0'
```
