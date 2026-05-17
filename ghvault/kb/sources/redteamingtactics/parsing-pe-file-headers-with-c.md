---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Parsing PE File Headers with C++

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-pe-file-header-parser-in-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Parsing PE File Headers with C++](../../topics/miscellaneous-reversing-forensics/parsing-pe-file-headers-with-c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-pe-file-header-parser-in-c |
| name | Parsing PE File Headers with C++ |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-11-06 20-13.gif
- Screenshot from 2018-11-06 20-11-12.png
- Screenshot from 2018-11-06 20-51-04.png
- Screenshot from 2018-11-06 20-51-27.png
- Screenshot from 2018-11-06 21-26-56.png
- Screenshot from 2018-11-06 22-08-49.png
- Screenshot from 2018-11-06 22-12-26.png
- Screenshot from 2018-11-06 22-27-43.png
- Screenshot from 2018-11-06 22-33-24.png
- Screenshot from 2018-11-06 22-34-51.png
- Screenshot from 2018-11-06 22-43-11.png
- Screenshot from 2018-11-06 22-51-11.png
- Screenshot from 2018-11-06 22-55-16.png
- Screenshot from 2018-11-06 22-59-13.png
- Screenshot from 2018-11-06 23-03-44.png
- Screenshot from 2018-11-06 23-14-05.png
- Screenshot from 2018-11-06 23-19-37.png
- Screenshot from 2018-11-06 23-23-15.png
- Screenshot from 2018-11-06 23-23-28.png
- Screenshot from 2018-11-06 23-23-38.png
_body: "# Parsing PE File Headers with C++\n\n## Context\n\nIn this lab I'm writing a simple Portable Executable (PE) file\
  \ header parser for 32bit binaries, using C++ as the programming language of choice. The lab was inspired by the techniques\
  \ such as reflective DLL injection and process hollowing which both deal with various parts of the PE files.\n\nThe purpose\
  \ of this lab is two-fold:\n\n* Get a bit more comfortable with C++\n* Get a better understanding of PE file headers\n\n\
  This lab is going to be light on text as most of the relevant info is shown in the [code](pe-file-header-parser-in-c++.md#code)\
  \ section, but I will touch on the piece that confused me the most in this endevour - parsing the DLL imports.\n\nBelow\
  \ is a graphic showing the end result - a program that parses a 32bit cmd.exe executable and spits out various pieces of\
  \ information from various PE headers as well as DLL imports.\n\n![](<../../.gitbook/assets/Peek 2018-11-06 20-13.gif>)\n\
  \n{% hint style=\"warning\" %}\n* The code is not able to parse 64bit executables correctly. This will not be fixed.\n*\
  \ The code was not meant to be clean and well organised - it was not the goal of this lab\n* The parser is not full-blown\
  \ - it only goes through the main headers and DLL imports, so no exports, relocations or resources will be touched.\n{%\
  \ endhint %}\n\n## The Big Hurdle\n\nFor the most part of this lab, header parsing was going smoothly, until it was time\
  \ to parse the DLL imports. The bit below is the final solution that worked for parsing out the DLL names and their functions:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-11-06 20-11-12.png>)\n\nParsing out imported DLLs and their functions\
  \ requires a good number of offset calculations that initially may seem confusing and this is the bit I will try to put\
  \ down in words in these notes.\n\nSo how do we go about extracting the DLL names the binary imports and the function names\
  \ that DLL exports?\n\n## Definitions\n\nFirst off, we need to define some terms:\n\n* `Section` - a PE header that defines\
  \ various sections contained in the PE. Some sections are `.text` - this is where the assembly code is stored, `.data` contains\
  \ global and static local variables, etc.\n* File item - part of a PE file, for example a code section `.text`\n* Relative\
  \ Virtual Address (RVA) - address of some file item in memory minus the base address of the image.\n* Virtual Address (VA)\
  \ - virtual memory address of some file item in memory without the image base address subtracted.\n  * For example, if we\
  \ have a VA `0x01004000` and we know that the image base address is `0x0100000`, the RVA is `0x01004000 - 0x01000000 = 0x0004000`.\n\
  * `Data Directories` - part of the `Optional Header` and contains RVAs to various tables - exports, resources and most importantly\
  \ for this lab - dll imports table. It also contains size of the table.\n\n## Calculating Offsets\n\nIf we look at the notepad.exe\
  \ binary using CFF Explorer (or any other similar program) and inspect the `Data Directories` from under the `Optional Header`\
  \ , we can see that the Import Table is located at RVA `0x0000A0A0` that according to CFF Explorer happens to live in the\
  \ `.text` section:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06 20-51-04.png>)\n\nIndeed, if we look at the\
  \ `Section Headers` and note the values `Virtual Size` and `Virtual Address` for the `.text` section:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 20-51-27.png>)\n\nand check if the `Import Directory RVA` of `0x0000A0A0` falls into the range of .text\
  \ section with this conditional statement in python:\n\n```csharp\n0x000a0a0 > 0x00001000 and 0x000a0a0 < 0x00001000 + 0x0000a6fc\n\
  ```\n\n...we can confirm it definitely does fall into the .text section's range:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 21-26-56.png>)\n\n### PIMAGE\\_IMPORT\\_DESCRIPTOR\n\nIn order to read out DLL names that this binary\
  \ imports, we first need to populate a data structure called `PIMAGE_IMPORT_DESCRIPTOR` with revlevant data from the binary,\
  \ but how do we find it?\n\nWe need to translate the `Import Directory RVA` to the file offset - a place in the binary file\
  \ where the DLL import information is stored. The way this can be achieved is by using the following formula:\n\n$$\noffset\
  \ = imageBase + text.RawOffset + (importDirectory.RVA - text.VA)\n$$\n\nwhere `imageBase` is the start address of where\
  \ the binary image is loaded, `text.RawOffset` is the `Raw Address` value from the `.text` section, `text.VA` is `Virtual\
  \ Address` value from the `.text` section and `importDirectory.RVA` is the `Import Directory RVA` value from `Data Directories`\
  \ in `Optional Header`.\n\n{% hint style=\"info\" %}\nIf you think about what was discussed so far and the above formula\
  \ for a moment, you will realise that:\n\n* `imageBase` in our case is 0 since the file is not loaded to memory and we are\
  \ inspecting it on the disk\n* import table is located in `.text` section of the binary. Since the binary is not loaded\
  \ to disk, we need to know the file offset of the `.text` section in relation to the `imageBase`\n* `imageBase + text.RawOffset`\
  \ gives us the file offset to the `.text` section - we need it, because remember - the import table is inside the `.text`\
  \ section\n* Since `importDirectory.RVA`, as mentioned earlier, lives in the `.text` section, `importDirectory.RVA - text.VA`\
  \ gives us the offset of the import table relative to the start of the `.text` section\n* We take the value of `importDirectory.RVA\
  \ - text.VA` and add it to the `text.RawOffset` and we get the offset of the import table in the raw `.text` data.\n{% endhint\
  \ %}\n\nBelow is some simple powershell to do the calculations for us to get the file offset that we can later use for filling\
  \ up the `PIMAGE_IMPORT_DESCRIPTOR` structure with:\n\n{% code title=\"PIMAGE_IMPORT_DESCRIPTOR\" %}\n```csharp\nPS C:\\\
  Users\\mantvydas> $fileBase = 0x0\nPS C:\\Users\\mantvydas> $textRawOffset = 0x00000400\nPS C:\\Users\\mantvydas> $importDirectoryRVA\
  \ = 0x0000A0A0\nPS C:\\Users\\mantvydas> $textVA = 0x00001000\nPS C:\\Users\\mantvydas>\nPS C:\\Users\\mantvydas> # this\
  \ points to the start of the .text section\nPS C:\\Users\\mantvydas> $rawOffsetToTextSection = $fileBase + $textRawOffset\n\
  PS C:\\Users\\mantvydas> $importDescriptor = $rawOffsetToTextSection + ($importDirectoryRVA - $textVA)\nPS C:\\Users\\mantvydas>\
  \ [System.Convert]::ToString($importDescriptor, 16)\n\n// this is the file offset we are looking for for PIMAGE_IMPORT_DESCRIPTOR\n\
  94a0\n```\n{% endcode %}\n\nIf we check the file offset 0x95cc, we can see we are getting close to a list of imported DLL\
  \ names - note that at we can see the VERSION.dll starting to show - that is a good start:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 22-08-49.png>)\n\nNow more importantly, note the value highlighted at offset `0x000094ac` - `7C A2 00\
  \ 00` (reads A2 7C due to little indianness) - this is important. If we consider the layout of the `PIMAGE_IMPORT_DESCRIPTOR`\
  \ structure, we can see that the fourth member of the structure (each member is a DWORD, so 4 bytes in size) is `DWORD Name`,\
  \ which implies that `0x000094ac` contains something that should be useful for us to get our first imported DLL's name:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-11-06 22-12-26.png>)\n\nIndeed, if we check the Import Directory of notepad.exe\
  \ in CFF Explorer, we see that the `0xA27C` is another RVA to the DLL name, which happens to be ADVAPI32.dll - and we will\
  \ manually [verify](pe-file-header-parser-in-c++.md#first-dll-name) this in a moment:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 22-27-43.png>)\n\nIf we look closer at the ADVAPI32.dll import details and compare it with the hex dump\
  \ of the binary at 0x94A0, we can see that the 0000a27c is surrounded by the same info we saw in CFF Explorer for the ADVAPI32.dll:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-11-06 22-43-11.png>)\n\n### First DLL Name\n\nLet's see if we can translate\
  \ this `Name RVA 0xA27c` to the file offset using the technique we used earlier and finally get the first imported DLL name.&#x20;\n\
  \nThis time the formula we need to use is:\n\n$$\noffset = imageBase + text.RawOffset + (nameRVA - text.VA)\n$$\n\nwhere\
  \ `nameRVA` is `Name RVA` value for ADVAPI32.dll from the Import Directory and `text.VA` is the `Virtual Address` of the\
  \ `.text` section.\n\nAgain, some powersehell to do the RVA to file offset calculation for us:\n\n```csharp\n# first dll\
  \ name\n$nameRVA = 0x0000A27C\n$firstDLLname = $rawOffsetToTextSection + ($nameRVA - $textVA)\n[System.Convert]::ToString($firstDLLname,\
  \ 16)\n967c\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06 22-33-24.png>)\n\nIf we check offset `0x967c`\
  \ in our hex editor - success, we found our first DLL name:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06 22-34-51.png>)\n\
  \n### DLL Imported Functions\n\nNow in order to get a list of imported functions from the given DLL, we need to use a structure\
  \ called `PIMAGE_THUNK_DATA32`which looks like this:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06 22-51-11.png>)\n\
  \nIn order to utilise the above structure, again, we need to translate an RVA of the `OriginalFirstThunk` member of the\
  \ structure `PIMAGE_IMPORT_DESCRIPTOR` which in our case was pointing to `0x0000A28C`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 22-55-16.png>)\n\nIf we use the same formula for calculating RVAs as previously and use the below Powershell\
  \ to calculate the file offset, we get:\n\n```csharp\n# first thunk\n$firstThunk = $rawOffsetToTextSection + (0x0000A28C\
  \ - $textVA)\n[System.Convert]::ToString($firstThunk, 16)\n\n968c\n```\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06\
  \ 22-59-13.png>)\n\nAt that offset 968c+4 (+4 because per `PIMAGE_THUNK_DATA32` structure layout, the second member is called\
  \ `Function` and this is the member we are interested in), we see a couple more values that look like RVAs - `0x0000a690`\
  \ and `0x0000a6a2`:\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06 23-03-44.png>)\n\nIf we do a final RVA to file\
  \ offset conversion for the second (we could do the same for 0x0000a690) RVA 0x0000a6a2:\n\n```csharp\n$firstFunction =\
  \ $rawOffsetToTextSection + (0x0000A6A2 - $textVA)\n[System.Convert]::ToString($firstFunction, 16)\n9aa2\n```\n\nFinally,\
  \ with the file offset 0x9aa2, we get to see a second (because we chose the offset a6a2 rather than a690) imported function\
  \ for the DLL ADVAPI32.\\\nNote that the function name actually starts 2 bytes further into the file, so the file offset\
  \ 9aa2 becomes 9aa2 + 2 = 9aa4 - currently I'm not sure what the reason for this is:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 23-14-05.png>)\n\nCross checking the above findings with CFF Explorer's Imported DLLs parser, we can see\
  \ that our calculations were correct - note the OFTs column and the values a6a2 and a690 we referred to earlier:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-11-06 23-19-37.png>)\n\n## Code\n\nThe below code shows how to loop through the file in its entirety to parse\
  \ all the DLLs and all of their imported functions.\n\n```cpp\n#include \"stdafx.h\"\n#include \"Windows.h\"\n#include <iostream>\n\
  \nint main(int argc, char* argv[]) {\n\tconst int MAX_FILEPATH = 255;\n\tchar fileName[MAX_FILEPATH] = {0};\n\tmemcpy_s(&fileName,\
  \ MAX_FILEPATH, argv[1], MAX_FILEPATH);\n\tHANDLE file = NULL;\n\tDWORD fileSize = NULL;\n\tDWORD bytesRead = NULL;\n\t\
  LPVOID fileData = NULL;\n\tPIMAGE_DOS_HEADER dosHeader = {};\n\tPIMAGE_NT_HEADERS imageNTHeaders = {};\n\tPIMAGE_SECTION_HEADER\
  \ sectionHeader = {};\n\tPIMAGE_SECTION_HEADER importSection = {};\n\tIMAGE_IMPORT_DESCRIPTOR* importDescriptor = {};\n\t\
  PIMAGE_THUNK_DATA thunkData = {};\n\tDWORD thunk = NULL;\n\tDWORD rawOffset = NULL;\n\n\t// open file\n\tfile = CreateFileA(fileName,\
  \ GENERIC_ALL, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);\n\tif (file == INVALID_HANDLE_VALUE)\
  \ printf(\"Could not read file\");\n\t\n\t// allocate heap\n\tfileSize = GetFileSize(file, NULL);\n\tfileData = HeapAlloc(GetProcessHeap(),\
  \ 0, fileSize);\n\t\n\t// read file bytes to memory\n\tReadFile(file, fileData, fileSize, &bytesRead, NULL);\n\n\t// IMAGE_DOS_HEADER\n\
  \tdosHeader = (PIMAGE_DOS_HEADER)fileData;\n\tprintf(\"******* DOS HEADER *******\\n\");\n\tprintf(\"\\t0x%x\\t\\tMagic\
  \ number\\n\", dosHeader->e_magic);\n\tprintf(\"\\t0x%x\\t\\tBytes on last page of file\\n\", dosHeader->e_cblp);\n\tprintf(\"\
  \\t0x%x\\t\\tPages in file\\n\", dosHeader->e_cp);\n\tprintf(\"\\t0x%x\\t\\tRelocations\\n\", dosHeader->e_crlc);\n\tprintf(\"\
  \\t0x%x\\t\\tSize of header in paragraphs\\n\", dosHeader->e_cparhdr);\n\tprintf(\"\\t0x%x\\t\\tMinimum extra paragraphs\
  \ needed\\n\", dosHeader->e_minalloc);\n\tprintf(\"\\t0x%x\\t\\tMaximum extra paragraphs needed\\n\", dosHeader->e_maxalloc);\n\
  \tprintf(\"\\t0x%x\\t\\tInitial (relative) SS value\\n\", dosHeader->e_ss);\n\tprintf(\"\\t0x%x\\t\\tInitial SP value\\\
  n\", dosHeader->e_sp);\n\tprintf(\"\\t0x%x\\t\\tInitial SP value\\n\", dosHeader->e_sp);\n\tprintf(\"\\t0x%x\\t\\tChecksum\\\
  n\", dosHeader->e_csum);\n\tprintf(\"\\t0x%x\\t\\tInitial IP value\\n\", dosHeader->e_ip);\n\tprintf(\"\\t0x%x\\t\\tInitial\
  \ (relative) CS value\\n\", dosHeader->e_cs);\n\tprintf(\"\\t0x%x\\t\\tFile address of relocation table\\n\", dosHeader->e_lfarlc);\n\
  \tprintf(\"\\t0x%x\\t\\tOverlay number\\n\", dosHeader->e_ovno);\n\tprintf(\"\\t0x%x\\t\\tOEM identifier (for e_oeminfo)\\\
  n\", dosHeader->e_oemid);\n\tprintf(\"\\t0x%x\\t\\tOEM information; e_oemid specific\\n\", dosHeader->e_oeminfo);\n\tprintf(\"\
  \\t0x%x\\t\\tFile address of new exe header\\n\", dosHeader->e_lfanew);\n\n\t// IMAGE_NT_HEADERS\n\timageNTHeaders = (PIMAGE_NT_HEADERS)((DWORD)fileData\
  \ + dosHeader->e_lfanew);\n\tprintf(\"\\n******* NT HEADERS *******\\n\");\n\tprintf(\"\\t%x\\t\\tSignature\\n\", imageNTHeaders->Signature);\n\
  \t\n\t// FILE_HEADER\n\tprintf(\"\\n******* FILE HEADER *******\\n\");\n\tprintf(\"\\t0x%x\\t\\tMachine\\n\", imageNTHeaders->FileHeader.Machine);\n\
  \tprintf(\"\\t0x%x\\t\\tNumber of Sections\\n\", imageNTHeaders->FileHeader.NumberOfSections);\n\tprintf(\"\\t0x%x\\tTime\
  \ Stamp\\n\", imageNTHeaders->FileHeader.TimeDateStamp);\n\tprintf(\"\\t0x%x\\t\\tPointer to Symbol Table\\n\", imageNTHeaders->FileHeader.PointerToSymbolTable);\n\
  \tprintf(\"\\t0x%x\\t\\tNumber of Symbols\\n\", imageNTHeaders->FileHeader.NumberOfSymbols);\n\tprintf(\"\\t0x%x\\t\\tSize\
  \ of Optional Header\\n\", imageNTHeaders->FileHeader.SizeOfOptionalHeader);\n\tprintf(\"\\t0x%x\\t\\tCharacteristics\\\
  n\", imageNTHeaders->FileHeader.Characteristics);\n\n\t// OPTIONAL_HEADER\n\tprintf(\"\\n******* OPTIONAL HEADER *******\\\
  n\");\n\tprintf(\"\\t0x%x\\t\\tMagic\\n\", imageNTHeaders->OptionalHeader.Magic);\n\tprintf(\"\\t0x%x\\t\\tMajor Linker\
  \ Version\\n\", imageNTHeaders->OptionalHeader.MajorLinkerVersion);\n\tprintf(\"\\t0x%x\\t\\tMinor Linker Version\\n\",\
  \ imageNTHeaders->OptionalHeader.MinorLinkerVersion);\n\tprintf(\"\\t0x%x\\t\\tSize Of Code\\n\", imageNTHeaders->OptionalHeader.SizeOfCode);\n\
  \tprintf(\"\\t0x%x\\t\\tSize Of Initialized Data\\n\", imageNTHeaders->OptionalHeader.SizeOfInitializedData);\n\tprintf(\"\
  \\t0x%x\\t\\tSize Of UnInitialized Data\\n\", imageNTHeaders->OptionalHeader.SizeOfUninitializedData);\n\tprintf(\"\\t0x%x\\\
  t\\tAddress Of Entry Point (.text)\\n\", imageNTHeaders->OptionalHeader.AddressOfEntryPoint);\n\tprintf(\"\\t0x%x\\t\\tBase\
  \ Of Code\\n\", imageNTHeaders->OptionalHeader.BaseOfCode);\n\t//printf(\"\\t0x%x\\t\\tBase Of Data\\n\", imageNTHeaders->OptionalHeader.BaseOfData);\n\
  \tprintf(\"\\t0x%x\\t\\tImage Base\\n\", imageNTHeaders->OptionalHeader.ImageBase);\n\tprintf(\"\\t0x%x\\t\\tSection Alignment\\\
  n\", imageNTHeaders->OptionalHeader.SectionAlignment);\n\tprintf(\"\\t0x%x\\t\\tFile Alignment\\n\", imageNTHeaders->OptionalHeader.FileAlignment);\n\
  \tprintf(\"\\t0x%x\\t\\tMajor Operating System Version\\n\", imageNTHeaders->OptionalHeader.MajorOperatingSystemVersion);\n\
  \tprintf(\"\\t0x%x\\t\\tMinor Operating System Version\\n\", imageNTHeaders->OptionalHeader.MinorOperatingSystemVersion);\n\
  \tprintf(\"\\t0x%x\\t\\tMajor Image Version\\n\", imageNTHeaders->OptionalHeader.MajorImageVersion);\n\tprintf(\"\\t0x%x\\\
  t\\tMinor Image Version\\n\", imageNTHeaders->OptionalHeader.MinorImageVersion);\n\tprintf(\"\\t0x%x\\t\\tMajor Subsystem\
  \ Version\\n\", imageNTHeaders->OptionalHeader.MajorSubsystemVersion);\n\tprintf(\"\\t0x%x\\t\\tMinor Subsystem Version\\\
  n\", imageNTHeaders->OptionalHeader.MinorSubsystemVersion);\n\tprintf(\"\\t0x%x\\t\\tWin32 Version Value\\n\", imageNTHeaders->OptionalHeader.Win32VersionValue);\n\
  \tprintf(\"\\t0x%x\\t\\tSize Of Image\\n\", imageNTHeaders->OptionalHeader.SizeOfImage);\n\tprintf(\"\\t0x%x\\t\\tSize Of\
  \ Headers\\n\", imageNTHeaders->OptionalHeader.SizeOfHeaders);\n\tprintf(\"\\t0x%x\\t\\tCheckSum\\n\", imageNTHeaders->OptionalHeader.CheckSum);\n\
  \tprintf(\"\\t0x%x\\t\\tSubsystem\\n\", imageNTHeaders->OptionalHeader.Subsystem);\n\tprintf(\"\\t0x%x\\t\\tDllCharacteristics\\\
  n\", imageNTHeaders->OptionalHeader.DllCharacteristics);\n\tprintf(\"\\t0x%x\\t\\tSize Of Stack Reserve\\n\", imageNTHeaders->OptionalHeader.SizeOfStackReserve);\n\
  \tprintf(\"\\t0x%x\\t\\tSize Of Stack Commit\\n\", imageNTHeaders->OptionalHeader.SizeOfStackCommit);\n\tprintf(\"\\t0x%x\\\
  t\\tSize Of Heap Reserve\\n\", imageNTHeaders->OptionalHeader.SizeOfHeapReserve);\n\tprintf(\"\\t0x%x\\t\\tSize Of Heap\
  \ Commit\\n\", imageNTHeaders->OptionalHeader.SizeOfHeapCommit);\n\tprintf(\"\\t0x%x\\t\\tLoader Flags\\n\", imageNTHeaders->OptionalHeader.LoaderFlags);\n\
  \tprintf(\"\\t0x%x\\t\\tNumber Of Rva And Sizes\\n\", imageNTHeaders->OptionalHeader.NumberOfRvaAndSizes);\n\n\t// DATA_DIRECTORIES\n\
  \tprintf(\"\\n******* DATA DIRECTORIES *******\\n\");\n\tprintf(\"\\tExport Directory Address: 0x%x; Size: 0x%x\\n\", imageNTHeaders->OptionalHeader.DataDirectory[0].VirtualAddress,\
  \ imageNTHeaders->OptionalHeader.DataDirectory[0].Size);\n\tprintf(\"\\tImport Directory Address: 0x%x; Size: 0x%x\\n\"\
  , imageNTHeaders->OptionalHeader.DataDirectory[1].VirtualAddress, imageNTHeaders->OptionalHeader.DataDirectory[1].Size);\n\
  \n\t// SECTION_HEADERS\n\tprintf(\"\\n******* SECTION HEADERS *******\\n\");\n\t// get offset to first section headeer\n\
  \tDWORD sectionLocation = (DWORD)imageNTHeaders + sizeof(DWORD) + (DWORD)(sizeof(IMAGE_FILE_HEADER)) + (DWORD)imageNTHeaders->FileHeader.SizeOfOptionalHeader;\n\
  \tDWORD sectionSize = (DWORD)sizeof(IMAGE_SECTION_HEADER);\n\t\n\t// get offset to the import directory RVA\n\tDWORD importDirectoryRVA\
  \ = imageNTHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].VirtualAddress;\n\n\t// print section data\n\
  \tfor (int i = 0; i < imageNTHeaders->FileHeader.NumberOfSections; i++) {\n\t\tsectionHeader = (PIMAGE_SECTION_HEADER)sectionLocation;\n\
  \t\tprintf(\"\\t%s\\n\", sectionHeader->Name);\n\t\tprintf(\"\\t\\t0x%x\\t\\tVirtual Size\\n\", sectionHeader->Misc.VirtualSize);\n\
  \t\tprintf(\"\\t\\t0x%x\\t\\tVirtual Address\\n\", sectionHeader->VirtualAddress);\n\t\tprintf(\"\\t\\t0x%x\\t\\tSize Of\
  \ Raw Data\\n\", sectionHeader->SizeOfRawData);\n\t\tprintf(\"\\t\\t0x%x\\t\\tPointer To Raw Data\\n\", sectionHeader->PointerToRawData);\n\
  \t\tprintf(\"\\t\\t0x%x\\t\\tPointer To Relocations\\n\", sectionHeader->PointerToRelocations);\n\t\tprintf(\"\\t\\t0x%x\\\
  t\\tPointer To Line Numbers\\n\", sectionHeader->PointerToLinenumbers);\n\t\tprintf(\"\\t\\t0x%x\\t\\tNumber Of Relocations\\\
  n\", sectionHeader->NumberOfRelocations);\n\t\tprintf(\"\\t\\t0x%x\\t\\tNumber Of Line Numbers\\n\", sectionHeader->NumberOfLinenumbers);\n\
  \t\tprintf(\"\\t\\t0x%x\\tCharacteristics\\n\", sectionHeader->Characteristics);\n\n\t\t// save section that contains import\
  \ directory table\n\t\tif (importDirectoryRVA >= sectionHeader->VirtualAddress && importDirectoryRVA < sectionHeader->VirtualAddress\
  \ + sectionHeader->Misc.VirtualSize) {\n\t\t\timportSection = sectionHeader;\n\t\t}\n\t\tsectionLocation += sectionSize;\n\
  \t}\n\n\t// get file offset to import table\n\trawOffset = (DWORD)fileData + importSection->PointerToRawData;\n\t\n\t//\
  \ get pointer to import descriptor's file offset. Note that the formula for calculating file offset is: imageBaseAddress\
  \ + pointerToRawDataOfTheSectionContainingRVAofInterest + (RVAofInterest - SectionContainingRVAofInterest.VirtualAddress)\n\
  \timportDescriptor = (PIMAGE_IMPORT_DESCRIPTOR)(rawOffset + (imageNTHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].VirtualAddress\
  \ - importSection->VirtualAddress));\n\t\n\tprintf(\"\\n******* DLL IMPORTS *******\\n\");\t\n\tfor (; importDescriptor->Name\
  \ != 0; importDescriptor++)\t{\n\t\t// imported dll modules\n\t\tprintf(\"\\t%s\\n\", rawOffset + (importDescriptor->Name\
  \ - importSection->VirtualAddress));\n\t\tthunk = importDescriptor->OriginalFirstThunk == 0 ? importDescriptor->FirstThunk\
  \ : importDescriptor->OriginalFirstThunk;\n\t\tthunkData = (PIMAGE_THUNK_DATA)(rawOffset + (thunk - importSection->VirtualAddress));\n\
  \t\t\n\t\t// dll exported functions\n\t\tfor (; thunkData->u1.AddressOfData != 0; thunkData++) {\n\t\t\t//a cheap and probably\
  \ non-reliable way of checking if the function is imported via its ordinal number ¯\\_(ツ)_/¯\n\t\t\tif (thunkData->u1.AddressOfData\
  \ > 0x80000000) {\n\t\t\t\t//show lower bits of the value to get the ordinal ¯\\_(ツ)_/¯\n\t\t\t\tprintf(\"\\t\\tOrdinal:\
  \ %x\\n\", (WORD)thunkData->u1.AddressOfData);\n\t\t\t} else {\n\t\t\t\tprintf(\"\\t\\t%s\\n\", (rawOffset + (thunkData->u1.AddressOfData\
  \ - importSection->VirtualAddress + 2)));\n\t\t\t}\n\t\t}\n\t}\n\n    return 0;\n}\n```\n\n{% file src=\"../../.gitbook/assets/perparser.exe\"\
  \ %}\npeparser.exe\n{% endfile %}\n\n## Output Screenshots\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06 23-23-15.png>)\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-11-06 23-23-28.png>)\n\n![](<../../.gitbook/assets/Screenshot from 2018-11-06\
  \ 23-23-38.png>)\n\n![](<../../.gitbook/assets/Peek 2018-11-06 20-13.gif>)\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/debug/pe-format\"\
  \ %}\n\n{% embed url=\"http://win32assembly.programminghorizon.com/pe-tut6.html\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winnt/ns-winnt-_image_section_header\"\
  \ %}\n\n{% embed url=\"https://msdn.microsoft.com/en-us/library/ms809762.aspx?f=255&MSPPError=-2147217396\" %}\n\n{% embed\
  \ url=\"http://sandsprite.com/CodeStuff/Understanding_imports.html\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md
````
