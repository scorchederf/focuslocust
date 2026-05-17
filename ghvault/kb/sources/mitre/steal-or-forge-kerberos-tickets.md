---
parsed_by: focuslocust
source: mitre
type: generated
---
# Steal or Forge Kerberos Tickets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1558` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Steal or Forge Kerberos Tickets](../../attack/techniques/T1558-steal-or-forge-kerberos-tickets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1558 |
| name | Steal or Forge Kerberos Tickets |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1558 |

## Preserved Source Material

```yaml
created: '2020-02-11T19:12:46.830Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to subvert Kerberos authentication by stealing or forging Kerberos tickets to enable
  [Pass the Ticket](https://attack.mitre.org/techniques/T1550/003). Kerberos is an authentication protocol widely used in
  modern Windows domain environments. In Kerberos environments, referred to as “realms”, there are three basic participants:
  client, service, and Key Distribution Center (KDC).(Citation: ADSecurity Kerberos Ring Decoder) Clients request access to
  a service and through the exchange of Kerberos tickets, originating from KDC, they are granted access after having successfully
  authenticated. The KDC is responsible for both authentication and ticket granting.  Adversaries may attempt to abuse Kerberos
  by stealing tickets or forging tickets to enable unauthorized access.


  On Windows, the built-in <code>klist</code> utility can be used to list and analyze cached Kerberos tickets.(Citation: Microsoft
  Klist)

  '
external_references:
- external_id: T1558
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1558
- description: Abolins, D., Boldea, C., Socha, K., Soria-Machado, M. (2016, April 26). Kerberos Golden Ticket Protection.
    Retrieved July 13, 2017.
  source_name: CERT-EU Golden Ticket Protection
  url: https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf
- description: Bani, M. (2018, February 23). Detecting Kerberoasting activity using Azure Security Center. Retrieved March
    23, 2018.
  source_name: Microsoft Detecting Kerberoasting Feb 2018
  url: https://blogs.technet.microsoft.com/motiba/2018/02/23/detecting-kerberoasting-activity-using-azure-security-center/
- description: French, D. (2018, October 2). Detecting Attempts to Steal Passwords from Memory. Retrieved October 11, 2019.
  source_name: Medium Detecting Attempts to Steal Passwords from Memory
  url: https://medium.com/threatpunter/detecting-attempts-to-steal-passwords-from-memory-558f16dce4ea
- description: Jeff Warren. (2019, February 19). How to Detect Pass-the-Ticket Attacks. Retrieved February 27, 2020.
  source_name: Stealthbits Detect PtT 2019
  url: https://blog.stealthbits.com/detect-pass-the-ticket-attacks
- description: Metcalf, S. (2015, December 31). Cracking Kerberos TGS Tickets Using Kerberoast – Exploiting Kerberos to Compromise
    the Active Directory Domain. Retrieved March 22, 2018.
  source_name: AdSecurity Cracking Kerberos Dec 2015
  url: https://adsecurity.org/?p=2293
- description: Metcalf, S. (2015, May 03). Detecting Forged Kerberos Ticket (Golden Ticket & Silver Ticket) Use in Active
    Directory. Retrieved December 23, 2015.
  source_name: ADSecurity Detecting Forged Tickets
  url: https://adsecurity.org/?p=1515
- description: Microsoft. (2015, March 24). Kerberos Golden Ticket Check (Updated). Retrieved February 27, 2020.
  source_name: Microsoft Kerberos Golden Ticket
  url: https://gallery.technet.microsoft.com/scriptcenter/Kerberos-Golden-Ticket-b4814285
- description: Microsoft. (2021, March 3). klist. Retrieved October 14, 2021.
  source_name: Microsoft Klist
  url: https://docs.microsoft.com/windows-server/administration/windows-commands/klist
- description: Sean Metcalf. (2014, September 12). Kerberos, Active Directory’s Secret Decoder Ring. Retrieved February 27,
    2020.
  source_name: ADSecurity Kerberos Ring Decoder
  url: https://adsecurity.org/?p=227
id: attack-pattern--3fc01293-ef5e-41c6-86ce-61f10706b64a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:41.885Z'
name: Steal or Forge Kerberos Tickets
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Tim (Wadhwa-)Brown
- Cody Thomas, SpecterOps
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.7'
```
