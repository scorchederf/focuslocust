---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# 9100/tcp - PJL (Printer Job Language)

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-9100-pjl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/9100-pjl.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [9100/tcp - PJL (Printer Job Language)](../../topics/network-services-pentesting/9100-tcp-pjl-printer-job-language.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-9100-pjl |
| name | 9100/tcp - PJL (Printer Job Language) |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/9100-pjl.md |

## Preserved Source Material

````yaml
_body: "# 9100/tcp - PJL (Printer Job Language)\n\n{{#include ../banners/hacktricks-training.md}}\n\n## Basic Information\n\
  \nFrom [here](http://hacking-printers.net/wiki/index.php/Port_9100_printing): Raw printing is what we define as the process\
  \ of making a connection to port 9100/tcp of a network printer. It is the default method used by CUPS and the Windows printing\
  \ architecture to communicate with network printers as it is considered as ‘_the simplest, fastest, and generally the most\
  \ reliable network protocol used for printers_’. Raw port 9100 printing, also referred to as JetDirect, AppSocket or PDL-datastream\
  \ actually **is not a printing protocol by itself**. Instead **all data sent is directly processed by the printing device**,\
  \ just like a parallel connection over TCP. In contrast to LPD, IPP and SMB, this can send direct feedback to the client,\
  \ including status and error messages. Such a **bidirectional channel** gives us direct **access** to **results** of **PJL**,\
  \ **PostScript** or **PCL** commands. Therefore raw port 9100 printing – which is supported by almost any network printer\
  \ – is used as the channel for security analysis with PRET and PFT.\n\nIf you want to learn more about [**hacking printers\
  \ read this page**](http://hacking-printers.net/wiki/index.php/Main_Page).\n\n**Default port:** 9100\n\n```\n9100/tcp open\
  \  jetdirect\n```\n\n## Enumeration\n\n### Manual\n\n```bash\nnc -vn <IP> 9100\n@PJL INFO STATUS      #CODE=40000   DISPLAY=\"\
  Sleep\"   ONLINE=TRUE\n@PJL INFO ID          # ID (Brand an version): Brother HL-L2360D series:84U-F75:Ver.b.26\n@PJL INFO\
  \ PRODINFO    #Product info\n@PJL FSDIRLIST NAME=\"0:\\\" ENTRY=1 COUNT=65535  #List dir\n@PJL INFO VARIABLES   #Env variales\n\
  @PJL INFO FILESYS     #?\n@PJL INFO TIMEOUT     #Timeout variables\n@PJL RDYMSG           #Ready message\n@PJL FSINIT\n\
  @PJL FSDIRLIST\n@PJL FSUPLOAD         #Useful to upload a file\n@PJL FSDOWNLOAD       #Useful to download a file\n@PJL FSDELETE\
  \         #Useful to delete a file\n```\n\n### Automatic\n\n```bash\nnmap -sV --script pjl-ready-message -p <PORT> <IP>\n\
  ```\n\n```bash\nmsf> use auxiliary/scanner/printer/printer_env_vars\nmsf> use auxiliary/scanner/printer/printer_list_dir\n\
  msf> use auxiliary/scanner/printer/printer_list_volumes\nmsf> use auxiliary/scanner/printer/printer_ready_message\nmsf>\
  \ use auxiliary/scanner/printer/printer_version_info\nmsf> use auxiliary/scanner/printer/printer_download_file\nmsf> use\
  \ auxiliary/scanner/printer/printer_upload_file\nmsf> use auxiliary/scanner/printer/printer_delete_file\n```\n\n## Printers\
  \ Hacking tool\n\nThis is the tool you want to use to abuse printers: [PRET](https://github.com/RUB-NDS/PRET)\n\n## XPS/TrueType\
  \ VM exploitation (Canon ImageCLASS)\n\n- Deliver XPS over PJL:\n  - `@PJL ENTER LANGUAGE = XPS`\n  - Then send the XPS\
  \ ZIP bytes on the same TCP connection.\n\n- Minimal XPS page referencing an attacker font:\n\n```xml\n<Glyphs Fill=\"#ff000000\"\
  \ FontUri=\"/Resources/evil.ttf\" FontRenderingEmSize=\"12\" OriginX=\"10\" OriginY=\"10\"/>\n```\n\n- RCE primitive summary\
  \ (TrueType hinting VM):\n  - Hinting bytecode in TTF is executed by a TrueType VM. Canon’s VM lacked stack bounds checks.\n\
  \  - CINDEX: OOB stack read → info leak\n  - DELTAP1: unchecked relative stack pivot → controlled writes with subsequent\
  \ pushes\n  - Combine `WS`/`RS` (VM storage write/read) to stage values and perform a precise 32-bit write after pivot.\n\
  \n- Exploit outline:\n  1) Create XPS with the page above and include `/Resources/evil.ttf`.\n  2) In `fpgm`/`prep`, use\
  \ `CINDEX` to leak and compute `stack_cur`.\n  3) Stage target value with `WS`; pivot with `DELTAP1` to the destination;\
  \ use `RS` to write it (e.g., to a function pointer) to gain PC control.\n\n- Send over 9100/tcp:\n\n```bash\n{ printf \"\
  @PJL ENTER LANGUAGE = XPS\\r\\n\"; cat exploit.xps; } | nc -q0 <PRINTER_IP> 9100\n```\n\n- `exploit.xps` is a valid XPS\
  \ ZIP containing `Documents/1/Pages/1.fpage` and `/Resources/evil.ttf`.\n\n## **Shodan**\n\n- `pjl port:9100`\n\n## References\n\
  - [Hacking printers using fonts (Canon ImageCLASS TrueType VM bugs)](https://haxx.in/posts/2025-09-23-canon-ttf/)\n- [Apple\
  \ TrueType Reference Manual – Instruction Set and VM (26.6 fixed point)](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM05/Chap5.html)\n\
  \n{{#include ../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/9100-pjl.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/9100-pjl.md
````
