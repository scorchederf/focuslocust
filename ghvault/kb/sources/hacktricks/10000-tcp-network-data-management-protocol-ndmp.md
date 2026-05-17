---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# 10000/tcp - Network Data Management Protocol (NDMP)

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-10000-network-data-management-protocol-ndmp` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/10000-network-data-management-protocol-ndmp.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [10000/tcp - Network Data Management Protocol (NDMP)](../../topics/network-services-pentesting/10000-tcp-network-data-management-protocol-ndmp.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-10000-network-data-management-protocol-ndmp |
| name | 10000/tcp - Network Data Management Protocol (NDMP) |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/10000-network-data-management-protocol-ndmp.md |

## Preserved Source Material

````yaml
_body: '# 10000/tcp - Network Data Management Protocol (NDMP)


  {{#include ../banners/hacktricks-training.md}}


  ## **Protocol Information**


  From [Wikipedia](https://en.wikipedia.org/wiki/NDMP):


  > **NDMP**, or **Network Data Management Protocol**, is a protocol meant to transport data between network attached storage
  \([NAS](https://en.wikipedia.org/wiki/Network-attached_storage)\) devices and [backup](https://en.wikipedia.org/wiki/Backup)
  devices. This removes the need for transporting the data through the backup server itself, thus enhancing speed and removing
  load from the backup server.


  **Default port:** 10000


  ```text

  PORT      STATE SERVICE REASON  VERSION

  10000/tcp open  ndmp    syn-ack Symantec/Veritas Backup Exec ndmp

  ```


  ## **Enumeration**


  ```bash

  nmap -n -sV --script "ndmp-fs-info or ndmp-version" -p 10000 <IP> #Both are default scripts

  ```


  ## Shodan


  `ndmp`


  {{#include ../banners/hacktricks-training.md}}'
_relative_path: network-services-pentesting/10000-network-data-management-protocol-ndmp.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/10000-network-data-management-protocol-ndmp.md
````
