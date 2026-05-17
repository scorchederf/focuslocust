---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS Useful Commands

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-useful-commands` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-useful-commands.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS Useful Commands](../../topics/macos-hardening/macos-useful-commands.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-useful-commands |
| name | macOS Useful Commands |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-useful-commands.md |

## Preserved Source Material

````yaml
_body: "# macOS Useful Commands\n\n{{#include ../banners/hacktricks-training.md}}\n\n### MacOS Automatic Enumeration Tools\n\
  \n- **MacPEAS**: [https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)\n\
  - **Metasploit**: [https://github.com/rapid7/metasploit-framework/blob/master/modules/post/osx/gather/enum_osx.rb](https://github.com/rapid7/metasploit-framework/blob/master/modules/post/osx/gather/enum_osx.rb)\n\
  - **SwiftBelt**: [https://github.com/cedowens/SwiftBelt](https://github.com/cedowens/SwiftBelt)\n\n### Specific MacOS Commands\n\
  \n```bash\n#System info\ndate\ncal\nuptime #show time from starting\nw #list users\nwhoami #this user\nfinger username #info\
  \ about user\nuname -a #sysinfo\ncat /proc/cpuinfo #processor\ncat /proc/meminfo #memory\nfree #check memory\ndf #check\
  \ disk\n\nlaunchctl list #List services\natq #List \"at\" tasks for the user\nsysctl -a #List kernel configuration\ndiskutil\
  \ list #List connected hard drives\nnettop #Monitor network usage of processes in top style\n\nsystem_profiler SPSoftwareDataType\
  \ #System info\nsystem_profiler SPPrintersDataType #Printer\nsystem_profiler SPApplicationsDataType #Installed Apps\nsystem_profiler\
  \ SPFrameworksDataType #Instaled framework\nsystem_profiler SPDeveloperToolsDataType #Developer tools info\nsystem_profiler\
  \ SPStartupItemDataType #Startup Items\nsystem_profiler SPNetworkDataType #Network Capabilities\nsystem_profiler SPFirewallDataType\
  \ #Firewall Status\nsystem_profiler SPNetworkLocationDataType #Known Network\nsystem_profiler SPBluetoothDataType #Bluetooth\
  \ Info\nsystem_profiler SPEthernetDataType #Ethernet Info\nsystem_profiler SPUSBDataType #USB info\nsystem_profiler SPAirPortDataType\
  \ #Airport Info\n\n\n#Searches\nmdfind password #Show all the files that contains the word password\nmfind -name password\
  \ #List all the files containing the word password in the name\n\n\n#Open any app\nopen -a <Application Name> --hide #Open\
  \ app hidden\nopen some.doc -a TextEdit #Open a file in one application\n\n\n#Computer doesn't go to sleep\ncaffeinate &\n\
  \n\n#Screenshot\n# This will ask for permission to the user\nscreencapture -x /tmp/ss.jpg #Save screenshot in that file\n\
  \n\n#Get clipboard info\npbpaste\n\n\n#system_profiler\nsystem_profiler --help #This command without arguments take lot\
  \ of memory and time.\nsystem_profiler -listDataTypes\nsystem_profiler SPSoftwareDataType SPNetworkDataType\n\n\n#Network\n\
  arp -i en0 -l -a #Print the macOS device's ARP table\nlsof -i -P -n | grep LISTEN\nsmbutil statshares -a #View smb shares\
  \ mounted to the hard drive\n\n#networksetup - set or view network options: Proxies, FW options and more\nnetworksetup -listallnetworkservices\
  \ #List network services\nnetworksetup -listallhardwareports #Hardware ports\nnetworksetup -getinfo Wi-Fi #Wi-Fi info\n\
  networksetup -getautoproxyurl Wi-Fi #Get proxy URL for Wifi\nnetworksetup -getwebproxy Wi-Fi #Wifi Web proxy\nnetworksetup\
  \ -getftpproxy Wi-Fi #Wifi ftp proxy\n\n\n#Brew\nbrew list #List installed\nbrew search <text> #Search package\nbrew info\
  \ <formula>\nbrew install <formula>\nbrew uninstall <formula>\nbrew cleanup #Remove older versions of installed formulae.\n\
  brew cleanup <formula> #Remove older versions of specified formula.\n\n\n#Make the machine talk\nsay hello -v diego\n#spanish:\
  \ diego, Jorge, Monica\n#mexican: Juan, Paulina\n#french: Thomas, Amelie\n\n########### High privileges actions\nsudo purge\
  \ #purge RAM\n#Sharing preferences\nsudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist (enable ssh)\nsudo launchctl\
  \ unload /System/Library/LaunchDaemons/ssh.plist (disable ssh)\n#Start apache\nsudo apachectl (start|status|restart|stop)\n\
  \ ##Web folder: /Library/WebServer/Documents/\n#Remove DNS cache\ndscacheutil -flushcache\nsudo killall -HUP mDNSResponder\n\
  ```\n\n### Quick anti-analysis / virtualization check\n\nSome macOS stealers call `system_profiler` to detect VMs and **abort\
  \ with a distinct exit code (e.g., 100)** to avoid sandbox detonation:\n\n```bash\nif system_profiler SPHardwareDataType\
  \ SPDisplaysDataType | grep -Eiq 'qemu|kvm|vmware|virtualbox'; then\n  exit 100\nfi\n```\n\n### Installed Software & Services\n\
  \nCheck for **suspicious** applications installed and **privileges** over the.installed resources:\n\n```\nsystem_profiler\
  \ SPApplicationsDataType #Installed Apps\nsystem_profiler SPFrameworksDataType #Instaled framework\nlsappinfo list #Installed\
  \ Apps\nlaunchctl list #Services\n```\n\n### User Processes\n\n```bash\n# will print all the running services under that\
  \ particular user domain.\nlaunchctl print gui/<users UID>\n\n# will print all the running services under root\nlaunchctl\
  \ print system\n\n# will print detailed information about the specific launch agent. And if it’s not running or you’ve mistyped,\
  \ you will get some output with a non-zero exit code: Could not find service “com.company.launchagent.label” in domain for\
  \ login\nlaunchctl print gui/<user's UID>/com.company.launchagent.label\n```\n\n### Create a user\n\nWithout prompts\n\n\
  <figure><img src=\"../images/image (79).png\" alt=\"\"><figcaption></figcaption></figure>\n\n## References\n\n- [2025, the\
  \ year of the Infostealer](https://www.pentestpartners.com/security-blog/2025-the-year-of-the-infostealer/)\n\n{{#include\
  \ ../banners/hacktricks-training.md}}"
_relative_path: macos-hardening/macos-useful-commands.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-useful-commands.md
````
