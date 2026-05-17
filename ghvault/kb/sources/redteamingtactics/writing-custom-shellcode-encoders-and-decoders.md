---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Writing Custom Shellcode Encoders and Decoders

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-writing-custom-shellcode-encoders-and-decoders` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/writing-custom-shellcode-encoders-and-decoders.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Writing Custom Shellcode Encoders and Decoders](../../topics/offensive-security/writing-custom-shellcode-encoders-and-decoders.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-writing-custom-shellcode-encoders-and-decoders |
| name | Writing Custom Shellcode Encoders and Decoders |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/writing-custom-shellcode-encoders-and-decoders.md |

## Preserved Source Material

````yaml
_asset_filenames:
- decoding-shellcode.gif
- follow-in-dump.gif
- image (659).png
- image (661).png
- image (662).png
- image (663).png
- image (664).png
- image (665).png
- image (666).png
- image (668).png
- make-memory-executable.gif
- pasting-in-shellcode.gif
- setting-new-origin.gif
_body: "# Writing Custom Shellcode Encoders and Decoders\n\nThe purpose of this lab is to get a bit more comfortable with\
  \ writing primitive custom shellcode encoders and decoders.\n\nShellcode encoding simply means transforming original shellcode\
  \ bytes into a set of arbitrary bytes by following some rules (encoding scheme), that can be later be reverted back to their\
  \ original values by following the same rules (decoding scheme) in reverse.\n\n{% hint style=\"success\" %}\nShellcode encoding\
  \ may be useful in evading static antivirus signatures and eliminating null bytes.\n{% endhint %}\n\n## Encoder\n\n### Raw\
  \ Shellcode\n\nTo make it simple, for this lab, let's imagine that our raw shellcode (before encoding) is made of the following\
  \ bytes:\n\n```csharp\n$shellcode = 0x6F,0x72,0x69,0x67,0x69,0x6E,0x61,0x6C,0x20,0x73,0x68,0x65,0x6C,0x6C,0x63,0x6F,0x64,0x65\n\
  ```\n\n...which is actually just a simple string `original shellcode` as you can see here:\n\n![](<../../.gitbook/assets/image\
  \ (659).png>)\n\n### Encoding Scheme\n\nNow that we have the raw shellcode bytes, we need to decide on the algorithm that\
  \ defines how each byte of the raw shellcode should be encoded/transformed. There's many ways to do it, but for this lab,\
  \ let's define our encoding steps like this:\n\n1. xor with 0x55\n2. increment by 1\n3. xor with  0x11\n\n### The Encoder\
  \ Itself\n\nLet's write a simple powershell script that will help us cycle through the raw shellcode bytes and encode them\
  \ by performing operations defined in our encoding scheme:\n\n```csharp\n<#\n    Encoding steps:\n    1. xor with 0x55\n\
  \    2. increment by 1\n    3. xor with 0x11\n#>\n\n# Original raw shellcode bytes\n$shellcode = 0x6F,0x72,0x69,0x67,0x69,0x6E,0x61,0x6C,0x20,0x73,0x68,0x65,0x6C,0x6C,0x63,0x6F,0x64,0x65\n\
  $printFriendly = ($shellcode | ForEach-Object ToString x2) -join ',0x'\nwrite-host \"Original shellcode: 0x$printFriendly\"\
  \n\n# Iterate through shellcode bytes and encode them\n$encodedShellcode = $shellcode | % {\n    $_ = $_ -bxor 0x55\n  \
  \  $_ = $_ + 0x1\n    $_ = $_ -bxor 0x11\n    Write-Output $_\n}\n\n# Print encoded shellcode\n$printFriendly = ($encodedShellcode\
  \ | ForEach-Object ToString x2) -join ',0x'\nwrite-host \"Encoded shellcode: 0x$printFriendly\"\n\n# Print encoded bytes\
  \ size\nwrite-host \"Size: \" ('0x{0:x}' -f $shellcode.count)\n\n# Check if encoded shellcode contains null bytes\nwrite-host\
  \ \"Contains NULL-bytes:\" $encodedShellcode.contains(0)\n```\n\nIf we run the encoder on our shellcode bytes `0x6F,0x72,0x69,0x67,0x69,0x6E,0x61,0x6C,0x20,0x73,0x68,0x65,0x6C,0x6C,0x63,0x6F,0x64,0x65`,\
  \ it will spit out the encoded shellcode bytes (lime) and show if null bytes were found (lime):\n\n![](<../../.gitbook/assets/image\
  \ (661).png>)\n\nNote that it also shows the shellcode size (orange) - we will need it later when writing a decoder, so\
  \ that we can tell the decoder how many shellcode bytes it should process.\n\n## Decoder\n\n### Decoding Scheme\n\nThe decoding\
  \ scheme is the same as the encoding scheme, only in reverse:\n\n![](<../../.gitbook/assets/image (668).png>)\n\n...which\
  \ means that we will have to iterate through all the encoded bytes of the shellcode and transform them into original bytes\
  \ like this:\n\n1. xor with 0x11\n2. decrement by 0x1 (because we incremented when encoding, we need to decrement now)\n\
  3. xor with 0x55\n\nA fully commented NASM `decoder.asm` is here:\n\n{% code title=\"decoder.asm\" %}\n```cpp\nglobal _start\n\
  \nsection .text\n    _start:\n        jmp short shellcode\n\n    decoder:\n        pop rax                 ; store encodedShellcode\
  \ address in rax - this is the address that we will jump to once all the bytes in the encodedShellcode have been decoded\n\
  \n    setup:\n        xor rcx, rcx            ; reset rcx to 0, will use this as a loop counter\n        mov rdx, 0x12 \
  \          ; shellcode size is 18 bytes\n\n    decoderStub:\n        cmp rcx, rdx            ; check if we've iterated and\
  \ decoded all the encoded bytes\n        je encodedShellcode     ; jump to the encodedShellcode, which actually now contains\
  \ the decoded shellcode\n        \n        ; encodedShellcode bytes are being decoded here per our decoding scheme\n   \
  \     xor byte [rax], 0x11    ; 1. xor byte with 0x11\n        dec byte [rax]          ; 2. decremenet byte by 1\n     \
  \   xor byte [rax], 0x55    ; 3. xor byte with 0x55\n        \n        inc rax                 ; point rax to the next encoded\
  \ byte in encodedShellcode\n        inc rcx                 ; increase loop counter\n        jmp short decoderStub   ; repeat\
  \ decoding procedure\n            \n    shellcode:\n        call decoder            ; jump to decoder label. This pushes\
  \ the address of encodedShellcode to the stack (to be popped into rax as the first instruction under the decoder label)\n\
  \        encodedShellcode: db 0x2a,0x39,0x2c,0x22,0x2c,0x2d,0x24,0x2b,0x67,0x36,0x2f,0x20,0x2b,0x2b,0x26,0x2a,0x23,0x20\n\
  ```\n{% endcode %}\n\n{% hint style=\"info\" %}\nNote that line 12 contains the shellcode size - `0x12` - the value that\
  \ was printed out by our `encoder.ps1`\n{% endhint %}\n\n### Assembling the Decoder\n\nLet's assemble our `decoder.asm`\
  \ with nasm:\n\n```\nnasm -f win64 .\\decoder.asm -o .\\decoder\n```\n\n### Extracting Decoder Op-Codes\n\nThe decoder file\
  \ assembled in the previous step, contains our decoder's bytes / op-codes (and our encoded shellcode) that can be executed\
  \ by the CPU once in process's executable memory. We need to extract them if we want to inject and execute those bytes as\
  \ shellcode.\n\nFor the sake of simplicity, let's do this manually by loading the assembled `decoder` file into the CFF\
  \ Explorer's `Quick Disassembler` and compare it with our assembly instructions in `decoder.asm`.\n\nWe can clearly see\
  \ that the op-codes of our decoder start at `0x3C` into the file assembled file:\n\n![](<../../.gitbook/assets/image (662).png>)\n\
  \nLet's switch to the Hex Editor and we can copy (right click on the selected bytes) the decoder bytes (for this lab, we\
  \ will go with a Hex format), starting at `0x3c` (blue) and ending with the last byte of our encoded shellcode `0x20` (red):\n\
  \n![](<../../.gitbook/assets/image (663).png>)\n\n## Confirming It Worked\n\nNow that we've extracted our decoder's (that\
  \ includes our encoded shellcode) op-codes, let's check if we can make them execute and see our encoded shellcode get decoded\
  \ and launched.\n\n{% hint style=\"warning\" %}\n**Reminder** \\\nOur decoded shellcode will not execute as it's simply\
  \ an ascii string `original shellcode`, but it would if it was actual executable code.\n{% endhint %}\n\nTo keep things\
  \ simple, let's fire up x64dbg and attach it to a new instance of notepad.exe - this is the process that we will be executing\
  \ our decoder in - and hit F9 so that we break at the entry point:\n\n![](<../../.gitbook/assets/image (664).png>)\n\n###\
  \ Changing Memory Permissions\n\nOnce at the entry point, let's change the memory permissions for the `.text` section, so\
  \ we can demo this decoder:\n\n1. Right click the instruction address and `Follow in Memory Map`\n2. Right click the `.text`\
  \ section and `Set Page Memory Rights`\n3. Ensure `Select Full Access` is selected and hit `Set Rights`\n\n![](../../.gitbook/assets/make-memory-executable.gif)\n\
  \n### Pasting The Bytes\n\nOnce the permissions are set, jump to the `.text` section with right click + `Follow in Disassembler`:\n\
  \n![](<../../.gitbook/assets/image (665).png>)\n\nSelect enough instructions that could be replaced with our shellcode bytes,\
  \ hit Ctrl + E (Binary Edit) and paste the extracted decoder op-codes there:\n\n![](../../.gitbook/assets/pasting-in-shellcode.gif)\n\
  \n### Changing RIP\n\nSet the instruction pointer RIP to the location we've just pasted our shellcode to:\n\n![](../../.gitbook/assets/setting-new-origin.gif)\n\
  \n### Following Memory Dump\n\nLet's now follow the same address we've pasted the bytes to in the Memoy Dump too, so we\
  \ can see how our shellcode is getting decoded as we step through the decoding stub:\n\n![](../../.gitbook/assets/follow-in-dump.gif)\n\
  \n### Decoding in Action\n\nWe can finally execute our decoder by repeatedly hitting F7 and observe how our shellcode gets\
  \ decoded and the initial string `original shellcode` is being revealed in the memory dump view:\n\n![](../../.gitbook/assets/decoding-shellcode.gif)\n\
  \nNote that after the decoding has completed, the code is transferred to our decoded shellcode:\n\n![](<../../.gitbook/assets/image\
  \ (666).png>)"
_relative_path: offensive-security/code-injection-process-injection/writing-custom-shellcode-encoders-and-decoders.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/writing-custom-shellcode-encoders-and-decoders.md
````
