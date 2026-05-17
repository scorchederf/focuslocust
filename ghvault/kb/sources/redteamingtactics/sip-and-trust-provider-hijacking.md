---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# SIP & Trust Provider Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1198-trust-provider-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1198-trust-provider-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SIP & Trust Provider Hijacking](../../topics/offensive-security/sip-and-trust-provider-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1198-trust-provider-hijacking |
| name | SIP & Trust Provider Hijacking |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1198-trust-provider-hijacking.md |

## Preserved Source Material

````yaml
_asset_filenames:
- trust-check-if-signing-block-exists.png
- trust-find-signed.png
- trust-from.png
- trust-not-signed.png
- trust-ps-file.png
- trust-script-with-ms-signing-code.png
- trust-signed.png
- trust-sysmon1.png
- trust-sysmon2.png
- trust-to.png
_body: "---\ndescription: 'Defense Evasion, Persistence, Whitelisting Bypass'\n---\n\n# SIP & Trust Provider Hijacking\n\n\
  In this lab, I will try to sign a simple \"rogue\" powershell script `test-forged.ps1` that only has one line of code, with\
  \ **Microsoft's** certificate and bypass any whitelisting protections/policies the script may be subject to if it is not\
  \ signed.\n\n## Execution\n\nThe script that I will try to sign:\n\n![](../../.gitbook/assets/trust-ps-file.png)\n\nJust\
  \ before I start, let's make sure that the script is not signed by using a `Get-AuthenticodeSignature` cmdlet and `sigcheck`\
  \ by SysInternals:\n\n![](../../.gitbook/assets/trust-not-signed.png)\n\nIn order to sign the script with Microsoft's certificate,\
  \ we need to first find a native Microsoft Signed PowerShell script. I used powershell for this:\n\n```csharp\nGet-ChildItem\
  \ -Path C:\\*.ps* -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern \"# SIG # Begin signature block\"\n```\n\
  \n![](../../.gitbook/assets/trust-find-signed.png)\n\nI chose one script at random and simply checked if it was signed -\
  \ luckily it was:\n\n```bash\ntype C:\\Windows\\WinSxS\\x86_microsoft-windows-m..ell-cmdlets-modules_31bf3856ad364e35_10.0.16299.15_none_c7c20f51cd336675\\\
  Wdac.psd1\n```\n\n![](../../.gitbook/assets/trust-check-if-signing-block-exists.png)\n\nLet's copy the Microsoft signature\
  \ block to my script:\n\n![](../../.gitbook/assets/trust-script-with-ms-signing-code.png)\n\nNow let's modify registry at:\n\
  \n```text\nHKLM\\SOFTWARE\\Microsoft\\Cryptography\\OID\\EncodingType 0\\CryptSIPDllVerifyIndirectData\\{603BCC1F-4B59-4E08-B724-D2C6297EF351}\n\
  ```\n\nFrom:\n\n![](../../.gitbook/assets/trust-from.png)\n\nTo:\n\n{% code title=\"DLL\" %}\n```csharp\nC:\\Windows\\System32\\\
  ntdll.dll\n```\n{% endcode %}\n\n{% code title=\"FuncName\" %}\n```text\nDbgUIContinue\n```\n{% endcode %}\n\n![](../../.gitbook/assets/trust-to.png)\n\
  \nNow, let's launch a new powershell instance \\(for the registry changes to take effect\\) and check the signature of the\
  \ forged script - note how it now shows as signed, verified and valid:\n\n![](../../.gitbook/assets/trust-signed.png)\n\n\
  ## Observations\n\nMonitoring the following registry keys/values helps discover this suspicious activity:\n\n![](../../.gitbook/assets/trust-sysmon1.png)\n\
  \n![](../../.gitbook/assets/trust-sysmon2.png)\n\n## References\n\nFor all the registry keys/values that should be used\
  \ as a baseline, please refer to the original research whitepaper by Matt Graeber:   \n[SpecterOps Subverting Trust inWindows](https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf)\n\
  \n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1198\" %}\n\n{% embed url=\"https://www.youtube.com/watch?v=wxmxxgL6Nz8\"\
  \ %}\n\n{% embed url=\"https://pentestlab.blog/2017/11/06/hijacking-digital-signatures/\" %}\n\n{% embed url=\"http://ultimate-sysadmin-fanboy.blogspot.com/2015/06/unable-to-renew-certificate-via.html\"\
  \ %}\n\n{% embed url=\"https://blogs.msdn.microsoft.com/sqlforum/2011/01/02/walkthrough-request-a-digital-certificate-from-certificate-server-or-create-a-testing-digital-certificate-to-sign-a-package/\"\
  \ %}\n\n{% embed url=\"https://www.youtube.com/watch?v=WrHTJQovDoY\" %}\n\n{% embed url=\"https://www.hanselman.com/blog/SigningPowerShellScripts.aspx\"\
  \ %}\n\n{% embed url=\"https://github.com/netbiosX/Digital-Signature-Hijack\" %}"
_relative_path: offensive-security/persistence/t1198-trust-provider-hijacking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1198-trust-provider-hijacking.md
````
