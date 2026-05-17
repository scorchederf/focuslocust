---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# WebRTC DoS

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-pentesting-network-webrtc-dos` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/pentesting-network/webrtc-dos.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WebRTC DoS](../../topics/generic-methodologies-and-resources/webrtc-dos.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-pentesting-network-webrtc-dos |
| name | WebRTC DoS |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/pentesting-network/webrtc-dos.md |

## Preserved Source Material

```yaml
_body: '# WebRTC DoS


  {{#include ../../banners/hacktricks-training.md}}


  **This issue was found in this blog post:** [**https://www.rtcsec.com/article/novel-dos-vulnerability-affecting-webrtc-media-servers/**](https://www.rtcsec.com/article/novel-dos-vulnerability-affecting-webrtc-media-servers/)


  The described vulnerability in WebRTC media servers arises from a **race condition** during the initialization of media
  sessions, specifically between the **ICE media consent verification** and the **DTLS traffic initiation**. Here’s a detailed
  breakdown:


  ### Vulnerability Origin


  1. **UDP Port Allocation:** When a user initiates a WebRTC call, the media server allocates UDP ports for handling the media
  streams, with the IP and port communicated via signaling.

  2. **ICE and STUN Processes:** The user''s browser uses ICE for media consent verification, utilizing STUN to determine
  the connection path to the media server.

  3. **DTLS Session:** Following successful STUN verification, a DTLS session starts to establish SRTP master keys, switching
  to SRTP for the media stream.


  ### Exploitation Mechanism


  - **Race Condition Exploitation:** An attacker can exploit a race condition by sending a DTLS ClientHello message before
  the legitimate user, potentially using an invalid cipher suite like `TLS_NULL_WITH_NULL_NULL`. This causes a DTLS error
  at the server, preventing the SRTP session from being established.


  ### Attack Process


  - **Port Scanning:** The attacker needs to guess which UDP ports are handling incoming media sessions, sending ClientHello
  messages with the null cipher suite to these ports to trigger the vulnerability.

  - **Diagram of Attack:** The sequence involves multiple ClientHello messages sent by the attacker to the server, interleaved
  with legitimate signaling and DTLS messages, leading to a handshake failure due to the erroneous cipher suite.


  ### Testing and Mitigation


  - **Safe Testing:** Using tools like Scapy, attackers replay DTLS ClientHello messages targeting specific media ports. For
  ethical testing, modifications to Chromium (e.g., `JsepTransport::AddRemoteCandidates`) were used to mimic victim behavior
  safely.

  - **Mitigation Measures:** Solutions involve dropping packets from unverified addresses, as implemented in newer versions
  of libraries like libnice. The primary solution emphasizes trusting the ICE verification process and only processing packets
  from validated IP and port combinations.


  ### Non-Vulnerable Scenarios


  - **DTLS Server Configurations:** Instances where the browser acts as a DTLS server or when the media server does not use
  ephemeral ports for media sessions are not susceptible to this vulnerability.


  ### Conclusion


  This vulnerability highlights the delicate balance in media session initialization processes and the need for precise timing
  and verification mechanisms to prevent exploitation. Developers are advised to implement recommended security fixes and
  ensure robust verification processes to mitigate such vulnerabilities.


  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: generic-methodologies-and-resources/pentesting-network/webrtc-dos.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/pentesting-network/webrtc-dos.md
```
