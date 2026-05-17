---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# From Beacon to Interactive RDP Session

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-lateral-movement-from-beacon-to-interactive-remote-desktop-rdp-session` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/from-beacon-to-interactive-remote-desktop-rdp-session.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [From Beacon to Interactive RDP Session](../../topics/offensive-security/from-beacon-to-interactive-rdp-session.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-lateral-movement-from-beacon-to-interactive-remote-desktop-rdp-session |
| name | From Beacon to Interactive RDP Session |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/lateral-movement/from-beacon-to-interactive-remote-desktop-rdp-session.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (178).png
- image (179).png
- image (180).png
- image (181).png
- image (182).png
- image (183).png
_body: '---

  description: Lateral Movement, Tunnelling, Firewall Evasion

  ---


  # From Beacon to Interactive RDP Session


  This is a quick note showing how to get an interactive Remote Desktop Session (RDP) session from a Cobalt Strike beacon
  by leveraging socks proxy and proxychains.


  ## Socks Proxy


  Say we have compromised a box and we have a beacon running on it:


  ![](<../../.gitbook/assets/image (183).png>)


  The same compromised machine is listening on 3389, meaning it accepts incoming RDP connections:


  ![](<../../.gitbook/assets/image (182).png>)


  Most often you will not be able to reach the machine via RDP from the outside due to corporate and host firewalls, however
  not all is lost - the machine is still reachable over RDP via sock proxy capability that the beacon provides.


  Using the beacon we control, let''s create a socks proxy on port 7777. This will expose a TCP port 7777 on the teamserver:


  ```

  socks 7777

  ```


  ![](<../../.gitbook/assets/image (180).png>)


  ## Proxychains


  With the socks proxy create, we can now jump onto any linux box (Kali in my case) and configure proxychains to point it
  to the teamserver and the port we''ve just exposed:


  ![](<../../.gitbook/assets/image (181).png>)


  We can now connect to the compromised box via RDP using xfreerdp:


  {% code title="attacker@kali" %}

  ```

  proxychains xfreerdp /v:127.0.0.1:3389 /u:spotless

  ```

  {% endcode %}


  Below illustrates a successful RDP connection was established although the user on the other end (me) killed the session:


  ![](<../../.gitbook/assets/image (179).png>)


  {% hint style="warning" %}

  **If you are getting...**\

  `Error: CredSSP initialize failed, do you have correct kerberos ticket initialized?`\

  `Failed to connect, CredSSP required by server`


  Suggestion is to use `xfreerdp` instead of `rdesktop` and the issue will go away.

  {% endhint %}


  ![CredSSP error using rdesktop](<../../.gitbook/assets/image (178).png>)'
_relative_path: offensive-security/lateral-movement/from-beacon-to-interactive-remote-desktop-rdp-session.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/lateral-movement/from-beacon-to-interactive-remote-desktop-rdp-session.md
````
