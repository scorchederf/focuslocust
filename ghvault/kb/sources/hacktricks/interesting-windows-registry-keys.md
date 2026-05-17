---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Interesting Windows Registry Keys

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-windows-forensics-interesting-windows-registry-keys` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/windows-forensics/interesting-windows-registry-keys.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Interesting Windows Registry Keys](../../topics/generic-methodologies-and-resources/interesting-windows-registry-keys.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-basic-forensic-methodology-windows-forensics-interesting-windows-registry-keys |
| name | Interesting Windows Registry Keys |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/basic-forensic-methodology/windows-forensics/interesting-windows-registry-keys.md |

## Preserved Source Material

```yaml
_body: "# Interesting Windows Registry Keys\n\n{{#include ../../../banners/hacktricks-training.md}}\n\n### **Windows Version\
  \ and Owner Info**\n\n- Located at **`Software\\Microsoft\\Windows NT\\CurrentVersion`**, you'll find the Windows version,\
  \ Service Pack, installation time, and the registered owner's name in a straightforward manner.\n\n### **Computer Name**\n\
  \n- The hostname is found under **`System\\ControlSet001\\Control\\ComputerName\\ComputerName`**.\n\n### **Time Zone Setting**\n\
  \n- The system's time zone is stored in **`System\\ControlSet001\\Control\\TimeZoneInformation`**.\n\n### **Access Time\
  \ Tracking**\n\n- By default, the last access time tracking is turned off (**`NtfsDisableLastAccessUpdate=1`**). To enable\
  \ it, use:\n  `fsutil behavior set disablelastaccess 0`\n\n### Windows Versions and Service Packs\n\n- The **Windows version**\
  \ indicates the edition (e.g., Home, Pro) and its release (e.g., Windows 10, Windows 11), while **Service Packs** are updates\
  \ that include fixes and, sometimes, new features.\n\n### Enabling Last Access Time\n\n- Enabling last access time tracking\
  \ allows you to see when files were last opened, which can be critical for forensic analysis or system monitoring.\n\n###\
  \ Network Information Details\n\n- The registry holds extensive data on network configurations, including **types of networks\
  \ (wireless, cable, 3G)** and **network categories (Public, Private/Home, Domain/Work)**, which are vital for understanding\
  \ network security settings and permissions.\n\n### Client Side Caching (CSC)\n\n- **CSC** enhances offline file access\
  \ by caching copies of shared files. Different **CSCFlags** settings control how and what files are cached, affecting performance\
  \ and user experience, especially in environments with intermittent connectivity.\n\n### AutoStart Programs\n\n- Programs\
  \ listed in various `Run` and `RunOnce` registry keys are automatically launched at startup, affecting system boot time\
  \ and potentially being points of interest for identifying malware or unwanted software.\n\n### Shellbags\n\n- **Shellbags**\
  \ not only store preferences for folder views but also provide forensic evidence of folder access even if the folder no\
  \ longer exists. They are invaluable for investigations, revealing user activity that isn't obvious through other means.\n\
  \n### USB Information and Forensics\n\n- The details stored in the registry about USB devices can help trace which devices\
  \ were connected to a computer, potentially linking a device to sensitive file transfers or unauthorized access incidents.\n\
  \n### Volume Serial Number\n\n- The **Volume Serial Number** can be crucial for tracking the specific instance of a file\
  \ system, useful in forensic scenarios where file origin needs to be established across different devices.\n\n### **Shutdown\
  \ Details**\n\n- Shutdown time and count (the latter only for XP) are kept in **`System\\ControlSet001\\Control\\Windows`**\
  \ and **`System\\ControlSet001\\Control\\Watchdog\\Display`**.\n\n### **Network Configuration**\n\n- For detailed network\
  \ interface info, refer to **`System\\ControlSet001\\Services\\Tcpip\\Parameters\\Interfaces{GUID_INTERFACE}`**.\n- First\
  \ and last network connection times, including VPN connections, are logged under various paths in **`Software\\Microsoft\\\
  Windows NT\\CurrentVersion\\NetworkList`**.\n\n### **Shared Folders**\n\n- Shared folders and settings are under **`System\\\
  ControlSet001\\Services\\lanmanserver\\Shares`**. The Client Side Caching (CSC) settings dictate offline file availability.\n\
  \n### **Programs that Start Automatically**\n\n- Paths like **`NTUSER.DAT\\Software\\Microsoft\\Windows\\CurrentVersion\\\
  Run`** and similar entries under `Software\\Microsoft\\Windows\\CurrentVersion` detail programs set to run at startup.\n\
  \n### **Searches and Typed Paths**\n\n- Explorer searches and typed paths are tracked in the registry under **`NTUSER.DAT\\\
  Software\\Microsoft\\Windows\\CurrentVersion\\Explorer`** for WordwheelQuery and TypedPaths, respectively.\n\n### **Recent\
  \ Documents and Office Files**\n\n- Recent documents and Office files accessed are noted in `NTUSER.DAT\\Software\\Microsoft\\\
  Windows\\CurrentVersion\\Explorer\\RecentDocs` and specific Office version paths.\n\n### **Most Recently Used (MRU) Items**\n\
  \n- MRU lists, indicating recent file paths and commands, are stored in various `ComDlg32` and `Explorer` subkeys under\
  \ `NTUSER.DAT`.\n\n### **User Activity Tracking**\n\n- The User Assist feature logs detailed application usage stats, including\
  \ run count and last run time, at **`NTUSER.DAT\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\UserAssist\\{GUID}\\\
  Count`**.\n\n### **Shellbags Analysis**\n\n- Shellbags, revealing folder access details, are stored in `USRCLASS.DAT` and\
  \ `NTUSER.DAT` under `Software\\Microsoft\\Windows\\Shell`. Use **[Shellbag Explorer](https://ericzimmerman.github.io/#!index.md)**\
  \ for analysis.\n\n### **USB Device History**\n\n- **`HKLM\\SYSTEM\\ControlSet001\\Enum\\USBSTOR`** and **`HKLM\\SYSTEM\\\
  ControlSet001\\Enum\\USB`** contain rich details on connected USB devices, including manufacturer, product name, and connection\
  \ timestamps.\n- The user associated with a specific USB device can be pinpointed by searching `NTUSER.DAT` hives for the\
  \ device's **{GUID}**.\n- The last mounted device and its volume serial number can be traced through `System\\MountedDevices`\
  \ and `Software\\Microsoft\\Windows NT\\CurrentVersion\\EMDMgmt`, respectively.\n\nThis guide condenses the crucial paths\
  \ and methods for accessing detailed system, network, and user activity information on Windows systems, aiming for clarity\
  \ and usability.\n\n{{#include ../../../banners/hacktricks-training.md}}"
_relative_path: generic-methodologies-and-resources/basic-forensic-methodology/windows-forensics/interesting-windows-registry-keys.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/basic-forensic-methodology/windows-forensics/interesting-windows-registry-keys.md
```
