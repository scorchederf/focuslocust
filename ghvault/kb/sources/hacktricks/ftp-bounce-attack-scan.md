---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# FTP Bounce attack - Scan

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-ftp-ftp-bounce-attack` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-ftp/ftp-bounce-attack.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [FTP Bounce attack - Scan](../../topics/network-services-pentesting/ftp-bounce-attack-scan.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-ftp-ftp-bounce-attack |
| name | FTP Bounce attack - Scan |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-ftp/ftp-bounce-attack.md |

## Preserved Source Material

````yaml
_body: "# FTP Bounce attack - Scan\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## FTP Bounce - Scanning\n\n###\
  \ Manual\n\n1. Connect to vulnerable FTP\n2. Use **`PORT`**or **`EPRT`**(but only 1 of them) to make it establish a connection\
  \ with the _\\<IP:Port>_ you want to scan:\n\n   `PORT 172,32,80,80,0,8080`\\\n   `EPRT |2|172.32.80.80|8080|`\n\n3. Use\
  \ **`LIST`**(this will just send to the connected _\\<IP:Port>_ the list of current files in the FTP folder) and check for\
  \ the possible responses: `150 File status okay` (This means the port is open) or `425 No connection established` (This\
  \ means the port is closed)\n   1. Instead of `LIST` you could also use **`RETR /file/in/ftp`** and look for similar `Open/Close`\
  \ responses.\n\nExample Using **PORT** (port 8080 of 172.32.80.80 is open and port 7777 is closed):\n\n![](<../../images/image\
  \ (241).png>)\n\nSame example using **`EPRT`**(authentication omitted in the image):\n\n![](<../../images/image (539).png>)\n\
  \nOpen port using `EPRT` instead of `LIST` (different env)\n\n![](<../../images/image (875).png>)\n\n### **nmap**\n\n```bash\n\
  nmap -b <name>:<pass>@<ftp_server> <victim>\nnmap -Pn -v -p 21,80 -b ftp:ftp@10.2.1.5 127.0.0.1 #Scan ports 21,80 of the\
  \ FTP\nnmap -v -p 21,22,445,80,443 -b ftp:ftp@10.2.1.5 192.168.0.1/24 #Scan the internal network (of the FTP) ports 21,22,445,80,443\n\
  ```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-ftp/ftp-bounce-attack.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-ftp/ftp-bounce-attack.md
````
