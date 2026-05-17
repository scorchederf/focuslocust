---
parsed_by: focuslocust
source: mitre
type: generated
---
# Golden Ticket

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1558.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Golden Ticket](../../attack/techniques/T1558.001-golden-ticket.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1558.001 |
| name | Golden Ticket |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1558/001 |

## Preserved Source Material

```yaml
created: '2020-02-11T19:13:33.643Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries who have the KRBTGT account password hash may forge Kerberos ticket-granting tickets (TGT), also\
  \ known as a golden ticket.(Citation: AdSecurity Kerberos GT Aug 2015) Golden tickets enable adversaries to generate authentication\
  \ material for any account in Active Directory.(Citation: CERT-EU Golden Ticket Protection) \n\nUsing a golden ticket, adversaries\
  \ are then able to request ticket granting service (TGS) tickets, which enable access to specific resources. Golden tickets\
  \ require adversaries to interact with the Key Distribution Center (KDC) in order to obtain TGS.(Citation: ADSecurity Detecting\
  \ Forged Tickets)\n\nThe KDC service runs all on domain controllers that are part of an Active Directory domain. KRBTGT\
  \ is the Kerberos Key Distribution Center (KDC) service account and is responsible for encrypting and signing all Kerberos\
  \ tickets.(Citation: ADSecurity Kerberos and KRBTGT) The KRBTGT password hash may be obtained using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003)\
  \ and privileged access to a domain controller."
external_references:
- external_id: T1558.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1558/001
- description: Metcalf, S. (2015, August 7). Kerberos Golden Tickets are Now More Golden. Retrieved December 1, 2017.
  source_name: AdSecurity Kerberos GT Aug 2015
  url: https://adsecurity.org/?p=1640
- description: Abolins, D., Boldea, C., Socha, K., Soria-Machado, M. (2016, April 26). Kerberos Golden Ticket Protection.
    Retrieved July 13, 2017.
  source_name: CERT-EU Golden Ticket Protection
  url: https://cert.europa.eu/static/WhitePapers/UPDATED%20-%20CERT-EU_Security_Whitepaper_2014-007_Kerberos_Golden_Ticket_Protection_v1_4.pdf
- description: Metcalf, S. (2015, May 03). Detecting Forged Kerberos Ticket (Golden Ticket & Silver Ticket) Use in Active
    Directory. Retrieved December 23, 2015.
  source_name: ADSecurity Detecting Forged Tickets
  url: https://adsecurity.org/?p=1515
- description: 'Sean Metcalf. (2014, November 10). Kerberos & KRBTGT: Active Directory’s Domain Kerberos Service Account.
    Retrieved January 30, 2020.'
  source_name: ADSecurity Kerberos and KRBTGT
  url: https://adsecurity.org/?p=483
- description: Jeff Warren. (2019, February 19). How to Detect Pass-the-Ticket Attacks. Retrieved February 27, 2020.
  source_name: Stealthbits Detect PtT 2019
  url: https://blog.stealthbits.com/detect-pass-the-ticket-attacks
- description: Microsoft. (2015, March 24). Kerberos Golden Ticket Check (Updated). Retrieved February 27, 2020.
  source_name: Microsoft Kerberos Golden Ticket
  url: https://gallery.technet.microsoft.com/scriptcenter/Kerberos-Golden-Ticket-b4814285
id: attack-pattern--768dce68-8d0d-477a-b01d-0eea98b963a1
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:58.155Z'
name: Golden Ticket
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Itamar Mizrahi, Cymptom
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '1.2'
```
