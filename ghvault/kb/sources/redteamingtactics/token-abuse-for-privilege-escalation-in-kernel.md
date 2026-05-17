---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Token Abuse for Privilege Escalation in Kernel

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-how-kernel-exploits-abuse-tokens-for-privilege-escalation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/how-kernel-exploits-abuse-tokens-for-privilege-escalation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Token Abuse for Privilege Escalation in Kernel](../../topics/miscellaneous-reversing-forensics/token-abuse-for-privilege-escalation-in-kernel.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-how-kernel-exploits-abuse-tokens-for-privilege-escalation |
| name | Token Abuse for Privilege Escalation in Kernel |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel/how-kernel-exploits-abuse-tokens-for-privilege-escalation.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (125).png
- image (154).png
- image (202).png
- image (232).png
- image (258).png
- image (326).png
- image (352).png
- image (409).png
- image (417).png
- image (439).png
- image (460).png
- image (48).png
- image (506).png
- image (514).png
- image (64).png
- image (73).png
- image (78).png
- replace-token.gif
_body: "# Token Abuse for Privilege Escalation in Kernel\n\nThe purpose of this lab is to understand at a high level \\(will\
  \ not be writing any kernel code, rather playing around with WinDBG\\) how kernel exploits abuse tokens for privilege escalation.\
  \ \n\nI will look briefly into two techniques:\n\n* [Token stealing/replacement](how-kernel-exploits-abuse-tokens-for-privilege-escalation.md#1-replacing-tokens-for-privilege-escalation)\
  \ - low privileged token is replaced with a high privileged token\n* [Token privilege adjustment](how-kernel-exploits-abuse-tokens-for-privilege-escalation.md#2-modifying-token-privileges)\
  \ - adding and enabling more privileges to an existing token\n\n## Key Structures\n\nBefore proceeding, there's a couple\
  \ of kernel memory structures we need to know about.\n\n### \\_EPROCESS\n\n`_EPROCESS` is a kernel memory structure that\
  \ describes system processes \\(or in other words - each process running on a system has its corresponding `_EPROCESS` object\
  \ somewhere in the kernel\\) as we know them as it contains details such as process image name, which desktop session it\
  \ is running in, how many open handles to other kernel objects it has, what access token it has and much more. \n\nBelow\
  \ is a snippet of the structure:\n\n```erlang\ndt _eprocess\n```\n\n![](../../.gitbook/assets/image%20%28439%29.png)\n\n\
  ### \\_TOKEN \n\n`_TOKEN` is a kernel memory structure that describes process's security context and contains information\
  \ such as process token privileges, logon id, session id, token type \\(i.e primary vs. impersonation\\) and much more.\
  \ \n\nBelow is a snippet of the `_TOKEN` structure:\n\n```erlang\ndt _token\n```\n\n![](../../.gitbook/assets/image%20%28326%29.png)\n\
  \nLet's now see how we can use the above information about processes and tokens to elevate a medium integrity process to\
  \ a system integrity process the way kernel exploits do it.\n\n## 1. Replacing Tokens for Privilege Escalation\n\nOne way\
  \ kernel exploits escalate privileges is by replacing a low privileged token with a high privileged token. Below are some\
  \ key points in explaining the exploitation process:\n\n* Each process running on the system has its corresponding `_EPROCESS`\
  \ kernel structure\n* `_EPROCESS` structure contains a pointer to a `_TOKEN` memory structure that describes process's security\
  \ context\n* Kernel exploit finds address of the `_TOKEN` structure of a low privileged process - the one it wants to escalate\
  \ from\n* Kernel exploit finds address of the `_TOKEN` structure of a privileged process, running as `NT\\SYSTEM`\n* Kernel\
  \ exploit replaces the low privileged process's token with the high privileged token\n\nIn this lab, I'm going to replace\
  \ the authentication token of a low privileged `powershell` process with a high privileged token of the `system` process\
  \ \\(always a PID 4\\) following the above described process, except I will do it manually using WinDBG.\n\n{% hint style=\"\
  info\" %}\nMy lab is running Windows 10 x64 1903\n{% endhint %}\n\nBelow is an attempt to visually represent the above described\
  \ process with a high level diagram:\n\n![Token stealing / swapping process](../../.gitbook/assets/image%20%2873%29.png)\n\
  \n* Boxes with blue headings represent a `MEDIUM` integrity process, running as `WS02\\spotless` \n  * `WS02` is my lab\
  \ machine name \n  * `spotless` is a low privileged local user. \n* Boxed with red headings indicate a `SYSTEM` integrity\
  \ process, effectively running as `NT\\SYSTEM` \n  * `WS02$` is my lab computer account \n  * `OFFENSE` is the domain the\
  \ machine is a member of\n* Red dotted line signifies that the low privileged process `powershell` will assume the high\
  \ privileged token from the process `system` once the `_TOKEN` kernel memory structure is manipulated.\n\nLet's now try\
  \ to see how we can replace process tokens using WinDBG.\n\n### Listing Processes\n\nFirst off, listing all running processes\
  \ on the system in WinDBG can be done like so:\n\n```erlang\n!process 0 0\n```\n\nBelow is a snippet of some of the processes\
  \ running on the system and highlighted are addresses pointing to `_EPROCESS` structures for given processes:\n\n![](../../.gitbook/assets/image%20%28409%29.png)\n\
  \n### Medium Integrity Process\n\nNext, let's launch `powershell` \\(this is the process for which we will replace the low\
  \ privileged token with a high privileged token\\) as a medium integrity/non-elevated process \\(in my case running as a\
  \ local non-admin user `ws02\\spotless`\\) and get its process ID:\n\n![](../../.gitbook/assets/image%20%2864%29.png)\n\n\
  Let's get a process summary in WinDBG for our `powershell` process with PID 2648 \\(0xa58\\):\n\n```erlang\n!process a58\
  \ 0\n```\n\nBelow confirms we're looking at our powershell.exe process. Note the `_EPROCESS` location `ffffdc8fbe1f1080`:\n\
  \n![](../../.gitbook/assets/image%20%28258%29.png)\n\n### Finding Powershell Token\n\nOnce we have powershell's `_EPROCESS`\
  \ location in the kernel, we can inspect its contents like so:\n\n```erlang\nkd> dt _eprocess ffffdc8fbe1f1080\n```\n\n\
  Since we're interested in swapping the token, the key member of the `_EPROCESS` memory structure we are after is `Token`\
  \ located at offset `0x358`:\n\n![](../../.gitbook/assets/image%20%28202%29.png)\n\n{% hint style=\"warning\" %}\nNote that\
  \ offset`0x358` suggests it's pointer to `_EX_FAST_REF` memory structure and we will come back to this shortly.\n{% endhint\
  \ %}\n\nLet's read memory contents of the pointer the `_EPROCESS.Token` is pointing to, which is ``ffffc507`dab7799f`` in\
  \ my case:\n\n```erlang\nkd> dq ffffdc8fbe1f1080+0x358 l1\nffffdc8f`be1f13d8  ffffc507`dab7799f\n```\n\nIf we try inspecting\
  \ the memory location ``ffffc507`dab7799f`` with `!token ffffc507dab7799f` command, we are told that this address does not\
  \ point to a token object, which we may find a bit odd:\n\n![](../../.gitbook/assets/image%20%28232%29.png)\n\nHowever,\
  \ this is where the `_EX_FAST_REF` comes into play. It was pointed out earlier that `_EPROCESS.Token` actually points to\
  \ a `_EX_FAST_REF` structure rather than a `_TOKEN` structure.\n\nLet's overlay the address stored in `_EPROCESS.Token`\
  \ which is ``ffffdc8f`be1f13d8`` \\(`_EPROCESS` location plus the `Token` member offset \\(`ffffdc8fbe1f1080+0x358`\\)\\\
  ) with the `_EX_FAST_REF` structure and see what's inside:\n\n```erlang\nkd> dt _EX_FAST_REF ffffdc8fbe1f1080+0x358\nntdll!_EX_FAST_REF\n\
  \   +0x000 Object           : 0xffffc507`dab7799f Void\n   +0x000 RefCnt           : 0y1111\n   +0x000 Value           \
  \ : 0xffffc507`dab7799f\n```\n\nNotice how all three members have the same offset and `Object` and `Value` are pointing\
  \ to the same address, but the interesting piece is the `RefCnt` with 4 bits on \\(equals to 0xF, which looks like it is\
  \ the last digit of both `Object` and `Value` members are pointing to - 0xffffc507\\`dab7799**f**\\). \n\nIf we inspect\
  \ the `_EX_FAST_REF` without data, based on the symbols, it's defined like so:\n\n```erlang\nntdll!_EX_FAST_REF\n   +0x000\
  \ Object           : Ptr64 Void\n   +0x000 RefCnt           : Pos 0, 4 Bits\n   +0x000 Value            : Uint8B\n```\n\n\
  Which indicates and confirms that the last 4 bits \\(the last hex digit of the `Object` or `Value`\\) of the value pointed\
  \ to by members `Object` and `Value` \\(in my case ``0xffffc507`dab7799f``\\) is used to denote the reference count to this\
  \ token, which means it's not part of the token address, which means we should be able to zero it out and get an actual\
  \ `_TOKEN` structure address for our powershell process.\n\nEssentially, if `Object` and `Value` are ``0xffffc507`dab7799f``,\
  \ we should be able to just swap the last `f` with `0` which would give us ``0xffffc507`dab77990`` and it should be our\
  \ `_TOKEN` address.\n\nIn fact, if we inspect our powershell process with a more verbose output like so:\n\n```erlang\n\
  !process ffffdc8fbe1f1080 1 \n// or !process 0xa58 1\n```\n\n..we see that indeed the `Token` is pointing to ``0xffffc507`dab77990``\
  \ - note the last digit is `0` rather than `f`, which confirms that we can always zero out the last digit pointed to by\
  \ `_EX_FAST_REF` to get the effective `_TOKEN` structure address:\n\n![](../../.gitbook/assets/image%20%2848%29.png)\n\n\
  We can mask out the last digit with a bitwise `AND` operation as shown below:\n\n```erlang\nkd> ? (ffffc507dab7799f & 0xFFFFFFF0);\
  \ !token (ffffc507dab7799f & 0xFFFFFFF0)\n```\n\n![0xf being zeroed out](../../.gitbook/assets/image%20%28125%29.png)\n\n\
  Now, if we try the `!token` command again with the last digit of `_EPROCESS.Token->Value` set to 0, we no longer see the\
  \ error message suggesting there's no token at that address and we start seeing some actual token details like user group\
  \ it belongs to, etc.:\n\n![](../../.gitbook/assets/image%20%2878%29.png)\n\n### Confirming SIDs\n\nWe can double check\
  \ we're actually looking at the right token - the SID's seen in the output of `whoami /all` and the `!token (ffffc507dab7799f\
  \ & 0xFFFFFFF0)` match:\n\n![](../../.gitbook/assets/image%20%28154%29.png)\n\n### Finding SYSTEM Token\n\nNow let's find\
  \ the address of the high privileged `_TOKEN` - the token that our low privileged powershell process will assume.\n\nBelow\
  \ shows some information about the `SYSTEM` process - we're interested in it's `_TOKEN` location which is at `ffffc507d8818040`\
  \ as shown below:\n\n```erlang\nkd> !process 4 1\nSearching for Process with Cid == 4\nPROCESS ffffdc8fbdad3040\n    SessionId:\
  \ none  Cid: 0004    Peb: 00000000  ParentCid: 0000\n    DirBase: 001aa002  ObjectTable: ffffc507d88032c0  HandleCount:\
  \ 3042.\n    Image: System\n    VadRoot ffffdc8fbdad1170 Vads 8 Clone 0 Private 21. Modified 76433. Locked 0.\n    DeviceMap\
  \ ffffc507d8818eb0\n    Token                             ffffc507d8818040\n```\n\n### Swapping Tokens\n\nWe now have all\
  \ the required information to successfully swap the powershell process token \\(located at `ffffdc8fbe1f1080+0x358`\\) with\
  \ that held by the `SYSTEM` process \\(`ffffc507d8818040`\\) by simply writing the `SYSTEM` process's token address to the\
  \ the `_EPROCESS.Token` of our powershell process:\n\n```erlang\neq ffffdc8fbe1f1080+0x358 ffffc507d8818040\n```\n\nBelow\
  \ shows the above in action and how prior to the token manipulation, the powershell was running as `ws02\\spotless` and\
  \ `nt authority\\system` after:\n\n![](../../.gitbook/assets/replace-token.gif)\n\n## 2. Modifying Token Privileges\n\n\
  Another interesting \\(and abused for privilege escalation\\) member of the `_TOKEN`structure is `Privileges` at offset\
  \ `0x040`, defined as `_SEP_TOKEN_PRIVILEGES` structure:\n\n```erlang\ndt _token 0xffffc507dab77990\n```\n\n![](../../.gitbook/assets/image%20%28460%29.png)\n\
  \n### Enabling Existing Privileges\n\nWe can overlay our low privileged powershell token address + offset 0x40 to inspect\
  \ the `_sep_token_privileges` structure:\n\n```erlang\ndt _sep_token_privileges 0xffffc507dab77990+0x40\n```\n\nIn essence,\
  \ `_sep_token_privileges` shows which privileges the token has and which of them are enabled/disabled - the info that we\
  \ can also check from the userland with `whoami /priv`. \n\nNote how `_sep_token_privileges` `Present` and `Enabled` values\
  \ do not match and this is what results in Enabled/Disabled privileges that we see in the `whoami /priv` `State` column:\n\
  \n![](../../.gitbook/assets/image%20%28506%29.png)\n\nWe can manipulate the kernel memory and make `Present` and `Enabled`\
  \ values match like so:\n\n```erlang\neq 0xffffc507dab77990+0x40+8 0x00000006`02880000\n```\n\nAfter manipulating the memory\
  \ and matching the `Present` and `Enabled` values, we can now see how all the privileges in the `State` column of the `whoami\
  \ /priv` output are `Enabled`:\n\n![](../../.gitbook/assets/image%20%28417%29.png)\n\n### Adding More Privileges\n\nLet's\
  \ see if we can try to add more privileges to that exsiting token rather than just enabling those that already exist. \n\
  \nHow do we know what is a valid value in the `Present` field that would give us more/elevated privileges? We can get a\
  \ good hint by inspecting the `Present` value of the `SYSTEM` process \\(PID 4\\) token:\n\n```erlang\n!process  4 1\nsep_token_privileges\
  \ 0x40+ffffde8fe9a06040\n```\n\n![](../../.gitbook/assets/image%20%28514%29.png)\n\nFrom the above, `Present` value is ``0x0000001f`f2ffffbc``\
  \ - this represents all the privileges the SYSTEM process token has. \n\nLet's see if we can assign this value to our powershell\
  \ process's token to both `Present` and `Enabled` fields. If successful, we should have all the SYSTEM privileges enabled\
  \ for our low privileged powershell process running in the context of the user `ws02\\spotless`:\n\n```erlang\nkd> eq 0x40+ffffde8ff8cde5f0+8\
  \ 0x0000001f`f2ffffbc\nkd> eq 0x40+ffffde8ff8cde5f0 0x0000001f`f2ffffbc\n```\n\nLet's check if the new values got assigned\
  \ to our `_sep_token_privileges` structure:\n\n```erlang\nkd> dt _sep_token_privileges 0x40+ffffde8ff8cde5f0\nnt!_SEP_TOKEN_PRIVILEGES\n\
  \   +0x000 Present          : 0x0000001f`f2ffffbc\n   +0x008 Enabled          : 0x0000001f`f2ffffbc\n   +0x010 EnabledByDefault\
  \ : 0x40800000\n```\n\nRunning `whoami /priv` now shows that we have all the SYSTEM privileges and all of them are enabled:\n\
  \n![](../../.gitbook/assets/image%20%28352%29.png)\n\n## References\n\n{% embed url=\"https://github.com/hatRiot/token-priv/blob/master/abusing\\\
  _token\\_eop\\_1.0.txt\" %}\n\n{% embed url=\"http://mcdermottcybersecurity.com/articles/x64-kernel-privilege-escalation\"\
  \ %}\n\n{% embed url=\"https://hshrzd.wordpress.com/2017/06/22/starting-with-windows-kernel-exploitation-part-3-stealing-the-access-token/\"\
  \ %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel/how-kernel-exploits-abuse-tokens-for-privilege-escalation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel/how-kernel-exploits-abuse-tokens-for-privilege-escalation.md
````
