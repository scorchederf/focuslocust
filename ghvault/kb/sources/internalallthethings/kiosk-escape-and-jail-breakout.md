---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Kiosk Escape and Jail Breakout

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-escape-breakout` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/escape-breakout.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Kiosk Escape and Jail Breakout](../../topics/cheatsheets/kiosk-escape-and-jail-breakout.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-escape-breakout |
| name | Kiosk Escape and Jail Breakout |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/escape-breakout.md |

## Preserved Source Material

````yaml
_body: "# Kiosk Escape and Jail Breakout\n\n## Summary\n\n* [Methodology](#methodology)\n* [Gaining a command shell](#gaining-a-command-shell)\n\
  * [Sticky Keys](#sticky-keys)\n* [Dialog Boxes](#dialog-boxes)\n    * [Creating new files](#creating-new-files)\n    * [Open\
  \ a new Windows Explorer instance](#open-a-new-windows-explorer-instance)\n    * [Exploring Context Menus](#exploring-context-menus)\n\
  \    * [Save as](#save-as)\n    * [Input Boxes](#input-boxes)\n    * [Bypass file restrictions](#bypass-file-restrictions)\n\
  * [Internet Explorer](#internet-explorer)\n* [Shell URI Handlers](#shell-uri-handlers)\n* [References](#references)\n\n\
  ## Tools\n\n* [kiosk.vsim.xyz](https://kiosk.vsim.xyz/) - Tooling for browser-based, Kiosk mode testing.\n* [break.yxz.red](https://break.yxz.red/)\
  \ - Breakout Kit for Web Browser / Kiosk breakout Assessments.\n\n## Methodology\n\n* Display global variables and their\
  \ permissions: `export -p`\n* Switch to another user using `sudo`/`su`\n* Basic privilege escalations such as CVE, sudo\
  \ misconfiguration, etc. Comprehensive list at [Linux](https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/linux-privilege-escalation/)\
  \ / [Windows](https://swisskyrepo.github.io/InternalAllTheThings/redteam/escalation/windows-privilege-escalation/)\n* List\
  \ default commands in the restricted shell: `compgen -c`\n* Container escape if it's running inside a `Docker`/`LXC` container\n\
  * Pivot onto the network\n    * Scan other machines on the network or attempt SSRF exploitation\n    * Metadata for Cloud\
  \ assets, see `cloud/aws` and `cloud/azure`\n* Use globbing capability built inside the shell: `echo *`, `echo .*`, `echo\
  \ /*`\n\n## Gaining a command shell\n\n* **Shortcut**\n    * [Window] + [R] -> cmd\n    * [CTRL] + [SHIFT] + [ESC] -> Task\
  \ Manager\n    * [CTRL] + [ALT] + [DELETE] -> Task Manager\n* **Access through file browser**: Browsing to the folder containing\
  \ the binary (i.e. `C:\\windows\\system32\\`), we can simply right click and `open` it\n* **Drag-and-drop**: dragging and\
  \ dropping any file onto the cmd.exe\n* **Hyperlink**: `file:///c:/Windows/System32/cmd.exe`\n* **Task Manager**: `File`\
  \ > `New Task (Run...)` > `cmd`\n* **MSPAINT.exe**\n    * Open MSPaint.exe and set the canvas size to: `Width=6` and `Height=1`\
  \ pixels\n    * Zoom in to make the following tasks easier\n    * Using the colour picker, set pixels values to (from left\
  \ to right):\n\n        ```ps1\n        1st: R: 10,  G: 0,   B: 0\n        2nd: R: 13,  G: 10,  B: 13\n        3rd: R: 100,\
  \ G: 109, B: 99\n        4th: R: 120, G: 101, B: 46\n        5th: R: 0,   G: 0,   B: 101\n        6th: R: 0,   G: 0,   B:\
  \ 0\n        ```\n\n    * Save it as 24-bit Bitmap (*.bmp;*.dib)\n    * Change its extension from bmp to bat and run\n \
  \   * The generated file is also available for download: [escape-breakout-mspaint.bmp](./files/escape-breakout-mspaint.bmp)\n\
  \n## Sticky Keys\n\n* Spawn the sticky keys dialog\n    * Via Shell URI : `shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}`\n\
  \    * Hit 5 times [SHIFT]\n* Visit \"Ease of Access Center\"\n* You land on \"Setup Sticky Keys\", move up a level on \"\
  Ease of Access Center\"\n* Start the OSK (On-Screen-Keyboard)\n* You can now use the keyboard shortcut (CTRL+N)\n\n## Dialog\
  \ Boxes\n\n### Creating new files\n\n* Batch files – Right click > New > Text File > rename to .BAT (or .CMD) > edit > open\n\
  * Shortcuts – Right click > New > Shortcut > `%WINDIR%\\system32`\n\n## Open a new Windows Explorer instance\n\n* Right\
  \ click any folder > select `Open in new window`\n\n## Exploring Context Menus\n\n* Right click any file/folder and explore\
  \ context menus\n* Clicking `Properties`, especially on shortcuts, can yield further access via `Open File Location`\n\n\
  ### Save as\n\n* \"Save as\" / \"Open as\" option\n* \"Print\" feature – selecting \"print to file\" option (XPS/PDF/etc)\n\
  * `\\\\127.0.0.1\\c$\\Windows\\System32\\` and execute `cmd.exe`\n\n### Input Boxes\n\nMany input boxes accept file paths;\
  \ try all inputs with UNC paths such as `//attacker–pc/` or `//127.0.0.1/c$` or `C:\\`\n\n### Bypass file restrictions\n\
  \nEnter *.* or *.exe or similar in `File name` box\n\n## Internet Explorer\n\n### Download and Run/Open\n\n* Text files\
  \ -> opened by Notepad\n\n### Menus\n\n* The address bar\n* Search menus\n* Help menus\n* Print menus\n* All other menus\
  \ that provide dialog boxes\n\n### Accessing filesystem\n\nEnter these paths in the address bar:\n\n* file://C:/windows\n\
  * C:/windows/\n* %HOMEDRIVE%\n* \\\\127.0.0.1\\c$\\Windows\\System32\n\n### Unassociated Protocols\n\nIt is possible to\
  \ escape a browser based kiosk with other protocols than usual `http` or `https`.\nIf you have access to the address bar,\
  \ you can use any known protocol (`irc`, `ftp`, `telnet`, `mailto`, etc.)\nto trigger the *open with* prompt and select\
  \ a program installed on the host.\nThe program will than be launched with the uri as a parameter, you need to select a\
  \ program that will not crash when recieving it.\nIt is possible to send multiple parameters to the program by adding spaces\
  \ in your uri.\n\nNote: This technique required that the protocol used is not already associated with a program.\n\nExample\
  \ - Launching Firefox with a custom profile:\n\nThis is a nice trick since Firefox launched with the custom profile may\
  \ not be as much hardened as the default profile.\n\n0. Firefox need to be installed.\n1. Enter the following uri in the\
  \ address bar: `irc://127.0.0.1 -P \"Test\"`\n2. Press enter to navigate to the uri.\n3. Select the firefox program.\n4.\
  \ Firefox will be launched with the profile `Test`.\n\nIn this example, it's the equivalent of running the following command:\n\
  \n```ps1\nfirefox irc://127.0.0.1 -P \"Test\"\n```\n\n## Shell URI Handlers\n\nA URI (Uniform Resource Identifier) handler\
  \ is a software component that enables a web browser or operating system to pass a URI to an appropriate application for\
  \ further handling.\n\nFor example, when you click on a \"mailto:\" link in a webpage, your device knows to open your default\
  \ email application. This is because the \"mailto:\" URI scheme is registered to be handled by an email application. Similarly,\
  \ \"http:\" and \"https:\" URIs are typically handled by a web browser.\n\nIn essence, URI handlers provide a bridge between\
  \ web content and desktop applications, allowing for a seamless user experience when navigating between different types\
  \ of resources.\n\nThe following URI handlers might trigger application on the machine:\n\n* shell:DocumentsLibrary\n* shell:Librariesshell:UserProfiles\n\
  * shell:Personal\n* shell:SearchHomeFolder\n* shell:System shell:NetworkPlacesFolder\n* shell:SendTo\n* shell:Common Administrative\
  \ Tools\n* shell:MyComputerFolder\n* shell:InternetFolder\n\n## References\n\n* [PentestPartners - Breaking out of Citrix\
  \ and other restricted desktop environments](https://www.pentestpartners.com/security-blog/breaking-out-of-citrix-and-other-restricted-desktop-environments/)\n\
  * [Breaking Out! of Applications Deployed via Terminal Services, Citrix, and Kiosks - Scott Sutherland - May 22nd, 2013](https://blog.netspi.com/breaking-out-of-applications-deployed-via-terminal-services-citrix-and-kiosks/)\n\
  * [Escaping from KIOSKs - HackTricks](https://book.hacktricks.xyz/physical-attacks/escaping-from-gui-applications)\n* [Breaking\
  \ out of Windows Kiosks using only Microsoft Edge - Firat Acar - May 24, 2022](https://blog.nviso.eu/2022/05/24/breaking-out-of-windows-kiosks-using-only-microsoft-edge/)\n\
  * [HOW TO LAUNCH COMMAND PROMPT AND POWERSHELL FROM MS PAINT - 2022-05-14 - Rickard](https://tzusec.com/how-to-launch-command-prompt-and-powershell-from-ms-paint/)"
_relative_path: cheatsheets/escape-breakout.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/escape-breakout.md
````
