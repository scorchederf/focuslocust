---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# ETW: Event Tracing for Windows 101

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-windows-kernel-internals-etw-event-tracing-for-windows-101` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [ETW: Event Tracing for Windows 101](../../topics/miscellaneous-reversing-forensics/etw-event-tracing-for-windows-101.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-windows-kernel-internals-etw-event-tracing-for-windows-101 |
| name | ETW: Event Tracing for Windows 101 |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (532).png
- image (533).png
- image (534).png
- image (535).png
- image (536).png
- image (537).png
- image (538).png
- image (539).png
- image (540).png
- image (541).png
- image (542).png
- image (543).png
- image (544).png
- image (545).png
- image (546).png
- kernel-consumer.gif
_body: "# ETW: Event Tracing for Windows 101\n\n## Terminology\n\n* `Event Tracing for Windows (ETW)` is a Windows OS logging\
  \ mechanism for troubleshooting and diagnostics, that allows us to tap into an enormous number of events that are generated\
  \ by the OS every second\n* `Providers` are applications that can generate some event logs\n* `Keywords` are event types\
  \ the provider is able to serve the consumers with\n* `Consumers` are applications that subscribe and listen to events \
  \ emitted by providers\n* `Tracing session` records events from one or more providers\n* `Contollers` are applications that\
  \ can start a trace session and enable or disable providers in that trace session\n\n## Logman\n\nLogman.exe is a native\
  \ Windows command-line utility, which is considered to be a `Controller`. Below, some of the concepts mentioned earlier\
  \ are explored.\n\n### Listing Providers\n\nWe can see all the providers registered to Windows like so:\n\n```\nlogman query\
  \ providers\n```\n\n![](<../../.gitbook/assets/image (532).png>)\n\n### Provider Information\n\nWe can get more information\
  \ about the provider with `logman query $providerName|$provider`.\n\nOne of the many built-in interesting providers available\
  \ to us in Windows is **Microsoft-Windows-Kernel-Process**, so let's check it out:\n\n```\nlogman query providers Microsoft-Windows-Kernel-Process\n\
  logman query providers \"{22FB2CD6-0E7B-422B-A0C7-2FAD1FD0E716}\"\n```\n\n![](<../../.gitbook/assets/image (533).png>)\n\
  \nAs we can tell from the above `keywords`, this provider could provide us with some process, thread and image (load/unload\
  \ as we will see later) related events.\n\n{% hint style=\"info\" %}\nUse [ETWExplorer](https://github.com/zodiacon/EtwExplorer)\
  \ for a deep provider inspection, and see what events and more importantly data it can provide.&#x20;\n{% endhint %}\n\n\
  Below shows Microsoft-Windows-Kernel-Process being inspected with ETWExplorer with some information, which looks like something\
  \ Sysmon and other similar security monitoring oriented tools could use:\n\n![ETWExplorer](<../../.gitbook/assets/image\
  \ (534).png>)\n\n### Creating a Tracing Session\n\nLet's now try to create a trace session called `spotless-tracing`:\n\n\
  ```\nlogman create trace spotless-tracing -ets\n```\n\nWe can see our session is now created:\n\n![](<../../.gitbook/assets/image\
  \ (535).png>)\n\nWe can query the tracing session and see some information about it:\n\n```\nlogman query spotless-tracing\
  \ -ets\n```\n\nNote that at the moment, although the tracing session is running, it is not recording any events as we have\
  \ not yet subscribed to any providers:\n\n![Events will be saved to the output location](<../../.gitbook/assets/image (536).png>)\n\
  \n### Subscribing to Microsoft-Windows-Kernel-Process\n\nInside the `spotless-tracing` tracing session, let's subscribe\
  \ to events about `PROCESSES` and `IMAGES` provided by the provider `Microsoft-Windows-Kernel-Process` and see what they\
  \ look like.\n\nIn order to subscribe to those events, we first need to refer back to `Microsoft-Windows-Kernel-Process`\
  \ available `keywords` (event types of this provider) and add `0x10` (`WINEVENT_KEYWORD_PROCESS`) to `0x40` (`WINEVENT_KEYWORD_IMAGE`),\
  \ which gives us the total of `0x50`:\n\n![](<../../.gitbook/assets/image (537).png>)\n\nWe can now register a provider\
  \ to the tracing session and ask it to emit events that map back to events `WINEVENT_KEYWORD_PROCESS` and `WINEVENT_KEYWORD_IMAGE`:\n\
  \n```\nlogman update spotless-tracing -p Microsoft-Windows-Kernel-Process 0x50 -ets\n```\n\nIf we query the tracing session\
  \ again, we see it now has `Microsoft-Windows-Kernel-Process`provider registered and listening to the two event types pertaining\
  \ to processes (start/exit) and images (load/unload):\n\n```\nlogman query spotless-tracing -ets\n```\n\n![](<../../.gitbook/assets/image\
  \ (538).png>)\n\n### Checking the .etl Log\n\nAfter the tracing session has run for some time, we can check the log file\
  \  by opening it with the Windows Event Viewer.\n\nWe can see process creation events (event ID 1):\n\n![](<../../.gitbook/assets/image\
  \ (539).png>)\n\nImage load events (event ID 5):\n\n![](<../../.gitbook/assets/image (540).png>)\n\nImage unload events\
  \ (event ID 6):\n\n![](<../../.gitbook/assets/image (541).png>)\n\n### Removing Providers from a Tracing Session\n\nWe can\
  \ remove a provider from a tracing session like so:\n\n```\nlogman update trace spotless-tracing --p Microsoft-Windows-Kernel-Process\
  \ 0x50 -ets\n```\n\nNote that the kernel provider is no longer associated with the `spotless-tracing` tracing session:\n\
  \n![](<../../.gitbook/assets/image (543).png>)\n\n### Killing the Tracing Session\n\nWe can kill the entire tracing session\
  \ like so:\n\n```\nlogman stop spotless-tracing -ets\n```\n\n...and the tracing session is no longer present on the system:\n\
  \n![](<../../.gitbook/assets/image (544).png>)\n\n### Listing Providers a Process is Registered with\n\nWe can check what\
  \ providers any currently running process is registered with, meaning that process will be writing events to those providers.\n\
  \nBelow shows how we can check which providers our current powershell console is registered with (`$pid` gives the current\
  \ powershell console process id):\n\n```\nlogman query providers -pid $pid\n```\n\n![](<../../.gitbook/assets/image (545).png>)\n\
  \n## Consuming Events via Code\n\nThanks to [Pavel Yosifovich](https://github.com/zodiacon), we can use the below C# code\
  \ to subscribe to a kernel provider, that will feed our console program with process related events:&#x20;\n\n```csharp\n\
  # code by Pavel Yosifovich, https://github.com/zodiacon/DotNextSP2019/blob/master/SimpleKernelConsumer/Program.cs\nusing\
  \ Microsoft.Diagnostics.Tracing;\nusing Microsoft.Diagnostics.Tracing.Parsers;\nusing Microsoft.Diagnostics.Tracing.Session;\n\
  using System;\nusing System.Collections.Generic;\nusing System.Diagnostics;\nusing System.Linq;\nusing System.Text;\nusing\
  \ System.Threading;\nusing System.Threading.Tasks;\n\nnamespace SimpleKernelConsumer {\n\tclass ProcessInfo {\n\t\tpublic\
  \ int Id { get; set; }\n\t\tpublic string Name { get; set; }\n\t}\n\n\tclass Program {\n\t\tstatic void Main(string[] args)\
  \ {\n\t\t\tvar processes = Process.GetProcesses().Select(p => new ProcessInfo {\n\t\t\t\tName = p.ProcessName,\n\t\t\t\t\
  Id = p.Id\n\t\t\t}).ToDictionary(p => p.Id);\n\n\t\t\tusing (var session = new TraceEventSession(Environment.OSVersion.Version.Build\
  \ >= 9200 ? \"MyKernelSession\" : KernelTraceEventParser.KernelSessionName)) {\n\t\t\t\tsession.EnableKernelProvider(KernelTraceEventParser.Keywords.Process\
  \ | KernelTraceEventParser.Keywords.ImageLoad);\n\t\t\t\tvar parser = session.Source.Kernel;\n\n\t\t\t\tparser.ProcessStart\
  \ += e => {\n\t\t\t\t\tConsole.ForegroundColor = ConsoleColor.Green;\n\t\t\t\t\tConsole.WriteLine($\"{e.TimeStamp}.{e.TimeStamp.Millisecond:D3}:\
  \ Process {e.ProcessID} ({e.ProcessName}) Created by {e.ParentID}: {e.CommandLine}\");\n\t\t\t\t\tprocesses.Add(e.ProcessID,\
  \ new ProcessInfo { Id = e.ProcessID, Name = e.ProcessName });\n\t\t\t\t};\n\t\t\t\tparser.ProcessStop += e => {\n\t\t\t\
  \t\tConsole.ForegroundColor = ConsoleColor.Red;\n\t\t\t\t\tConsole.WriteLine($\"{e.TimeStamp}.{e.TimeStamp.Millisecond:D3}:\
  \ Process {e.ProcessID} {TryGetProcessName(e)} Exited\");\n\t\t\t\t};\n\n\t\t\t\tparser.ImageLoad += e => {\n\t\t\t\t\t\
  Console.ForegroundColor = ConsoleColor.Yellow;\n\t\t\t\t\tvar name = TryGetProcessName(e);\n\t\t\t\t\tConsole.WriteLine($\"\
  {e.TimeStamp}.{e.TimeStamp.Millisecond:D3}: Image Loaded: {e.FileName} into process {e.ProcessID} ({name}) Size=0x{e.ImageSize:X}\"\
  );\n\t\t\t\t};\n\n\t\t\t\tparser.ImageUnload += e => {\n\t\t\t\t\tConsole.ForegroundColor = ConsoleColor.DarkYellow;\n\t\
  \t\t\t\tvar name = TryGetProcessName(e);\n\t\t\t\t\tConsole.WriteLine($\"{e.TimeStamp}.{e.TimeStamp.Millisecond:D3}: Image\
  \ Unloaded: {e.FileName} from process {e.ProcessID} ({name})\");\n\t\t\t\t};\n\n\t\t\t\tTask.Run(() => session.Source.Process());\n\
  \t\t\t\tThread.Sleep(TimeSpan.FromSeconds(60));\n\t\t\t}\n\n\t\t\tstring TryGetProcessName(TraceEvent evt) {\n\t\t\t\tif\
  \ (!string.IsNullOrEmpty(evt.ProcessName))\n\t\t\t\t\treturn evt.ProcessName;\n\t\t\t\treturn processes.TryGetValue(evt.ProcessID,\
  \ out var info) ? info.Name : string.Empty;\n\t\t\t}\n\t\t}\n\t}\n}\n```\n\nDon't forget to install the package:\n\n![](<../../.gitbook/assets/image\
  \ (542).png>)\n\nIf we compile and run the code, we will now see events flowing in:\n\n![](../../.gitbook/assets/kernel-consumer.gif)\n\
  \n## Notes\n\nFrom an attacker's perspective, if you are up against some EDR or logging capability, you may be able to blind\
  \ the system by killing their tracing session or removing certain providers from their tracing session.\n\nFrom a defender's\
  \ perspective, you may want to:\n\n* learn about the additional telemetry you could get from ETW\n* think about detections\
  \ that target attackers trying to tamper with your telemetry through ETW\n\n## References\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/etw/about-event-tracing\"\
  \ %}\n\n{% embed url=\"https://medium.com/palantir/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63\"\
  \ %}\n\n{% embed url=\"https://github.com/zodiacon/EtwExplorer\" %}\n\n[Microsoft-Windows-Threat-Intelligence](https://pastebin.com/6VGHjGjH)\
  \ Provider Manifest as [mentioned](https://twitter.com/FancyCyber/status/1267536407272345602) by @FancyCyber:\n\n![](<../../.gitbook/assets/image\
  \ (546).png>)"
_relative_path: miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101.md
````
