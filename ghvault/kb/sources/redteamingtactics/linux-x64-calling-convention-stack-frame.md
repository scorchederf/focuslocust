---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Linux x64 Calling Convention: Stack Frame

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-linux-x64-calling-convention-stack-frame` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Linux x64 Calling Convention: Stack Frame](../../topics/miscellaneous-reversing-forensics/linux-x64-calling-convention-stack-frame.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-linux-x64-calling-convention-stack-frame |
| name | Linux x64 Calling Convention: Stack Frame |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (866).png
- image (883).png
- image (884).png
- image (890).png
- image (891).png
- image (893).png
- image (894).png
- image (906).png
- image (911).png
_body: "# Linux x64 Calling Convention: Stack Frame\n\n## TL; DR\n\nIn 64-bit Linux system, function arguments of type integer/pointers\
  \ are passed to the callee function in the following way:\n\n* Arguments 1-6 are passed via registers RDI, RSI, RDX, RCX,\
  \ R8, R9 respectively;\n* Arguments 7 and above are pushed on to the stack.\n\nOnce inside the callee function:\n\n* Arguments\
  \ 1-6 are accessed via registers RDI, RSI, RDX, RCX, R8, R9 before they are modified or via  offsets from the RBP register\
  \ like so: `rbp - $offset`. For example, if the first argument passed to the callee is `int` (4 bytes) and there are no\
  \ local variables defined in the function, we could access it via `rbp - 0x4`;&#x20;\n* It's worth noting, that:\n  * if\
  \ the 1st argument was 8 bytes (for example, `long int`), we'd access it via `rbp - 0x8`;\n  * if the callee function had\
  \ 1 local variable defined that is smaller or equal to 16 bytes, the first argument of type `int` would be accessed via\
  \ `rbp - (0x10 + 0x4)` or simply `rbp - 0x14`;\n  * if the callee function had more than 16 bytes reserved for local variables,\
  \ we'd access the first argument of type `int` via `rbp - 0x24`, which suggests that with every 16 bytes worth of local\
  \ variables defined, the first argument is shifted by 0x10 bytes as shown [here](linux-x64-calling-convention-stack-frame.md#accessing-1st-argument);\n\
  * Argument 7 can be accessed via `rbp + 0x10`, argument 8 via `rbp + 0x18` and so on.\n\n{% hint style=\"warning\" %}\n\
  Conclusions listed above are based on the code sample and screenshots provided in the below sections.\n{% endhint %}\n\n\
  ## Code\n\nThis lab and conclusions are based on the following C program compiled on a 64-bit Linux machine:\n\n{% tabs\
  \ %}\n{% tab title=\"stack.c\" %}\n```cpp\n#include <stdio.h>\n\nint test(int a, int b, int c, int d, int e, int f, int\
  \ g, int h, int i)\n{\n    //int a2 = 0x555577;\n    return 1;\n}\n\nint main(int argc, char *argv[])\n{\n    test(0x1,\
  \ 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9);\n    return 1;\n}\n\n// compile with gcc stack.c -o stack\n```\n{% endtab %}\n\
  {% endtabs %}\n\n## How Arguments Are Passed\n\nLet's now see how arguments are passed from a caller to callee.\n\nBelow\
  \ is a screenshot that shows where the 9 arguments `0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9`  passed to the function\
  \ `test(int a, int b, int c, int d, int e, int f, int g, int h, int i)` end up in registers and the stack:\n\n![](<../../.gitbook/assets/image\
  \ (894).png>)\n\nBelow is a table that complements the above screenshot and shows where arguments live in registers and\
  \ on the stack and how they get there:\n\n| Argument # | Location   | Variable | Value | Colour |\n| ---------- | ----------\
  \ | -------- | ----- | ------ |\n| 1          | RDI        | a        | 0x1   | Red    |\n| 2          | RSI        | b\
  \        | 0x2   | Red    |\n| 3          | RDX        | c        | 0x3   | Red    |\n| 4          | RCX        | d    \
  \    | 0x4   | Red    |\n| 5          | R8         | e        | 0x5   | Orange |\n| 6          | R9         | f        |\
  \ 0x6   | Orange |\n| 7          | RSP + 0x10 | g        | 0x7   | Lime   |\n| 8          | RSP + 0x18 | h        | 0x8\
  \   | Lime   |\n| 9          | RSP + 0x20 | i        | 0x9   | Lime   |\n\n{% hint style=\"info\" %}\nSame applies to arguments\
  \ that are memory addresses/pointers.\n{% endhint %}\n\n## Stack Inside test()\n\nBelow shows how function's `test` stack\
  \ frame looks like on a 64-bit platform:\n\n![Stack frame x64 inside the function test()](<../../.gitbook/assets/image (891).png>)\n\
  \nAgain, note the following:\n\n* Arguments 1 - 6 are moved through the registers `edi`, `esi`, `edx`, `ecx`, `r8d`, `r9d`\
  \ (orange);\n* Arguments 7 - 9 are pushed to the stack via `push` (blue);\n\n### Accessing the 1st Argument & Local Variables\n\
  \nUntil now, our `test()` function did not have any local variables defined, so let's see how the stack changes once we\
  \ have some variables and how we can access them.\n\nIf the callee had a local variable defined, such as `int a1 = 0x555577`\
  \ (4 bytes, lime) as in our case shown below (lime), we'd access the first argument not via `rbp - 0x4` as it was the case\
  \ previously when the callee had no local variables, but via `rbp - 0x14` (i.e it shifted by 0x10 bytes, red):\n\n![First\
  \ argument (red) is now shifted by 0x10 on the stack and can be accessed via rbp - 0x14](<../../.gitbook/assets/image (893).png>)\n\
  \nBased on the above case, the `test()` function stack frame, would now look like this:\n\n![64-bit stack frame with 1 local\
  \ variable defined inside the callee function](<../../.gitbook/assets/image (890).png>)\n\n{% hint style=\"warning\" %}\n\
  Note that the 1st argument, that we previously could access via `rbp - 0x4` has been shifted up by 0x10 bytes and is now\
  \ accessible via `rbp - 0x14 `whereas the local variable is now at `rbp - 0x4` (where the 1st argument was when the function\
  \ did not have a local variable defined) followed by 0x10 bytes of padding.\n{% endhint %}\n\nFollowing the same principle\
  \ as outlined above, if the callee had more than 16 bytes of local variables defined (17 bytes in our case as shown in the\
  \ below screenshot), we'd now access the first argument via `rbp - 0x24` (i.e another 0x10 bytes shift from `rbp - 0x14`):\n\
  \n![First argument is shifted by 0x10 once again and can be accessed via rbp - 0x24](<../../.gitbook/assets/image (883).png>)\n\
  \nSimilarly, if the callee had more than 32 bytes of local variables defined (33 bytes in our case as shown in the below\
  \ screenshot), we'd now access the first argument via `rbp - 0x34` (i.e yet another 0x10 bytes  shift):\n\n![First argument\
  \ is shifted by 0x10 once again and can be accessed via rbp - 0x34](<../../.gitbook/assets/image (884).png>)\n\n...and so\
  \ on.\n\n## State Inside main()\n\nBelow captures program's state once inside `main()`:\n\n![RDI and RSI registers inside\
  \ main() contain argument count and argument values](<../../.gitbook/assets/image (866).png>)\n\nNote from the above screenshot:\n\
  \n* Lime - `RDI` contains the the count of arguments our program was launched with (`argc`);\n* Orange - `RSI` contains\
  \ the address to an array of arguments our program was run with (`argv[]`) and the first one (`argv[0]`), as expected, is\
  \ always the full path to the program itself, which is `/home/kali/labs/stack/stack` in our case.\n\nAlso, if we check what's\
  \ happening higher up at the stack, we will see that it contains the environment variables the program was started with:\n\
  \n![](<../../.gitbook/assets/image (906).png>)\n\nCombining all the above knowledge, we can get a general view of the stack\
  \ layout:\n\n![Stack layout for 64-bit program on 64-bit Linux system](<../../.gitbook/assets/image (911).png>)\n\n## References\n\
  \n{% embed url=\"https://revers.engineering/applied-re-the-stack/\" %}\n\n{% embed url=\"https://revers.engineering/applied-re-accelerated-assembly-p1/\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/linux-x64-calling-convention-stack-frame.md
````
