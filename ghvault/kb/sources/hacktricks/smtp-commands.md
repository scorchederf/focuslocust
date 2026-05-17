---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# SMTP - Commands

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-smtp-smtp-commands` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-smtp/smtp-commands.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [SMTP - Commands](../../topics/network-services-pentesting/smtp-commands.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-smtp-smtp-commands |
| name | SMTP - Commands |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-smtp/smtp-commands.md |

## Preserved Source Material

```yaml
_body: '# SMTP - Commands


  {{#include ../../banners/hacktricks-training.md}}



  **Commands from:** [**https://serversmtp.com/smtp-commands/**](https://serversmtp.com/smtp-commands/)


  **HELO**\

  It’s the first SMTP command: is starts the conversation identifying the sender server and is generally followed by its domain
  name.


  **EHLO**\

  An alternative command to start the conversation, underlying that the server is using the Extended SMTP protocol.


  **MAIL FROM**\

  With this SMTP command the operations begin: the sender states the source email address in the “From” field and actually
  starts the email transfer.


  **RCPT TO**\

  It identifies the recipient of the email; if there are more than one, the command is simply repeated address by address.


  **SIZE**\

  This SMTP command informs the remote server about the estimated size (in terms of bytes) of the attached email. It can also
  be used to report the maximum size of a message to be accepted by the server.


  **DATA**\

  With the DATA command the email content begins to be transferred; it’s generally followed by a 354 reply code given by the
  server, giving the permission to start the actual transmission.


  **VRFY**\

  The server is asked to verify whether a particular email address or username actually exists.


  **TURN**\

  This command is used to invert roles between the client and the server, without the need to run a new connaction.


  **AUTH**\

  With the AUTH command, the client authenticates itself to the server, giving its username and password. It’s another layer
  of security to guarantee a proper transmission.


  **RSET**\

  It communicates the server that the ongoing email transmission is going to be terminated, though the SMTP conversation won’t
  be closed (like in the case of QUIT).


  **EXPN**\

  This SMTP command asks for a confirmation about the identification of a mailing list.


  **HELP**\

  It’s a client’s request for some information that can be useful for the a successful transfer of the email.


  **QUIT**\

  It terminates the SMTP conversation.



  {{#include ../../banners/hacktricks-training.md}}'
_relative_path: network-services-pentesting/pentesting-smtp/smtp-commands.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-smtp/smtp-commands.md
```
