---
parsed_by: focuslocust
source: commands
type: generated
---
# hashcat Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## hashcat

Tool page: [hashcat](../../tools/linux/hashcat.md)

### file-write

```text
echo -n DATA | tee /path/to/wordlist | md5sum | awk '{print $1}' >/path/to/hash
hashcat -m 0 --quiet --potfile-disable -o /path/to/output-file --outfile-format=2 --outfile-autohex-disable /path/to/hash /path/to/wordlist
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/hashcat` |
| Evidence | Function example preserved from source parser. |
