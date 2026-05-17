---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Detecting Hooked Syscalls

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-detecting-hooked-syscall-functions` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/detecting-hooked-syscall-functions.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Detecting Hooked Syscalls](../../topics/offensive-security/detecting-hooked-syscalls.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-detecting-hooked-syscall-functions |
| name | Detecting Hooked Syscalls |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/detecting-hooked-syscall-functions.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (711).png
- image (712).png
- image (713).png
- image (714).png
- image (717).png
- image (719).png
_body: "# Detecting Hooked Syscalls\n\nIt's possible to enumerate which Windows API calls are hooked by an EDR using inline\
  \ patching technique, where a `jmp` instruction is inserted at the beginning of the syscall stub to be hooked.\n\n## Related\
  \ Notes\n\n{% content-ref url=\"../code-injection-process-injection/how-to-hook-windows-api-using-c++.md\" %}\n[how-to-hook-windows-api-using-c++.md](../code-injection-process-injection/how-to-hook-windows-api-using-c++.md)\n\
  {% endcontent-ref %}\n\n{% content-ref url=\"bypassing-cylance-and-other-avs-edrs-by-unhooking-windows-apis.md\" %}\n[bypassing-cylance-and-other-avs-edrs-by-unhooking-windows-apis.md](bypassing-cylance-and-other-avs-edrs-by-unhooking-windows-apis.md)\n\
  {% endcontent-ref %}\n\n{% content-ref url=\"../code-injection-process-injection/api-monitoring-and-hooking-for-offensive-tooling.md\"\
  \ %}\n[api-monitoring-and-hooking-for-offensive-tooling.md](../code-injection-process-injection/api-monitoring-and-hooking-for-offensive-tooling.md)\n\
  {% endcontent-ref %}\n\n## Walkthrough\n\n### Function before Hooking\n\nBelow shows the stub for for `NtReadVirtualMemory`\
  \ on a system with no EDR present, meaning the syscall `NtReadVirtualMemory` is not hooked:\n\n![](<../../.gitbook/assets/image\
  \ (712).png>)\n\nWe can see the `NtReadVirtualMemory` syscall stub starts with instructions:\n\n```\n00007ffc`d6dcc780 4c8bd1\
  \          mov     r10,rcx\n00007ffc`d6dcc783 b83f000000      mov     eax,3Fh\n...\n```\n\n{% hint style=\"info\" %}\nThe\
  \ above applies to most routines starting with `Zw`, i.e `ZwReadVirtualMemory` too.\n{% endhint %}\n\n...which translates\
  \ to the following 4 opcodes:\n\n```\n4c 8b d1 b8\n```\n\n![](<../../.gitbook/assets/image (713).png>)\n\n`4c 8b d1 b8`\
  \ - are important for this lab - we will come back to this in a moment in a section [Checking for Hooks](detecting-hooked-syscall-functions.md#checking-for-hooks).\n\
  \n### Function after Hooking\n\nBelow shows an example of how `NtReadVirtualMemory` syscall stub looks like when it's hooked\
  \ by an EDR:\n\n![](<../../.gitbook/assets/image (711).png>)\n\nNote that in this case, the first instruction is a `jmp`\
  \ instruction, redirecting the code execution somewhere else (another module in the process's memory):\n\n```\njmp 0000000047980084\n\
  ```\n\n...which translates to the following 5 opcodes:\n\n```\ne9 0f 64 f8 c7\n```\n\n{% hint style=\"info\" %}\n`e9` -\
  \ opcode for near jump\\\n`0f64f8c7`- offset, which is relative to the address of the current instruction, where the code\
  \ will jump to\n{% endhint %}\n\n### Checking for Hooks\n\nKnowing that interesting functions/syscalls (that are often used\
  \ in malware), starting with `Nt` | `Zw`, before hooking, start with opcodes: `4c 8b d1 b8`, we can determine if a given\
  \ function is hooked or not by following this process:\n\n1. Iterate through all the exported functions of the ntdll.dll\n\
  2. Read the first 4 bytes of the the syscall stub and check if they start with `4c 8b d1 b8`\n   1. If yes, the function\
  \ is not hooked\n   2. If no, the function is most likely hooked (with a couple of exceptions mentioned in the False Positives\
  \ callout).\n\nBelow is a simplified visual example attempting to further explain the above process:\n\n1. `NtReadVirtualMemory`\
  \ starts with opcodes `e9 0f 64 f8` rather than `4c 8b d1 b8`, meaning it's most likely hooked\n2. `NtWriteVirtualMemory`\
  \ starts with opcodes `4c 8b d1 b8`, meaning it has not been hooked\n\n![Hooked and unhooked functions](<../../.gitbook/assets/image\
  \ (714).png>)\n\n### Detecting who placed the Hook\n\nAs additional verification for a function really being hooked by a\
  \ different DLL, we can resolve the jump target and check which module it belongs to using GetMappedFileName.\n\nThis can\
  \ also help detect false-positives. If the jump leads into ntdll.dll itself, it is either supposed to be there, or it could\
  \ be a more sophisticated hook trying to disguise itself against this technique.\n\n```cpp\nif (*((unsigned char*)targetFunction)\
  \ == 0xE9) // first byte is a jmp instruction, where does it jump to?\n{\n\t// E9 jump instruction has 32bit offset, relative\
  \ to the address of the first instruction AFTER our jump instruction.\n\tDWORD jumpTargetRelative = *((PDWORD)((char*)functionAddress\
  \ + 1));\n\t// Its possible for target to be 0x000025FF, which is jmp QWORD PTR [rip+0x0], or similar variants, this is\
  \ not handled in this example\n\tPDWORD jumpTarget = targetFunction + 5 /*Instruction pointer after our jmp instruction*/\
  \ + jumpTargetRelative;  \n\tchar moduleNameBuffer[512];\n\tGetMappedFileNameA(GetCurrentProcess(), jumpTarget, moduleNameBuffer,\
  \ 512);\n}\n```\n\n{% hint style=\"warning\" %}\n**False Positives**\\\n\\*\\*\\*\\*Although highly effective at detecting\
  \ functions hooked with inline patching, this method returns a few false positives when enumerating hooked functions inside\
  \ ntdll.dll, such as:\\\n\\\n`NtGetTickCount`\\\n`NtQuerySystemTime`\\\n`NtdllDefWindowProc_A`\\\n`NtdllDefWindowProc_W`\\\
  \n`NtdllDialogWndProc_A`\\\n`NtdllDialogWndProc_W`\\\n`ZwQuerySystemTime`\n\nThe above functions are not hooked.\n{% endhint\
  \ %}\n\n## Code\n\nBelow is the code that we can compile and run on an endpoint running an AV/EDR to see enumerate APIs\
  \ that were most likely hooked:\n\n```cpp\n#include <iostream>\n#include <Windows.h>\n#include <psapi.h>\n\nint main()\n\
  {\n\tPDWORD functionAddress = (PDWORD)0;\n\t\n\t// Get ntdll base address\n\tHMODULE libraryBase = LoadLibraryA(\"ntdll\"\
  );\n\n\tPIMAGE_DOS_HEADER dosHeader = (PIMAGE_DOS_HEADER)libraryBase;\n\tPIMAGE_NT_HEADERS imageNTHeaders = (PIMAGE_NT_HEADERS)((DWORD_PTR)libraryBase\
  \ + dosHeader->e_lfanew);\n\n\t// Locate export address table\n\tDWORD_PTR exportDirectoryRVA = imageNTHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT].VirtualAddress;\n\
  \tPIMAGE_EXPORT_DIRECTORY imageExportDirectory = (PIMAGE_EXPORT_DIRECTORY)((DWORD_PTR)libraryBase + exportDirectoryRVA);\n\
  \n\t// Offsets to list of exported functions and their names\n\tPDWORD addresOfFunctionsRVA = (PDWORD)((DWORD_PTR)libraryBase\
  \ + imageExportDirectory->AddressOfFunctions);\n\tPDWORD addressOfNamesRVA = (PDWORD)((DWORD_PTR)libraryBase + imageExportDirectory->AddressOfNames);\n\
  \tPWORD addressOfNameOrdinalsRVA = (PWORD)((DWORD_PTR)libraryBase + imageExportDirectory->AddressOfNameOrdinals);\n\n\t\
  // Iterate through exported functions of ntdll\n\tfor (DWORD i = 0; i < imageExportDirectory->NumberOfNames; i++)\n\t{\n\
  \t\t// Resolve exported function name\n\t\tDWORD functionNameRVA = addressOfNamesRVA[i];\n\t\tDWORD_PTR functionNameVA =\
  \ (DWORD_PTR)libraryBase + functionNameRVA;\n\t\tchar* functionName = (char*)functionNameVA;\n\t\t\n\t\t// Resolve exported\
  \ function address\n\t\tDWORD_PTR functionAddressRVA = 0;\n\t\tfunctionAddressRVA = addresOfFunctionsRVA[addressOfNameOrdinalsRVA[i]];\n\
  \t\tfunctionAddress = (PDWORD)((DWORD_PTR)libraryBase + functionAddressRVA);\n\n\t\t// Syscall stubs start with these bytes\n\
  \t\tunsigned char syscallPrologue[4] = { 0x4c, 0x8b, 0xd1, 0xb8 };\n\n\t\t// Only interested in Nt|Zw functions\n\t\tif\
  \ (strncmp(functionName, (char*)\"Nt\", 2) == 0 || strncmp(functionName, (char*)\"Zw\", 2) == 0)\n\t\t{\n\t\t\t// Check\
  \ if the first 4 instructions of the exported function are the same as the sycall's prologue\n\t\t\tif (memcmp(functionAddress,\
  \ syscallPrologue, 4) != 0) {\n\t\t\t\n\t\t\t\tif (*((unsigned char*)functionAddress) == 0xE9) // first byte is a jmp instruction,\
  \ where does it jump to?\n\t\t\t\t{\n\t\t\t\t\tDWORD jumpTargetRelative = *((PDWORD)((char*)functionAddress + 1));\n\t\t\
  \t\t\tPDWORD jumpTarget = functionAddress + 5 /*Instruction pointer after our jmp instruction*/ + jumpTargetRelative;  \n\
  \t\t\t\t\tchar moduleNameBuffer[512];\n\t\t\t\t\tGetMappedFileNameA(GetCurrentProcess(), jumpTarget, moduleNameBuffer, 512);\n\
  \t\t\t\t\t\n\t\t\t\t\tprintf(\"Hooked: %s : %p into module %s\\n\", functionName, functionAddress, moduleNameBuffer);\n\t\
  \t\t\t}\n\t\t\t\telse\n\t\t\t\t{\n\t\t\t\t\tprintf(\"Potentially hooked: %s : %p\\n\", functionName, functionAddress);\n\
  \t\t\t\t}\n\t\t\t\n\t\t\t\n\t\t\t\t\n\t\t\t}\n\t\t}\n\t}\n\n\treturn 0;\n}\n```\n\n## Demo\n\nBelow is a snippet of the\
  \ output of the program compiled from the above source code and run on a system with an EDR present. It shows some of the\
  \ interesting functions (not all displayed) that are most likely hooked, with an exception of `NtGetTickCount`, which is\
  \ a false positive, as mentioned earlier:\n\n![Usual suspects hooked + some false positives](<../../.gitbook/assets/image\
  \ (717).png>)\n\n## Updates\n\nAfter I've posted this note on my twitter, I got a message from someone who is smarter than\
  \ I am suggesting to check if the `syscall` instruction itself is not hooked. The `syscall` handler routine (responsible\
  \ for locating functions in the [SSDT](../../miscellaneous-reversing-forensics/windows-kernel-internals/glimpse-into-ssdt-in-windows-x64-kernel.md)\
  \ based on a syscall number) location can be found by reading the Model Specific Register (MSR) at location `0xc0000082`\
  \ and confirming that the address stored there points to `nt!KiSystemCall64Shadow`.\n\nBelow shows how this could be done\
  \ manually in WinBDG:\n\n```\nlkd> rdmsr c0000082\nmsr[c0000082] = fffff803`24a13180\n\nlkd> u fffff803`24a13180\nnt!KiSystemCall64Shadow:\n\
  fffff803`24a13180 0f01f8          swapgs\nfffff803`24a13183 654889242510900000 mov   qword ptr gs:[9010h],rsp\n```\n\n![](<../../.gitbook/assets/image\
  \ (719).png>)\n\n## References\n\n{% embed url=\"https://posts.specterops.io/adventures-in-dynamic-evasion-1fe0bac57aa\"\
  \ %}\n\n{% embed url=\"https://rayanfam.com/topics/hypervisor-from-scratch-part-8/\" %}"
_relative_path: offensive-security/defense-evasion/detecting-hooked-syscall-functions.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/detecting-hooked-syscall-functions.md
````
