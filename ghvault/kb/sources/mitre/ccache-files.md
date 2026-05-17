---
parsed_by: focuslocust
source: mitre
type: generated
---
# Ccache Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1558.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ccache Files](../../attack/techniques/T1558.005-ccache-files.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1558.005 |
| name | Ccache Files |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1558/005 |

## Preserved Source Material

```yaml
created: '2024-09-17T15:02:31.324Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "\nAdversaries may attempt to steal Kerberos tickets stored in credential cache files (or ccache). These files\
  \ are used for short term storage of a user's active session credentials. The ccache file is created upon user authentication\
  \ and allows for access to multiple services without the user having to re-enter credentials. \n\nThe <code>/etc/krb5.conf</code>\
  \ configuration file and the <code>KRB5CCNAME</code> environment variable are used to set the storage location for ccache\
  \ entries. On Linux, credentials are typically stored in the `/tmp` directory with a naming format of `krb5cc_%UID%` or\
  \ `krb5.ccache`. On macOS, ccache entries are stored by default in memory with an `API:{uuid}` naming scheme. Typically,\
  \ users interact with ticket storage using <code>kinit</code>, which obtains a Ticket-Granting-Ticket (TGT) for the principal;\
  \ <code>klist</code>, which lists obtained tickets currently held in the credentials cache; and other built-in binaries.(Citation:\
  \ Kerberos GNU/Linux)(Citation: Binary Defense Kerberos Linux)\n\nAdversaries can collect tickets from ccache files stored\
  \ on disk and authenticate as the current user without their password to perform [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003)\
  \ attacks. Adversaries can also use these tickets to impersonate legitimate users with elevated privileges to perform [Privilege\
  \ Escalation](https://attack.mitre.org/tactics/TA0004). Tools like Kekeo can also be used by adversaries to convert ccache\
  \ files to Windows format for further [Lateral Movement](https://attack.mitre.org/tactics/TA0008). On macOS, adversaries\
  \ may use open-source tools or the Kerberos framework to interact with ccache files and extract TGTs or Service Tickets\
  \ via lower-level APIs.(Citation: SpectorOps Bifrost Kerberos macOS 2019)(Citation: Linux Kerberos Tickets)(Citation: Brining\
  \ MimiKatz to Unix)(Citation: Kekeo) "
external_references:
- external_id: T1558.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1558/005
- description: ' ARC Labs, Dwyer, John. Gonzalez, Eric. Hudak, Tyler. (2024, October 1). Shining a Light in the Dark – How
    Binary Defense Uncovered an APT Lurking in Shadows of IT. Retrieved October 7, 2024.'
  source_name: Binary Defense Kerberos Linux
  url: https://www.binarydefense.com/resources/blog/shining-a-light-in-the-dark-how-binary-defense-uncovered-an-apt-lurking-in-shadows-of-it/
- description: Adepts of 0xCC. (2021, January 28). The Kerberos Credential Thievery Compendium (GNU/Linux). Retrieved September
    17, 2024.
  source_name: Kerberos GNU/Linux
  url: https://adepts.of0x.cc/kerberos-thievery-linux/
- description: Benjamin Delpy. (n.d.). Kekeo. Retrieved October 4, 2021.
  source_name: Kekeo
  url: https://github.com/gentilkiwi/kekeo
- description: Cody Thomas. (2019, November 14). When Kirbi walks the Bifrost. Retrieved October 6, 2021.
  source_name: SpectorOps Bifrost Kerberos macOS 2019
  url: https://posts.specterops.io/when-kirbi-walks-the-bifrost-4c727807744f
- description: Tim Wadhwa-Brown. (2018, November). Where 2 worlds collide Bringing Mimikatz et al to UNIX. Retrieved October
    13, 2021.
  source_name: Brining MimiKatz to Unix
  url: https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf
- description: Trevor Haskell. (2020, April 1). Kerberos Tickets on Linux Red Teams. Retrieved October 4, 2021.
  source_name: Linux Kerberos Tickets
  url: https://www.fireeye.com/blog/threat-research/2020/04/kerberos-tickets-on-linux-red-teams.html
id: attack-pattern--394220d9-8efc-4252-9040-664f7b115be6
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-04-15T21:56:03.788Z'
name: Ccache Files
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
- macOS
x_mitre_version: '1.0'
```
