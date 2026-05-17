---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Process Environment Block

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-process-environment-block` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/process-environment-block.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Environment Block](../../topics/miscellaneous-reversing-forensics/process-environment-block.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-process-environment-block |
| name | Process Environment Block |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/process-environment-block.md |

## Preserved Source Material

````yaml
_asset_filenames:
- peb-baseimage.png
- peb-cmdline.png
- peb-cmdline2.png
- peb-cmdline3.png
- peb-dll-automated.gif
- peb-dll-automated2.gif
- peb-manual1.png
- peb-manual2.png
- peb-modulelist.png
- peb-modules2.png
- peb-overlay.png
- peb-structure (1).png
- peb.png
_body: "---\ndescription: Exploring a couple of interesting members of the PEB memory structure fields\n---\n\n# Process Environment\
  \ Block\n\nA very brief look into the PEB memory structure found, aiming to get a bit more comfortable with WinDBG and walking\
  \ memory structures.\n\n## Basics\n\nFirst of, checking what members the `_PEB` structure actually entails:\n\n```text\n\
  dt _peb\n```\n\nThere are many fields in the structure among which there are `ImageBaseAddresss` and `ProcessParameters`\
  \ which are interesting to us for this lab:\n\n![](../.gitbook/assets/peb-structure%20%281%29.png)\n\nGetting the PEB address\
  \ of the process:\n\n```bash\n0:001> r $peb\n$peb=000007fffffd5000\n```\n\nThe `_PEB` structure can now be overlaid on the\
  \ memory pointed to by the `$peb` to see what values the structure members are holding/pointing to:\n\n```bash\n0:001> dt\
  \ _peb @$peb\n```\n\n`_PEB` structure is now populated with the actual data pulled from the process memory:\n\n![](../.gitbook/assets/peb-overlay.png)\n\
  \nLet's check what's in memory at address `0000000049d40000` - pointed to by the `ImageBaseAddress` member of the `_peb`\
  \ structure:\n\n```cpp\n0:001> db 0000000049d40000 L100\n```\n\nExactly! This is the actual binary image of the running\
  \ process:\n\n![](../.gitbook/assets/peb-baseimage.png)\n\nAnother way of finding the `ImageBaseAddress` is:\n\n```csharp\n\
  0:001> dt _peb\nntdll!_PEB\n//snip\n      +0x010 ImageBaseAddress : Ptr64 Void\n//snip\n\n0:001> dd @$peb+0x010 L2\n000007ff`fffd5010\
  \  49d40000 00000000\n\n// 49d40000 00000000 is little-endian byte format - need to invert\n0:001> db 0000000049d40000 L100\n\
  ```\n\n## Convenience\n\nWe can forget about all of the above and just use:\n\n```text\n!peb\n```\n\nThis gets us a nicely\
  \ formatted PEB information of some of the key members of the structure:\n\n![](../.gitbook/assets/peb.png)\n\n## Finding\
  \ Commandline Arguments\n\nOne of the interesting fields the PEB holds is the process commandline arguments. Let's find\
  \ them:\n\n```cpp\ndt _peb @$peb processp*\nntdll!_PEB\n   +0x020 ProcessParameters : 0x00000000`002a1f40 _RTL_USER_PROCESS_PARAMETERS\n\
  \ndt _RTL_USER_PROCESS_PARAMETERS 0x00000000`002a1f40\n```\n\n![](../.gitbook/assets/peb-cmdline.png)\n\nWe can be more\
  \ direct and ask the same question like so:\n\n```cpp\n0:001> dt _UNICODE_STRING 0x00000000`002a1f40+70\nntdll!_UNICODE_STRING\n\
  \ \"\"C:\\Windows\\system32\\cmd.exe\" \"\n   +0x000 Length           : 0x3c\n   +0x002 MaximumLength    : 0x3e\n   +0x008\
  \ Buffer           : 0x00000000`002a283c  \"\"C:\\Windows\\system32\\cmd.exe\" \"\n```\n\nor even this:\n\n```cpp\n0:001>\
  \ dd 0x00000000`002a1f40+70+8 L2\n00000000`002a1fb8  002a283c 00000000\n0:001> du 00000000002a283c\n00000000`002a283c  \"\
  \"C:\\Windows\\system32\\cmd.exe\" \"\n```\n\n![](../.gitbook/assets/peb-cmdline2.png)\n\nSince we now know where the commandline\
  \ arguments are stored - can we modify them? Of course.\n\n## Forging Commandline Arguments\n\n```cpp\n0:001> eu 00000000002a283c\
  \ \"cmdline-logging? Are You Sure?\"\n```\n\n![](../.gitbook/assets/peb-cmdline3.png)\n\n## \\_PEB\\_LDR\\_DATA <a id=\"\
  _peb_ldr_data-structure\"></a>\n\nGetting a list of loaded modules \\(exe/dll\\) by the process:\n\n```cpp\n// get the first\
  \ _LIST_ENTRY structure address\n0:001> dt _peb @$peb ldr->InMemoryOrderModuleList*\nntdll!_PEB\n   +0x018 Ldr         \
  \                 : \n      +0x020 InMemoryOrderModuleList      : _LIST_ENTRY [ 0x00000000`002a2980 - 0x00000000`002a1e40\
  \ ]\n\n\n// walking the list manually and getting loaded module info\ndt _LIST_ENTRY 0x00000000`002a2980\n// cmd module\n\
  dt _LDR_DATA_TABLE_ENTRY 0x00000000`002a2980\n\ndt _LIST_ENTRY 0x00000000`002a2980 \n// ntdll module\ndt _LDR_DATA_TABLE_ENTRY\
  \ 0x00000000`002a2a70\n\ndt _LIST_ENTRY 0x00000000`002a2a70\n// kernel32 module\ndt _LDR_DATA_TABLE_ENTRY 0x00000000`002a2df0\n\
  \n...loop...\n```\n\n![](../.gitbook/assets/peb-modulelist.png)\n\nIf we check the loaded modules with `!peb`, it shows\
  \ we were walking the list correctly:\n\n![](../.gitbook/assets/peb-modules2.png)\n\nHere is another way to find the first\
  \ `_LDR_DATA_TABLE_ENTRY`:\n\n```cpp\ndt _peb @$peb\ndt _PEB_LDR_DATA 0x00000000`774ed640\n```\n\n![](../.gitbook/assets/peb-manual1.png)\n\
  \n```cpp\ndt _LDR_DATA_TABLE_ENTRY 0x00000000`002a2980\n```\n\n![](../.gitbook/assets/peb-manual2.png)\n\nA nice way of\
  \ getting a list of linked-list structure addresses is by providing address of the first `list_entry` structure to the command\
  \ `dl` and specifying how many list items it should print out:\n\n```cpp\n0:001> dl 0x00000000`002a2980 6\n00000000`002a2980\
  \  00000000`002a2a70 00000000`774ed660\n00000000`002a2990  00000000`00000000 00000000`00000000\n00000000`002a2a70  00000000`002a2df0\
  \ 00000000`002a2980\n00000000`002a2a80  00000000`002a2f70 00000000`774ed670\n00000000`002a2df0  00000000`002a2f60 00000000`002a2a70\n\
  00000000`002a2e00  00000000`002a3cb0 00000000`002a2f70\n00000000`002a2f60  00000000`002a3ca0 00000000`002a2df0\n00000000`002a2f70\
  \  00000000`002a2e00 00000000`002a2a80\n00000000`002a3ca0  00000000`002a41f0 00000000`002a2f60\n00000000`002a3cb0  00000000`002defc0\
  \ 00000000`002a2e00\n00000000`002a41f0  00000000`002a3ff0 00000000`002a3ca0\n00000000`002a4200  00000000`002e1320 00000000`002a4000\n\
  ```\n\nAnother way of achieving the same would be to use the !list command to list through the list items and dump the info:\n\
  \n```cpp\n!list -x \"dt _LDR_DATA_TABLE_ENTRY\" 0x00000000`002a2980\n```\n\n![](../.gitbook/assets/peb-dll-automated.gif)\n\
  \nContinuing further:\n\n![](../.gitbook/assets/peb-dll-automated2.gif)\n\n## Abusing PEB\n\nIt is possible to abuse the\
  \ PEB structure and masquerade one windows processes with another process. See this lab for more:\n\n{% page-ref page=\"\
  ../offensive-security/defense-evasion/masquerading-processes-in-userland-through-\\_peb.md\" %}\n\n## References\n\n{% embed\
  \ url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winternl/ns-winternl-\\_peb\\_ldr\\_data\" %}\n\n{% embed url=\"\
  http://windbg.info/doc/1-common-cmds.html\\#13\\_breakpoints\" %}\n\n{% embed url=\"https://www.aldeid.com/wiki/PEB\\_LDR\\\
  _DATA\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/-list\" %}\n\n{% embed url=\"\
  https://docs.microsoft.com/en-us/windows/desktop/api/winternl/ns-winternl-\\_peb\\_ldr\\_data\" %}\n\n{% embed url=\"http://jumpdollar.blogspot.com/2014/08/windbg-peb-command.html\"\
  \ %}\n\n{% embed url=\"http://jumpdollar.blogspot.com/search/label/.process\" %}"
_relative_path: miscellaneous-reversing-forensics/process-environment-block.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/process-environment-block.md
````
