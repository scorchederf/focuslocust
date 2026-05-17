---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Miscellaneous & Tricks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-miscellaneous-tricks` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/miscellaneous-tricks.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

All the tricks that couldn't be classified somewhere else.

## Preserved Body

````markdown
All the tricks that couldn't be classified somewhere else.

## Send Messages to Other Users

* Windows

```powershell
PS C:\> msg Swissky /SERVER:CRASHLAB "Stop rebooting the XXXX service !"
PS C:\> msg * /V /W /SERVER:CRASHLAB "Hello all !"
```

* Linux

```powershell
wall "Stop messing with the XXX service !"
wall -n "System will go down for 2 hours maintenance at 13:00 PM"  # "-n" only for root
who
write root pts/2 # press Ctrl+D  after typing the message. 
```

## NetExec Credential Database

```ps1
nxcdb (default) > workspace create test
nxcdb (test) > workspace default
nxcdb (test) > proto smb
nxcdb (test)(smb) > creds
nxcdb (test)(smb) > export creds csv /tmp/creds
```

NetExec workspaces

```ps1
# get current workspace
poetry run nxcdb -gw 

# create workspace
poetry run nxcdb -cw testing

# set workspace
poetry run nxcdb -sw testing 
```
````

## Source Verification

[source record](../../sources/internalallthethings/miscellaneous-and-tricks.md)

## Evidence Excerpt

````text
_body: "# Miscellaneous & Tricks\n\nAll the tricks that couldn't be classified somewhere else.\n\n## Send Messages to Other\
\ Users\n\n* Windows\n\n```powershell\nPS C:\\> msg Swissky /SERVER:CRASHLAB \"Stop rebooting the XXXX service !\"\nPS C:\\\
> msg * /V /W /SERVER:CRASHLAB \"Hello all !\"\n```\n\n* Linux\n\n```powershell\nwall \"Stop messing with the XXX service\
\ !\"\nwall -n \"System will go down for 2 hours maintenance at 13:00 PM\"  # \"-n\" only for root\nwho\nwrite root pts/2\
\ # press Ctrl+D  after typing the message. \n```\n\n## NetExec Credential Database\n\n```ps1\nnxcdb (default) > workspace\
\ create test\nnxcdb (test) > workspace default\nnxcdb (test) > proto smb\nnxcdb (test)(smb) > creds\nnxcdb (test)(smb)\
\ > export creds csv /tmp/creds\n```\n\nNetExec workspaces\n\n```ps1\n# get current workspace\npoetry run nxcdb -gw \n\n\
# create workspace\npoetry run nxcdb -cw testing\n\n# set workspace\npoetry run nxcdb -sw testing \n```"
````
