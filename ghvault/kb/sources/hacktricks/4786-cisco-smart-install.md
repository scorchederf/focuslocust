---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# 4786 - Cisco Smart Install

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-4786-cisco-smart-install` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/4786-cisco-smart-install.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [4786 - Cisco Smart Install](../../topics/network-services-pentesting/4786-cisco-smart-install.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-4786-cisco-smart-install |
| name | 4786 - Cisco Smart Install |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/4786-cisco-smart-install.md |

## Preserved Source Material

````yaml
_body: '# 4786 - Cisco Smart Install


  {{#include ../banners/hacktricks-training.md}}



  ## Basic Information


  **Cisco Smart Install** is a Cisco designed to automate the initial configuration and loading of an operating system image
  for new Cisco hardware. **By default, Cisco Smart Install is active on Cisco hardware and uses the transport layer protocol,
  TCP, with port number 4786.**


  **Default port:** 4786


  ```

  PORT      STATE  SERVICE

  4786/tcp  open   smart-install

  ```


  ## **Smart Install Exploitation Tool**


  **In 2018, a critical vulnerability, CVE-2018–0171, was found in this protocol. The threat level is 9.8 on the CVSS scale.**


  **A specially crafted packet sent to the TCP/4786 port, where Cisco Smart Install is active, triggers a buffer overflow,
  allowing an attacker to:**


  - forcibly reboot the device

  - call RCE

  - steal configurations of network equipment.


  **The** [**SIET**](https://github.com/frostbits-security/SIET) **(Smart Install Exploitation Tool)** was developed to exploit
  this vulnerability, it allows you to abuse Cisco Smart Install. In this article I will show you how you can read a legitimate
  network hardware configuration file. Configure exfiltration can be valuable for a pentester because it will learn about
  the unique features of the network. And this will make life easier and allow finding new vectors for an attack.


  **The target device will be a “live” Cisco Catalyst 2960 switch. Virtual images do not have Cisco Smart Install, so you
  can only practice on the real hardware.**


  The address of the target switch is **10.10.100.10 and CSI is active.** Load SIET and start the attack. **The -g argument**
  means exfiltration of the configuration from the device, **the -i argument** allows you to set the IP address of the vulnerable
  target.


  ```

  ~/opt/tools/SIET$ sudo python2 siet.py -g -i 10.10.100.10

  ```


  <figure><img src="../images/image (773).png" alt=""><figcaption></figcaption></figure>


  The switch configuration **10.10.100.10** will be in the **tftp/** folder


  <figure><img src="../images/image (1116).png" alt=""><figcaption></figcaption></figure>



  {{#include ../banners/hacktricks-training.md}}'
_relative_path: network-services-pentesting/4786-cisco-smart-install.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/4786-cisco-smart-install.md
````
