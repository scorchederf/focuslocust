---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Linux - Evasion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-evasion-linux-evasion` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/linux-evasion.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Linux - Evasion](../../topics/redteam/linux-evasion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-evasion-linux-evasion |
| name | Linux - Evasion |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/evasion/linux-evasion.md |

## Preserved Source Material

````yaml
_body: "# Linux - Evasion\n\n## Summary\n\n- [File Names](#file-names)\n- [Command History](#command-history)\n- [Hiding Text](#hiding-text)\n\
  - [Timestomping](#timestomping)\n- [Hiding PID Listings From Non-Root Users](#hiding-pid-listings-from-non-root-users)\n\
  \n## File Names\n\nAn Unicode zero-width space can be inserted into filenames which makes the names visually indistinguishable:\n\
  \n```bash\n# A decoy file with no special characters\ntouch 'index.php'\n\n# An imposter file with visually identical name\n\
  touch $'index\\u200D.php'\n```\n\n## Command History\n\nMost shells save their command history so a user can recall them\
  \ again later.  The command history can be viewed with the `history` command or by manually inspecting the contents of the\
  \ file pointed to by `$HISTFILE` (e.g. `~/.bash_history`).\nThis can be prevented in a number of ways.\n\n```bash\n# Prevent\
  \ writing to the history file at all\nunset HISTFILE\n\n# Don't save this session's command history in memory\nexport HISTSIZE=0\n\
  ```\n\nIndividual commands that match a pattern in `HISTIGNORE` will be excluded from the command history, regardless of\
  \ `HISTFILE` or `HISTSIZE` settings.  \nBy default, `HISTIGNORE` will ignore all commands that begin with whitespace:\n\n\
  ```bash\n# Note the leading space character:\n my-sneaky-command\n```\n\nIf commands are accidentally added to the command\
  \ history, individual command entries can be removed with `history -d`:\n\n```bash\n# Removes the most recently logged command.\n\
  # Note that we actually have to delete two history entries at once,\n# otherwise the `history -d` command itself will be\
  \ logged as well.\nhistory -d -2 && history -d -1\n```\n\nThe entire command history can be purged as well, although this\
  \ approach is much less subtle and very likely to be noticed:\n\n```bash\n# Clears the in-memory history and writes the\
  \ empty history to disk.\nhistory -c && history -w\n```\n\nFor a more destructive approach, you can either delete the contents\
  \ of the `.bash_history` file or link it to `/dev/null` to prevent future history logging.\n\n```ps1\n# Permanently disable\
  \ bash history by linking it to /dev/null\nln /dev/null -/.bash_history -sf\n\n# Clear the existing bash history\necho \"\
  \" > .bash history\n```\n\n## Hiding Text\n\nANSI escape sequences can be abused to hide text under certain circumstances.\
  \  \nIf the file's contents are printed to the terminal (e.g. `cat`, `head`, `tail`) then the text will be hidden.  \nIf\
  \ the file is viewed with an editor (e.g. `vim`, `nano`, `emacs`), then the escape sequences will be visible.\n\n```bash\n\
  echo \"sneaky-payload-command\" > script.sh\necho \"# $(clear)\" >> script.sh\necho \"# Do not remove. Generated from /etc/issue.conf\
  \ by configure.\" >> script.sh\n\n# When printed, the terminal will be cleared and only the last line will be visible:\n\
  cat script.sh\n```\n\n## Timestomping\n\nTimestomping refers to the alteration of a file or directory's modification/access\
  \ timestamps in order to conceal the fact that it was modified.  \nThe simplest way to accomplish this is with the `touch`\
  \ command:\n\n```bash\n# Changes the access (-a) and modification (-m) times using YYYYMMDDhhmm format.\ntouch -a -m -t\
  \ 202210312359 \"example\"\n\n# Changes time using a Unix epoch timestamp.\ntouch -a -m -d @1667275140 \"example\"\n\n#\
  \ Copies timestamp from one file to another.\ntouch -a -m -r \"other_file\" \"example\"\n\n# Get the file's modification\
  \ timestamp, modify the file, then restore the timestamp.\nMODIFIED_TS=$(stat --format=\"%Y\" \"example\")\necho \"backdoor\"\
  \ >> \"example\"\ntouch -a -m -d @$MODIFIED_TS \"example\"\n```\n\nIt should be noted that `touch` can only modify the access\
  \ and modification timestamps.  It can't be used to update a file's \"change\" or \"birth\" timestamps.  The birth timestamp,\
  \ if supported by the filesystem, tracks when the file was created.  The change timestamp tracks whenever the file's metadata\
  \ changes, including updates to the access and modification timestamps.\n\nIf an attacker has root privileges, they can\
  \ work around this limitation by modifying the system clock, creating or modifying a file, then reverting the system clock:\n\
  \n```bash\nORIG_TIME=$(date)\ndate -s \"2022-10-31 23:59:59\"\ntouch -a -m \"example\"\ndate -s \"${ORIG_TIME}\"\n```\n\n\
  Don't forget that creating a file also updates the parent directory's modification timestamp as well!\n\n## Hiding PID Listings\
  \ From Non-Root Users\n\nBy default, the `/proc` filesystem exposes process information to all users. You can limit this\
  \ access to only root by modifying the `/proc` mount options.\n\n```ps1\nsudo mount -o remount,rw,nosuid,nodev,noexec,relatime,hidepid=2\
  \ /proc\n```\n\n- `hidepid=2`: Hides all processes that don't belong to the user.\n- `hidepid=1`: Hides only process details\
  \ (command line, environment variables) but still shows PIDs.\n\n## References\n\n- [ATT&CK - Impair Defenses: Impair Command\
  \ History Logging](https://attack.mitre.org/techniques/T1562/003/)\n- [ATT&CK - Indicator Removal: Timestomp](https://attack.mitre.org/techniques/T1070/006/)\n\
  - [ATT&CK - Indicator Removal on Host: Clear Command History](https://attack.mitre.org/techniques/T1070/003/)\n- [ATT&CK\
  \ - Masquerading: Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005/)\n- [Wikipedia - ANSI\
  \ escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code)\n- [InverseCos - Detecting Linux Anti-Forensics: Timestomping](https://www.inversecos.com/2022/08/detecting-linux-anti-forensics.html)"
_relative_path: redteam/evasion/linux-evasion.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/linux-evasion.md
````
