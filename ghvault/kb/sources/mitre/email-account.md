---
parsed_by: focuslocust
source: mitre
type: generated
---
# Email Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1087.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Email Account](../../attack/techniques/T1087.003-email-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1087.003 |
| name | Email Account |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1087/003 |

## Preserved Source Material

```yaml
created: '2020-02-21T21:08:33.237Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of email addresses and accounts. Adversaries may try to dump Exchange
  address lists such as global address lists (GALs).(Citation: Microsoft Exchange Address Lists)


  In on-premises Exchange and Exchange Online, the <code>Get-GlobalAddressList</code> PowerShell cmdlet can be used to obtain
  email addresses and accounts from a domain using an authenticated session.(Citation: Microsoft getglobaladdresslist)(Citation:
  Black Hills Attacking Exchange MailSniper, 2016)


  In Google Workspace, the GAL is shared with Microsoft Outlook users through the Google Workspace Sync for Microsoft Outlook
  (GWSMO) service. Additionally, the Google Workspace Directory allows for users to get a listing of other users within the
  organization.(Citation: Google Workspace Global Access List)'
external_references:
- external_id: T1087.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1087/003
- description: Bullock, B.. (2016, October 3). Attacking Exchange with MailSniper. Retrieved October 6, 2019.
  source_name: Black Hills Attacking Exchange MailSniper, 2016
  url: https://www.blackhillsinfosec.com/attacking-exchange-with-mailsniper/
- description: Google. (n.d.). Retrieved March 16, 2021.
  source_name: Google Workspace Global Access List
  url: https://support.google.com/a/answer/166870?hl=en
- description: Microsoft. (2020, February 7). Address lists in Exchange Server. Retrieved March 26, 2020.
  source_name: Microsoft Exchange Address Lists
  url: https://docs.microsoft.com/en-us/exchange/email-addresses-and-address-books/address-lists/address-lists?view=exchserver-2019
- description: Microsoft. (n.d.). Get-GlobalAddressList. Retrieved October 6, 2019.
  source_name: Microsoft getglobaladdresslist
  url: https://docs.microsoft.com/en-us/powershell/module/exchange/email-addresses-and-address-books/get-globaladdresslist
id: attack-pattern--4bc31b94-045b-4752-8920-aebaebdb6470
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:44.685Z'
name: Email Account
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
- Windows
- Office Suite
x_mitre_version: '1.2'
```
