---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Dump Virtual Box Memory

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-dump-virtual-box-memory` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/dump-virtual-box-memory.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

erlang

## Preserved Body

````markdown
## List Available VMs

```erlang
cd "C:\Program Files\Oracle\VirtualBox\"
.\VBoxManage.exe list vms

...
"win1002 debugee" {5f176ebb-a0cc-4dc7-9c6f-988fcbcca867}
...
```

## Enable Debug Mode
```bash
mantvydas@~: virtualbox --startvm 'yourVMName or VM UUID' --dbg
```
## Dump VM Memory

Launch the VirtualBox debug console by navigating to "Debug" menu an select "Command Line":

![](<../_assets/vbox-menu.png>)

Once you select "Command Line", you will be presented with a console that looks like this:

![memory dump will be a raw file dumped to /home/youruser directory](<../_assets/vbox-debug.png>)

To create a memory dump, issue the below command \(also highlighted in the above graphic\):
```text
VBoxDbg> .pgmphystofile 'w7-nc-shell.bin'
```
## Persistence

If you want the debug options to be always available, you can:

* export `VBOX_GUI_DBG_ENABLED=true` before launching the VM or
* put export `VBOX_GUI_DBG_ENABLED=true` in your `.bashrc` or `/etc/environment`
````

## Source Verification

[source record](../../sources/redteamingtactics/dump-virtual-box-memory.md)

## Evidence Excerpt

````text
_asset_filenames:
- vbox-debug.png
- vbox-menu.png
_body: "---\ndescription: >-\n  A quick reminder of one of the ways of how to dump memory of a VM running on\n  VirtualBox\
\ in Linux environment.\n---\n\n# Dump Virtual Box Memory\n\n## List Available VMs\n\n```erlang\ncd \"C:\\Program Files\\\
Oracle\\VirtualBox\\\"\n.\\VBoxManage.exe list vms\n\n...\n\"win1002 debugee\" {5f176ebb-a0cc-4dc7-9c6f-988fcbcca867}\n\
...\n```\n\n## Enable Debug Mode\n\n{% code title=\"linux host\" %}\n```bash\nmantvydas@~: virtualbox --startvm 'yourVMName\
\ or VM UUID' --dbg\n```\n{% endcode %}\n\n## Dump VM Memory\n\nLaunch the VirtualBox debug console by navigating to \"\
````
