---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Integrity Levels

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-windows-hardening-windows-local-privilege-escalation-integrity-levels` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/windows-local-privilege-escalation/integrity-levels.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Integrity Levels](../../topics/windows-hardening/integrity-levels.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-windows-hardening-windows-local-privilege-escalation-integrity-levels |
| name | Integrity Levels |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/windows-hardening/windows-local-privilege-escalation/integrity-levels.md |

## Preserved Source Material

````yaml
_body: "# Integrity Levels\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Integrity Levels\n\nIn Windows Vista\
  \ and later versions, all protected items come with an **integrity level** tag. This setup mostly assigns a \"medium\" integrity\
  \ level to files and registry keys, except for certain folders and files that Internet Explorer 7 can write to at a low\
  \ integrity level. The default behavior is for processes initiated by standard users to have a medium integrity level, whereas\
  \ services typically operate at a system integrity level. A high-integrity label safeguards the root directory.\n\nA key\
  \ rule is that objects can't be modified by processes with a lower integrity level than the object's level. The integrity\
  \ levels are:\n\n- **Untrusted**: This level is for processes with anonymous logins. Example: Chrome\n- **Low**: Mainly\
  \ for internet interactions, especially in Internet Explorer's Protected Mode, affecting associated files and processes,\
  \ and certain folders like the **Temporary Internet Folder**. Low integrity processes face significant restrictions, including\
  \ no registry write access and limited user profile write access.\n- **Medium**: The default level for most activities,\
  \ assigned to standard users and objects without specific integrity levels. Even members of the Administrators group operate\
  \ at this level by default.\n- **High**: Reserved for administrators, allowing them to modify objects at lower integrity\
  \ levels, including those at the high level itself.\n- **System**: The highest operational level for the Windows kernel\
  \ and core services, out of reach even for administrators, ensuring protection of vital system functions.\n- **Installer**:\
  \ A unique level that stands above all others, enabling objects at this level to uninstall any other object.\n\nYou can\
  \ get the integrity level of a process using **Process Explorer** from **Sysinternals**, accessing the **properties** of\
  \ the process and viewing the \"**Security**\" tab:\n\n![](<../../images/image (824).png>)\n\nYou can also get your **current\
  \ integrity level** using `whoami /groups`\n\n![](<../../images/image (325).png>)\n\n### Integrity Levels in File-system\n\
  \nA object inside the file-system may need an **minimum integrity level requirement** and if a process doesn't have this\
  \ integrity process it won't be able to interact with it.\\\nFor example, lets **create a regular from a regular user console\
  \ file and check the permissions**:\n\n```\necho asd >asd.txt\nicacls asd.txt\nasd.txt BUILTIN\\Administrators:(I)(F)\n\
  \        DESKTOP-IDJHTKP\\user:(I)(F)\n        NT AUTHORITY\\SYSTEM:(I)(F)\n        NT AUTHORITY\\INTERACTIVE:(I)(M,DC)\n\
  \        NT AUTHORITY\\SERVICE:(I)(M,DC)\n        NT AUTHORITY\\BATCH:(I)(M,DC)\n```\n\nNow, lets assign a minimum integrity\
  \ level of **High** to the file. This **must be done from a console** running as **administrator** as a **regular console**\
  \ will be running in Medium Integrity level and **won't be allowed** to assign High Integrity level to an object:\n\n```\n\
  icacls asd.txt /setintegritylevel(oi)(ci) High\nprocessed file: asd.txt\nSuccessfully processed 1 files; Failed processing\
  \ 0 files\n\nC:\\Users\\Public>icacls asd.txt\nasd.txt BUILTIN\\Administrators:(I)(F)\n        DESKTOP-IDJHTKP\\user:(I)(F)\n\
  \        NT AUTHORITY\\SYSTEM:(I)(F)\n        NT AUTHORITY\\INTERACTIVE:(I)(M,DC)\n        NT AUTHORITY\\SERVICE:(I)(M,DC)\n\
  \        NT AUTHORITY\\BATCH:(I)(M,DC)\n        Mandatory Label\\High Mandatory Level:(NW)\n```\n\nThis is where things\
  \ get interesting. You can see that the user `DESKTOP-IDJHTKP\\user` has **FULL privileges** over the file (indeed this\
  \ was the user that created the file), however, due to the minimum integrity level implemented he won't be able to modify\
  \ the file anymore unless he is running inside a High Integrity Level (note that he will be able to read it):\n\n```\necho\
  \ 1234 > asd.txt\nAccess is denied.\n\ndel asd.txt\nC:\\Users\\Public\\asd.txt\nAccess is denied.\n```\n\n> [!TIP]\n> **Therefore,\
  \ when a file has a minimum integrity level, in order to modify it you need to be running at least in that integrity level.**\n\
  \n### Integrity Levels in Binaries\n\nI made a copy of `cmd.exe` in `C:\\Windows\\System32\\cmd-low.exe` and set it an **integrity\
  \ level of low from an administrator console:**\n\n```\nicacls C:\\Windows\\System32\\cmd-low.exe\nC:\\Windows\\System32\\\
  cmd-low.exe NT AUTHORITY\\SYSTEM:(I)(F)\n                                BUILTIN\\Administrators:(I)(F)\n              \
  \                  BUILTIN\\Users:(I)(RX)\n                                APPLICATION PACKAGE AUTHORITY\\ALL APPLICATION\
  \ PACKAGES:(I)(RX)\n                                APPLICATION PACKAGE AUTHORITY\\ALL RESTRICTED APP PACKAGES:(I)(RX)\n\
  \                                Mandatory Label\\Low Mandatory Level:(NW)\n```\n\nNow, when I run `cmd-low.exe` it will\
  \ **run under a low-integrity level** instead of a medium one:\n\n![](<../../images/image (313).png>)\n\nFor curious people,\
  \ if you assign high integrity level to a binary (`icacls C:\\Windows\\System32\\cmd-high.exe /setintegritylevel high`)\
  \ it won't run with high integrity level automatically (if you invoke it from a medium integrity level --by default-- it\
  \ will run under a medium integrity level).\n\n### Integrity Levels in Processes\n\nNot all files and folders have a minimum\
  \ integrity level, **but all processes are running under an integrity level**. And similar to what happened with the file-system,\
  \ **if a process wants to write inside another process it must have at least the same integrity level**. This means that\
  \ a process with low integrity level can’t open a handle with full access to a process with medium integrity level.\n\n\
  Due to the restrictions commented in this and the previous section, from a security point of view, it's always **recommended\
  \ to run a process in the lower level of integrity possible**.\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: windows-hardening/windows-local-privilege-escalation/integrity-levels.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/windows-hardening/windows-local-privilege-escalation/integrity-levels.md
````
