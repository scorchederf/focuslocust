---
parsed_by: focuslocust
source: gtfobins
type: generated
---
# tcpdump

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `gtfobins` |
| Type | `tool` |
| Record ID | `tcpdump` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [tcpdump](../../tools/linux/tcpdump.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tcpdump |
| name | tcpdump |
| type | tool |
| source | gtfobins |
| url | https://gtfobins.github.io/gtfobins/tcpdump/ |

## Preserved Source Material

````yaml
_body: ''
_name: tcpdump
_source_path: /home/adams/scorchederf/focuslocust/.cache/gtfobins/_gtfobins/tcpdump
functions:
  command:
  - code: 'echo /path/to/command >/path/to/temp-file

      chmod +x /path/to/temp-file

      tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z /path/to/temp-file'
    comment: This requires some traffic to be actually captured. Also note that the subprocess is immediately sent to the
      background.
    contexts:
      sudo:
        code: 'echo /path/to/command >/path/to/temp-file

          chmod +x /path/to/temp-file

          tcpdump -ln -i lo -w /dev/null -W 1 -G 1 -z /path/to/temp-file -Z root'
      unprivileged: null
    version: In recent distributions (e.g., Debian 10 and Ubuntu 18) AppArmor limits the `postrotate-command` to a small subset
      of predefined commands thus preventing the execution of the following.
  - code: tcpdump -ln -i lo -w 'command-argument' -W 1 -G 1 -z /path/to/command
    comment: This require some traffic to be actually captured. Also note that the `command-argument` string is both passed
      to the command and written as file, hence some restrictions apply.
    contexts:
      sudo: null
      unprivileged: null
  file-write:
  - code: tcpdump -ln -i lo -w /path/to/output-file -c 1 -Z user
    comment: 'This saves the packet dump (count is 1) from the loopback interface to a file. To trigger the capture use something
      like:


      ```

      nc -u localhost 1 <<<DATA

      ```


      While `user` is the owner of the packet dump file, the invoking user must be able to capture traffic on the device.'
    contexts:
      sudo: null
      suid: null
      unprivileged: null
````
