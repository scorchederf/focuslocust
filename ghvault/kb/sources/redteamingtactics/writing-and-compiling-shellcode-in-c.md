---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Writing and Compiling Shellcode in C

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-writing-and-compiling-shellcode-in-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/writing-and-compiling-shellcode-in-c.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Writing and Compiling Shellcode in C](../../topics/offensive-security/writing-and-compiling-shellcode-in-c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-writing-and-compiling-shellcode-in-c |
| name | Writing and Compiling Shellcode in C |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/writing-and-compiling-shellcode-in-c.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (670).png
- image (677).png
- image (679).png
- image (680).png
- image (681).png
- image (682).png
- image (684).png
- image (685).png
- image (686).png
- image (687).png
- image (688).png
- pasting-executing-shellcode (1).gif
_body: "# Writing and Compiling Shellcode in C\n\nThis is a quick lab to get familiar with the process of writing and compiling\
  \ shellcode in C and is merely a personal conspectus of the paper [From a C project, through assembly, to shellcode](https://vxug.fakedoma.in/papers/VXUG/Exclusive/FromaCprojectthroughassemblytoshellcodeHasherezade.pdf)\
  \ by [hasherezade](https://twitter.com/hasherezade) for [vxunderground](https://twitter.com/vxunderground) - go check it\
  \ out for a deep dive on all the subtleties involved in this process, that will not be covered in these notes.\n\nFor the\
  \ sake of this lab, we are going to turn a simple C program (that is provided by [hasherezade](https://twitter.com/hasherezade)\
  \ in the aforementioned paper) that pops a message box, to shellcode and execute it by manually injecting it into an RWX\
  \ memory location inside notepad.\n\n{% hint style=\"info\" %}\nCode samples used throughout this lab are written by [hasherezade](https://twitter.com/hasherezade),\
  \ unless stated otherwise.\n{% endhint %}\n\n## Overview\n\nBelow is a quick overview of how writing and compiling shellcode\
  \ in C works:\n\n1. Shellcode is written in C\n2. C code is compiled to a list of assembly instructions\n3. Assembly instructions\
  \ are cleaned up and external dependencies removed\n4. Assembly is linked to a binary\n5. Shellcode is extracted from the\
  \ binary\n6. This shellcode can now be injected/executed by leveraging [code injection techniques](./)\n\n## Walkthrough\n\
  \n{% hint style=\"info\" %}\n1. This lab is based on Visual Studio 2019 Community Edition.&#x20;\n2. Program and shellcode\
  \ in this lab targets x64 architecture.\n{% endhint %}\n\n### 1. Preparing Dev Environment\n\nFirst of, let's start the\
  \ Developer Command Prompt for VS 2019, which will set up our dev environment required for compiling and linking the C code\
  \ used in this lab:\n\n![](<../../.gitbook/assets/image (685).png>)\n\nIn my case, the said console is located here:\n\n\
  ```\nC:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat\n```\n\nLet's start\
  \ it like so:\n\n```\ncmd /k \"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat\"\
  \n```\n\n![](<../../.gitbook/assets/image (670).png>)\n\n### 2. Generating Assembly Listing\n\nBelow are two C files that\
  \ make up the program we will be converting to shellcode:\n\n* `c-shellcode.cpp` - the program that pops a message box\n\
  * `peb-lookup.h` - header file required by the `c-shellcode.cpp`, which contains functions for resolving addresses for `LoadLibraryA`\
  \ and `GetProcAddress`\n\n{% tabs %}\n{% tab title=\"c-shellcode.cpp\" %}\n```cpp\n#include <Windows.h>\n#include \"peb-lookup.h\"\
  \n\n// It's worth noting that strings can be defined nside the .text section:\n#pragma code_seg(\".text\")\n\n__declspec(allocate(\"\
  .text\"))\nwchar_t kernel32_str[] = L\"kernel32.dll\";\n\n__declspec(allocate(\".text\"))\nchar load_lib_str[] = \"LoadLibraryA\"\
  ;\n\nint main()\n{\n    // Stack based strings for libraries and functions the shellcode needs\n    wchar_t kernel32_dll_name[]\
  \ = { 'k','e','r','n','e','l','3','2','.','d','l','l', 0 };\n    char load_lib_name[] = { 'L','o','a','d','L','i','b','r','a','r','y','A',0\
  \ };\n    char get_proc_name[] = { 'G','e','t','P','r','o','c','A','d','d','r','e','s','s', 0 };\n    char user32_dll_name[]\
  \ = { 'u','s','e','r','3','2','.','d','l','l', 0 };\n    char message_box_name[] = { 'M','e','s','s','a','g','e','B','o','x','W',\
  \ 0 };\n\n    // stack based strings to be passed to the messagebox win api\n    wchar_t msg_content[] = { 'H','e','l','l','o',\
  \ ' ', 'W','o','r','l','d','!', 0 };\n    wchar_t msg_title[] = { 'D','e','m','o','!', 0 };\n\n    // resolve kernel32 image\
  \ base\n    LPVOID base = get_module_by_name((const LPWSTR)kernel32_dll_name);\n    if (!base) {\n        return 1;\n  \
  \  }\n\n    // resolve loadlibraryA() address\n    LPVOID load_lib = get_func_by_name((HMODULE)base, (LPSTR)load_lib_name);\n\
  \    if (!load_lib) {\n        return 2;\n    }\n\n    // resolve getprocaddress() address\n    LPVOID get_proc = get_func_by_name((HMODULE)base,\
  \ (LPSTR)get_proc_name);\n    if (!get_proc) {\n        return 3;\n    }\n\n    // loadlibrarya and getprocaddress function\
  \ definitions\n    HMODULE(WINAPI * _LoadLibraryA)(LPCSTR lpLibFileName) = (HMODULE(WINAPI*)(LPCSTR))load_lib;\n    FARPROC(WINAPI\
  \ * _GetProcAddress)(HMODULE hModule, LPCSTR lpProcName)\n        = (FARPROC(WINAPI*)(HMODULE, LPCSTR)) get_proc;\n\n  \
  \  // load user32.dll\n    LPVOID u32_dll = _LoadLibraryA(user32_dll_name);\n\n    // messageboxw function definition\n\
  \    int (WINAPI * _MessageBoxW)(\n        _In_opt_ HWND hWnd,\n        _In_opt_ LPCWSTR lpText,\n        _In_opt_ LPCWSTR\
  \ lpCaption,\n        _In_ UINT uType) = (int (WINAPI*)(\n            _In_opt_ HWND,\n            _In_opt_ LPCWSTR,\n  \
  \          _In_opt_ LPCWSTR,\n            _In_ UINT)) _GetProcAddress((HMODULE)u32_dll, message_box_name);\n\n    if (_MessageBoxW\
  \ == NULL) return 4;\n\n\n    // invoke the message box winapi\n    _MessageBoxW(0, msg_content, msg_title, MB_OK);\n\n\
  \    return 0;\n}\n```\n{% endtab %}\n\n{% tab title=\"peb-lookup.h\" %}\n```cpp\n#pragma once\n#include <Windows.h>\n\n\
  #ifndef __NTDLL_H__\n\n#ifndef TO_LOWERCASE\n#define TO_LOWERCASE(out, c1) (out = (c1 <= 'Z' && c1 >= 'A') ? c1 = (c1 -\
  \ 'A') + 'a': c1)\n#endif\n\n\ntypedef struct _UNICODE_STRING\n{\n    USHORT Length;\n    USHORT MaximumLength;\n    PWSTR\
  \  Buffer;\n\n} UNICODE_STRING, * PUNICODE_STRING;\n\ntypedef struct _PEB_LDR_DATA\n{\n    ULONG Length;\n    BOOLEAN Initialized;\n\
  \    HANDLE SsHandle;\n    LIST_ENTRY InLoadOrderModuleList;\n    LIST_ENTRY InMemoryOrderModuleList;\n    LIST_ENTRY InInitializationOrderModuleList;\n\
  \    PVOID      EntryInProgress;\n\n} PEB_LDR_DATA, * PPEB_LDR_DATA;\n\n//here we don't want to use any functions imported\
  \ form extenal modules\n\ntypedef struct _LDR_DATA_TABLE_ENTRY {\n    LIST_ENTRY  InLoadOrderModuleList;\n    LIST_ENTRY\
  \  InMemoryOrderModuleList;\n    LIST_ENTRY  InInitializationOrderModuleList;\n    void* BaseAddress;\n    void* EntryPoint;\n\
  \    ULONG   SizeOfImage;\n    UNICODE_STRING FullDllName;\n    UNICODE_STRING BaseDllName;\n    ULONG   Flags;\n    SHORT\
  \   LoadCount;\n    SHORT   TlsIndex;\n    HANDLE  SectionHandle;\n    ULONG   CheckSum;\n    ULONG   TimeDateStamp;\n}\
  \ LDR_DATA_TABLE_ENTRY, * PLDR_DATA_TABLE_ENTRY;\n\n\ntypedef struct _PEB\n{\n    BOOLEAN InheritedAddressSpace;\n    BOOLEAN\
  \ ReadImageFileExecOptions;\n    BOOLEAN BeingDebugged;\n    BOOLEAN SpareBool;\n    HANDLE Mutant;\n\n    PVOID ImageBaseAddress;\n\
  \    PPEB_LDR_DATA Ldr;\n\n    // [...] this is a fragment, more elements follow here\n\n} PEB, * PPEB;\n\n#endif //__NTDLL_H__\n\
  \ninline LPVOID get_module_by_name(WCHAR* module_name)\n{\n    PPEB peb = NULL;\n#if defined(_WIN64)\n    peb = (PPEB)__readgsqword(0x60);\n\
  #else\n    peb = (PPEB)__readfsdword(0x30);\n#endif\n    PPEB_LDR_DATA ldr = peb->Ldr;\n    LIST_ENTRY list = ldr->InLoadOrderModuleList;\n\
  \n    PLDR_DATA_TABLE_ENTRY Flink = *((PLDR_DATA_TABLE_ENTRY*)(&list));\n    PLDR_DATA_TABLE_ENTRY curr_module = Flink;\n\
  \n    while (curr_module != NULL && curr_module->BaseAddress != NULL) {\n        if (curr_module->BaseDllName.Buffer ==\
  \ NULL) continue;\n        WCHAR* curr_name = curr_module->BaseDllName.Buffer;\n\n        size_t i = 0;\n        for (i\
  \ = 0; module_name[i] != 0 && curr_name[i] != 0; i++) {\n            WCHAR c1, c2;\n            TO_LOWERCASE(c1, module_name[i]);\n\
  \            TO_LOWERCASE(c2, curr_name[i]);\n            if (c1 != c2) break;\n        }\n        if (module_name[i] ==\
  \ 0 && curr_name[i] == 0) {\n            //found\n            return curr_module->BaseAddress;\n        }\n        // not\
  \ found, try next:\n        curr_module = (PLDR_DATA_TABLE_ENTRY)curr_module->InLoadOrderModuleList.Flink;\n    }\n    return\
  \ NULL;\n}\n\ninline LPVOID get_func_by_name(LPVOID module, char* func_name)\n{\n    IMAGE_DOS_HEADER* idh = (IMAGE_DOS_HEADER*)module;\n\
  \    if (idh->e_magic != IMAGE_DOS_SIGNATURE) {\n        return NULL;\n    }\n    IMAGE_NT_HEADERS* nt_headers = (IMAGE_NT_HEADERS*)((BYTE*)module\
  \ + idh->e_lfanew);\n    IMAGE_DATA_DIRECTORY* exportsDir = &(nt_headers->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_EXPORT]);\n\
  \    if (exportsDir->VirtualAddress == NULL) {\n        return NULL;\n    }\n\n    DWORD expAddr = exportsDir->VirtualAddress;\n\
  \    IMAGE_EXPORT_DIRECTORY* exp = (IMAGE_EXPORT_DIRECTORY*)(expAddr + (ULONG_PTR)module);\n    SIZE_T namesCount = exp->NumberOfNames;\n\
  \n    DWORD funcsListRVA = exp->AddressOfFunctions;\n    DWORD funcNamesListRVA = exp->AddressOfNames;\n    DWORD namesOrdsListRVA\
  \ = exp->AddressOfNameOrdinals;\n\n    //go through names:\n    for (SIZE_T i = 0; i < namesCount; i++) {\n        DWORD*\
  \ nameRVA = (DWORD*)(funcNamesListRVA + (BYTE*)module + i * sizeof(DWORD));\n        WORD* nameIndex = (WORD*)(namesOrdsListRVA\
  \ + (BYTE*)module + i * sizeof(WORD));\n        DWORD* funcRVA = (DWORD*)(funcsListRVA + (BYTE*)module + (*nameIndex) *\
  \ sizeof(DWORD));\n\n        LPSTR curr_name = (LPSTR)(*nameRVA + (BYTE*)module);\n        size_t k = 0;\n        for (k\
  \ = 0; func_name[k] != 0 && curr_name[k] != 0; k++) {\n            if (func_name[k] != curr_name[k]) break;\n        }\n\
  \        if (func_name[k] == 0 && curr_name[k] == 0) {\n            //found\n            return (BYTE*)module + (*funcRVA);\n\
  \        }\n    }\n    return NULL;\n}\n```\n{% endtab %}\n{% endtabs %}\n\nWe can now convert the C code in `c-shellcode.cpp`\
  \ to assembly instructions like so:\n\n```\n\"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\\
  MSVC\\14.26.28801\\bin\\Hostx64\\x64\\cl.exe\" /c /FA /GS- c-shellcode.cpp\n```\n\nThe switches' instruct the compiler to:\n\
  \n* `/c` - Prevent the automatic call to LINK\n* `/FA` - Create a listing file containing assembler code for the provided\
  \ C code\n* `/GS-` - Turn off detection of some buffer overruns\n\nBelow shows how we compile the `c-shellcode.cpp` into\
  \ `c-shellcode.asm`:\n\n![Assembly instructions are generated based on the c-shellcode.asm](<../../.gitbook/assets/image\
  \ (688).png>)\n\n### 3. Massaging Assembly Listing\n\nNow that our C code has been convered to assembly in `c-shellcode.asm`,\
  \ we need to clean up the file a bit, so we can link it to an .exe without errors and to avoid the shellcode from crashing.\
  \ Specifically, we need to:\n\n1. Remove dependencies from external libraries\n2. Align stack\n3. Fix a simple syntax issue\n\
  \n#### 3.1 Remove Exteranal Libraries\n\nFirst off, we need to comment out or remove instructions to link this module with\
  \ libraries `libcmt` and `oldnames`:\n\n![Comment out both includelib directives](<../../.gitbook/assets/image (680).png>)\n\
  \n#### 3.2 Fix Stack Alignment\n\nAdd procedure `AlignRSP` right at the top of the first `_TEXT` segment in our `c-shellcode.asm`:\n\
  \n```css\n; https://github.com/mattifestation/PIC_Bindshell/blob/master/PIC_Bindshell/AdjustStack.asm\n\n; AlignRSP is a\
  \ simple call stub that ensures that the stack is 16-byte aligned prior\n; to calling the entry point of the payload. This\
  \ is necessary because 64-bit functions\n; in Windows assume that they were called with 16-byte stack alignment. When amd64\n\
  ; shellcode is executed, you can't be assured that you stack is 16-byte aligned. For example,\n; if your shellcode lands\
  \ with 8-byte stack alignment, any call to a Win32 function will likely\n; crash upon calling any ASM instruction that utilizes\
  \ XMM registers (which require 16-byte)\n; alignment.\n\nAlignRSP PROC\n    push rsi ; Preserve RSI since we're stomping\
  \ on it\n    mov rsi, rsp ; Save the value of RSP so it can be restored\n    and rsp, 0FFFFFFFFFFFFFFF0h ; Align RSP to\
  \ 16 bytes\n    sub rsp, 020h ; Allocate homing space for ExecutePayload\n    call main ; Call the entry point of the payload\n\
  \    mov rsp, rsi ; Restore the original value of RSP\n    pop rsi ; Restore RSI\n    ret ; Return to caller\nAlignRSP ENDP\n\
  ```\n\nBelow shows how it should look like in the `c-shellcode.asm`:\n\n![Add AlignRSP at the top of \\_TEXT segment](<../../.gitbook/assets/image\
  \ (677).png>)\n\n#### 3.3 Remove PDATA and XDATA Segments\n\nRemove or comment out `PDATA` and `XDATA` segments as shown\
  \ below:\n\n![](<../../.gitbook/assets/image (687).png>)\n\n#### 3.4 Fix Syntax Issues\n\nWe need to change line `mov rax,\
  \ QWORD PTR gs:96` to `mov rax, QWORD PTR gs:[96]`:&#x20;\n\n![](<../../.gitbook/assets/image (679).png>)\n\n### 4. Linking\
  \ to an EXE\n\nWe are now ready to link the assembly listings inside `c-shellcode.asm` to get an executable `c-shellcode.exe`:\n\
  \n```\n\"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Tools\\MSVC\\14.26.28801\\bin\\Hostx64\\\
  x64\\ml64.exe\" c-shellcode.asm /link /entry:AlignRSP\n```\n\n![](<../../.gitbook/assets/image (681).png>)\n\n### 5. Testing\
  \ the EXE\n\nWe can now check that if `c-shellcode.exe` does what it was meant to - pops a message box:\n\n![](<../../.gitbook/assets/image\
  \ (682).png>)\n\n### 6. Copying Out Shellcode\n\nOnce we have the `c-shellcode.exe` binary, we can extract the shellcode\
  \ and execute it using any [code injection](./) technique, but for the sake of this lab, we will copy it out as a list of\
  \ hex values and simply paste them into an RWX memory slot inside a notepad.exe.\n\nLet's copy out the shellcode from the\
  \ `.text` section, which in our case starts at 0x200 into the raw file:\n\n![](<../../.gitbook/assets/image (684).png>)\n\
  \nIf you are wondering how we found the shellcode location, look at the `.text` section - you can extract  if from there\
  \ too:\n\n![](<../../.gitbook/assets/image (686).png>)\n\n### 7. Testing Shellcode\n\nOnce the shellcode is copied, let's\
  \ paste it to an RWX memory area (you can set any memory location to have permissions RWX with xdbg64) inside notepad, set\
  \ RIP to that location and resume code execution in that location. If we did all the previous steps correctly, we should\
  \ see our shellcode execute and pop the message box:\n\n![notepad.exe executing shellcode that pops a MessageBox as seen\
  \ in xdbg64](<../../.gitbook/assets/pasting-executing-shellcode (1).gif>)\n\n## References\n\n[From a C project, through\
  \ assembly, to shellcode](https://vxug.fakedoma.in/papers/VXUG/Exclusive/FromaCprojectthroughassemblytoshellcodeHasherezade.pdf)"
_relative_path: offensive-security/code-injection-process-injection/writing-and-compiling-shellcode-in-c.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/writing-and-compiling-shellcode-in-c.md
````
