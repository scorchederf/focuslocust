---
parsed_by: focuslocust
source: commands
type: generated
---
# Url.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Url.dll

Tool page: [Url.dll](../../tools/windows/url.dll.md)

### Invoke an HTML Application via mshta.exe (Default Handler).

```text
rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.hta}
```

Description:

Launch a HTML application payload by calling OpenURL.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Evidence | Command preserved from source parser. |

### Load an executable payload by calling a .url file.

```text
rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.url}
```

Description:

Launch an executable payload via proxy through a .url (information) file by calling OpenURL.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Evidence | Command preserved from source parser. |

### Load an executable payload by specifying the file protocol handler (obfuscated).

```text
rundll32.exe url.dll,OpenURL file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
```

Description:

Launch an executable by calling OpenURL.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Evidence | Command preserved from source parser. |

### Launch an executable.

```text
rundll32.exe url.dll,FileProtocolHandler {PATH_ABSOLUTE:.exe}
```

Description:

Launch an executable by calling FileProtocolHandler.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Evidence | Command preserved from source parser. |

### Load an executable payload by specifying the file protocol handler (obfuscated).

```text
rundll32.exe url.dll,FileProtocolHandler file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
```

Description:

Launch an executable by calling FileProtocolHandler.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Evidence | Command preserved from source parser. |

### Invoke an HTML Application via mshta.exe (Default Handler).

```text
rundll32.exe url.dll,FileProtocolHandler file:///C:/test/test.hta
```

Description:

Launch a HTML application payload by calling FileProtocolHandler.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Evidence | Command preserved from source parser. |
