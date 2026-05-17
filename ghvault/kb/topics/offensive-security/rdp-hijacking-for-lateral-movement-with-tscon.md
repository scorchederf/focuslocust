---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# RDP Hijacking for Lateral Movement with tscon

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-t1076-rdp-hijacking-for-lateral-movement` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/t1076-rdp-hijacking-for-lateral-movement.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It is possible by design to switch from one user's desktop session to another through the Task Manager (one of the ways).

## Preserved Body

````markdown
## Execution

It is possible by design to switch from one user's desktop session to another through the Task Manager (one of the ways).

Below shows that there are two users on the system and currently the administrator session is in active:

![](<../../_assets/rdp-admin.png>)

Let's switch to the `spotless` session - this requires knowing the user's password, which for this exercise is known, so lets enter it:

![](<../../_assets/rdp-login.png>)

![](<../../_assets/rdp-password.png>)

We are now reconnected to the `spotless` session:

![](<../../_assets/rdp-spotless.png>)

Now this is where it gets interesting. It is possible to reconnect to a users session without knowing their password if you have `SYSTEM` level privileges on the system. \
Let's elevate to `SYSTEM` using psexec (privilege escalation exploits, service creation or any other technique will also do):

```
psexec -s cmd
```

![](<../../_assets/rdp-system.png>)

Enumerate available sessions on the host with `query user`:

![](<../../_assets/rdp-sessions.png>)

Switch to the `spotless` session without getting requested for a password by using the native windows binary `tscon.exe`that enables users to connect to other desktop sessions by specifying which session ID (`2` in this case for the `spotless` session) should be connected to which session (`console` in this case, where the active `administator` session originates from):

```csharp
cmd /k tscon 2 /dest:console
```

![](<../../_assets/rdp-hijack-no-password.png>)

Immediately after that, we are presented with the desktop session for `spotless`:

![](<../../_assets/rdp-spotless-with-system.png>)

## Observations

Looking at the logs, `tscon.exe` being executed as a `SYSTEM` user is something you may want to investigate further to make sure this is not a lateral movement attempt:

![](<../../_assets/rdp-logs (1).png>)

Also, note how `event_data.LogonID` and event\_ids `4778` (logon) and `4779` (logoff) events can be used to figure out which desktop sessions got disconnected/reconnected:

![Administrator session disconnected](<../../_assets/rdp-session-disconnect.png>)

![Spotless session reconnected (hijacked)](<../../_assets/rdp-session-reconnect.png>)

Just reinforcing the above - note the usernames and logon session IDs:

![](<../../_assets/rdp-logon-sessions.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/rdp-hijacking-for-lateral-movement-with-tscon.md)

## Evidence Excerpt

```text
_asset_filenames:
- rdp-admin.png
- rdp-hijack-no-password.png
- rdp-login.png
- rdp-logon-sessions.png
- rdp-logs (1).png
- rdp-password.png
- rdp-session-disconnect.png
```
