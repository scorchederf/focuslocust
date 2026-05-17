---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Injecting .NET Assembly to an Unmanaged Process

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-injecting-and-executing-.net-assemblies-to-unmanaged-process` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/injecting-and-executing-.net-assemblies-to-unmanaged-process.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Injecting .NET Assembly to an Unmanaged Process](../../topics/offensive-security/injecting-.net-assembly-to-an-unmanaged-process.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-injecting-and-executing-.net-assemblies-to-unmanaged-process |
| name | Injecting .NET Assembly to an Unmanaged Process |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/injecting-and-executing-.net-assemblies-to-unmanaged-process.md |

## Preserved Source Material

````yaml
_asset_filenames:
- unmanaged-process-load-clr.gif
_body: "# Injecting .NET Assembly to an Unmanaged Process\n\nThis is a quick lab to see what API sequence makes it possible\
  \ to inject C\\# .NET assemblies / PE files \\(.exe and .dll\\) into an unmanaged process and invoke their methods. \n\n\
  {% hint style=\"info\" %}\nThis is the technique that makes `execute-assembly` command possible in Cobalt Strike.\n{% endhint\
  \ %}\n\n## Overview\n\nAt a high level, it works as follows:\n\n1. `CLRCreateInstance` is used to retrieve an interface\
  \ [`ICLRMetaHost`](https://docs.microsoft.com/en-us/dotnet/framework/unmanaged-api/hosting/iclrmetahost-interface)\n2. `ICLRMetaHost->GetRuntime`\
  \ is used to retrieve [`ICLRRuntimeInfo`](https://docs.microsoft.com/en-us/dotnet/framework/unmanaged-api/hosting/iclrruntimeinfo-interface)\
  \ interface for a specified CLR version\n3. `ICLRRuntimeInfo->GetInterface` is used to load the CLR into the current process\
  \ and retrieve an interface [`ICLRRuntimeHost`](https://docs.microsoft.com/en-us/dotnet/framework/unmanaged-api/hosting/iclrruntimehost-interface)\n\
  4. `ICLRRuntimeHost->Start` is used to initialize the CLR into the current process\n5. `ICLRRuntimeHost->ExecuteInDefaultAppDomain`\
  \ is used to load the C\\# .NET assembly and call a particular method with an optionally provided argument\n\n## Code\n\n\
  * `unmanaged.cpp` \\(in my lab compiled to `LoadCLR.exe`\\) - a C++ program that loads a C\\# assembly \n\n  `CLRHello1.exe`\
  \ and invokes its method `spotlessMethod`\n\n* `managed.cs` \\(in my lab compiled to `CLRHello1.exe`\\) - a C\\# program\
  \ that is loaded by the unmanaged process \\(`LoadCLR.exe`\\). It has a method `spotlessMethod` that is invoked via `ExecuteInDefaultAppDomain.`O\n\
  \nOnce invoked, the `spotlessMethod` prints out `Hi from CLR` to the console window.\n\n{% tabs %}\n{% tab title=\"unmanaged.cpp\"\
  \ %}\n```cpp\n// code mostly stolen from pabloko's comment in https://gist.github.com/xpn/e95a62c6afcf06ede52568fcd8187cc2\n\
  #include <iostream>\n#include <metahost.h>\n#include <corerror.h>\n#pragma comment(lib, \"mscoree.lib\")\n\nint main()\n\
  {\n    ICLRMetaHost* metaHost = NULL;\n    ICLRRuntimeInfo* runtimeInfo = NULL;\n    ICLRRuntimeHost* runtimeHost = NULL;\n\
  \    DWORD pReturnValue;\n\n    CLRCreateInstance(CLSID_CLRMetaHost, IID_ICLRMetaHost, (LPVOID*)&metaHost);\n    metaHost->GetRuntime(L\"\
  v4.0.30319\", IID_ICLRRuntimeInfo, (LPVOID*)&runtimeInfo);\n    runtimeInfo->GetInterface(CLSID_CLRRuntimeHost, IID_ICLRRuntimeHost,\
  \ (LPVOID*)&runtimeHost);\n    runtimeHost->Start();\n    HRESULT res = runtimeHost->ExecuteInDefaultAppDomain(L\"C:\\\\\
  labs\\\\CLRHello1\\\\CLRHello1\\\\CLRHello1\\\\bin\\\\Debug\\\\CLRHello1.exe\", L\"CLRHello1.Program\", L\"spotlessMethod\"\
  , L\"test\", &pReturnValue);\n    if (res == S_OK)\n    {\n        std::cout << \"CLR executed successfully\\n\";\n    }\n\
  \    \n    runtimeInfo->Release();\n    metaHost->Release();\n    runtimeHost->Release();\n    return 0;\n}\n```\n{% endtab\
  \ %}\n\n{% tab title=\"managed.cs\" %}\n```csharp\nusing System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
  using System.Text;\nusing System.Threading.Tasks;\n\nnamespace CLRHello1\n{\n    class Program\n    {\n        static void\
  \ Main(string[] args)\n        {\n            return;   \n        }\n        \n        // important: methods called by ExecuteInDefaultAppDomain\
  \ need to stick to this signature\n        static int spotlessMethod(String pwzArgument)\n        {\n            Console.WriteLine(\"\
  Hi from CLR\");\n            return 1;\n        }\n    }\n}\n```\n{% endtab %}\n{% endtabs %}\n\n## Demo\n\nBelow shows\
  \ how `LoadCLR.exe` loaded our C\\# assembly `CLRHello.exe` \\(seen in `LoadCLR.exe` loaded modules tab\\) and invoked the\
  \ `spotlessMethod`, that printed `Hi from CLR` to the console:\n\n![](../../.gitbook/assets/unmanaged-process-load-clr.gif)\n\
  \n## References\n\n{% embed url=\"https://blog.xpnsec.com/hiding-your-dotnet-etw/\" %}\n\n[https://gist.github.com/xpn/e95a62c6afcf06ede52568fcd8187cc2](https://gist.github.com/xpn/e95a62c6afcf06ede52568fcd8187cc2)"
_relative_path: offensive-security/code-injection-process-injection/injecting-and-executing-.net-assemblies-to-unmanaged-process.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/injecting-and-executing-.net-assemblies-to-unmanaged-process.md
````
