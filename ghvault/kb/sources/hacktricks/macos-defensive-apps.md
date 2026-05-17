---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS Defensive Apps

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-defensive-apps` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-defensive-apps.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS Defensive Apps](../../topics/macos-hardening/macos-defensive-apps.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-defensive-apps |
| name | macOS Defensive Apps |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-security-and-privilege-escalation/macos-defensive-apps.md |

## Preserved Source Material

```yaml
_body: '# macOS Defensive Apps


  {{#include ../../banners/hacktricks-training.md}}


  ## Firewalls


  - [**Little Snitch**](https://www.obdev.at/products/littlesnitch/index.html): It will monitor every connection made by each
  process. Depending on the mode (silent allow connections, silent deny connection and alert) it will **show you an alert**
  every time a new connection is stablished. It also has a very nice GUI to see all this information.

  - [**LuLu**](https://objective-see.org/products/lulu.html): Objective-See firewall. This is a basic firewall that will alert
  you for suspicious connections (it has a GUI but it isn''t as fancy as the one of Little Snitch).


  ## Persistence detection


  - [**KnockKnock**](https://objective-see.org/products/knockknock.html): Objective-See application that will search in several
  locations where **malware could be persisting** (it''s a one-shot tool, not a monitoring service).

  - [**BlockBlock**](https://objective-see.org/products/blockblock.html): Like KnockKnock by monitoring processes that generate
  persistence.


  ## Keyloggers detection


  - [**ReiKey**](https://objective-see.org/products/reikey.html): Objective-See application to find **keyloggers** that install
  keyboard "event taps"


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: macos-hardening/macos-security-and-privilege-escalation/macos-defensive-apps.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-defensive-apps.md
```
