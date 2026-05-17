---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Enumerating Users without net, Services without sc and Scheduled Tasks without schtasks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-enumeration-and-discovery-enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

It is possible to use MMC snap-ins to enumerate local users and local groups, services, scheduled tasks, SMB shares and sessions on a system if you have an interactive desktop session on the compromised system either via RDP or if you are s

## Preserved Body

```markdown
It is possible to use MMC snap-ins to enumerate local users and local groups, services, scheduled tasks, SMB shares and sessions on a system if you have an interactive desktop session on the compromised system either via RDP or if you are simulating an insider threat during a pentest and you are given a company's laptop.

## Why would you do it?

The use of well known lolbins like net, sc and schtasks on a host where an EDR solution is running is risky and may get you caught. Using snap-ins may help evade commandline detections SOC may be relying on. 

Of course, marketing department is unlikely to run mmc snap-ins either, so beware :\)

## Enumerating Users and Local Groups

Launch mmc.exe, click File &gt; Add\remove snap-in &gt; Local users and Groups:

![](<../../_assets/snapin.gif>)

## Enumerating Services

Same could be done for enumerating services running on the system:

![](<../../_assets/snapins.PNG>)

Note that `services.msc` could give you the same view.

## Enumerating Scheduled Tasks

![](<../../_assets/tasksch.PNG>)

Persistence anyone? Note that `taskschd.msc` could give you the same view:

![](<../../_assets/scheduler-new-task.PNG>)

## Shares and Sessions

![](<../../_assets/sessions+shares.PNG>)
```

## Source Verification

[source record](../../sources/redteamingtactics/enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks.md)

## Evidence Excerpt

```text
_asset_filenames:
- scheduler-new-task.PNG
- sessions+shares.PNG
- snapin.gif
- snapins.PNG
- tasksch.PNG
_body: "# Enumerating Users without net, Services without sc and Scheduled Tasks without schtasks\n\nIt is possible to use\
\ MMC snap-ins to enumerate local users and local groups, services, scheduled tasks, SMB shares and sessions on a system\
```
