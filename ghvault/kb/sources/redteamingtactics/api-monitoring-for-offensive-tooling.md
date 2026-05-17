---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# API Monitoring for Offensive Tooling

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-api-monitoring-for-offensive-tooling` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/api-monitoring-for-offensive-tooling.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [API Monitoring for Offensive Tooling](../../topics/offensive-security/api-monitoring-for-offensive-tooling.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-api-monitoring-for-offensive-tooling |
| name | API Monitoring for Offensive Tooling |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/api-monitoring-for-offensive-tooling.md |

## Preserved Source Material

````yaml
_asset_filenames:
- capture-password.gif
- find-computername-windbg.gif
- find-computername.gif
- image (113).png
- image (150).png
- image (156).png
- image (168).png
- image (185).png
- image (224).png
- image (227).png
- image (234).png
- image (34).png
- image (5).png
- image (73).png
- image (87).png
- image (94).png
- inject-rdp-thief-credreadw.gif
- inject-rdp-thief.gif
_body: "# API Monitoring for Offensive Tooling\n\n[Rio Sherri](https://twitter.com/0x09al) recently posted about his tool\
  \ [RdpThief](https://www.mdsec.co.uk/2019/11/rdpthief-extracting-clear-text-credentials-from-remote-desktop-clients/) which\
  \ I thought was plain genius. It allows for offensive operators to steal RDP credentials by injecting RdpThief's DLL into\
  \ the RDP client mstc.exe.\n\nUnder the hood, RdpThief does the following:\n\n* hooks mstc.exe functions responsible for\
  \ dealing with user supplied credentials\n* intercepts the user supplied username, password, hostname during authentication\n\
  * writes out intercepted credentials and hostname to a file\n\nThese are some notes of me tinkering with [API Monitor](http://www.rohitab.com/apimonitor),\
  \ WinDBG and Detours \\(Microsoft's library for hooking Windows APIs\\) and reproducing some of the steps Rio took during\
  \ his research and development of [RdpThief](https://github.com/0x09AL/RdpThief). \n\nThese notes will serve me as a reference\
  \ for future on how to identify and hook interesting functions that can be useful when writing offensive tooling.\n\n##\
  \ Walkthrough\n\nIf we launch mstc.exe and attempt connecting to a remote host WS01:\n\n![](../../.gitbook/assets/image%20%28227%29.png)\n\
  \n..we are prompted to enter credentials:\n\n![RDP authentication prompt](../../.gitbook/assets/image%20%2834%29.png)\n\n\
  If API monitor was attached to mstc.exe when we tried to authenticate to the remote host WS01, we should now have a huge\
  \ list of API calls invoked by mstsc.exe and its module logged.\n\n### Intercepting Username\n\nIf we search for a string\
  \ `spotless`, we will find some functions that take `spotless` as a string argument and one of those functions is `CredIsMarshaledCredentialW`\
  \ as shown below: \n\n![CredIsMarshaledCredentialW contains the string spotless](../../.gitbook/assets/find-computername.gif)\n\
  \n![CredIsMarshaledCredentialW contains the string spotless](../../.gitbook/assets/image%20%28113%29.png)\n\nIn WinDBG,\
  \ if we put a breakpoint on `ADVAPI32!CredIsMarshaledCredentialW` and print out its first and only argument \\(stored in\
  \ RCX register for 64 bit architecture\\), we will see `DESKTOP-NU8QCIB\\spotless` printed out:\n\n```c\nbp ADVAPI32!CredIsMarshaledCredentialW\
  \ \"du @rcx\"\n```\n\n![ADVAPI32!CredIsMarshaledCredentialW breakpoint hit and username printed](../../.gitbook/assets/find-computername-windbg.gif)\n\
  \n![ADVAPI32!CredIsMarshaledCredentialW breakpoint hit and username printed - still](../../.gitbook/assets/image%20%28168%29.png)\n\
  \n### Intercepting Hostname\n\nTo find the hostname of the RDP connection, we find API calls that took `ws01` \\(our hostname\\\
  ) as a string argument. Although RdpThief hooks `SSPICLI!SspiPrepareForCredRead` \\(hostname supplied as a second argument\\\
  ), another function that could be considered for hooking is `CredReadW` \\(hostname a the first argument\\) as seen below:\n\
  \n![](../../.gitbook/assets/image%20%28224%29.png)\n\nIf we jump back to WinDBG and set another breakpoint for `CredReadW`\
  \ and attempt to RDP to our host `ws01`, we get a hit:\n\n```cpp\nbp ADVAPI32!CredReadW \"du @rcx\"\n```\n\n![](../../.gitbook/assets/image%20%2873%29.png)\n\
  \nOut of curiosity, let's also put a breakpoint on `SSPICLI!SspiPrepareForCredRead` and once it's hit, print out the second\
  \ argument supplied to the function, which is stored in the RDX register:\n\n```text\nbp SSPICLI!SspiPrepareForCredRead\n\
  du @rdx\n```\n\n![](../../.gitbook/assets/image%20%2894%29.png)\n\n### Intercepting Password\n\nWe now know the functions\
  \ required to hook for intercepting the username and the hostname. What's now left is hooking the function that deals in\
  \ one way or another with the password and from Rio's article, we know it's the DPAPI `CryptProtectMemory`. \n\nWeirdly,\
  \ searching for my password in API Monitor resulted in nothing. Reviewing `CryptProtectMemory` calls manually in API Monitor\
  \ showed no plaintext passwor deither, although there were multiple calls to the function. I could see the password already\
  \ encrypted:\n\n![32 byte encrypted binary blob](../../.gitbook/assets/image%20%28150%29.png)\n\n{% hint style=\"info\"\
  \ %}\nFrom the above screenshot, note the size of the encrypted blob is 32 bytes - we will come back to this in WinDBG\n\
  {% endhint %}\n\nI could, however, see the unencrypted password in the `CryptUnprotectMemory` call, so I guess this is another\
  \ function you could consider hooking for nefarious purposes:\n\n![](../../.gitbook/assets/image%20%28185%29.png)\n\nLet's\
  \ now check what we can see in WinDBG if we hit the breakpoint on `CryptProtectMemory` and print out a unicode string starting\
  \ 4 bytes into the address \\(first 4 bytes indicate the size of the encrypted data\\) pointed by the RCX register:\n\n\
  ```cpp\nbp dpapi!cryptprotectmemory \"du @rcx+4\"\n```\n\nBelow shows the plain text password on a second break:\n\n![](../../.gitbook/assets/capture-password.gif)\n\
  \n![](../../.gitbook/assets/image%20%2887%29.png)\n\nEarlier, I emphasized the 32 bytes encrypted blob seen in `CryptProtectMemory`\
  \ function call \\(in API Monitor\\) and also mentioned the 4 byte offset into RCX that holds the size of the encrypted\
  \ blob - below shows that - first 4 bytes found at RCX \\(during the `CryptProtectMemory` break\\) are 0x20 or 32 in decimal:\n\
  \n![](../../.gitbook/assets/image%20%285%29.png)\n\n## RdpThief in Action\n\nCompiling RdpThief provides us with 2 DLLs\
  \ for 32 and 64 bit architectures. Let's inject the 64 bit DLL into mstc.exe and attempt to RDP into `ws01` - we see the\
  \ credentials getting intercepted and written to a file: \n\n![RDP credentials get intercepted and written to a file](../../.gitbook/assets/inject-rdp-thief.gif)\n\
  \n## Intercepting Hostname via CredReadW\n\nI wanted to confirm if my previous hypothesis about hooking `CredReadW` for\
  \ intercepting the hostname was possible, so I made some quick changes to the RdpThief's project to test it. \n\nI commented\
  \ out the `_SspiPrepareForCredRead` signature and hooked `CreadReadW` with a new function called `HookedCredReadW` which\
  \ will pop a message box each time `CredReadW` is called and print its first argument as the message box text. \n\nAlso,\
  \ it will update the `lpServer` variable which is later written to the file creds.txt together with the username and password.\n\
  \nBelow screenshot shows the code changes:\n\n![](../../.gitbook/assets/image%20%28156%29.png)\n\nOf course, we need to\
  \ register the new hook `HookedCredReadW` and unregist the old hook `_SspiPrepareForCredRead`:\n\n![](../../.gitbook/assets/image%20%28234%29.png)\n\
  \nCompiling and injecting the new RdpThief DLL confirms that the `CredReadW` can be used to intercept the the hostname:\n\
  \n![](../../.gitbook/assets/inject-rdp-thief-credreadw.gif)\n\n## References\n\n{% embed url=\"https://www.mdsec.co.uk/2019/11/rdpthief-extracting-clear-text-credentials-from-remote-desktop-clients/\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/cpp/build/x64-calling-convention?view=vs-2019\" %}\n\n{% embed url=\"\
  https://docs.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credismarshaledcredentialw\" %}\n\n{% embed url=\"\
  https://docs.microsoft.com/en-us/dotnet/framework/tools/developer-command-prompt-for-vs\\#manually-locate-the-files-on-your-machine\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/api-monitoring-for-offensive-tooling.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/api-monitoring-for-offensive-tooling.md
````
