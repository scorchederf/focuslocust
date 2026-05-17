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

## Generated Concept Page

- [Miscellaneous & Tricks](../../topics/cheatsheets/miscellaneous-and-tricks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-miscellaneous-tricks |
| name | Miscellaneous & Tricks |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/miscellaneous-tricks.md |

## Preserved Source Material

````yaml
_body: "# Miscellaneous & Tricks\n\nAll the tricks that couldn't be classified somewhere else.\n\n## Send Messages to Other\
  \ Users\n\n* Windows\n\n```powershell\nPS C:\\> msg Swissky /SERVER:CRASHLAB \"Stop rebooting the XXXX service !\"\nPS C:\\\
  > msg * /V /W /SERVER:CRASHLAB \"Hello all !\"\n```\n\n* Linux\n\n```powershell\nwall \"Stop messing with the XXX service\
  \ !\"\nwall -n \"System will go down for 2 hours maintenance at 13:00 PM\"  # \"-n\" only for root\nwho\nwrite root pts/2\
  \ # press Ctrl+D  after typing the message. \n```\n\n## NetExec Credential Database\n\n```ps1\nnxcdb (default) > workspace\
  \ create test\nnxcdb (test) > workspace default\nnxcdb (test) > proto smb\nnxcdb (test)(smb) > creds\nnxcdb (test)(smb)\
  \ > export creds csv /tmp/creds\n```\n\nNetExec workspaces\n\n```ps1\n# get current workspace\npoetry run nxcdb -gw \n\n\
  # create workspace\npoetry run nxcdb -cw testing\n\n# set workspace\npoetry run nxcdb -sw testing \n```"
_relative_path: cheatsheets/miscellaneous-tricks.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/miscellaneous-tricks.md
````
