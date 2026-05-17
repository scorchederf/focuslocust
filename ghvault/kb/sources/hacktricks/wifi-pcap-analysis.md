---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Wifi Pcap Analysis

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-pcap-inspection-wifi-pcap-analysis` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/wifi-pcap-analysis.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wifi Pcap Analysis](../../topics/generic-methodologies-and-resources/wifi-pcap-analysis.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-pcap-inspection-wifi-pcap-analysis |
| name | Wifi Pcap Analysis |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/wifi-pcap-analysis.md |

## Preserved Source Material

````yaml
_body: '# Wifi Pcap Analysis


  {{#include ../../../banners/hacktricks-training.md}}


  ## Check BSSIDs


  When you receive a capture whose principal traffic is Wifi using WireShark you can start investigating all the SSIDs of
  the capture with _Wireless --> WLAN Traffic_:


  ![](<../../../images/image (106).png>)


  ![](<../../../images/image (492).png>)


  ### Brute Force


  One of the columns of that screen indicates if **any authentication was found inside the pcap**. If that is the case you
  can try to Brute force it using `aircrack-ng`:


  ```bash

  aircrack-ng -w pwds-file.txt -b <BSSID> file.pcap

  ```


  For example it will retrieve the WPA passphrase protecting a PSK (pre shared-key), that will be required to decrypt the
  trafic later.


  ## Data in Beacons / Side Channel


  If you suspect that **data is being leaked inside beacons of a Wifi network** you can check the beacons of the network using
  a filter like the following one: `wlan contains <NAMEofNETWORK>`, or `wlan.ssid == "NAMEofNETWORK"` search inside the filtered
  packets for suspicious strings.


  ## Find Unknown MAC Addresses in A Wifi Network


  The following link will be useful to find the **machines sending data inside a Wifi Network**:


  - `((wlan.ta == e8:de:27:16:70:c9) && !(wlan.fc == 0x8000)) && !(wlan.fc.type_subtype == 0x0005) && !(wlan.fc.type_subtype
  ==0x0004) && !(wlan.addr==ff:ff:ff:ff:ff:ff) && wlan.fc.type==2`


  If you already know **MAC addresses you can remove them from the output** adding checks like this one: `&& !(wlan.addr==5c:51:88:31:a0:3b)`


  Once you have detected **unknown MAC** addresses communicating inside the network you can use **filters** like the following
  one: `wlan.addr==<MAC address> && (ftp || http || ssh || telnet)` to filter its traffic. Note that ftp/http/ssh/telnet filters
  are useful if you have decrypted the traffic.


  ## Decrypt Traffic


  Edit --> Preferences --> Protocols --> IEEE 802.11--> Edit


  ![](<../../../images/image (499).png>)


  {{#include ../../../banners/hacktricks-training.md}}'
_relative_path: generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/wifi-pcap-analysis.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/wifi-pcap-analysis.md
````
