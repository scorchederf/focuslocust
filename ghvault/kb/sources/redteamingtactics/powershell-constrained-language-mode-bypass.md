---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Powershell Constrained Language Mode ByPass

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-execution-powershell-constrained-language-mode-bypass` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/powershell-constrained-language-mode-bypass.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell Constrained Language Mode ByPass](../../topics/offensive-security/powershell-constrained-language-mode-bypass.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-execution-powershell-constrained-language-mode-bypass |
| name | Powershell Constrained Language Mode ByPass |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-execution/powershell-constrained-language-mode-bypass.md |

## Preserved Source Material

````yaml
_asset_filenames:
- ps-constrained-download-denied.png
- ps-constrained.png
- ps-downgrade.png
- ps-invoke.gif
_body: '---

  description: Understanding ConstrainedLanguageMode

  ---


  # Powershell Constrained Language Mode ByPass


  Constrained Language Mode in short locks down the nice features of Powershell usually required for complex attacks to be
  carried out.


  ## Powershell Inside Powershell


  For fun - creating another powershell instance inside powershell without actually spawning a new `powershell.exe` process:


  ![](../../.gitbook/assets/ps-invoke.gif)


  ## Constrained Language Mode


  Enabling constrained language mode, that does not allow powershell execute complex attacks (i.e. mimikatz):


  ```csharp

  [Environment]::SetEnvironmentVariable(‘__PSLockdownPolicy‘, ‘4’, ‘Machine‘)

  ```


  Checking constrained language mode is enabled:


  ```csharp

  PS C:\Users\mantvydas> $ExecutionContext.SessionState.LanguageMode

  ConstrainedLanguage

  ```


  ![](../../.gitbook/assets/ps-constrained.png)


  With `ConstrainedLanguage`, trying to download a file from remote machine, we get `Access Denied`:


  ![](../../.gitbook/assets/ps-constrained-download-denied.png)


  However, if you have access to the system and enough privileges to change environment variables, the lock can be lifted
  by removing the variable `__PSLockdownPolicy` and re-spawning another powershell instance.


  ### Powershell Downgrade


  If you have the ability to downgrade to Powershell 2.0, this can allow you to bypass the `ConstrainedLanguage`mode. Note
  how `$ExecutionContext.SessionState.LanguageMode` keeps returning `ConstrainedLangue` in powershell instances that were
  not launched with `-version Powershell 2` until it does not:


  ![](../../.gitbook/assets/ps-downgrade.png)


  ## System32 Bypass


  [Carrie Roberts](https://twitter.com/OrOneEqualsOne) discovered and wrote in her post [https://www.blackhillsinfosec.com/constrained-language-mode-bypass-when-pslockdownpolicy-is-used/](https://www.blackhillsinfosec.com/constrained-language-mode-bypass-when-pslockdownpolicy-is-used/)
  that there''s another way to bypass the contrained language mode and it''s super easy - the path from where your script
  is being executed, needs to contain the string `system32`, meaning even if you rename the script to `system32.ps1`, it should
  work, so let''s try it and confirm it works:


  ```

  PS>.\test.ps1; mv .\test.ps1 system32.ps1; .\system32.ps1

  ConstrainedLanguage

  FullLanguage


  PS>cat .\system32.ps1

  $ExecutionContext.SessionState.LanguageMode

  ```


  ## References


  {% embed url="https://blogs.msdn.microsoft.com/powershell/2017/11/02/powershell-constrained-language-mode/" %}


  {% embed url="https://www.blackhillsinfosec.com/powershell-without-powershell-how-to-bypass-application-whitelisting-environment-restrictions-av/"
  %}


  {% embed url="https://adsecurity.org/?p=2604" %}


  {% embed url="https://pentestn00b.wordpress.com/2017/03/20/simple-bypass-for-powershell-constrained-language-mode/" %}'
_relative_path: offensive-security/code-execution/powershell-constrained-language-mode-bypass.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-execution/powershell-constrained-language-mode-bypass.md
````
