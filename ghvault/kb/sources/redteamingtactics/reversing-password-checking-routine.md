---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Reversing Password Checking Routine

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-reversing-password-checking-routine` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/reversing-password-checking-routine.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reversing Password Checking Routine](../../topics/miscellaneous-reversing-forensics/reversing-password-checking-routine.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-reversing-password-checking-routine |
| name | Reversing Password Checking Routine |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/reversing-password-checking-routine.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-12-19 12-43-29.png
- Screenshot from 2018-12-19 12-47-01.png
- Screenshot from 2018-12-19 12-47-37.png
- Screenshot from 2018-12-19 13-22-04.png
- Screenshot from 2018-12-19 13-29-31 (1).png
- Screenshot from 2018-12-19 13-30-49.png
- Screenshot from 2018-12-19 13-33-13.png
- Screenshot from 2018-12-19 13-38-14.png
- Screenshot from 2018-12-19 13-43-00.png
- Screenshot from 2018-12-19 13-43-39.png
- Screenshot from 2018-12-19 14-27-02.png
- Screenshot from 2018-12-19 14-47-40.png
_body: "# Reversing Password Checking Routine\n\n## Context\n\nA couple of my internet fellas were working on a CTF that presented\
  \ them a binary file, which had the flag inside they had to retrieve. I jumped on this without expecting much, but anyway.\n\
  \n## Triage\n\nI did a quick `file bin` to check what type of file it was:\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19\
  \ 12-43-29.png>)\n\nThe file was a non-stripped out linux binary file, which means debugging will be easier since we will\
  \ be able to see original function names used in the binary.\n\n## Strings\n\nI ran the file through strings `strings bin`\
  \ to see if anything stood out:\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19 12-47-01.png>)\n\nWe can notice some\
  \ interesting things that we can make some assumptions about - notably the following strings:\n\n* ACCESS GRANTED/ACCESS\
  \ DENIED - possibly will need to enter a password somewhere in the binary and these messages will be printed to the user\
  \ depending on if the provded password is correct/incorrect.\n* some long strings - maybe something interesting encoded\
  \ here or maybe those strings are used as part of the password decryption algorithm?\n* a string `%32s` - maybe a C string\
  \ output format (32 characters)?\n\nSimply running the file prompted for a password and failed with an error message `ACCESS\
  \ DENIED`:\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19 12-47-37.png>)\n\n## Disassembly\n\nLet's have a quick\
  \ look at the disassembly of the file and look at its `main` function:\n\n```\nobjdump -d bin | more\n```\n\n![](<../.gitbook/assets/Screenshot\
  \ from 2018-12-19 13-22-04.png>)\n\nNote the following from the above screenshot:\n\n* We can see that at offset `b14` (cyan)\
  \ there is a C function `scanf` called which reads from the standard input.\n* instruction at `b20` (orange) calls a `check_pw`\
  \ routine - we can assume that the input captured from the instruction at `b14` will be passed to `check_pw` function to\
  \ decide if the string received from the standard input matches the password the binary is protected with or not\n* instruction\
  \ at `b25` carries out a check against the `eax` register and based on if eax==0 or eax!=0, it will  either take a jump\
  \ to instructions at `b27` (if eax==0) or continue executing instructions at `b29` if eax!=0. Pressumably, the jumps are\
  \ carried out based on if the provided password is correct or incorrect.\n\n## GDB\n\n* Let's look at the file through GDB\
  \ with Peda plugin\n  * Let's set a break point on the main function&#x20;\n  * Do a quick `disas` of the `main` function\
  \ to remind ourselves once again what the routine for password checking was\n  * Let's set a breakpoint `check_pw` routine\
  \ as well\n\n```\ngdb bin\nb main\ndisas\nb check_pw\n```\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19 13-29-31\
  \ (1).png>)\n\nLet's hit `c` to continue running the program until the `scanf` function is called and then provide it with\
  \ some dummy password, say `test`:\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19 14-27-02.png>)\n\n### Check\\_pw\
  \ Routine: Round 1\n\nOnce the password is entered, the program breaks on `check_pw`:\n\n![](<../.gitbook/assets/Screenshot\
  \ from 2018-12-19 13-30-49.png>)\n\nIf we skip through instructions one by one and keep observing how register values change\
  \ over time and what instructions are executed, we will soon end up at `check_pw+88`:\n\n![](<../.gitbook/assets/Screenshot\
  \ from 2018-12-19 13-33-13.png>)\n\nNote this from the above screenshot:\n\n* current instruction at `check_pw+88: cmp dl,\
  \ al` - al and dl register values are being compared\n* register `rax` and `rdx` values are `b` and `t` respectively (organge\
  \ at the top). If you followed the register values whilst stepping through the code, you would notice that the value in\
  \ the rdx is actually the first letter of our password **`t`**`est`. Having said this, it looks like the binary is checking\
  \ if the first character of the  provided password is actually an ascii **`b`**\n* If `dl==al`, the code should jump to\
  \ `check_pw+99` as seen at offset `check_pw+90`\n\nHowever, stepping through the instructions further, we can see that the\
  \ jump is NOT taken - the program continues executing instructions at offset `check_pw+92` - suggesting the first character\
  \ of the password does NOT start with a **`t`**:\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19 13-43-00.png>)\n\n\
  ### Check\\_pw Routine: Round 2\n\nWhat if we rerun the program and supply it with a password **`b`**`est` this time (replacing\
  \ the first `t` with `b`, since the binary seemed to be expecting to see in the `dl` register)?\n\nWell, this time the `cmp\
  \ al,dl` sets the `zero` flag to `true` and the jump at `check_pw+90` is taken - suggesting that the first character of\
  \ the password is indeed a **`b`**:\n\n![](<../.gitbook/assets/Screenshot from 2018-12-19 13-38-14.png>)\n\nIf we repeat\
  \ this process 32 more times (remember the `%32s` string discussed previously?), we will eventually get the full password:\n\
  \n![](<../.gitbook/assets/Screenshot from 2018-12-19 13-43-39.png>)\n\nGoing back to the long strings we saw earlier - they\
  \ were indeed used in the password decryption routine, but going through the algorithm is out of scope for today:\n\n![](<../.gitbook/assets/Screenshot\
  \ from 2018-12-19 14-47-40.png>)\n\nNow, there is probably a better/automated way of solving this, so if you know a better\
  \ way, I would like to hear about it!"
_relative_path: miscellaneous-reversing-forensics/reversing-password-checking-routine.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/reversing-password-checking-routine.md
````
