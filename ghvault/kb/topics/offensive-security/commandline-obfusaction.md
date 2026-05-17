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

## Summary

This lab is based on the research done by Daniel Bohannon from FireEye.

## Preserved Body

````markdown
This lab is based on the research done by Daniel Bohannon from FireEye.

## Environment variables

```csharp
C:\Users\mantvydas>set a=/c & set b=calc
C:\Users\mantvydas>cmd %a% %b%
```

Note though that the commandline logging (dynamic detection) still works as the commandline needs to be expanded before it can get executed, but static detection could be bypassed:

![](<../../_assets/environment-variables.png>)

## Double quotes

```csharp
C:\Users\mantvydas>c""m"d"
```

Note how double quotes can actually make both static and dynamic detection a bit more difficult:

![](<../../_assets/double-quotes.png>)

## Carets

```csharp
C:\Users\mantvydas>n^e^t u^s^er
```

Commandline logging, same as with using environment variables, is not affected, however static detection could be affected:

![](<../../_assets/carets.png>)

## Garbage delimiters

A very interesting technique. Let's look at this first without garbage delimiters:

```csharp
PS C:\Users\mantvydas> cmd /c "set x=calc & echo %x% | cmd"
```

The above sets en environment variable x to `calc` and then prints it and pipes it to the standard input of the cmd:

![](<../../_assets/garbage1.png>)

Introducing garbage delimiters `@` into the equation:

```csharp
PS C:\Users\mantvydas> cmd /c "set x=c@alc & echo %x:@=% | cmd"
```

The above does the same as the earlier example, except that it introduces more filth into the command (`c@lc`). You can see from the below screenshot that Windows does not recognize such a command `c@lc`, but the second attempt when the `%x:@=%` removes the extraneous `@` symbol from the string, gets executed successfully:

![](<../../_assets/garbage2.png>)

If it is confusing, the below should help clear it up:

```
PS C:\Users\mantvydas> cmd /c "set x=c@alc & echo %x:@=mantvydas% | cmd"
```

![](<../../_assets/garbage3.png>)

In the above, the value `mantvydas` got inserted in the `c@lc` in place of @, suggesting that `%x:@=%` (`:@=` to be precise) is just a string replacement capability in the cmd.exe utility.

With this knowledge, the original obfuscated command

```csharp
PS C:\Users\mantvydas> cmd /c "set x=c@alc & echo %x:@=% | cmd"
```

reads: replace the @ symbol with text that goes after the `=` sign, which is empty in this case, which effectively means - remove @ from the value stored in the variable x.

## Substring

Cmd.exe also has a substring capability. See below:

```csharp
# this will take the C character from %programdata% and will launch the cmd prompt
%programdata:~0,1%md
```

Note that this is only good for bypassing static detection:

![](<../../_assets/substring1.png>)

## Batch FOR, DELIMS + TOKENS

We can use a builtin batch looping to extract the Powershell string from environment variables in order to launch it and bypass static detection that looks for a string "powershell" in program invocations:
```csharp
set pSM 
PSModulePath=C:\Users\mantvydas\Documents\WindowsPowerShell\Modules;....
```
Note how the `WindowsPowerShell` string is present in the `PSModule` environment variable - this mean we can extract it like so:

```csharp
FOR /F "tokens=7 delims=s\" %g IN ('set^|findstr PSM') do %g
```

What the above command does:

1. Executes `set^|findstr PSM` to get the PSModulePath variable value
2. Splits the string using delimiters `s` & `\`
3. Prints out the 7th token, which happens to be the `PowerShell`
4. Which effectively launches PowerShell

![](<../../_assets/batch-powershell.png>)

## Comma, semicolon

This may be used for both static and dynamic detection bypasses:

```csharp
C:\Users\mantvydas>cmd,/c;hostname
PC-MANTVYDAS
```

![](<../../_assets/comasemicoma.png>)

## FORCoding

What happens below is essentially there is a loop that goes through the list of indexes (0 1 2 3 2 6 2 4 5 6 0 7) which are used to point to characters in the variable `unique` which acts like an alphabet. This allows for the FOR loop to cycle through the index, pick out characters from the alphabet pointed to by the index and concatenate them into a final string that eventually gets called with `CALL %final%` when the loop reaches the index 1337.

```csharp
PS C:\Users\mantvydas> cmd /V /C "set unique=nets /ao&&FOR %A IN (0 1 2 3 2 6 2 4 5 6 0 7 1337) DO set final=!final!!uni
que:~%A,1!&& IF %A==1337 CALL %final:~-12%"
```

![](<../../_assets/forcoding.png>)

In verbose python this could look something like this:
```python
import os

dictionary = "nets -ao"
indexes = [0, 1, 2, 3, 2, 6, 2, 4, 5, 6, 0, 7, 1337]
final = ""

for index in indexes:
    if index == 1337:        
        break
    final += dictionary[index]
os.system(final)
```
![](<../../_assets/forcoding-python (1).png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/commandline-obfusaction.md)

## Evidence Excerpt

```text
_asset_filenames:
- batch-powershell.png
- carets.png
- comasemicoma.png
- double-quotes.png
- environment-variables.png
- forcoding-python (1).png
- forcoding.png
```
