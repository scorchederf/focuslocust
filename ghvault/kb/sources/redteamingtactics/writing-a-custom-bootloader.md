---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Writing a Custom Bootloader

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-writing-a-custom-bootloader` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/writing-a-custom-bootloader.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Writing a Custom Bootloader](../../topics/miscellaneous-reversing-forensics/writing-a-custom-bootloader.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-writing-a-custom-bootloader |
| name | Writing a Custom Bootloader |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/writing-a-custom-bootloader.md |

## Preserved Source Material

````yaml
_asset_filenames:
- baking-bootloader-to-usb (2).gif
- emulate-bootloader.gif
- image (758).png
- image (764).png
- image (769).png
- image (771).png
- image (772).png
- image (775).png
- image (777).png
- image (779).png
- image (782).png
- image (787).png
- image (789).png
_body: "# Writing a Custom Bootloader\n\nThe purpose of this lab is to:\n\n* Familiarize with bootloaders - what it is, who\
  \ loads it, when, how and where\n* Familiarize with some BIOS interrupts\n* Learn how to write a simple valid bootloader\
  \ (it does not have to do anything useful)\n* Try [Qemu](https://www.qemu.org/download/) and exercise assembly and [NASM](https://www.nasm.us/)\n\
  * Attempt to bake the bootloader into a USB stick and try to boot it\n\n## Bootloader Overview\n\n* Bootloader is a program\
  \ that is loaded into computer's Random Access Memory (RAM) by the BIOS, after it finishes with its Power-On Self Test (POST);\n\
  * Bootloader's primary purpose is to help computer find the Operating System it needs to load. Most of the time though,\
  \ it means loading a second bootloader, because the first bootloader has a size limit of 512 bytes;\n* When BIOS needs to\
  \ load an OS, it goes through the available devices on the system such as HDDs / CD-ROM / USB / Floppy and checks if any\
  \ of them are bootable and contain a bootloader by:\n  1. Reading in the first 512 bytes (boot sector) from the medium and\
  \ storing them at computer memory location `0x7c00`;\n  2. Checking if the last 2 bytes are `0xaa55` - the magic number\
  \ signifying to the BIOS that it's a bootable disk that contains a bootloader;\n* Once the bootloader is found, the BIOS\
  \ transfers code execution to `0x7c00` and the bootloader code gets executed;\n* In Windows, the bootloader loads the second\
  \ stage loader called `NTLDR`, which eventually loads the Windows kernel image `c:\\Windows\\System32\\ntoskrnl.exe`;\n\
  * During bootloader's execution, the processor operates in 16 bit mode (real mode), meaning the bootloader can only use\
  \ 16 bit registers in its code.\n\nTo re-inforce the fact that bootloaders reside in the first sector of a bootable device,\
  \ see below screenshot of a hex dump of the first sector of a HDD, that has Windows 10 installed on it. As a reminder, note\
  \ the last 2 bytes `0xAA55` that indicate, that this sector contains a bootloader and the medium is bootable:\n\n![512 bytes\
  \ of bootloader in the 1st sector of a HDD](<../../.gitbook/assets/image (782).png>)\n\n## First Bootloader&#x20;\n\nLet's\
  \ create our first bootable sector that will be 512 bytes in size, using assembly code written in [NASM](https://www.nasm.us/):\n\
  \n![](<../../.gitbook/assets/image (758).png>)\n\nKey aspects of the above code:\n\n1. Line 2 - instructs NASM to generate\
  \ code for CPU operating in 16 bit mode\n2. Lines 5-6 - the bootloader's code, which is simply an infinite loop\n3. Line\
  \ 11 - `times 510 - ($-$$) db 0` - instructs NASM to fill the space between instruction `jmp loop` (2 bytes in size) and\
  \ the last two bytes `0xaa55` (line 13, signifies the magic bytes of the boot sector) with `0x00` 508 null bytes, to make\
  \ sure that the boot sector is exactly 512 bytes in size.\n\nHow does NASM know it needs to pad the binary with 508 null\
  \ bytes?\n\n* $ - address of the current instruction - `jmp loop` (2 bytes)\n* \\$$ - address of the start of our code section\
  \ - 0x00 when the binary is on the disk\n\nGiven the above, `times 510 - ($-$$) db 0` reads as - pad the binary with 00\
  \ bytes 508 times: 510 - (2-0) = 508.&#x20;\n\nVisually, our first booloader binary, once compiled, should have the structure\
  \ like the graphic on the left:\n\n![Our bootloader on the left and proper bootloader structure on the right](<../../.gitbook/assets/image\
  \ (789).png>)\n\n{% hint style=\"info\" %}\nIn the above screenshot on the right, we can see the structure of how a real-life\
  \ bootloader should look like, but for this lab, we're going to ignore it.\n{% endhint %}\n\nAgain, note that the total\
  \ size of the bootloader is 512 bytes:\n\n* 2 bytes for instructions jmp loop\n* 508 NULL bytes\n* 2 magic bytes\n\nIf we\
  \ compile the following bootloader code:\n\n{% code title=\"bootloader-dev.asm\" %}\n```csharp\n; Instruct NASM to generate\
  \ code that is to be run on CPU that is running in 16 bit mode\nbits 16\n\n; Infinite loop\nloop:\n    jmp loop\n\n; Fill\
  \ remaining space of the 512 bytes minus our instrunctions, with 00 bytes\n; $ - address of the current instruction\n; $$\
  \ - address of the start of the image .text section we're executing this code in\ntimes 510 - ($-$$) db 0\n; Bootloader\
  \ magic number\ndw 0xaa55\n```\n{% endcode %}\n\n...with NASM like so:\n\n```\nnasm -f bin bootloader-dev.asm -o bootloader.bin\n\
  ```\n\n...and dump the bytes of `bootloader.bin`, we can confirm that our bootloader file structure is as follows - 2 bytes\
  \ for the `jmp loop` instruction (`eb fe`) at offset 0, followed by 510 null bytes and 2 magic bytes `0x55aa` at the end,\
  \ making up a total of 512 bytes:\n\n![](<../../.gitbook/assets/image (764).png>)\n\n## Emulate the Bootloader\n\nWe can\
  \ now check if we can load our bootloader with qemu:\n\n```\ncd c:\\program files\\qemu\nqemu-system-x86_64.exe C:\\labs\\\
  bootloader\\bootloader.bin\n```\n\nBelow shows how our bootloader is executed from the hard disk and goes into an infinite\
  \ loop:\n\n![First valid bootloader running in Qemu](../../.gitbook/assets/emulate-bootloader.gif)\n\n## Bootloader Location\
  \ in Memory\n\nAs mentioned previously, BIOS reads in the boot sector (512 bytes), containing the bootloader, from a bootable\
  \ device into computer memory. It's known that bootloader gets stored at the memory location `0x7c00` as shown in the below\
  \ graphic:\n\n![Source: https://www.cs.bham.ac.uk/\\~exr/lectures/opsys/10\\_11/lectures/os-dev.pdf](<../../.gitbook/assets/image\
  \ (769).png>)\n\nWe can confirm that the bootloader code is placed at `0x7c00` by performing two simple tests.\n\n### Test\
  \ 1\n\nLet's take a look at the below code:\n\n{% code title=\"bootloader-x.asm\" %}\n```csharp\nbits 16\n\n; Define a label\
  \ X that is a memory offset of the start of our code.\n; It points to a character B.\nx:\n    db \"B\"\n\n; Move offset\
  \ of x to bx\nmov bx, x\n\n; Add 0x7c00 to bx - it's universally known that BIOS loads bootloaders to this location.\n;\
  \ add bx, 0x7c00\n\n; Move contents of bx to al\nmov al, [bx]\n\n; Prepare interrupt to print a character in TTY mode and\
  \ issue the interrupt.\nmov ah, 0x0e\nint 0x10                                                \n\ntimes 510 - ($-$$) db\
  \ 0\ndw 0xaa55\n```\n{% endcode %}\n\n{% hint style=\"info\" %}\nNote the line 12 with instrunctions `add bx, 0x7c00` is\
  \ commented out - we will uncomment it in Test 2 and confirm that the bootloader is indeed loaded at `0x7c00`.\n{% endhint\
  \ %}\n\n...which does the following:\n\n* Creates a label `X` that is a memory offset to the character `B` from **the start\
  \ of** **computer** **memory.** Important to highlight - label offset is not relative to the start of our code location\
  \ in memory, but from the start of computer memory.\n* Populate `bx` with the offset of the label `x` (0 in our case) with\
  \ the aim to make `bx` point to the character `B`.\n* Dereference `bx` (take the value from memory address pointed to by\
  \ the `bx`) and put it in `al`\n* Issue a BIOS interrupt and attempt to print the value of `al` to the screen, which one\
  \ could expect to be the character `B`, but as we will soon see, will not be the case.\n\n{% hint style=\"warning\" %}\n\
  **Remember**\\\nThe CPU treats assembly labels (like our label `x`) as offsets from the start of computer memory and not\
  \ from the start of the memory location where our code is loaded to.\n{% endhint %}\n\nWe can compile the above code with\
  \ `nasm -f bin .\\bootloader-x.asm -o bootloader.bin` and launch it with `qemu-system-x86_64.exe C:\\labs\\bootloader\\\
  bootloader.bin` and see the result:\n\n![B character not displayed](<../../.gitbook/assets/image (772).png>)\n\nNote how\
  \ instead of seeing the character `B`, we actually see a character `S`, which suggests that we are simply reading the wrong\
  \ memory location and our character `B` is not stored in memory where we thought it was.\n\nFor reference, this is a snippet\
  \ of the hex dump of our `bootloader.bin` we've just compiled:\n\n![](<../../.gitbook/assets/image (777).png>)\n\nIn the\
  \ above screenshot, note that the very first byte (offset 0 while it's on disk) is `42`, which is a letter `B` in ASCII\
  \ - the character our label `x` is pointing to, which we wanted to print to the screen with Test 1, but failed. Let's look\
  \ at the Test 2.\n\n### Test 2\n\nTest 1 confirmed that we do not know where the character `B` is located in memory. Let's\
  \ now take the same code we used in the Test 1 and uncomment the instruction `add bx, 0x7c00` in line 12, which adds `0x7c00`\
  \ to our label `x`:\n\n{% code title=\"bootloader-x.asm\" %}\n```cpp\nbits 16\n\n; Define a label X that is a memory offset\
  \ of the start of our code.\n; It points to a character B.\nx:\n    db \"B\"\n\n; Move offset of x to bx\nmov bx, x\n\n\
  ; Add 0x7c00 to bx - it's universally known that BIOS loads bootloaders to this location.\nadd bx, 0x7c00\n\n; Move contents\
  \ of bx to al\nmov al, [bx]\n\n; Prepare interrupt to print a character in TTY mode and issue the interrupt.\nmov ah, 0x0e\n\
  int 0x10                                                \n\ntimes 510 - ($-$$) db 0\ndw 0xaa55\n```\n{% endcode %}\n\n...and\
  \ re-compile the above code with `nasm -f bin .\\bootloader-x.asm -o bootloader.bin` and launch it with `qemu-system-x86_64.exe\
  \ C:\\labs\\bootloader\\bootloader.bin`:\n\n![B character is now displayed](<../../.gitbook/assets/image (771).png>)\n\n\
  ...we can now see that the character `B` is finally printed to the screen, which confirms that our bootlaoder code (and\
  \ the character `B`) is located at memory location `0x7c00`.\n\nIndeed, if we inspect the qemu process memory, that has\
  \ our bootloader loaded and running, search for the bytes `42bb 0000 8a07 b40e cd10 0000` (the starting bytes of our bootloader,\
  \ as seen in the hex dump on the right hand side highlighted in lime), we can see that our bootloader resides at 44D**07C00**:\n\
  \n![Our bootloader in memory (left) and on disk (right)](<../../.gitbook/assets/image (775).png>)\n\nNote that in the above\
  \ screenshot, the character `B` (in red) is our character `B` that we print to the screen, that sits at the start of our\
  \ bootloader - at offsets `0x0` in a raw binary on the disk and `0x07c00` when it's loaded to memory by the BIOS as a bootloader,\
  \ or in the case of emulation with qemu - at `0x44d`**`07c00`**.\n\n### `org 0x7c00` / NASM org directive\n\nTest 2 confirms\
  \ we now know where our bootloader is loaded in memory, but adding `0x7c00` to our operations each time we need to reference\
  \ some label is not ideal. Lukcily, we can instruct NASM to calculate offsets to the labels in our code in relation to the\
  \ memory address of our liking (i.e `0x7c00`), by utilising the directive `org 0x7c00`. This simply tells NASM that we expect\
  \ our program to be loaded at `0x7c00` and it's almost like we're saying to NASM: \"Hey, please keep in mind that we expect\
  \ this code to be located at `0x7c00`, so whenever you calculate any offsets for us, please calculate those in relation\
  \ to that `0x7c00` - much appreciated\".\n\nLet's take the code from Test 1 (with lines 14-15 comented out, that we uncommented\
  \ in the Test 2) and add `org 0x7c00` before our code - in line 4:\n\n```cpp\nbits 16\n\n; Tell NASM that we expect our\
  \ bootloader to be laoded at this address, hence offsets should be calculated in relation to this address\norg 0x7c00\n\n\
  ; Define a label X that is a memory offset of the start of our code.\n; It points to a character B.\nx:\n    db \"B\"\n\n\
  ; Move offset of x to bx\nmov bx, x\n\n; Add 0x7c00 to bx - it's universally known that BIOS loads bootloaders to this location.\n\
  ; add bx, 0x7c00\n\n; Move contents of bx to al\nmov al, [bx]\n\n; Prepare interrupt to print a character in TTY mode and\
  \ issue the interrupt\nmov ah, 0x0e\nint 0x10                                                \n\ntimes 510 - ($-$$) db 0\n\
  dw 0xaa55\n```\n\nCompile it, run it and check the results - the `B` character is still printed:\n\n![](<../../.gitbook/assets/image\
  \ (779).png>)\n\n## Baking Bootloader to USB Key + ASCII Art\n\nMalware is known to have tampered with a system's Master\
  \ Boot Records (MBR) in the past, so I wanted to see if I could bake my bootloader into a USB key and load it on my computer.\
  \ For this, I felt that some ASCII art was needed in order to make this exercise worthwile.\n\nBelow is the bootloader code\
  \ that draws some simple ASCII art:\n\n```cpp\n; Instruct NASM to generate code that is to be run on CPU that is running\
  \ in 16 bit mode\nbits 16\n\n; Tell NASM that we expect our bootloader to be laoded at this address, hence offsets should\
  \ be calculated in relation to this address\norg 0x7c00\n\n; Set background and foreground colour\nmov ah, 0x06    ; Clear\
  \ / scroll screen up function\nxor al, al      ; Number of lines by which to scroll up (00h = clear entire window)\nxor\
  \ cx, cx      ; Row,column of window's upper left corner\nmov dx, 0x184f  ; Row,column of window's lower right corner\n\
  mov bh, 0x4e    ; Background/foreground colour. In our case - red background / yellow foreground (https://en.wikipedia.org/wiki/BIOS_color_attributes)\n\
  int 0x10        ; Issue BIOS video services interrupt with function 0x06\n\n; Move label's bootloaderBanner memory address\
  \ to si\nmov si, bootloaderBanner\n; Put 0x0e to ah, which stands for \"Write Character in TTY mode\" when issuing a BIOS\
  \ Video Services interrupt 0x10\nmov ah, 0x0e\nloop:\n    ; Load byte at address si to al\n    lodsb\n    ; Check if al==0\
  \ / a NULL byte, meaning end of a C string\n    test al, al\n    ; If al==0, jump to end, where the bootloader will be halted\n\
  \    jz end\n    ; Issue a BIOS interrupt 0x10 for video services\n    int 0x10                                        \
  \        \n    ; Repeat\n    jmp loop\nend:\n    ; Halt the program until the next interrupt\n    hlt\nbootloaderBanner:\
  \ db \"          uuUUUUUUUUuu\",13,10,\"     uuUUUUUUUUUUUUUUUUUuu\",13,10,\"    uUUUUUUUUUUUUUUUUUUUUUu\",13,10,\"  uUUUUUUUUUUUUUUUUUUUUUUUUUu\"\
  ,13,10,\"  uUUUUUUUUUUUUUUUUUUUUUUUUUu\",13,10,\"  uUUUU       UUU       UUUUu\",13,10, \"   UUU        uUu        UUU\"\
  ,13,10,\"   UUUu      uUUUu     uUUU\",13,10,\"    UUUUuuUUU     UUUuuUUUU\",13,10, \"     UUUUUUU       UUUUUUU\",13,10,\
  \ \"       uUUUUUUUuUUUUUUUu\",13,10,\"           uUUUUUUUu\",13,10,\"         UUUUUuUuUuUUU\",13,10,\"           UUUUUUUUU\"\
  ,13,10,13,10,\"  Hacked by @spotheplanet at ired.team\", 0\n\n; Fill remaining space of the 512 bytes minus our instrunctions,\
  \ with 00 bytes\n; $ - address of the current instruction\n; $$ - address of the start of the image .text section we're\
  \ executing this code in\ntimes 510 - ($-$$) db 0\n; Bootloader magic number\ndw 0xaa55         \n```\n\n...which we can\
  \ now compile, dump the bytes to the USB key's (drive `D:\\` in my case) boot sector using `dd` utility on Linux or `HxD`\
  \ on Windows:\n\n![Bootloader.bin bytes written to the boot sector of our USB key D:\\\\](<../../.gitbook/assets/baking-bootloader-to-usb\
  \ (2).gif>)\n\nWe can now restart our computer and instruct it to boot from the USB, or reconfigure the BIOS bootable device\
  \ search order and make USB drives a priority.\n\nShortly, the BIOS will determine that our USB key contains a bootloader\
  \ and transfer CPU control to it, at which point, we will be greeted with our ASCII art:\n\n![Our bootloader running from\
  \ a USB stick](<../../.gitbook/assets/image (787).png>)\n\n## References\n\n[https://www.cs.bham.ac.uk/\\~exr/lectures/opsys/10\\\
  _11/lectures/os-dev.pdf](https://www.cs.bham.ac.uk/\\~exr/lectures/opsys/10\\_11/lectures/os-dev.pdf)\n\n{% embed url=\"\
  https://manybutfinite.com/post/how-computers-boot-up/\" %}\n\n{% embed url=\"https://www.ionos.com/digitalguide/server/configuration/what-is-a-bootloader/\"\
  \ %}\n\n{% embed url=\"https://github.com/cfenollosa/os-tutorial\" %}\n\n{% embed url=\"http://3zanders.co.uk/2017/10/13/writing-a-bootloader/\"\
  \ %}\n\n{% embed url=\"http://www.ctyme.com/intr/rb-0096.htm\" %}\n\n{% embed url=\"https://en.wikipedia.org/wiki/INT_10H\"\
  \ %}\n\n{% embed url=\"https://en.wikipedia.org/wiki/BIOS_color_attributes\" %}\n\n{% embed url=\"https://en.wikibooks.org/wiki/X86_Assembly/Bootloaders\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/writing-a-custom-bootloader.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/writing-a-custom-bootloader.md
````
