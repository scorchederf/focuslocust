---
parsed_by: focuslocust
source: commands
type: generated
---
# Zipfldr.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Zipfldr.dll

Tool page: [Zipfldr.dll](../../tools/windows/zipfldr.dll.md)

### Launch an executable.

```text
rundll32.exe zipfldr.dll,RouteTheCall {PATH:.exe}
```

Description:

Launch an executable payload by calling RouteTheCall.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Zipfldr.yml` |
| Evidence | Command preserved from source parser. |

### Launch an executable.

```text
rundll32.exe zipfldr.dll,RouteTheCall file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
```

Description:

Launch an executable payload by calling RouteTheCall (obfuscated).

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Zipfldr.yml` |
| Evidence | Command preserved from source parser. |
