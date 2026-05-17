---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Manipulating ActiveProcessLinks to Hide Processes in Userland

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-manipulating-activeprocesslinks-to-unlink-processes-in-userland` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/manipulating-activeprocesslinks-to-unlink-processes-in-userland.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Manipulating ActiveProcessLinks to Hide Processes in Userland](../../topics/miscellaneous-reversing-forensics/manipulating-activeprocesslinks-to-hide-processes-in-userland.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-manipulating-activeprocesslinks-to-unlink-processes-in-userland |
| name | Manipulating ActiveProcessLinks to Hide Processes in Userland |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/manipulating-activeprocesslinks-to-unlink-processes-in-userland.md |

## Preserved Source Material

````yaml
_asset_filenames:
- hide-process.gif
- image (13).png
- image (190).png
- image (191).png
- image (193).png
- image (282).png
- image (285).png
- image (294).png
- image (318).png
- image (34).png
- image (366).png
- image (383).png
- image (431).png
- image (452).png
- image (455).png
- image (467).png
- image (471).png
- image (68).png
_body: "# Manipulating ActiveProcessLinks to Hide Processes in Userland\n\nThe purpose of this lab is to look into how Windows\
  \ kernel rootkits hide / unlink \\(or used to\\) processes in the userland for utilities trying to list all running processes\
  \ on the system such as `Windows Task Manager`, `tasklist` or `Get-Process` cmdlet in Powershell.\n\nThis is going to be\
  \ a high level overview and no kernel code will be written, instead, kernel memory structures will be manipulated manually\
  \ with WinDBG.\n\n{% hint style=\"info\" %}\nLab is performed on Windows 10 Professional x64, 1903.\n{% endhint %}\n\n**Update\
  \ 1**  \nSome replies to my tweet to this post suggested that PatchGuard would normally kick-in and BSOD the OS, which I\
  \ am sure is the case, although in my lab I experienced no BSODs even though the kernel stayed patched with an unlinked\
  \ process for 12+ hours.\n\n**Update 2**  \nI realized that my Windows VM is running in test mode with no integrity checks,\
  \ possibly explaining the lack os BSODs - unconfirmed.  \n  \n**Update 3**  \nThanks ****[**@**FuzzySec](https://twitter.com/FuzzySec)\
  \ for clarifying the BSOD/PatchGuard matter!\n\n![](../../.gitbook/assets/image%20%2834%29.png)\n\n## Key Structures\n\n\
  We need to be familiar with two kernel memory structures before we proceed.\n\n### \\_EPROCESS <a id=\"_eprocess\"></a>\n\
  \n`_EPROCESS` is a kernel memory structure that describes system processes \\(or in other words - each process running on\
  \ a system has its corresponding `_EPROCESS` object somewhere in the kernel\\) as we know them. It contains details such\
  \ as process image name, which desktop session it is running in, how many open handles to other kernel objects it has, what\
  \ access token it has and much more.\n\nBelow shows a snippet of the structure and a highlighted a member that is **key**\
  \ to this lab - `ActiveProcessLinks` . It is a pointer to a structure called `LIST_ENTRY`:\n\n```text\ndt _eprocess\n```\n\
  \n![](../../.gitbook/assets/image%20%28190%29.png)\n\n### \\_LIST\\_ENTRY\n\nIn programming, there is a data structure known\
  \ as `doubly-linked list` . It contains records \\(also called nodes\\) that are linked to each other, meaning each node\
  \ in the list contains two fields \\(hence doubly\\), that reference previous and the next record of that linked list.\n\
  \nSimplified \\(head and tail omitted\\) graphical representation of the doubly-linked list is shown below:\n\n![](../../.gitbook/assets/image%20%28285%29.png)\n\
  \n`LIST_ENTRY` is the doubly-linked list equivalent data structure in Windows kernel and is defined as: \n\n```erlang\n\
  kd> dt _list_entry\nntdll!_LIST_ENTRY\n   +0x000 Flink            : Ptr64 _LIST_ENTRY\n   +0x008 Blink            : Ptr64\
  \ _LIST_ENTRY\n```\n\n...where `FLINK` \\(forward link\\) and `BLINK` \\(backward link\\) are the equivalents of `Next`\
  \ and `Previous` references to the next and previous element in the list in our graphical representation of the doubly-linked\
  \ list discussed above.\n\n## LIST\\_ENTRY Importance\n\nAll Windows processes have their corresponding kernel objects in\
  \ the form of an EPROCESS kernel structure. All those EPROCESS objects are stored in a doubly-linked list.\n\nEffectively,\
  \ this means that when a `cmd /c tasklist` or `get-process` is invoked to get a list of all running processes on the system,\
  \ Windows walks through the doubly-linked list of EPROCESS nodes, utilizing the `LIST_ENTRY` structures and retrieves information\
  \ about all currently active processes.\n\nBelow is a simplified visualization of the above:\n\n![](../../.gitbook/assets/image%20%28455%29.png)\n\
  \n## Goal of the Lab\n\nWith all of the above information, we can now define what we're trying to do in the lab - we want\
  \ to hide a process of our choice from being shown in a process list when a `get-process` cmdlet or similar is issued in\
  \ the userland.\n\nBelow is a simplified diagram illustrating how this will be achieved by manually manipulating kernel\
  \ structures in WinDBG in order to hide the EPROCESS 2 \\(white\\):\n\n![](../../.gitbook/assets/image%20%28318%29.png)\n\
  \n* `ActiveProcessLinks.Flink` in EPROCESS 1 will be pointed to EPROCESS 3 `ActiveProcessLinks.Flink`\n* `ActiveProcessLinks.Blink`\
  \ in EPROCESS 3 will be pointed to EPROCESS 1 `ActiveProcessLinks.Flink`\n\nKernel memory manipulations will unlink the\
  \ EPROCESS 2 from the previous node \\(EPROCESS 1\\) and the next node \\(EPROCESS 3\\) in the doubly-linked list and, effectively,\
  \ render it invisible to all userland APIs that retrieve running system processes - exactly like Windows kernel rootkits\
  \ do it.\n\n## Walkthrough\n\n### Launching Target Process\n\nLet's launch a process that we will try to hide - a notepad.exe\
  \ in my case:\n\n![](../../.gitbook/assets/image%20%2868%29.png)\n\nIn kernel, we can get more information about our `notepad`\
  \ process like so:\n\n```erlang\nkd> !process e14 0\n```\n\nBelow shows that our notepad's corresponding `EPROCESS` structure\
  \ is located at `ffffb208f8b304c0`:\n\n![](../../.gitbook/assets/image%20%28471%29.png)\n\nChecking the EPROCESS structure\
  \ of our notepad:\n\n```erlang\nkd> dt _eprocess ffffb208f8b304c0\n```\n\n...we can see the `ActiveProcessLinks`, the doubly-linked\
  \ list, populated with two pointers \\(Flink and Blink\\):\n\n![](../../.gitbook/assets/image%20%28294%29.png)\n\nWe can\
  \ also read those values with `dt _list_entry ffffb208f8b304c0+2f0` or by dumping two 64-bit long values from `ffffb208f8b304c0+2f0`:\n\
  \n```erlang\nkd> dq ffffb208f8b304c0+2f0 L2\nffffb208`f8b307b0  ffffb208`f8d1e7b0 ffffb208`f8b89370\n```\n\n### Notepad's\
  \ Flink and Blink\n\nLet's now figure out the previous and next EPROCESS nodes our notepad.exe is pointing to.\n\nBelow\
  \ shows in two different ways \\(1. observing `ActiveProcessLinks` from the EPROCESS structure; 2. reading two 64-bit values\
  \ from the `EPROCESS+0x2f0`\\) that our notepad's:\n\n* FLINK \\(green\\) is pointing to ``ffffb208`f8d1e7b0`` \n* BLINK\
  \ \\(blue\\) is pointing to ``ffffb208`f8b89370``\n\n![](../../.gitbook/assets/image%20%28282%29.png)\n\nFor curiosity,\
  \ we can check the process's image name referenced by the notepad's FLINK at ``ffffb208`f8d1e7b0`` - the next EPROCESS node\
  \ to our notepad's EPROCESS: \n\nWe need to: \n\n* find the EPROCESS location by subtracting 0x2f0 from the FLINK ``ffffb208`f8d1e7b0``.\
  \ This is because FLINK points to `EPROCESS.ActiveProcessLinks` and `ActiveProcessLinks` is located at offset 0x2f0 from\
  \ the beginning of the EPROCESS location\n* add 0x450 since this is the offset of the `ImageFileName` in the EPROCESS structure\n\
  \n```erlang\nkd> da ffffb208`f8d1e7b0-2f0+450\n```\n\n![](../../.gitbook/assets/image%20%28431%29.png)\n\nLet's do the same\
  \ for the process referenced by the notepad's BLINK to get the previous EPROCESS node to our notepad's EPROCESS:\n\n```erlang\n\
  kd> da ffffb208`f8b89370-2f0+450\n```\n\n![](../../.gitbook/assets/image%20%28191%29.png)\n\nLooks like our notepad EPROCESS\
  \ is surrounded by two svchost EPROCESS nodes.\n\nContinuing, we can get PIDs of those two svchost.exe processes referenced\
  \ by FLINK and BLINK and they are `0x000009cc` and `0x00001464` respectively as shown below:\n\n```erlang\nkd> dd ffffb208`f8d1e7b0-2f0+2e8\
  \ L1\nffffb208`f8d1e7a8  000009cc\n\nkd> dd ffffb208`f8b89370-2f0+2e8 L1\nffffb208`f8b89368  00001464\n\nkd> !process 000009cc\
  \ 0\nSearching for Process with Cid == 9cc\nPROCESS ffffb208f8d1e4c0\n    SessionId: 0  Cid: 09cc    Peb: 44b2cd5000  ParentCid:\
  \ 025c\n    DirBase: 1e5730002  ObjectTable: 00000000  HandleCount:   0.\n    Image: svchost.exe\n\nkd> !process 00001464\
  \ 0\nSearching for Process with Cid == 1464\nPROCESS ffffb208f8b89080\n    SessionId: 0  Cid: 1464    Peb: a260bb6000  ParentCid:\
  \ 025c\n    DirBase: 19071002  ObjectTable: ffffc208ea7e4a80  HandleCount: 141.\n    Image: svchost.exe\n```\n\nBelow shows\
  \ essentially the same as the above output with some colour-coding: \n\n![](../../.gitbook/assets/image%20%2813%29.png)\n\
  \n...where highlighted in green is the svchost \\(0x09cc\\) referenced by notepad's FLINK and in blue is the svchost \\\
  (0x1464\\) referenced by notepad's BLINK.\n\n### Svchost 9cc Flink and Blink\n\nLet's get the FLINK and BLINK for the svchost.exe\
  \ \\(PID 0x9cc\\) and note that ``ffffb208`f8d1e7b0`` is the location of `EPROCESS.ActiveProcessLinks` which will be important\
  \ later:\n\n```erlang\nkd> dq ffffb208f8d1e4c0+2f0 L2\nffffb208`f8d1e7b0  ffffb208`f94ee7b0 ffffb208`f8b307b0\n\ndt _eprocess\
  \ ffffb208f8d1e4c0\n```\n\nGreen is FLINK and blue is BLINK:\n\n![](../../.gitbook/assets/image%20%28452%29.png)\n\n###\
  \ Svchost 1464 Flink and Blink\n\nLet's get FLINK and BLINK for the svchost.exe \\(PID 0x1464\\) and note that ``ffffb208`f8b89370``\
  \ is the location of `EPROCESS.ActiveProcessLinks` which will be important later:\n\n```erlang\nkd> dq ffffb208f8b89080+2f0\
  \ L2\nffffb208`f8b89370  ffffb208`f8b307b0 ffffb208`f96c97b0\n\nkd> dt _eprocess ffffb208f8b89080\n```\n\nGreen is FLINK\
  \ and blue is BLINK:\n\n![](../../.gitbook/assets/image%20%28193%29.png)\n\n### Unlinking the Notepad\n\nWe can now summarize\
  \ the FLINK and BLINK pointers we have for all the processes we are interested in:\n\n| Image | PID | EPROCESS | ActiveProcessLinks\
  \ | Flink | Blink |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n| svchost | 0x1464 | ffffb208f8b89080 | ffffb208\\`f8b89370\
  \ | ffffb208\\`f8b307b0 | ffffb208\\`f96c97b0 |\n| notepad | 0xe14  | ffffb208f8b304c0 | ffffb208\\`f8b307b0 | ffffb208\\\
  `f8d1e7b0 | ffffb208\\`f8b89370 |\n| svchost | 0x9cc | ffffb208f8d1e4c0 | ffffb208\\`f8d1e7b0 | ffffb208\\`f94ee7b0 | ffffb208\\\
  `f8b307b0 |\n\nBelow are the two kernel modifications we need to perform in order to hide notepad.exe from process listing\
  \ APIs in the userland:\n\n1. Point svchost's \\(0x1464\\) FLINK at ``ffffb208`f8b89370`` to svchost's \\(0x9cc\\) FLINK\
  \ at ``ffffb208`f8d1e7b0``\n2. Point svchost's \\(0x9cc\\) BLINK at ``ffffb208`f8d1e7b0+8`` \\(+8 because LIST\\_ENTRY is\
  \ two fields FLINK/BLINK and are 8 bytes each on x64\\) to svchost's \\(0x1464\\) FLINK at ``ffffb208`f8b89370``\n\nBelow\
  \ visualizes the above outlined steps:\n\n![](../../.gitbook/assets/image%20%28383%29.png)\n\nLet's perform the above mentioned\
  \ kernel modifications:\n\n```text\nkd> eq ffffb208`f8b89370 ffffb208`f8d1e7b0\nkd> eq ffffb208`f8d1e7b0+8 ffffb208`f8b89370\n\
  ```\n\n### Moment of Truth\n\nOnce the kernel memory is modified, we can run a `get-process` or `ps notepad` in powershell\
  \ and observe that notepad.exe has been successfully hidden:\n\n![notepad not seen when &quot;ps notepad&quot; is executed,\
  \ although notepad is still running in the foreground](../../.gitbook/assets/image%20%28467%29.png)\n\n...although it can\
  \ still be looked up by its PID in the kernel:\n\n```erlang\n!process e14 0\n```\n\n![](../../.gitbook/assets/image%20%28366%29.png)\n\
  \nBelow is another quick demo showing how notepad.exe disappears from the Windows Task Manager once the kernel memory is\
  \ tampered and the debugger is resumed. Additionally, `ps notepad` returns nothing, although notepad is visible in the taskbar\
  \ and underneath the Windows Task Manager:\n\n![](../../.gitbook/assets/hide-process.gif)\n\n{% hint style=\"info\" %}\n\
  In the above demo, memory offsets of structures are different due to a system reboot since the initial write up.\n{% endhint\
  \ %}\n\n## Detection\n\nIn order to detect unlinked processes exhibited by malware on systems without PatchGuard, explore\
  \ [`psscan`](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference#psscan) and [`psxview`](https://github.com/volatilityfoundation/volatility/wiki/Command-Reference-Mal#psxview)\
  \ from Volatility.\n\n## References\n\n{% embed url=\"https://www.aldeid.com/wiki/LIST\\_ENTRY\" %}\n\n{% embed url=\"https://www.hackerearth.com/practice/notes/doubly-linked-list-data-structure-in-c/\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel/manipulating-activeprocesslinks-to-unlink-processes-in-userland.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/manipulating-activeprocesslinks-to-unlink-processes-in-userland.md
````
