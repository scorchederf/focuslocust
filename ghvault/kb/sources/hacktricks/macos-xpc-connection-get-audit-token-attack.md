---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS xpc_connection_get_audit_token Attack

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-proces-abuse-macos-ipc-inter-process-communication-macos-xpc-macos-xpc-connecting-process-check-macos-xpc-connection-get-audit-token-attack` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-xpc_connection_get_audit_token-attack.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS xpc_connection_get_audit_token Attack](../../topics/macos-hardening/macos-xpc-connection-get-audit-token-attack.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-proces-abuse-macos-ipc-inter-process-communication-macos-xpc-macos-xpc-connecting-process-check-macos-xpc-connection-get-audit-token-attack |
| name | macOS xpc_connection_get_audit_token Attack |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-xpc_connection_get_audit_token-attack.md |

## Preserved Source Material

````yaml
_body: "# macOS xpc_connection_get_audit_token Attack\n\n{{#include ../../../../../../banners/hacktricks-training.md}}\n\n\
  **For further information check the original post:** [**https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing/**](https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing/).\
  \ This is a summary:\n\n## Mach Messages Basic Info\n\nIf you don't know what Mach Messages are start checking this page:\n\
  \n\n{{#ref}}\n../../\n{{#endref}}\n\nFor the moment remember that ([definition from here](https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing)):\\\
  \nMach messages are sent over a _mach port_, which is a **single receiver, multiple sender communication** channel built\
  \ into the mach kernel. **Multiple processes can send messages** to a mach port, but at any point **only a single process\
  \ can read from it**. Just like file descriptors and sockets, mach ports are allocated and managed by the kernel and processes\
  \ only see an integer, which they can use to indicate to the kernel which of their mach ports they want to use.\n\n## XPC\
  \ Connection\n\nIf you don't know how a XPC connection is established check:\n\n\n{{#ref}}\n../\n{{#endref}}\n\n## Vuln\
  \ Summary\n\nWhat is interesting for you to know is that **XPC’s abstraction is a one-to-one connection**, but it is based\
  \ on top of a technology which **can have multiple senders, so:**\n\n- Mach ports are single receiver, **multiple sender**.\n\
  - An XPC connection’s audit token is the audit token of **copied from the most recently received message**.\n- Obtaining\
  \ the **audit token** of an XPC connection is critical to many **security checks**.\n\nAlthough the previous situation sounds\
  \ promising there are some scenarios where this is not going to cause problems ([from here](https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing)):\n\
  \n- Audit tokens are often used for an authorization check to decide whether to accept a connection. As this happens using\
  \ a message to the service port, there is **no connection established yet**. More messages on this port will just be handled\
  \ as additional connection requests. So any **checks before accepting a connection are not vulnerable** (this also means\
  \ that within `-listener:shouldAcceptNewConnection:` the audit token is safe). We are therefore **looking for XPC connections\
  \ that verify specific actions**.\n- XPC event handlers are handled synchronously. This means that the event handler for\
  \ one message must be completed before calling it for the next one, even on concurrent dispatch queues. So inside an **XPC\
  \ event handler the audit token can not be overwritten** by other normal (non-reply!) messages.\n\nTwo different methods\
  \ this might be exploitable:\n\n1. Variant1:\n   - **Exploit** **connects** to service **A** and service **B**\n     - Service\
  \ **B** can call a **privileged functionality** in service A that the user cannot\n   - Service **A** calls **`xpc_connection_get_audit_token`**\
  \ while _**not**_ inside the **event handler** for a connection in a **`dispatch_async`**.\n     - So a **different** message\
  \ could **overwrite the Audit Token** because it's being dispatched asynchronously outside of the event handler.\n   - The\
  \ exploit passes to **service B the SEND right to service A**.\n     - So svc **B** will be actually **sending** the **messages**\
  \ to service **A**.\n   - The **exploit** tries to **call** the **privileged action.** In a RC svc **A** **checks** the\
  \ authorization of this **action** while **svc B overwrote the Audit token** (giving the exploit access to call the privileged\
  \ action).\n2. Variant 2:\n   - Service **B** can call a **privileged functionality** in service A that the user cannot\n\
  \   - Exploit connects with **service A** which **sends** the exploit a **message expecting a response** in a specific **replay**\
  \ **port**.\n   - Exploit sends **service** B a message passing **that reply port**.\n   - When service **B replies**, it\
  \ s**ends the message to service A**, **while** the **exploit** sends a different **message to service A** trying to **reach\
  \ a privileged functionality** and expecting that the reply from service B will overwrite the Audit token in the perfect\
  \ moment (Race Condition).\n\n## Variant 1: calling xpc_connection_get_audit_token outside of an event handler <a href=\"\
  #variant-1-calling-xpc_connection_get_audit_token-outside-of-an-event-handler\" id=\"variant-1-calling-xpc_connection_get_audit_token-outside-of-an-event-handler\"\
  ></a>\n\nScenario:\n\n- Two mach services **`A`** and **`B`** that we can both connect to (based on the sandbox profile\
  \ and the authorization checks before accepting the connection).\n- _**A**_ must have an **authorization check** for a specific\
  \ action that **`B`** can pass (but our app can’t).\n  - For example, if B has some **entitlements** or is running as **root**,\
  \ it might allow him to ask A to perform a privileged action.\n- For this authorization check, **`A`** obtains the audit\
  \ token asynchronously, for example by calling `xpc_connection_get_audit_token` from **`dispatch_async`**.\n\n> [!CAUTION]\n\
  > In this case an attacker could trigger a **Race Condition** making a **exploit** that **asks A to perform an action**\
  \ several times while making **B send messages to `A`**. When the RC is **successful**, the **audit token** of **B** will\
  \ be copied in memory **while** the request of our **exploit** is being **handled** by A, giving it **access to the privilege\
  \ action only B could request**.\n\nThis happened with **`A`** as `smd` and **`B`** as `diagnosticd`. The function [`SMJobBless`](https://developer.apple.com/documentation/servicemanagement/1431078-smjobbless?language=objc)\
  \ from smb an be used to install a new privileged helper toot (as **root**). If a **process running as root contact** **smd**,\
  \ no other checks will be performed.\n\nTherefore, the service **B** is **`diagnosticd`** because it runs as **root** and\
  \ can be used to **monitor** a process, so once monitoring has started, it will **send multiple messages per second.**\n\
  \nTo perform the attack:\n\n1. Initiate a **connection** to the service named `smd` using the standard XPC protocol.\n2.\
  \ Form a secondary **connection** to `diagnosticd`. Contrary to normal procedure, rather than creating and sending two new\
  \ mach ports, the client port send right is substituted with a duplicate of the **send right** associated with the `smd`\
  \ connection.\n3. As a result, XPC messages can be dispatched to `diagnosticd`, but responses from `diagnosticd` are rerouted\
  \ to `smd`. To `smd`, it appears as though the messages from both the user and `diagnosticd` are originating from the same\
  \ connection.\n\n![Image depicting the exploit process](https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing/exploit.png)\n\
  \n4. The next step involves instructing `diagnosticd` to initiate monitoring of a chosen process (potentially the user's\
  \ own). Concurrently, a flood of routine 1004 messages is sent to `smd`. The intent here is to install a tool with elevated\
  \ privileges.\n5. This action triggers a race condition within the `handle_bless` function. The timing is critical: the\
  \ `xpc_connection_get_pid` function call must return the PID of the user's process (as the privileged tool resides in the\
  \ user's app bundle). However, the `xpc_connection_get_audit_token` function, specifically within the `connection_is_authorized`\
  \ subroutine, must reference the audit token belonging to `diagnosticd`.\n\n## Variant 2: reply forwarding\n\nIn an XPC\
  \ (Cross-Process Communication) environment, although event handlers don't execute concurrently, the handling of reply messages\
  \ has a unique behavior. Specifically, two distinct methods exist for sending messages that expect a reply:\n\n1. **`xpc_connection_send_message_with_reply`**:\
  \ Here, the XPC message is received and processed on a designated queue.\n2. **`xpc_connection_send_message_with_reply_sync`**:\
  \ Conversely, in this method, the XPC message is received and processed on the current dispatch queue.\n\nThis distinction\
  \ is crucial because it allows for the possibility of **reply packets being parsed concurrently with the execution of an\
  \ XPC event handler**. Notably, while `_xpc_connection_set_creds` does implement locking to safeguard against the partial\
  \ overwrite of the audit token, it does not extend this protection to the entire connection object. Consequently, this creates\
  \ a vulnerability where the audit token can be replaced during the interval between the parsing of a packet and the execution\
  \ of its event handler.\n\nTo exploit this vulnerability, the following setup is required:\n\n- Two mach services, referred\
  \ to as **`A`** and **`B`**, both of which can establish a connection.\n- Service **`A`** should include an authorization\
  \ check for a specific action that only **`B`** can perform (the user's application cannot).\n- Service **`A`** should send\
  \ a message that anticipates a reply.\n- The user can send a message to **`B`** that it will respond to.\n\nThe exploitation\
  \ process involves the following steps:\n\n1. Wait for service **`A`** to send a message that expects a reply.\n2. Instead\
  \ of replying directly to **`A`**, the reply port is hijacked and used to send a message to service **`B`**.\n3. Subsequently,\
  \ a message involving the forbidden action is dispatched, with the expectation that it will be processed concurrently with\
  \ the reply from **`B`**.\n\nBelow is a visual representation of the described attack scenario:\n\n!\\[https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing/variant2.png]\\\
  (../../../../../../images/image (1) (1) (1) (1) (1) (1) (1).png)\n\n<figure><img src=\"../../../../../../images/image (33).png\"\
  \ alt=\"https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing/variant2.png\" width=\"563\"><figcaption></figcaption></figure>\n\
  \n## Discovery Problems\n\n- **Difficulties in Locating Instances**: Searching for instances of `xpc_connection_get_audit_token`\
  \ usage was challenging, both statically and dynamically.\n- **Methodology**: Frida was employed to hook the `xpc_connection_get_audit_token`\
  \ function, filtering calls not originating from event handlers. However, this method was limited to the hooked process\
  \ and required active usage.\n- **Analysis Tooling**: Tools like IDA/Ghidra were used for examining reachable mach services,\
  \ but the process was time-consuming, complicated by calls involving the dyld shared cache.\n- **Scripting Limitations**:\
  \ Attempts to script the analysis for calls to `xpc_connection_get_audit_token` from `dispatch_async` blocks were hindered\
  \ by complexities in parsing blocks and interactions with the dyld shared cache.\n\n## The fix <a href=\"#the-fix\" id=\"\
  the-fix\"></a>\n\n- **Reported Issues**: A report was submitted to Apple detailing the general and specific issues found\
  \ within `smd`.\n- **Apple's Response**: Apple addressed the issue in `smd` by substituting `xpc_connection_get_audit_token`\
  \ with `xpc_dictionary_get_audit_token`.\n- **Nature of the Fix**: The `xpc_dictionary_get_audit_token` function is considered\
  \ secure as it retrieves the audit token directly from the mach message tied to the received XPC message. However, it's\
  \ not part of the public API, similar to `xpc_connection_get_audit_token`.\n- **Absence of a Broader Fix**: It remains unclear\
  \ why Apple didn't implement a more comprehensive fix, such as discarding messages not aligning with the saved audit token\
  \ of the connection. The possibility of legitimate audit token changes in certain scenarios (e.g., `setuid` usage) might\
  \ be a factor.\n- **Current Status**: The issue persists in iOS 17 and macOS 14, posing a challenge for those seeking to\
  \ identify and understand it.\n\n## Finding vulnerable code paths in practice (2024–2025)\n\nWhen auditing XPC services\
  \ for this bug class, focus on authorization performed outside the message’s event handler or concurrently with reply processing.\n\
  \nStatic triage hints:\n- Search for calls to `xpc_connection_get_audit_token` reachable from blocks queued via `dispatch_async`/`dispatch_after`\
  \ or other worker queues that run outside the message handler.\n- Look for authorization helpers that mix per-connection\
  \ and per-message state (e.g., fetch PID from `xpc_connection_get_pid` but audit token from `xpc_connection_get_audit_token`).\n\
  - In NSXPC code, verify that checks are done in `-listener:shouldAcceptNewConnection:` or, for per-message checks, that\
  \ the implementation uses a per-message audit token (e.g., the message’s dictionary via `xpc_dictionary_get_audit_token`\
  \ in lower-level code).\n\nDynamic triage tips:\n- Hook `xpc_connection_get_audit_token` and flag invocations whose user\
  \ stack does not include the event-delivery path (e.g., `_xpc_connection_mach_event`). Example Frida hook:\n\n```javascript\n\
  Interceptor.attach(Module.getExportByName(null, 'xpc_connection_get_audit_token'), {\n  onEnter(args) {\n    const bt =\
  \ Thread.backtrace(this.context, Backtracer.ACCURATE)\n      .map(DebugSymbol.fromAddress).join('\\n');\n    if (!bt.includes('_xpc_connection_mach_event'))\
  \ {\n      console.log('[!] xpc_connection_get_audit_token outside handler\\n' + bt);\n    }\n  }\n});\n```\n\nNotes:\n\
  - On macOS, instrumenting protected/Apple binaries may require SIP disabled or a development environment; prefer testing\
  \ your own builds or userland services.\n- For reply-forwarding races (Variant 2), monitor concurrent parsing of reply packets\
  \ by fuzzing timings of `xpc_connection_send_message_with_reply` vs. normal requests and checking whether the effective\
  \ audit token used during authorization can be influenced.\n\n## Exploitation primitives you will likely need\n\n- Multi-sender\
  \ setup (Variant 1): create connections to A and B; duplicate the send right of A’s client port and use it as B’s client\
  \ port so that B’s replies are delivered to A.\n\n```c\n// Duplicate a SEND right you already hold\nmach_port_t dup;\nmach_port_insert_right(mach_task_self(),\
  \ a_client, a_client, MACH_MSG_TYPE_MAKE_SEND);\ndup = a_client; // use `dup` when crafting B’s connect packet instead of\
  \ a fresh client port\n```\n\n- Reply hijack (Variant 2): capture the send-once right from A’s pending request (reply port),\
  \ then send a crafted message to B using that reply port so B’s reply lands on A while your privileged request is being\
  \ parsed.\n\nThese require low-level mach message crafting for the XPC bootstrap and message formats; review the mach/XPC\
  \ primer pages in this section for the exact packet layouts and flags.\n\n## Useful tooling\n\n- XPC sniffing/dynamic inspection:\
  \ gxpc (open-source XPC sniffer) can help enumerate connections and observe traffic to validate multi-sender setups and\
  \ timing. Example: `gxpc -p <PID> --whitelist <service-name>`.\n- Classic dyld interposing for libxpc: interpose on `xpc_connection_send_message*`\
  \ and `xpc_connection_get_audit_token` to log call sites and stacks during black-box testing.\n\n\n\n## References\n\n-\
  \ Sector 7 – Don’t Talk All at Once! Elevating Privileges on macOS by Audit Token Spoofing: <https://sector7.computest.nl/post/2023-10-xpc-audit-token-spoofing/>\n\
  - Apple – About the security content of macOS Ventura 13.4 (CVE‑2023‑32405): <https://support.apple.com/en-us/106333>\n\n\
  \n{{#include ../../../../../../banners/hacktricks-training.md}}"
_relative_path: macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-xpc_connection_get_audit_token-attack.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-xpc_connection_get_audit_token-attack.md
````
