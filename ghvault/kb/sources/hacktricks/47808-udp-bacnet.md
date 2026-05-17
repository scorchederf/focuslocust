---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# 47808/udp - BACnet

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-47808-udp-bacnet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/47808-udp-bacnet.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [47808/udp - BACnet](../../topics/network-services-pentesting/47808-udp-bacnet.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-47808-udp-bacnet |
| name | 47808/udp - BACnet |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/47808-udp-bacnet.md |

## Preserved Source Material

````yaml
_body: "# 47808/udp - BACnet\n\n{{#include ../banners/hacktricks-training.md}}\n\n## Protocol Information\n\n**BACnet** is\
  \ a **communications protocol** for Building Automation and Control (BAC) networks that leverages the **ASHRAE**, **ANSI**,\
  \ and **ISO 16484-5 standard** protocol. It facilitates communication among building automation and control systems, enabling\
  \ applications such as HVAC control, lighting control, access control, and fire detection systems to exchange information.\
  \ BACnet ensures interoperability and allows computerized building automation devices to communicate, regardless of the\
  \ specific services they provide.\n\n**Default port:** 47808\n\n```text\nPORT      STATE SERVICE\n47808/udp open  BACNet\
  \ -- Building Automation and Control NetworksEnumerate\n```\n\n## Enumeration\n\n### Manual\n\n```bash\npip3 install BAC0\n\
  pip3 install netifaces\n\nimport BAC0\nimport time\n\nmyIP = '<Your IP>/<MASK>' #You need to be on the same subnet as the\
  \ bacnet device. Example: '192.168.1.4/24'\nbacnet = BAC0.connect(ip=myIP)\nbacnet.whois() #Broadcast request of bacnet\
  \ devices\ntime.sleep(5)  #Wait for devices to respond\nfor i, (deviceId, companyId, devIp, numDeviceId) in enumerate(bacnet.devices):\n\
  \    print(f\"-------- Device #{numDeviceId} --------\")\n    print(f\"Device:     {deviceId}\")\n    print(f\"IP:     \
  \    {devIp}\")\n    print(f\"Company:    {companyId}\")\n    readDevice = bacnet.readMultiple(f\"{devIp} device {numDeviceId}\
  \ all\")\n    print(f\"Model Name: {readDevice[11]}\")\n    print(f\"Version:    {readDevice[2]}\")\n    # print(readDevice)\
  \ #List all available info about the device\n```\n\n### Automatic\n\n```bash\nnmap --script bacnet-info --script-args full=yes\
  \ -sU -n -sV -p 47808 <IP>\n```\n\nThis script does not attempt to join a BACnet network as a foreign device, it simply\
  \ sends BACnet requests directly to an IP addressable device.\n\n### Shodan\n\n- `port:47808 instance`\n- `\"Instance ID\"\
  \ \"Vendor Name\"`\n\n{{#include ../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/47808-udp-bacnet.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/47808-udp-bacnet.md
````
