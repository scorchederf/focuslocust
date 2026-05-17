---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Exploring Injected Threads

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-get-injectedthread` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/get-injectedthread.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exploring Injected Threads](../../topics/miscellaneous-reversing-forensics/exploring-injected-threads.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-get-injectedthread |
| name | Exploring Injected Threads |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/get-injectedthread.md |

## Preserved Source Material

````yaml
_asset_filenames:
- injected-threads-address.png
- injected-threads-explorer-injected.png
- injected-threads-get-injected-thread.png
- injected-threads-inspection.png
- injected-threads-shellcode.png
- injected-threads-shellcode2.png
- injected-threads-threadid-windbg.png
- injected-threads-threadid.png
_body: "---\ndescription: >-\n  A short exploration of injected threads with Get-InjectedThreads.ps1 and\n  WinDBG\n---\n\n\
  # Exploring Injected Threads\n\n## Injecting Shellcode\n\nFirstly, let's use an [injector](../../offensive-security/code-injection-process-injection/process-injection.md)\
  \ program we wrote earlier to inject some shellcode into a process that will give us a reverse shell. In this case, we are\
  \ injecting the shellcode into explorer.exe:\n\n![](../../.gitbook/assets/injected-threads-explorer-injected.png)\n\n##\
  \ Detecting Injection\n\nNow that we have injected the code into a new thread of the explorer.exe process, let's scan all\
  \ the running processes for any injected threads using [Get-InjectedThreads.ps1](https://gist.github.com/jaredcatkinson/23905d34537ce4b5b1818c3e6405c1d2):\n\
  \n```csharp\n$a = Get-InjectedThread; $a\n```\n\nLooks like the injected thread was successfully detected:\n\n![](../../.gitbook/assets/injected-threads-get-injected-thread.png)\n\
  \n## Cross-checking Shellcode\n\nLets check the payload found in the injected thread:\n\n```csharp\n($a.Bytes | ForEach-Object\
  \ tostring x2) -join \"\\x\"\n```\n\n![](../../.gitbook/assets/injected-threads-shellcode2.png)\n\nand cross-verify it with\
  \ the shellcode specified in our injector binary. We see they match as expected:\n\n![](../../.gitbook/assets/injected-threads-shellcode.png)\n\
  \n## Inspecting with WinDBG\n\nIn order to inspect the newly created thread that executes the above shellcode with WinDBG,\
  \ we need to know the injected thread id. For this, we use Process Explorer and note the newly created thread's ID which\
  \ is `2112`. Note the `ThreadId` is also shown in the output of Get-InjectedThread powershell script:\n\n![](../../.gitbook/assets/injected-threads-threadid.png)\n\
  \nWe can get all the threads for a process being debugged in WinDBG with `~` command:\n\n![](../../.gitbook/assets/injected-threads-threadid-windbg.png)\n\
  \nAdditionally, in order to inspect the bytes stored/executed in the injected thread, we need to get the thread's `StartAddress`\
  \ which can be retrieved with  `~.` command when in the context of the thread of interest.\n\nBelow graphic shows the injected\
  \ thread's contents with WinDBG:\n\n![Injected thread id + StartAddress + content bytes](../../.gitbook/assets/injected-threads-inspection.png)\n\
  \nThe above also highlights the thread `0x1494 = 5268` ID. That thread is then inspected for its `StartAddress`, which happened\
  \ to be `0x03730000 = 57868288`.&#x20;\n\nFor reference, the original shellcode bytes are displayed in the upper right corner.\
  \ Bottom right corner shows the output of the `Get-InjectedThreads` indicating `ThreadId` and `StartAddress` in decimal.\n\
  \n## How Get-InjectedThreads detects code injection?\n\nOne of the things Get-InjectedThreads does in order to detect code\
  \ injection is:&#x20;\n\n* it enumerates all the threads in each running process on the system\n* performs the following\
  \ checks on memory regions holding those threads: `MemoryType == MEM_IMAGE && MemoryState == MEM_COMMIT`&#x20;\n* If the\
  \ condition is not met, it means that the code, running from the thread being inspected, does not have a corresponding image\
  \ file on the disk, suggesting the code may be injected directly to memory.\n\nBelow graphic shows details of the memory\
  \ region containing the injected thread using WinDBG and Get-InjectedThreads. Note the Type/MemoryType and State/MemoryState\
  \ in WinDBG/Get-InjectedThreads outputs respectively:\n\n![](../../.gitbook/assets/injected-threads-address.png)\n\n## References\n\
  \n{% embed url=\"https://posts.specterops.io/defenders-think-in-graphs-too-part-1-572524c71e91\" %}\n\n{% embed url=\"https://blog.xpnsec.com/undersanding-and-evading-get-injectedthread/\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winnt/ns-winnt-_memory_basic_information\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/get-injectedthread.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/get-injectedthread.md
````
