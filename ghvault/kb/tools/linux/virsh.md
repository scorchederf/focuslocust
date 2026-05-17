---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# virsh

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `virsh` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/virsh` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

GTFOBins entry for virsh covering command, file-write.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/virsh.md)
- Source verification: [source record](../../sources/gtfobins/virsh.md)

## Aliases

- `virsh`

## Source Verification

[source record](../../sources/gtfobins/virsh.md)

## Evidence Excerpt

```text
_body: ''
_name: virsh
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/virsh
functions:
command:
- code: "cat >/path/to/temp-file.xml <<EOF\n<domain type='kvm'>\n  <name>x</name>\n  <os>\n    <type arch='x86_64'>hvm</type>\n\
\  </os>\n  <memory unit='KiB'>1</memory>\n  <devices>\n    <interface type='ethernet'>\n      <script path='/path/to/command'/>\n\
\    </interface>\n  </devices>\n</domain>\nEOF\nvirsh -c qemu:///system create /path/to/temp-file.xml\nvirsh -c qemu:///system\
```
