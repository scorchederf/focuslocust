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

## Generated Concept Page

- [Enumerating Users without net, Services without sc and Scheduled Tasks without schtasks](../../topics/offensive-security/enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-enumeration-and-discovery-enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks |
| name | Enumerating Users without net, Services without sc and Scheduled Tasks without schtasks |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/enumeration-and-discovery/enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks.md |

## Preserved Source Material

```yaml
_asset_filenames:
- scheduler-new-task.PNG
- sessions+shares.PNG
- snapin.gif
- snapins.PNG
- tasksch.PNG
_body: "# Enumerating Users without net, Services without sc and Scheduled Tasks without schtasks\n\nIt is possible to use\
  \ MMC snap-ins to enumerate local users and local groups, services, scheduled tasks, SMB shares and sessions on a system\
  \ if you have an interactive desktop session on the compromised system either via RDP or if you are simulating an insider\
  \ threat during a pentest and you are given a company's laptop.\n\n## Why would you do it?\n\nThe use of well known lolbins\
  \ like net, sc and schtasks on a host where an EDR solution is running is risky and may get you caught. Using snap-ins may\
  \ help evade commandline detections SOC may be relying on. \n\nOf course, marketing department is unlikely to run mmc snap-ins\
  \ either, so beware :\\)\n\n## Enumerating Users and Local Groups\n\nLaunch mmc.exe, click File &gt; Add\\remove snap-in\
  \ &gt; Local users and Groups:\n\n![](../../.gitbook/assets/snapin.gif)\n\n## Enumerating Services\n\nSame could be done\
  \ for enumerating services running on the system:\n\n![](../../.gitbook/assets/snapins.PNG)\n\nNote that `services.msc`\
  \ could give you the same view.\n\n## Enumerating Scheduled Tasks\n\n![](../../.gitbook/assets/tasksch.PNG)\n\nPersistence\
  \ anyone? Note that `taskschd.msc` could give you the same view:\n\n![](../../.gitbook/assets/scheduler-new-task.PNG)\n\n\
  ## Shares and Sessions\n\n![](../../.gitbook/assets/sessions+shares.PNG)"
_relative_path: offensive-security/enumeration-and-discovery/enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/enumeration-and-discovery/enumerating-users-without-net-services-without-sc-and-scheduled-tasks-without-schtasks.md
```
