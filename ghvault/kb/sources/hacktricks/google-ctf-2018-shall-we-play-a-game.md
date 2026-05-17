---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Google CTF 2018 - Shall We Play a Game?

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-mobile-pentesting-android-app-pentesting-google-ctf-2018-shall-we-play-a-game` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/google-ctf-2018-shall-we-play-a-game.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Google CTF 2018 - Shall We Play a Game?](../../topics/mobile-pentesting/google-ctf-2018-shall-we-play-a-game.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-mobile-pentesting-android-app-pentesting-google-ctf-2018-shall-we-play-a-game |
| name | Google CTF 2018 - Shall We Play a Game? |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/mobile-pentesting/android-app-pentesting/google-ctf-2018-shall-we-play-a-game.md |

## Preserved Source Material

````yaml
_body: "# Google CTF 2018 - Shall We Play a Game?\n\n{{#include ../../banners/hacktricks-training.md}}\n\nDownload the APK\
  \ here:\n\nI am going to upload the APK to [https://appetize.io/](https://appetize.io) (free account) to see how the apk\
  \ is behaving:\n\n![](<../../images/image (421).png>)\n\nLooks like you need to win 1000000 times to get the flag.\n\nFollowing\
  \ the steps from [pentesting Android]() you can decompile the application to get the smali code and read the Java code using\
  \ jadx.\n\nReading the java code:\n\n![](<../../images/image (495).png>)\n\nIt looks like the function that is going print\
  \ the flag is **m().**\n\n## **Smali changes**\n\n### **Call m() the first time**\n\nLets make the application call m()\
  \ if the variable _this.o != 1000000_ to do so, just cange the condition:\n\n```\n if-ne v0, v9, :cond_2\n```\n\nto:\n\n\
  ```\n if-eq v0, v9, :cond_2\n```\n\n![Before](<../../images/image (383).png>)\n\n![After](<../../images/image (838).png>)\n\
  \nFollow the steps of [pentest Android]() to recompile and sign the APK. Then, upload it to [https://appetize.io/](https://appetize.io)\
  \ and lets see what happens:\n\n![](<../../images/image (128).png>)\n\nLooks like the flag is written without being completely\
  \ decrypted. Probably the m() function should be called 1000000 times.\n\n**Other way** to do this is to not change the\
  \ instrucction but change the compared instructions:\n\n![](<../../images/image (840).png>)\n\n**Another way** is instead\
  \ of comparing with 1000000, set the value to 1 so this.o is compared with 1:\n\n![](<../../images/image (629).png>)\n\n\
  A forth way is to add an instruction to move to value of v9(1000000) to v0 _(this.o)_:\n\n![](<../../images/image (414).png>)\n\
  \n![](<../../images/image (424).png>)\n\n## Solution\n\nMake the application run the loop 100000 times when you win the\
  \ first time. To do so, you only need to create the **:goto_6** loop and make the application **jump there if `this.o`**\
  \ does not value 100000:\n\n![](<../../images/image (1090).png>)\n\nYou need to do this inside a physical device as (I don't\
  \ know why) this doesn't work in an emulated device.\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: mobile-pentesting/android-app-pentesting/google-ctf-2018-shall-we-play-a-game.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/mobile-pentesting/android-app-pentesting/google-ctf-2018-shall-we-play-a-game.md
````
