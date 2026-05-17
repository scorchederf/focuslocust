---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Web Cache Deception

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-web-cache-deception-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Web Cache Deception/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Cache Deception](../../topics/web-cache-deception/web-cache-deception.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-web-cache-deception-readme |
| name | Web Cache Deception |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Web%20Cache%20Deception/README.md |

## Preserved Source Material

````yaml
_body: "# Web Cache Deception\n\n> Web Cache Deception (WCD) is a security vulnerability that occurs when a web server or\
  \ caching proxy misinterprets a client's request for a web resource and subsequently serves a different resource, which\
  \ may often be more sensitive or private, after caching it.\n\n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n\
  \    * [Caching Sensitive Data](#caching-sensitive-data)\n    * [Caching Custom JavaScript](#caching-custom-javascript)\n\
  * [CloudFlare Caching](#cloudflare-caching)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [PortSwigger/param-miner](https://github.com/PortSwigger/param-miner)\
  \ - Web Cache Poisoning Burp Extension\n\n## Methodology\n\nExample of Web Cache Deception:\n\nImagine an attacker lures\
  \ a logged-in victim into accessing `http://www.example.com/home.php/non-existent.css`\n\n1. The victim's browser requests\
  \ the resource `http://www.example.com/home.php/non-existent.css`\n2. The requested resource is searched for in the cache\
  \ server, but it's not found (resource not in cache).\n3. The request is then forwarded to the main server.\n4. The main\
  \ server returns the content of `http://www.example.com/home.php`, most probably with HTTP caching headers that instruct\
  \ not to cache this page.\n5. The response passes through the cache server.\n6. The cache server identifies that the file\
  \ has a CSS extension.\n7. Under the cache directory, the cache server creates a directory named home.php and caches the\
  \ imposter \"CSS\" file (non-existent.css) inside it.\n8. When the attacker requests `http://www.example.com/home.php/non-existent.css`,\
  \ the request is sent to the cache server, and the cache server returns the cached file with the victim's sensitive `home.php`\
  \ data.\n\n![WCD Demonstration](Images/wcd.jpg)\n\n### Caching Sensitive Data\n\n**Example 1** - Web Cache Deception on\
  \ PayPal Home Page\n\n1. Normal browsing, visit home : `https://www.example.com/myaccount/home/`\n2. Open the malicious\
  \ link : `https://www.example.com/myaccount/home/malicious.css`\n3. The page is displayed as /home and the cache is saving\
  \ the page\n4. Open a private tab with the previous URL : `https://www.example.com/myaccount/home/malicious.css`\n5. The\
  \ content of the cache is displayed\n\nVideo of the attack by Omer Gil - Web Cache Deception Attack in PayPal Home Page\n\
  [![DEMO](https://i.vimeocdn.com/video/674856618-f9bac811a4c7bcf635c4eff51f68a50e3d5532ca5cade3db784c6d178b94d09a-d)](https://vimeo.com/249130093)\n\
  \n**Example 2** - Web Cache Deception on OpenAI\n\n1. Attacker crafts a dedicated .css path of the `/api/auth/session` endpoint.\n\
  2. Attacker distributes the link\n3. Victims visit the legitimate link.\n4. Response is cached.\n5. Attacker harvests JWT\
  \ Credentials.\n\n### Caching Custom JavaScript\n\n1. Find an un-keyed input for a Cache Poisoning\n\n    ```js\n    Values:\
  \ User-Agent\n    Values: Cookie\n    Header: X-Forwarded-Host\n    Header: X-Host\n    Header: X-Forwarded-Server\n   \
  \ Header: X-Forwarded-Scheme (header; also in combination with X-Forwarded-Host)\n    Header: X-Original-URL (Symfony)\n\
  \    Header: X-Rewrite-URL (Symfony)\n    ```\n\n2. Cache poisoning attack - Example for `X-Forwarded-Host` un-keyed input\
  \ (remember to use a buster to only cache this webpage instead of the main page of the website)\n\n    ```js\n    GET /test?buster=123\
  \ HTTP/1.1\n    Host: target.com\n    X-Forwarded-Host: test\"><script>alert(1)</script>\n\n    HTTP/1.1 200 OK\n    Cache-Control:\
  \ public, no-cache\n    [..]\n    <meta property=\"og:image\" content=\"https://test\"><script>alert(1)</script>\">\n  \
  \  ```\n\n## Tricks\n\nThe following URL format are a good starting point to check for \"cache\" feature.\n\n* `https://example.com/app/conversation/.js?test`\n\
  * `https://example.com/app/conversation/;.js`\n* `https://example.com/home.php/non-existent.css`\n\n## Detecting Web Cache\
  \ Deception\n\n1. Detecting delimiter discrepancies: `/path/<dynamic-resource>;<static-resource>`\n   * For example: `/settings/profile;script.js`\n\
  \   * If the origin server uses `;` as a delimiter but the cache isn't\n   * The cache interprets the path as: `/settings/profile;script.js`\n\
  \   * The origin server interprets the path as: `/settings/profile`\n   * For more delimiter characters: see [Web cache\
  \ deception lab delimiter list](https://portswigger.net/web-security/web-cache-deception/wcd-lab-delimiter-list)\n2. Detecting\
  \ normalization: `/wcd/..%2fprofile`\n   * If the origin server resolved the path traversal sequence but the cache isn't\n\
  \   * The cache interprets the path as: `/wcd/..%2fprofile`\n   * The origin server interprets the path as: `/profile`\n\
  \n## CloudFlare Caching\n\nCloudFlare caches the resource when the `Cache-Control` header is set to `public` and `max-age`\
  \ is greater than 0.\n\n* The Cloudflare CDN does not cache HTML by default\n* Cloudflare only caches based on file extension\
  \ and not by MIME type: [cloudflare/default-cache-behavior](https://developers.cloudflare.com/cache/about/default-cache-behavior/)\n\
  \nIn Cloudflare CDN, one can implement a `Cache Deception Armor`, it is not enabled by default.\nWhen the `Cache Deception\
  \ Armor` is enabled, the rule will verify a URL's extension matches the returned `Content-Type`.\n\nCloudFlare has a list\
  \ of default extensions that gets cached behind their Load Balancers.\n\n|       |      |      |      |      |       | \
  \     |\n|-------|------|------|------|------|-------|------|\n| 7Z    | CSV  | GIF  | MIDI | PNG  | TIF   | ZIP  |\n| AVI\
  \   | DOC  | GZ   | MKV  | PPT  | TIFF  | ZST  |\n| AVIF  | DOCX | ICO  | MP3  | PPTX | TTF   | CSS  |\n| APK   | DMG  |\
  \ ISO  | MP4  | PS   | WEBM  | FLAC |\n| BIN   | EJS  | JAR  | OGG  | RAR  | WEBP  | MID  |\n| BMP   | EOT  | JPG  | OTF\
  \  | SVG  | WOFF  | PLS  |\n| BZ2   | EPS  | JPEG | PDF  | SVGZ | WOFF2 | TAR  |\n| CLASS | EXE  | JS   | PICT | SWF  |\
  \ XLS   | XLSX |\n\nExceptions and bypasses:\n\n* If the returned Content-Type is application/octet-stream, the extension\
  \ does not matter because that is typically a signal to instruct the browser to save the asset instead of to display it.\n\
  * Cloudflare allows .jpg to be served as image/webp or .gif as video/webm and other cases that we think are unlikely to\
  \ be attacks.\n* [Bypassing Cache Deception Armor using .avif extension file - fixed](https://hackerone.com/reports/1391635)\n\
  \n## Labs\n\n* [PortSwigger Labs for Web Cache Deception](https://portswigger.net/web-security/all-labs#web-cache-poisoning)\n\
  \n## References\n\n* [Cache Deception Armor - Cloudflare - May 20, 2023](https://web.archive.org/web/20230520042703/https://developers.cloudflare.com/cache/cache-security/cache-deception-armor/)\n\
  * [Exploiting cache design flaws - PortSwigger - May 4, 2020](https://web.archive.org/web/20260117063619/https://portswigger.net/web-security/web-cache-poisoning/exploiting-design-flaws)\n\
  * [Exploiting cache implementation flaws - PortSwigger - May 4, 2020](https://web.archive.org/web/20200919065854/https://portswigger.net/web-security/web-cache-poisoning/exploiting-implementation-flaws)\n\
  * [How I Test For Web Cache Vulnerabilities + Tips And Tricks - bombon (0xbxmbn) - July 21, 2022](https://web.archive.org/web/20251213233158/https://bxmbn.medium.com/how-i-test-for-web-cache-vulnerabilities-tips-and-tricks-9b138da08ff9)\n\
  * [OpenAI Account Takeover - Nagli (@naglinagli) - March 24, 2023](https://web.archive.org/web/20230412113849/https://twitter.com/naglinagli/status/1639343866313601024)\n\
  * [Practical Web Cache Poisoning - James Kettle (@albinowax) - August 9, 2018](https://web.archive.org/web/20180810041437/https://portswigger.net/blog/practical-web-cache-poisoning)\n\
  * [Shockwave Identifies Web Cache Deception and Account Takeover Vulnerability affecting OpenAI's ChatGPT - Nagli (@naglinagli)\
  \ - July 15, 2024](https://web.archive.org/web/20251010025345/https://www.shockwave.cloud/blog/shockwave-works-with-openai-to-fix-critical-chatgpt-vulnerability)\n\
  * [Web Cache Deception Attack - Omer Gil - February 27, 2017](https://web.archive.org/web/20170308135717/https://omergil.blogspot.fr:80/2017/02/web-cache-deception-attack.html)\n\
  * [Web Cache Deception Attack leads to user info disclosure - Kunal Pandey (@kunal94) - February 25, 2019](https://web.archive.org/web/20191217174659/https://medium.com/@kunal94/web-cache-deception-attack-leads-to-user-info-disclosure-805318f7bb29)\n\
  * [Web Cache Entanglement: Novel Pathways to Poisoning - James Kettle (@albinowax) - August 5, 2020](https://web.archive.org/web/20200805185253/https://portswigger.net/research/web-cache-entanglement)\n\
  * [Web cache poisoning - PortSwigger - May 4, 2020](https://web.archive.org/web/20200416160055/https://portswigger.net/web-security/web-cache-poisoning)"
_relative_path: Web Cache Deception/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Web Cache Deception/README.md
````
