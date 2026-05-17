---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Commandline Obfusaction

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-commandline-obfusaction` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/commandline-obfusaction.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Commandline Obfusaction](../../topics/offensive-security/commandline-obfusaction.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-defense-evasion-commandline-obfusaction |
| name | Commandline Obfusaction |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/defense-evasion/commandline-obfusaction.md |

## Preserved Source Material

````yaml
_asset_filenames:
- batch-powershell.png
- carets.png
- comasemicoma.png
- double-quotes.png
- environment-variables.png
- forcoding-python (1).png
- forcoding.png
- garbage1.png
- garbage2.png
- garbage3.png
- substring1.png
_body: "---\ndescription: Commandline obfuscation\n---\n\n# Commandline Obfusaction\n\nThis lab is based on the research done\
  \ by Daniel Bohannon from FireEye.\n\n## Environment variables\n\n```csharp\nC:\\Users\\mantvydas>set a=/c & set b=calc\n\
  C:\\Users\\mantvydas>cmd %a% %b%\n```\n\nNote though that the commandline logging (dynamic detection) still works as the\
  \ commandline needs to be expanded before it can get executed, but static detection could be bypassed:\n\n![](../../.gitbook/assets/environment-variables.png)\n\
  \n## Double quotes\n\n```csharp\nC:\\Users\\mantvydas>c\"\"m\"d\"\n```\n\nNote how double quotes can actually make both\
  \ static and dynamic detection a bit more difficult:\n\n![](../../.gitbook/assets/double-quotes.png)\n\n## Carets\n\n```csharp\n\
  C:\\Users\\mantvydas>n^e^t u^s^er\n```\n\nCommandline logging, same as with using environment variables, is not affected,\
  \ however static detection could be affected:\n\n![](../../.gitbook/assets/carets.png)\n\n## Garbage delimiters\n\nA very\
  \ interesting technique. Let's look at this first without garbage delimiters:\n\n```csharp\nPS C:\\Users\\mantvydas> cmd\
  \ /c \"set x=calc & echo %x% | cmd\"\n```\n\nThe above sets en environment variable x to `calc` and then prints it and pipes\
  \ it to the standard input of the cmd:\n\n![](../../.gitbook/assets/garbage1.png)\n\nIntroducing garbage delimiters `@`\
  \ into the equation:\n\n```csharp\nPS C:\\Users\\mantvydas> cmd /c \"set x=c@alc & echo %x:@=% | cmd\"\n```\n\nThe above\
  \ does the same as the earlier example, except that it introduces more filth into the command (`c@lc`). You can see from\
  \ the below screenshot that Windows does not recognize such a command `c@lc`, but the second attempt when the `%x:@=%` removes\
  \ the extraneous `@` symbol from the string, gets executed successfully:\n\n![](../../.gitbook/assets/garbage2.png)\n\n\
  If it is confusing, the below should help clear it up:\n\n```\nPS C:\\Users\\mantvydas> cmd /c \"set x=c@alc & echo %x:@=mantvydas%\
  \ | cmd\"\n```\n\n![](../../.gitbook/assets/garbage3.png)\n\nIn the above, the value `mantvydas` got inserted in the `c@lc`\
  \ in place of @, suggesting that `%x:@=%` (`:@=` to be precise) is just a string replacement capability in the cmd.exe utility.\n\
  \nWith this knowledge, the original obfuscated command\n\n```csharp\nPS C:\\Users\\mantvydas> cmd /c \"set x=c@alc & echo\
  \ %x:@=% | cmd\"\n```\n\nreads: replace the @ symbol with text that goes after the `=` sign, which is empty in this case,\
  \ which effectively means - remove @ from the value stored in the variable x.\n\n## Substring\n\nCmd.exe also has a substring\
  \ capability. See below:\n\n```csharp\n# this will take the C character from %programdata% and will launch the cmd prompt\n\
  %programdata:~0,1%md\n```\n\nNote that this is only good for bypassing static detection:\n\n![](../../.gitbook/assets/substring1.png)\n\
  \n## Batch FOR, DELIMS + TOKENS\n\nWe can use a builtin batch looping to extract the Powershell string from environment\
  \ variables in order to launch it and bypass static detection that looks for a string \"powershell\" in program invocations:\n\
  \n{% code title=\"@cmd\" %}\n```csharp\nset pSM \nPSModulePath=C:\\Users\\mantvydas\\Documents\\WindowsPowerShell\\Modules;....\n\
  ```\n{% endcode %}\n\nNote how the `WindowsPowerShell` string is present in the `PSModule` environment variable - this mean\
  \ we can extract it like so:\n\n```csharp\nFOR /F \"tokens=7 delims=s\\\" %g IN ('set^|findstr PSM') do %g\n```\n\nWhat\
  \ the above command does:\n\n1. Executes `set^|findstr PSM` to get the PSModulePath variable value\n2. Splits the string\
  \ using delimiters `s` & `\\`\n3. Prints out the 7th token, which happens to be the `PowerShell`\n4. Which effectively launches\
  \ PowerShell\n\n![](../../.gitbook/assets/batch-powershell.png)\n\n## Comma, semicolon\n\nThis may be used for both static\
  \ and dynamic detection bypasses:\n\n```csharp\nC:\\Users\\mantvydas>cmd,/c;hostname\nPC-MANTVYDAS\n```\n\n![](../../.gitbook/assets/comasemicoma.png)\n\
  \n## FORCoding\n\nWhat happens below is essentially there is a loop that goes through the list of indexes (0 1 2 3 2 6 2\
  \ 4 5 6 0 7) which are used to point to characters in the variable `unique` which acts like an alphabet. This allows for\
  \ the FOR loop to cycle through the index, pick out characters from the alphabet pointed to by the index and concatenate\
  \ them into a final string that eventually gets called with `CALL %final%` when the loop reaches the index 1337.\n\n```csharp\n\
  PS C:\\Users\\mantvydas> cmd /V /C \"set unique=nets /ao&&FOR %A IN (0 1 2 3 2 6 2 4 5 6 0 7 1337) DO set final=!final!!uni\n\
  que:~%A,1!&& IF %A==1337 CALL %final:~-12%\"\n```\n\n![](../../.gitbook/assets/forcoding.png)\n\nIn verbose python this\
  \ could look something like this:\n\n{% code title=\"forcoding.py\" %}\n```python\nimport os\n\ndictionary = \"nets -ao\"\
  \nindexes = [0, 1, 2, 3, 2, 6, 2, 4, 5, 6, 0, 7, 1337]\nfinal = \"\"\n\nfor index in indexes:\n    if index == 1337:   \
  \     \n        break\n    final += dictionary[index]\nos.system(final)\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/forcoding-python\
  \ (1).png>)\n\n## References\n\n{% embed url=\"https://www.youtube.com/watch?v=mej5L9PE1fs\" %}\n\n{% embed url=\"https://www.fireeye.com/blog/threat-research/2018/03/dosfuscation-exploring-obfuscation-and-detection-techniques.html\"\
  \ %}"
_relative_path: offensive-security/defense-evasion/commandline-obfusaction.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/commandline-obfusaction.md
````
