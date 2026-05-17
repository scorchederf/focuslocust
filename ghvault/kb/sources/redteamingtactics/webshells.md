---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# WebShells

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-privilege-escalation-t1108-redundant-access` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1108-redundant-access.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WebShells](../../topics/offensive-security/webshells.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-privilege-escalation-t1108-redundant-access |
| name | WebShells |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/privilege-escalation/t1108-redundant-access.md |

## Preserved Source Material

```yaml
_asset_filenames:
- webshell-attacker.png
- webshell-iis-logs.png
- webshell-pcap.png
- webshell-stream.png
- webshell-sysmon.png
_body: '---

  description: Redundant Access - Webshells for evading defenses and persistence.

  ---


  # WebShells


  This demo assumes a server compromise and that the attacker has already uploaded a webshell to the compromised host for
  persistence.


  ## Execution


  Below illustrates the existence of a simple webshell on a compromised Windows 2008R at 10.0.0.6 running IIS web service.
  It also shows output of the classic system enumeration commands - `net`, `whoami`, `ipconfig`, etc:


  ![](../../.gitbook/assets/webshell-attacker.png)


  ## Observations


  Note that this particular webshell''s HTTP requests are sent to the webserver via POST method which means that looking at
  the IIS web logs will not allow you to see what commands were executed using the webshell. The only things you will just
  will be a bunch of POST requests to the `c.aspx` file:


  ![](../../.gitbook/assets/webshell-iis-logs.png)


  However, if you are collecting network traffic data, you can see the attacker''s commands and their outputs:


  ![](../../.gitbook/assets/webshell-pcap.png)


  ![](../../.gitbook/assets/webshell-stream.png)


  Looking at sysmon process creation logs, we can immediately identify nefarious behaviour - we can see multiple enumeration
  commands being invoked from `c:\windows\system\inetsrv` working directory under a `ISS\APPOOL\DefaultAppPool` user - this
  should not happen under normal circumstances and should raise your suspicion:


  ![](../../.gitbook/assets/webshell-sysmon.png)


  ## References


  {% embed url="https://attack.mitre.org/wiki/Technique/T1108" %}'
_relative_path: offensive-security/privilege-escalation/t1108-redundant-access.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/privilege-escalation/t1108-redundant-access.md
```
