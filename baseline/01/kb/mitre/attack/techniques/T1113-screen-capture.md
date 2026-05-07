---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1113
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/collection
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1113-screen-capture
tactic:
    - Collection
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as `CopyFromScreen`, `xwd`, or `screencapture`.[^1] [^2] <br>

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0004](https://attack.mitre.org/software/S0004) | TinyZBot | TinyZBot contains screen capture functionality.[^1]  |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX allows the operator to capture screenshots.[^1]  |
| [S0017](https://attack.mitre.org/software/S0017) | BISCUIT | BISCUIT has a command to periodically take screenshots of the system.[^1]  |
| [S0021](https://attack.mitre.org/software/S0021) | Derusbi | Derusbi is capable of performing screen captures.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | CHOPSTICK has the capability to capture screenshots.[^1]  |
| [S0030](https://attack.mitre.org/software/S0030) | Carbanak | Carbanak performs desktop video recording and captures screenshots of the desktop and sends it to the C2 server.[^1]  |
| [S0032](https://attack.mitre.org/software/S0032) | gh0st RAT | gh0st RAT can capture the victim’s screen remotely.[^1]  |
| [S0044](https://attack.mitre.org/software/S0044) | JHUHUGIT | A JHUHUGIT variant takes screenshots by simulating the user pressing the "Take Screenshot" key (VK_SCREENSHOT), accessing the screenshot saved in the clipboard, and converting it to a JPG image.[^1] [^2]  |
| [S0050](https://attack.mitre.org/software/S0050) | CosmicDuke | CosmicDuke takes periodic screenshots and exfiltrates them.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky captures PNG screenshots of the main screen.[^1]  |
| [S0086](https://attack.mitre.org/software/S0086) | ZLib | ZLib has the ability to obtain screenshots of the compromised system.[^1]  |
| [S0088](https://attack.mitre.org/software/S0088) | Kasidet | Kasidet has the ability to initiate keylogging and screen captures.[^1]  |
| [S0089](https://attack.mitre.org/software/S0089) | BlackEnergy | BlackEnergy is capable of taking screenshots.[^1]  |
| [S0090](https://attack.mitre.org/software/S0090) | Rover | Rover takes screenshots of the compromised system's desktop and saves them to `C:\system\screenshot.bmp` for exfiltration every 60 minutes.[^1]  |
| [S0094](https://attack.mitre.org/software/S0094) | Trojan.Karagany | Trojan.Karagany can take a desktop screenshot and save the file into `\ProgramData\Mail\MailAg\shot.png`.[^1] [^2]  |
| [S0098](https://attack.mitre.org/software/S0098) | T9000 | T9000 can take screenshots of the desktop and target application windows, saving them to user directories as one byte XOR encrypted .dat files.[^1]  |
| [S0113](https://attack.mitre.org/software/S0113) | Prikormka | Prikormka contains a module that captures screenshots of the victim's desktop.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson contains a command to perform screen captures.[^2] [^1] [^3]  |
| [S0128](https://attack.mitre.org/software/S0128) | BADNEWS | BADNEWS has a command to take a screenshot and send it to the C2 server.[^1] [^2]  |
| [S0143](https://attack.mitre.org/software/S0143) | Flame | Flame can take regular screenshots when certain applications are open that are sent to the command and control server.[^1]  |
| [S0147](https://attack.mitre.org/software/S0147) | Pteranodon | Pteranodon can capture screenshots at a configurable interval.[^1] [^2]  |
| [S0148](https://attack.mitre.org/software/S0148) | RTM | RTM can capture screenshots.[^1] [^2]  |
| [S0151](https://attack.mitre.org/software/S0151) | HALFBAKED | HALFBAKED can obtain screenshots from the victim.[^1]  |
| [S0152](https://attack.mitre.org/software/S0152) | EvilGrab | EvilGrab has the capability to capture screenshots.[^1]  |
| [S0153](https://attack.mitre.org/software/S0153) | RedLeaves | RedLeaves can capture screenshots.[^2] [^1]  |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike's Beacon payload is capable of capturing screenshots.[^1] [^2] [^3]  |
| [S0161](https://attack.mitre.org/software/S0161) | XAgentOSX | XAgentOSX contains the takeScreenShot (along with startTakeScreenShot and stopTakeScreenShot) functions to take screenshots using the CGGetActiveDisplayList, CGDisplayCreateImage, and NSImage:initWithCGImage methods.[^1]  |
| [S0163](https://attack.mitre.org/software/S0163) | Janicab | Janicab captured screenshots and sent them out to a C2 server.[^1] [^2]  |
| [S0167](https://attack.mitre.org/software/S0167) | Matryoshka | Matryoshka is capable of performing screen captures.[^1] [^2]  |
| [S0182](https://attack.mitre.org/software/S0182) | FinFisher | FinFisher takes a screenshot of the screen and displays it on top of all other windows for few seconds in an apparent attempt to hide some messages showed by the system during the setup process.[^2] [^1]  |
| [S0184](https://attack.mitre.org/software/S0184) | POWRUNER | POWRUNER can capture a screenshot from a victim.[^1]  |
| [S0187](https://attack.mitre.org/software/S0187) | Daserf | Daserf can take screenshots.[^1] [^2]  |
| [[kb/mitre/attack/software/S0192-pupy\|S0192]] | Pupy | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.[^1]  |
| [[kb/mitre/attack/software/S0194-powersploit\|S0194]] | PowerSploit | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-TimedScreenshot` Exfiltration module can take screenshots at regular intervals.[^1] [^2]  |
| [S0198](https://attack.mitre.org/software/S0198) | NETWIRE | NETWIRE can capture the victim's screen.[^3] [^2] [^1] [^4]  |
| [S0199](https://attack.mitre.org/software/S0199) | TURNEDUP | TURNEDUP is capable of taking screenshots.[^1]  |
| [S0203](https://attack.mitre.org/software/S0203) | Hydraq | Hydraq includes a component based on the code of VNC that can stream a live feed of the desktop of an infected host.[^1]  |
| [S0213](https://attack.mitre.org/software/S0213) | DOGCALL | DOGCALL is capable of capturing screenshots of the victim's machine.[^1] [^2]  |
| [S0216](https://attack.mitre.org/software/S0216) | POORAIM | POORAIM can perform screen capturing.[^1]  |
| [S0217](https://attack.mitre.org/software/S0217) | SHUTTERSPEED | SHUTTERSPEED can capture screenshots.[^1]  |
| [S0223](https://attack.mitre.org/software/S0223) | POWERSTATS | POWERSTATS can retrieve screenshots from compromised hosts.[^1] [^2]  |
| [S0234](https://attack.mitre.org/software/S0234) | Bandook | Bandook is capable of taking an image of and uploading the current desktop.[^1] [^2]  |
| [S0235](https://attack.mitre.org/software/S0235) | CrossRAT | CrossRAT is capable of taking screen captures.[^1]  |
| [S0240](https://attack.mitre.org/software/S0240) | ROKRAT | ROKRAT can capture screenshots of the infected system using the `gdi32` library.[^1] [^2] [^3] [^4] [^5]  |
| [S0248](https://attack.mitre.org/software/S0248) | yty | yty collects screenshots of the victim machine.[^1]  |
| [S0251](https://attack.mitre.org/software/S0251) | Zebrocy | A variant of Zebrocy captures screenshots of the victim’s machine in JPEG and BMP format.[^1] [^2] [^3] [^4] [^5] [^6]  |
| [S0257](https://attack.mitre.org/software/S0257) | VERMIN | VERMIN can perform screen captures of the victim’s machine.[^1]  |
| [S0260](https://attack.mitre.org/software/S0260) | InvisiMole | InvisiMole can capture screenshots of not only the entire screen, but of each separate window open, in case they are overlapping.[^1] [^2]  |
| [S0261](https://attack.mitre.org/software/S0261) | Catchamas | Catchamas captures screenshots based on specific keywords in the window’s title.[^1]  |
| [S0265](https://attack.mitre.org/software/S0265) | Kazuar | Kazuar captures screenshots of the victim’s screen.[^1]  |
| [S0270](https://attack.mitre.org/software/S0270) | RogueRobin | RogueRobin has a command named `$screenshot` that may be responsible for taking screenshots of the victim machine.[^1]  |
| [S0271](https://attack.mitre.org/software/S0271) | KEYMARBLE | KEYMARBLE can capture screenshots of the victim’s machine.[^1]  |
| [S0273](https://attack.mitre.org/software/S0273) | Socksbot | Socksbot can take screenshots.[^1]  |
| [S0275](https://attack.mitre.org/software/S0275) | UPPERCUT | UPPERCUT can capture desktop screenshots in the PNG format and send them to the C2 server.[^4] [^3] [^2] [^1]  |
| [S0277](https://attack.mitre.org/software/S0277) | FruitFly | FruitFly takes screenshots of the user's desktop.[^1]  |
| [S0279](https://attack.mitre.org/software/S0279) | Proton | Proton captures the content of the desktop with the screencapture binary.[^1]  |
| [S0282](https://attack.mitre.org/software/S0282) | MacSpy | MacSpy can capture screenshots of the desktop over multiple monitors.[^1]  |
| [S0283](https://attack.mitre.org/software/S0283) | jRAT | jRAT has the capability to take screenshots of the victim’s machine.[^1] [^2]  |
| [S0330](https://attack.mitre.org/software/S0330) | Zeus Panda | Zeus Panda can take screenshots of the victim’s machine.[^1]  |
| [S0331](https://attack.mitre.org/software/S0331) | Agent Tesla | Agent Tesla can capture screenshots of the victim’s desktop.[^1] [^2] [^3] [^4] [^5]  |
| [[kb/mitre/attack/software/S0332-remcos\|S0332]] | Remcos | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] takes automated screenshots of the infected machine.[^1] [^2]  |
| [S0337](https://attack.mitre.org/software/S0337) | BadPatch | BadPatch captures screenshots in .jpg format and then exfiltrates them.[^1]  |
| [S0338](https://attack.mitre.org/software/S0338) | Cobian RAT | Cobian RAT has a feature to perform screen capture.[^1]  |
| [S0339](https://attack.mitre.org/software/S0339) | Micropsia | Micropsia takes screenshots every 90 seconds by calling the Gdi32.BitBlt API.[^1]  |
| [S0340](https://attack.mitre.org/software/S0340) | Octopus | Octopus can capture screenshots of the victims’ machine.[^1] [^2] [^3]  |
| [S0344](https://attack.mitre.org/software/S0344) | Azorult | Azorult can capture screenshots of the victim’s machines.[^1]  |
| [S0348](https://attack.mitre.org/software/S0348) | Cardinal RAT | Cardinal RAT can capture screenshots.[^1]  |
| [S0351](https://attack.mitre.org/software/S0351) | Cannon | Cannon can take a screenshot of the desktop.[^1]  |
| [S0356](https://attack.mitre.org/software/S0356) | KONNI | KONNI can take screenshots of the victim’s machine.[^1]  |
| [[kb/mitre/attack/software/S0363-empire\|S0363]] | Empire | [[kb/mitre/attack/software/S0363-empire\|Empire]] is capable of capturing screenshots on Windows and macOS systems.[^1]  |
| [S0375](https://attack.mitre.org/software/S0375) | Remexi | Remexi takes screenshots of windows of interest.[^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT has a plugin for screen capture.[^1]  |
| [S0380](https://attack.mitre.org/software/S0380) | StoneDrill | StoneDrill can take screenshots.[^1] 	 |
| [S0381](https://attack.mitre.org/software/S0381) | FlawedAmmyy | FlawedAmmyy can capture screenshots.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can capture screenshots of the victim’s machines.[^2] [^1]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has used hooked APIs to take screenshots.[^1] [^2]  |
| [S0387](https://attack.mitre.org/software/S0387) | KeyBoy | KeyBoy has a command to perform screen grabbing.[^1]  |
| [S0398](https://attack.mitre.org/software/S0398) | HyperBro | HyperBro has the ability to take screenshots.[^1]  |
| [S0409](https://attack.mitre.org/software/S0409) | Machete | Machete captures screenshots.[^1] [^2] [^3] [^4]  |
| [S0412](https://attack.mitre.org/software/S0412) | ZxShell | ZxShell can capture screenshots.[^1]  |
| [S0417](https://attack.mitre.org/software/S0417) | GRIFFON | GRIFFON has used a screenshot module that can be used to take a screenshot of the remote system.[^1]  |
| [S0428](https://attack.mitre.org/software/S0428) | PoetRAT | PoetRAT has the ability to take screen captures.[^1] [^2]  |
| [S0431](https://attack.mitre.org/software/S0431) | HotCroissant | HotCroissant has the ability to do real time screen viewing on an infected host.[^1]  |
| [S0437](https://attack.mitre.org/software/S0437) | Kivars | Kivars has the ability to capture screenshots on the infected host.[^1]  |
| [S0438](https://attack.mitre.org/software/S0438) | Attor | Attor's has a plugin that captures screenshots of the target applications.[^1]  |
| [S0454](https://attack.mitre.org/software/S0454) | Cadelspy | Cadelspy has the ability to capture screenshots and webcam photos.[^1]  |
| [S0455](https://attack.mitre.org/software/S0455) | Metamorfo | Metamorfo can collect screenshots of the victim’s machine.[^1] [^2]   |
| [S0456](https://attack.mitre.org/software/S0456) | Aria-body | Aria-body has the ability to capture screenshots on compromised hosts.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can take screenshots every 30 seconds as well as when an external removable storage device is connected.[^1]  |
| [S0467](https://attack.mitre.org/software/S0467) | TajMahal | TajMahal has the ability to take screenshots on an infected host including capturing content from windows of instant messaging applications.[^1]  |
| [S0476](https://attack.mitre.org/software/S0476) | Valak | Valak has the ability to take screenshots on a compromised host.[^1] 	  |
| [S0484](https://attack.mitre.org/software/S0484) | Carberp | Carberp can capture display screenshots with the screens_dll.dll plugin.[^1]  |
| [S0495](https://attack.mitre.org/software/S0495) | RDAT | RDAT can take a screenshot on the infected system.[^1] 	 |
| [S0533](https://attack.mitre.org/software/S0533) | SLOTHFULMEDIA | SLOTHFULMEDIA has taken a screenshot of a victim's desktop, named it "Filter3.jpg", and stored it in the local directory.[^1]  |
| [S0546](https://attack.mitre.org/software/S0546) | SharpStage | SharpStage has the ability to capture the victim's screen.[^1] [^2]  |
| [S0582](https://attack.mitre.org/software/S0582) | LookBack | LookBack can take desktop screenshots.[^1]  |
| [[kb/mitre/attack/software/S0591-connectwise\|S0591]] | ConnectWise | [[kb/mitre/attack/software/S0591-connectwise\|ConnectWise]] can take screenshots on remote hosts.[^1]  |
| [[kb/mitre/attack/software/S0592-remoteutilities\|S0592]] | RemoteUtilities | [[kb/mitre/attack/software/S0592-remoteutilities\|RemoteUtilities]] can take screenshots on a compromised host.[^1]  |
| [S0593](https://attack.mitre.org/software/S0593) | ECCENTRICBANDWAGON | ECCENTRICBANDWAGON can capture screenshots and store them locally.[^1]  |
| [S0622](https://attack.mitre.org/software/S0622) | AppleSeed | AppleSeed can take screenshots on a compromised host by calling a series of APIs.[^1] [^2]  |
| [S0629](https://attack.mitre.org/software/S0629) | RainyDay | RainyDay has the ability to capture screenshots.[^1]  |
| [S0631](https://attack.mitre.org/software/S0631) | Chaes | Chaes can capture screenshots of the infected machine.[^1]  |
| [[kb/mitre/attack/software/S0633-sliver\|S0633]] | Sliver | [[kb/mitre/attack/software/S0633-sliver\|Sliver]] can take screenshots of the victim’s active display.[^1]  |
| [S0643](https://attack.mitre.org/software/S0643) | Peppy | Peppy can take screenshots on targeted systems.[^1]  |
| [S0644](https://attack.mitre.org/software/S0644) | ObliqueRAT | ObliqueRAT can capture a screenshot of the current screen.[^1] <br> |
| [S0647](https://attack.mitre.org/software/S0647) | Turian | Turian has the ability to take screenshots.[^1]  |
| [S0649](https://attack.mitre.org/software/S0649) | SMOKEDHAM | SMOKEDHAM can capture screenshots of the victim’s desktop.[^1] [^2]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can capture screenshots that are initially saved as ‘scr.jpg’.[^1]  |
| [S0657](https://attack.mitre.org/software/S0657) | BLUELIGHT | BLUELIGHT has captured a screenshot of the display every 30 seconds for the first 5 minutes after initiating a C2 loop, and then once every five minutes thereafter.[^1]  |
| [S0658](https://attack.mitre.org/software/S0658) | XCSSET | XCSSET saves a screen capture of the victim's system with a numbered filename and `.jpg` extension. Screen captures are taken at specified intervals based on the system. [^1]  |
| [S0660](https://attack.mitre.org/software/S0660) | Clambling | Clambling has the ability to capture screenshots.[^1]  |
| [S0662](https://attack.mitre.org/software/S0662) | RCSession | RCSession can capture screenshots from a compromised host.[^1]  |
| [S0663](https://attack.mitre.org/software/S0663) | SysUpdate | SysUpdate has the ability to capture screenshots.[^1]  |
| [S0667](https://attack.mitre.org/software/S0667) | Chrommme | Chrommme has the ability to capture screenshots.[^1]  |
| [S0674](https://attack.mitre.org/software/S0674) | CharmPower | CharmPower has the ability to capture screenshots.[^1]  |
| [S0680](https://attack.mitre.org/software/S0680) | LitePower | LitePower can take system screenshots and save them to `%AppData%`.[^1]  |
| [S0681](https://attack.mitre.org/software/S0681) | Lizar | Lizar can take JPEG screenshots of an infected system.[^2] [^1]  Lizar has also used a plugin to take a screenshot of the infected system.[^1]   |
| [S0686](https://attack.mitre.org/software/S0686) | QuietSieve | QuietSieve has taken screenshots every five minutes and saved them to the user's local Application Data folder under `Temp\SymbolSourceSymbols\icons` or `Temp\ModeAuto\icons`.[^1]  |
| [[kb/mitre/attack/software/S0692-silenttrinity\|S0692]] | SILENTTRINITY | [[kb/mitre/attack/software/S0692-silenttrinity\|SILENTTRINITY]] can take a screenshot of the current desktop.[^1]  |
| [S1016](https://attack.mitre.org/software/S1016) | MacMa | MacMa has used Apple’s Core Graphic APIs, such as `CGWindowListCreateImageFromArray`, to capture the user's screen and open windows.[^1] [^2]  |
| [S1034](https://attack.mitre.org/software/S1034) | StrifeWater | StrifeWater has the ability to take screen captures.[^1]  |
| [S1044](https://attack.mitre.org/software/S1044) | FunnyDream | The FunnyDream ScreenCap component can take screenshots on a compromised host.[^1]  |
| [[kb/mitre/attack/software/S1050-pcshare\|S1050]] | PcShare | [[kb/mitre/attack/software/S1050-pcshare\|PcShare]] can take screen shots of a compromised machine.[^1]  |
| [S1059](https://attack.mitre.org/software/S1059) | metaMain | metaMain can take and save screenshots.[^1] [^2]  |
| [S1060](https://attack.mitre.org/software/S1060) | Mafalda | Mafalda can take a screenshot of the target machine and save it to a file.[^1]  |
| [[kb/mitre/attack/software/S1063-brute-ratel-c4\|S1063]] | Brute Ratel C4 | [[kb/mitre/attack/software/S1063-brute-ratel-c4\|Brute Ratel C4]] can take screenshots on compromised hosts.[^1]  |
| [S1064](https://attack.mitre.org/software/S1064) | SVCReady | SVCReady can take a screenshot from an infected host.[^1]  |
| [S1065](https://attack.mitre.org/software/S1065) | Woody RAT | Woody RAT has the ability to take a screenshot of the infected host desktop using Windows GDI+.[^1]   |
| [S1081](https://attack.mitre.org/software/S1081) | BADHATCH | BADHATCH can take screenshots and send them to an actor-controlled C2 server.[^1]  |
| [[kb/mitre/attack/software/S1087-asyncrat\|S1087]] | AsyncRAT | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has the ability to view the screen on compromised hosts.[^1]  |
| [S1090](https://attack.mitre.org/software/S1090) | NightClub | NightClub can load a module to call `CreateCompatibleDC` and `GdipSaveImageToStream` for screen capture.[^1]  |
| [S1107](https://attack.mitre.org/software/S1107) | NKAbuse | NKAbuse can take screenshots of the victim machine.[^1]  |
| [S1122](https://attack.mitre.org/software/S1122) | Mispadu | Mispadu has the ability to capture screenshots on compromised hosts.[^3] [^4] [^1] [^2]   |
| [S1142](https://attack.mitre.org/software/S1142) | LunarMail | LunarMail can capture screenshots from compromised hosts.[^1]  |
| [S1148](https://attack.mitre.org/software/S1148) | Raccoon Stealer | Raccoon Stealer can capture screenshots from victim systems.[^2] [^1]  |
| [S1149](https://attack.mitre.org/software/S1149) | CHIMNEYSWEEP | CHIMNEYSWEEP can capture screenshots on targeted systems using a timer and either upload them or store them to disk.[^1]  |
| [S1153](https://attack.mitre.org/software/S1153) | Cuckoo Stealer | Cuckoo Stealer can run `screencapture` to collect screenshots from compromised hosts. [^1]  |
| [S1156](https://attack.mitre.org/software/S1156) | Manjusaka | Manjusaka can take screenshots of the victim desktop.[^1]  |
| [S1159](https://attack.mitre.org/software/S1159) | DUSTTRAP | DUSTTRAP can capture screenshots.[^1]  |
| [S1185](https://attack.mitre.org/software/S1185) | LightSpy | LightSpy uses Apple's built-in AVFoundation Framework library to access the user's camera and screen. It uses the `AVCaptureStillImage` to take a picture using the user's camera and the `AVCaptureScreen` to take a screenshot or record the user's screen for a specified period of time.[^1]  |
| [S1196](https://attack.mitre.org/software/S1196) | Troll Stealer | Troll Stealer can capture screenshots from victim machines.[^1] [^2]  |
| [S1201](https://attack.mitre.org/software/S1201) | TRANSLATEXT | TRANSLATEXT has the ability to capture screenshots of new browser tabs, based on the presence of the `Capture` flag.[^1]   |
| [S1207](https://attack.mitre.org/software/S1207) | XLoader | XLoader can capture screenshots on compromised hosts.[^2] [^1]  |
| [[kb/mitre/attack/software/S1209-quick-assist\|S1209]] | Quick Assist | [[kb/mitre/attack/software/S1209-quick-assist\|Quick Assist]] allows for the remote administrator to take screenshots of the running system.[^1]  |
| [S1213](https://attack.mitre.org/software/S1213) | Lumma Stealer | Lumma Stealer has taken screenshots of victim machines.[^1]  |
| [S1229](https://attack.mitre.org/software/S1229) | Havoc | Havoc can capture screenshots.[^3] [^2] [^1]  |
| [S1239](https://attack.mitre.org/software/S1239) | TONESHELL | TONESHELL has conducted screen capturing.[^1]   |
| [S1240](https://attack.mitre.org/software/S1240) | RedLine Stealer | RedLine Stealer can capture screenshots on a compromised host.[^1] [^2]  |
| [S9007](https://attack.mitre.org/software/S9007) | HTTPTroy | HTTPTroy has obtained screen captures leveraging the `screen` command which captures, encrypts and uploads the stolen image to the adversary controlled C2 server.[^1]  |
| [S9020](https://attack.mitre.org/software/S9020) | LODEINFO | LODEINFO has the ability to take screenshots.[^2] [^1] [^3]  |
| [S9031](https://attack.mitre.org/software/S9031) | AshTag | The AshTag AshenOrchestrator component has the ability to take screenshots.[^1]  |

 [^1]: [CopyFromScreen .NET](https://docs.microsoft.com/en-us/dotnet/api/system.drawing.graphics.copyfromscreen?view=netframework-4.8)
 [^2]: [Antiquated Mac Malware](https://blog.malwarebytes.com/threat-analysis/2017/01/new-mac-backdoor-using-antiquated-code/)
 [^3]: [Palo Alto Ashen Lepus DEC 2025](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
 [^4]: [Palo Alto Gamaredon Feb 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit-42-title-gamaredon-group-toolset-evolution/)
 [^5]: [Unit 42 Gamaredon February 2022](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/)
 [^6]: [SecureList Griffon May 2019](https://securelist.com/fin7-5-the-infamous-cybercrime-rig-fin7-continues-its-activities/90703/)
 [^7]: [Unit 42 Playbook Dec 2017](https://pan-unit42.github.io/playbook_viewer/)
 [^8]: [Talos Seduploader Oct 2017](https://blog.talosintelligence.com/2017/10/cyber-conflict-decoy-document.html)
 [^9]: [Talos Agent Tesla Oct 2018](https://blog.talosintelligence.com/2018/10/old-dog-new-tricks-analysing-new-rtf_15.html)
 [^10]: [DigiTrust Agent Tesla Jan 2017](https://www.digitrustgroup.com/agent-tesla-keylogger/)
 [^11]: [Fortinet Agent Tesla April 2018](https://www.fortinet.com/blog/threat-research/analysis-of-new-agent-tesla-spyware-variant.html)
 [^12]: [Fortinet Agent Tesla June 2017](https://www.fortinet.com/blog/threat-research/in-depth-analysis-of-net-malware-javaupdtr.html)
 [^13]: [Bitdefender Agent Tesla April 2020](https://labs.bitdefender.com/2020/04/oil-gas-spearphishing-campaigns-drop-agent-tesla-spyware-in-advance-of-historic-opec-deal/)
 [^14]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^15]: [FireEye APT33 Sept 2017](https://www.fireeye.com/blog/threat-research/2017/09/apt33-insights-into-iranian-cyber-espionage.html)
 [^16]: [Symantec Dragonfly](https://community.broadcom.com/symantecenterprise/communities/community-home/librarydocuments/viewdocument?DocumentKey=7382dce7-0260-4782-84cc-890971ed3f17&CommunityKey=1ecf5f55-9545-44d6-b0f4-4e4a7f5f5e68&tab=librarydocuments)
 [^17]: [Secureworks Karagany July 2019](https://www.secureworks.com/research/updated-karagany-malware-targets-energy-sector)
 [^18]: [Microsoft FinFisher March 2018](https://cloudblogs.microsoft.com/microsoftsecure/2018/03/01/finfisher-exposed-a-researchers-tale-of-defeating-traps-tricks-and-complex-virtual-machines/)
 [^19]: [FinFisher Citation](https://web.archive.org/web/20171222050934/http://www.finfisher.com/FinFisher/index.html)
 [^20]: [Netskope XLoader 2022](https://www.netskope.com/blog/new-formbook-campaign-delivered-through-phishing-emails)
 [^21]: [Google XLoader 2017](https://cloud.google.com/blog/topics/threat-intelligence/formbook-malware-distribution-campaigns/)
 [^22]: [Zscaler Cobian Aug 2017](https://www.zscaler.com/blogs/research/cobian-rat-backdoored-rat)
 [^23]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^24]: [PaloAlto Patchwork Mar 2018](https://researchcenter.paloaltonetworks.com/2018/03/unit42-patchwork-continues-deliver-badnews-indian-subcontinent/)
 [^25]: [Antiy CERT Ramsay April 2020](https://www.programmersought.com/article/62493896999/)
 [^26]: [Securelist BlackEnergy Nov 2014](https://securelist.com/be2-custom-plugins-router-abuse-and-target-profiles/67353/)
 [^27]: [S2W Troll Stealer 2024](https://medium.com/s2wblog/kimsuky-disguised-as-a-korean-company-signed-with-a-valid-certificate-to-distribute-troll-stealer-cfa5d54314e2)
 [^28]: [Symantec Troll Stealer 2024](https://www.security.com/threat-intelligence/springtail-kimsuky-backdoor-espionage)
 [^29]: [FireEye CARBANAK June 2017](https://www.fireeye.com/blog/threat-research/2017/06/behind-the-carbanak-backdoor.html)
 [^30]: [Palo Alto Unit42 STATELY TAURUS TONESHELL September 2023](https://unit42.paloaltonetworks.com/stately-taurus-attacks-se-asian-government/)
 [^31]: [Talos Oblique RAT March 2021](https://blog.talosintelligence.com/2021/02/obliquerat-new-campaign.html)
 [^32]: [Trend Micro DRBControl February 2020](https://documents.trendmicro.com/assets/white_papers/wp-uncovering-DRBcontrol.pdf)
 [^33]: [Cybereason LumaStealer Undated](https://www.cybereason.com/blog/threat-analysis-rise-of-lummastealer)
 [^34]: [Bitdefender FunnyDream Campaign November 2020](https://www.bitdefender.com/files/News/CaseStudies/study/379/Bitdefender-Whitepaper-Chinese-APT.pdf)
 [^35]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^36]: [ESET Security Mispadu Facebook Ads 2019](https://www.welivesecurity.com/2019/11/19/mispadu-advertisement-discounted-unhappy-meal/)
 [^37]: [Metabase Q Mispadu Trojan 2023](https://www.metabaseq.com/mispadu-banking-trojan/)
 [^38]: [SCILabs Malteiro 2021](https://blog.scilabs.mx/en/cyber-threat-profile-malteiro/)
 [^39]: [SCILabs URSA/Mispadu Evolution 2023](https://blog.scilabs.mx/en/evolution-of-banking-trojan-ursa-mispadu/)
 [^40]: [Lookout Dark Caracal Jan 2018](https://info.lookout.com/rs/051-ESQ-475/images/Lookout_Dark-Caracal_srr_20180118_us_v.1.0.pdf)
 [^41]: [ESET Operation Groundbait](http://www.welivesecurity.com/wp-content/uploads/2016/05/Operation-Groundbait.pdf)
 [^42]: [Mandiant APT1 Appendix](https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf)
 [^43]: [ESET DazzleSpy Jan 2022](https://www.welivesecurity.com/2022/01/25/watering-hole-deploys-new-macos-malware-dazzlespy-asia/)
 [^44]: [Objective-See MacMa Nov 2021](https://objective-see.org/blog/blog_0x69.html)
 [^45]: [BitDefender BADHATCH Mar 2021](https://www.bitdefender.com/files/News/CaseStudies/study/394/Bitdefender-PR-Whitepaper-BADHATCH-creat5237-en-EN.pdf)
 [^46]: [Huntress LightSpy macOS 2024](https://www.huntress.com/blog/lightspy-malware-variant-targeting-macos)
 [^47]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)
 [^48]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^49]: [ESET BackdoorDiplomacy Jun 2021](https://www.welivesecurity.com/2021/06/10/backdoordiplomacy-upgrading-quarian-turian/)
 [^50]: [Immersive Labs Havoc C2 APR 2024](https://www.immersivelabs.com/resources/blog/havoc-c2-framework-a-defensive-operators-guide)
 [^51]: [Zscaler Havoc FEB 2023](https://www.zscaler.com/blogs/security-research/havoc-across-cyberspace)
 [^52]: [Havoc Framework Documentation](https://havocframework.com/docs/welcome)
 [^53]: [Unit42 Cannon Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-sofacy-continues-global-attacks-wheels-new-cannon-trojan/)
 [^54]: [ESET Zebrocy Nov 2018](https://www.welivesecurity.com/2018/11/20/sednit-whats-going-zebrocy/)
 [^55]: [Unit42 Sofacy Dec 2018](https://unit42.paloaltonetworks.com/dear-joohn-sofacy-groups-global-campaign/)
 [^56]: [ESET Zebrocy May 2019](https://www.welivesecurity.com/2019/05/22/journey-zebrocy-land/)
 [^57]: [Accenture SNAKEMACKEREL Nov 2018](https://www.accenture.com/t20181129T203820Z__w__/us-en/_acnmedia/PDF-90/Accenture-snakemackerel-delivers-zekapab-malware.pdf#zoom=50)
 [^58]: [CISA Zebrocy Oct 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-303b)
 [^59]: [Kaspersky TajMahal April 2019](https://securelist.com/project-tajmahal/90240/)
 [^60]: [cobaltstrike manual](https://web.archive.org/web/20210825130434/https://cobaltstrike.com/downloads/csmanual38.pdf)
 [^61]: [Amnesty Intl. Ocean Lotus February 2021](https://www.amnestyusa.org/wp-content/uploads/2021/02/Click-and-Bait_Vietnamese-Human-Rights-Defenders-Targeted-with-Spyware-Attacks.pdf)
 [^62]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^63]: [Cybereason Molerats Dec 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/Molerats-in-the-Cloud-New-Malware-Arsenal-Abuses-Cloud-Platforms-in-Middle-East-Espionage-Campaign.pdf)
 [^64]: [BleepingComputer Molerats Dec 2020](https://www.bleepingcomputer.com/news/security/hacking-group-s-new-malware-abuses-google-and-facebook-services/)
 [^65]: [ESET InvisiMole June 2018](https://www.welivesecurity.com/2018/06/07/invisimole-equipped-spyware-undercover/)
 [^66]: [ESET InvisiMole June 2020](https://www.welivesecurity.com/wp-content/uploads/2020/06/ESET_InvisiMole.pdf)
 [^67]: [Accenture Hogfish April 2018](http://web.archive.org/web/20220810112638/https:/www.accenture.com/t20180423T055005Z_w_/se-en/_acnmedia/PDF-76/Accenture-Hogfish-Threat-Analysis.pdf)
 [^68]: [FireEye APT10 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/apt10_menupass_grou.html)
 [^69]: [GitHub SILENTTRINITY Modules July 2019](https://github.com/byt3bl33d3r/SILENTTRINITY/tree/master/silenttrinity/core/teamserver/modules/boo)
 [^70]: [Unit42 RDAT July 2020](https://unit42.paloaltonetworks.com/oilrig-novel-c2-channel-steganography/)
 [^71]: [GDATA Zeus Panda June 2017](https://cyberwtf.files.wordpress.com/2017/07/panda-whitepaper.pdf)
 [^72]: [FireEye APT41 Aug 2019](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf)
 [^73]: [FireEye APT37 Feb 2018](https://services.google.com/fh/files/misc/apt37-reaper-the-overlooked-north-korean-actor.pdf)
 [^74]: [Profero APT27 December 2020](https://web.archive.org/web/20210104144857/https://shared-public-reports.s3-eu-west-1.amazonaws.com/APT27+turns+to+ransomware.pdf)
 [^75]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
 [^76]: [Trend Micro Earth Kasha Anel NOV 2024](https://www.trendmicro.com/en_us/research/24/k/return-of-anel-in-the-recent-earth-kasha-spearphishing-campaign.html)
 [^77]: [Trend Micro Earth Kasha Updates APR 2025](https://www.trendmicro.com/en_us/research/25/d/earth-kasha-updates-ttps.html)
 [^78]: [FireEye APT10 Sept 2018](https://www.fireeye.com/blog/threat-research/2018/09/apt10-targeting-japanese-corporations-using-updated-ttps.html)
 [^79]: [Palo Alto Brute Ratel July 2022](https://unit42.paloaltonetworks.com/brute-ratel-c4-tool/)
 [^80]: [Kaspersky WIRTE November 2021](https://securelist.com/wirtes-campaign-in-the-middle-east-living-off-the-land-since-at-least-2019/105044)
 [^81]: [Unit 42 BadPatch Oct 2017](https://researchcenter.paloaltonetworks.com/2017/10/unit42-badpatch/)
 [^82]: [CheckPoint Naikon May 2020](https://research.checkpoint.com/2020/naikon-apt-cyber-espionage-reloaded/)
 [^83]: [McAfee RedLine Stealer April 2024](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/redline-stealer-a-novel-approach/)
 [^84]: [Splunk RedLine Stealer June 2023](https://www.splunk.com/en_us/blog/security/do-not-cross-the-redline-stealer-detections-and-analysis.html)
 [^85]: [Kandji Cuckoo April 2024](https://www.kandji.io/blog/malware-cuckoo-infostealer-spyware)
 [^86]: [Cybereason Valak May 2020](https://www.cybereason.com/blog/valak-more-than-meets-the-eye)
 [^87]: [Google Cloud APT41 2024](https://cloud.google.com/blog/topics/threat-intelligence/apt41-arisen-from-dust)
 [^88]: [Palo Alto Rover](http://researchcenter.paloaltonetworks.com/2016/02/new-malware-rover-targets-indian-ambassador-to-afghanistan/)
 [^89]: [BiZone Lizar May 2021](https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319)
 [^90]: [Threatpost Lizar May 2021](https://threatpost.com/fin7-backdoor-ethical-hacking-tool/166194/)
 [^91]: [Microsoft Quick Assist 2024](https://learn.microsoft.com/en-us/windows/client-management/client-tools/quick-assist)
 [^92]: [Proofpoint Operation Transparent Tribe March 2016](https://www.proofpoint.com/sites/default/files/proofpoint-operation-transparent-tribe-threat-insight-en.pdf)
 [^93]: [Trend Micro Daserf Nov 2017](http://blog.trendmicro.com/trendlabs-security-intelligence/redbaldknight-bronze-butler-daserf-backdoor-now-using-steganography/)
 [^94]: [Secureworks BRONZE BUTLER Oct 2017](https://www.secureworks.com/research/bronze-butler-targets-japanese-businesses)
 [^95]: [ESET MirrorFace DEC 2022](https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/)
 [^96]: [Kaspersky LODEINFO Part II OCT 2022](https://securelist.com/apt10-tracking-down-lodeinfo-2022-part-ii/107745/)
 [^97]: [ITOCHU LODEINFO JAN 2024](https://blog-en.itochuci.co.jp/entry/2024/01/24/134100)
 [^98]: [Cylance Cleaver](https://web.archive.org/web/20200302085133/https://www.cylance.com/content/dam/cylance/pages/operation-cleaver/Cylance_Operation_Cleaver_Report.pdf)
 [^99]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^100]: [Cisco Talos Transparent Tribe Education Campaign July 2022](https://blog.talosintelligence.com/2022/07/transparent-tribe-targets-education.html)
 [^101]: [DOJ GRU Indictment Jul 2018](https://cdn.cnn.com/cnn/2018/images/07/13/gru.indictment.pdf)
 [^102]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
 [^103]: [F-Secure Cosmicduke](https://blog.f-secure.com/wp-content/uploads/2019/10/CosmicDuke.pdf)
 [^104]: [ESET Attor Oct 2019](https://www.welivesecurity.com/wp-content/uploads/2019/10/ESET_Attor.pdf)
 [^105]: [SentinelLabs Metador Sept 2022](https://assets.sentinelone.com/sentinellabs22/metador#page=1)
 [^106]: [SentinelLabs Metador Technical Appendix Sept 2022](https://docs.google.com/document/d/1e9ZTW9b71YwFWS_18ZwDAxa-cYbV8q1wUefmKZLYVsA/edit#heading=h.lmnbtht1ikzm)
 [^107]: [HP SVCReady Jun 2022](https://threatresearch.ext.hp.com/svcready-a-new-loader-reveals-itself/)
 [^108]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^109]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^110]: [Kaspersky Flame](https://securelist.com/the-flame-questions-and-answers-51/34344/)
 [^111]: [Gen Digital Kimsuky HTTPTroy October 2025](https://www.gendigital.com/blog/insights/research/dprk-kimsuky-lazarus-analysis)
 [^112]: [Cybereason StrifeWater Feb 2022](https://www.cybereason.com/blog/research/strifewater-rat-iranian-apt-moses-staff-adds-new-trojan-to-ransomware-operations)
 [^113]: [Unit 42 VERMIN Jan 2018](https://researchcenter.paloaltonetworks.com/2018/01/unit42-vermin-quasar-rat-custom-malware-used-ukraine/)
 [^114]: [Talos Manjusaka 2022](https://blog.talosintelligence.com/manjusaka-offensive-framework/)
 [^115]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
 [^116]: [TrendMicro BKDR_URSNIF.SM](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/BKDR_URSNIF.SM?_ga=2.129468940.1462021705.1559742358-1202584019.1549394279)
 [^117]: [MalwareBytes WoodyRAT Aug 2022](https://www.malwarebytes.com/blog/threat-intelligence/2022/08/woody-rat-a-new-feature-rich-malware-spotted-in-the-wild)
 [^118]: [Proofpoint LookBack Malware Aug 2019](https://www.proofpoint.com/us/threat-insight/post/lookback-malware-targets-united-states-utilities-sector-phishing-attacks)
 [^119]: [CISA EB Aug 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-239a)
 [^120]: [TrendMicro BlackTech June 2017](https://blog.trendmicro.com/trendlabs-security-intelligence/following-trail-blacktech-cyber-espionage-campaigns/)
 [^121]: [GitHub Sliver Screen](https://github.com/BishopFox/sliver/blob/master/implant/sliver/screen/screenshot_windows.go)
 [^122]: [Unit 42 Nokki Oct 2018](https://researchcenter.paloaltonetworks.com/2018/10/unit42-nokki-almost-ties-the-knot-with-dogcall-reaper-group-uses-new-malware-to-deploy-rat/)
 [^123]: [Trend Micro Iron Tiger April 2021](https://www.trendmicro.com/en_us/research/21/d/iron-tiger-apt-updates-toolkit-with-evolved-sysupdate-malware-va.html)
 [^124]: [Unit42 Emissary Panda May 2019](https://unit42.paloaltonetworks.com/emissary-panda-attacks-middle-east-government-sharepoint-servers/)
 [^125]: [Zscaler Kimsuky TRANSLATEXT](https://www.zscaler.com/blogs/security-research/kimsuky-deploys-translatext-target-south-korean-academia#technical-analysis)
 [^126]: [ESET Gelsemium June 2021](https://www.welivesecurity.com/wp-content/uploads/2021/06/eset_gelsemium.pdf)
 [^127]: [objsee mac malware 2017](https://objective-see.com/blog/blog_0x25.html)
 [^128]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^129]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^130]: [MoustachedBouncer ESET August 2023](https://www.welivesecurity.com/en/eset-research/moustachedbouncer-espionage-against-foreign-diplomats-in-belarus/)
 [^131]: [Korean FSI TA505 2020](https://www.fsec.or.kr/user/bbs/fsec/163/344/bbsDataView/1382.do?page=1&column=&search=&searchSDate=&searchEDate=&bbsDataCategory=)
 [^132]: [ClearSky Wilted Tulip July 2017](http://www.clearskysec.com/wp-content/uploads/2017/07/Operation_Wilted_Tulip.pdf)
 [^133]: [CopyKittens Nov 2015](https://cdn2.hubspot.net/hubfs/1903456/Whitepapers/CopyKittens.pdf)
 [^134]: [Sekoia Raccoon2 2022](https://blog.sekoia.io/raccoon-stealer-v2-part-2-in-depth-analysis/)
 [^135]: [S2W Racoon 2022](https://medium.com/s2wblog/raccoon-stealer-is-back-with-a-new-version-5f436e04b20d)
 [^136]: [Kaspersky MoleRATs April 2019](https://securelist.com/gaza-cybergang-group1-operation-sneakypastes/90068/)
 [^137]: [CheckPoint Bandook Nov 2020](https://research.checkpoint.com/2020/bandook-signed-delivered/)
 [^138]: [Symantec Hydraq Jan 2010](https://www.symantec.com/security_response/writeup.jsp?docid=2010-011114-1830-99)
 [^139]: [Bitdefender Naikon April 2021](https://www.bitdefender.com/files/News/CaseStudies/study/396/Bitdefender-PR-Whitepaper-NAIKON-creat5397-en-EN.pdf)
 [^140]: [Zscaler Kasidet](http://research.zscaler.com/2016/01/malicious-office-files-dropping-kasidet.html)
 [^141]: [Talos Konni May 2017](https://blog.talosintelligence.com/2017/05/konni-malware-under-radar-for-years.html)
 [^142]: [Nccgroup Gh0st April 2018](https://research.nccgroup.com/2018/04/17/decoding-network-data-from-a-gh0st-rat-variant/)
 [^143]: [Unit 42 Kazuar May 2017](https://researchcenter.paloaltonetworks.com/2017/05/unit42-kazuar-multiplatform-espionage-backdoor-api-access/)
 [^144]: [PWC Cloud Hopper Technical Annex April 2017](https://www.pwc.co.uk/cyber-security/pdf/pwc-uk-operation-cloud-hopper-technical-annex-april-2017.pdf)
 [^145]: [FireEye FIN7 April 2017](https://www.fireeye.com/blog/threat-research/2017/04/fin7-phishing-lnk.html)
 [^146]: [FireEye Metamorfo Apr 2018](https://www.fireeye.com/blog/threat-research/2018/04/metamorfo-campaign-targeting-brazilian-users.html)
 [^147]: [ESET Casbaneiro Oct 2019](https://www.welivesecurity.com/2019/10/03/casbaneiro-trojan-dangerous-cooking/)
 [^148]: [ASERT Donot March 2018](https://www.arbornetworks.com/blog/asert/donot-team-leverages-new-modular-malware-framework-south-asia/)
 [^149]: [Radware Micropsia July 2018](https://www.radware.com/blog/security/2018/07/micropsia-malware/)
 [^150]: [FireEye Shining A Light on DARKSIDE May 2021](https://www.fireeye.com/blog/threat-research/2021/05/shining-a-light-on-darkside-ransomware-operations.html)
 [^151]: [FireEye SMOKEDHAM June 2021](https://www.fireeye.com/blog/threat-research/2021/06/darkside-affiliate-supply-chain-software-compromise.html)
 [^152]: [CIRCL PlugX March 2013](http://circl.lu/assets/files/tr-12/tr-12-circl-plugx-analysis-v1.pdf)
 [^153]: [PWC KeyBoys Feb 2017](https://web.archive.org/web/20211129064701/https://www.pwc.co.uk/issues/cyber-security-services/research/the-keyboys-are-back-in-town.html)
 [^154]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^155]: [XAgentOSX 2017](https://researchcenter.paloaltonetworks.com/2017/02/unit42-xagentosx-sofacys-xagent-macos-tool/)
 [^156]: [US-CERT KEYMARBLE Aug 2018](https://www.us-cert.gov/ncas/analysis-reports/AR18-221A)
 [^157]: [Anomali Static Kitten February 2021](https://www.anomali.com/blog/probable-iranian-cyber-actors-static-kitten-conducting-cyberespionage-campaign-targeting-uae-and-kuwait-government-agencies)
 [^158]: [ESET Turla Lunar toolset May 2024](https://www.welivesecurity.com/en/eset-research/moon-backdoors-lunar-landing-diplomatic-missions/)
 [^159]: [Talos ROKRAT](https://blog.talosintelligence.com/2017/04/introducing-rokrat.html)
 [^160]: [Talos ROKRAT 2](https://blog.talosintelligence.com/2017/11/ROKRAT-Reloaded.html)
 [^161]: [Securelist ScarCruft May 2019](https://securelist.com/scarcruft-continues-to-evolve-introduces-bluetooth-harvester/90729/)
 [^162]: [NCCGroup RokRat Nov 2018](https://research.nccgroup.com/2018/11/08/rokrat-analysis/)
 [^163]: [Malwarebytes RokRAT VBA January 2021](https://blog.malwarebytes.com/threat-analysis/2021/01/retrohunting-apt37-north-korean-apt-used-vba-self-decode-technique-to-inject-rokrat/)
 [^164]: [Cylance Shaheen Nov 2018](https://www.cylance.com/content/dam/cylance-web/en-us/resources/knowledge-center/resource-library/reports/WhiteCompanyOperationShaheenReport.pdf?_ga=2.161661948.1943296560.1555683782-1066572390.1555511517)
 [^165]: [FireEye Periscope March 2018](https://www.fireeye.com/blog/threat-research/2018/03/suspected-chinese-espionage-group-targeting-maritime-and-engineering-industries.html)
 [^166]: [Red Canary NETWIRE January 2020](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
 [^167]: [FireEye NETWIRE March 2019](https://www.mandiant.com/resources/blog/dissecting-netwire-phishing-campaigns-usage-process-hollowing)
 [^168]: [McAfee Netwire Mar 2015](https://securingtomorrow.mcafee.com/mcafee-labs/netwire-rat-behind-recent-targeted-attacks/)
 [^169]: [Proofpoint NETWIRE December 2020](https://www.proofpoint.com/us/blog/threat-insight/geofenced-netwire-campaigns)
 [^170]: [Mandiant ROADSWEEP August 2022](https://cloud.google.com/blog/topics/threat-intelligence/likely-iranian-threat-actor-conducts-politically-motivated-disruptive-activity-against/)
 [^171]: [Malwarebytes Kimsuky June 2021](https://blog.malwarebytes.com/threat-analysis/2021/06/kimsuky-apt-continues-to-target-south-korean-government-using-appleseed-backdoor/)
 [^172]: [KISA Operation Muzabi](https://web.archive.org/web/20220328121326/https://boho.or.kr/filedownload.do?attach_file_seq=2695&attach_file_id=EpF2695.pdf)
 [^173]: [Securelist Remexi Jan 2019](https://securelist.com/chafer-used-remexi-malware/89538/)
 [^174]: [Talos PoetRAT April 2020](https://blog.talosintelligence.com/2020/04/poetrat-covid-19-lures.html)
 [^175]: [Dragos Threat Report 2020](https://hub.dragos.com/hubfs/Year-in-Review/Dragos_2020_ICS_Cybersecurity_Year_In_Review.pdf?hsCtaTracking=159c0fc3-92d8-425d-aeb8-12824f2297e8%7Cf163726d-579b-4996-9a04-44e5a124d770)
 [^176]: [Symantec Chafer Dec 2015](https://www.symantec.com/connect/blogs/iran-based-attackers-use-back-door-threats-spy-middle-eastern-targets)
 [^177]: [Palo Alto T9000 Feb 2016](http://researchcenter.paloaltonetworks.com/2016/02/t9000-advanced-modular-backdoor-uses-complex-anti-analysis-techniques/)
 [^178]: [Check Point APT35 CharmPower January 2022](https://research.checkpoint.com/2022/apt35-exploits-log4j-vulnerability-to-distribute-new-modular-powershell-toolkit/)
 [^179]: [Prevx Carberp March 2011](https://web.archive.org/web/20231227000328/http://pxnow.prevx.com/content/blog/carberp-a_modular_information_stealing_trojan.pdf)
 [^180]: [Volexity InkySquid BLUELIGHT August 2021](https://www.volexity.com/blog/2021/08/17/north-korean-apt-inkysquid-infects-victims-using-browser-exploits/)
 [^181]: [CISA MAR SLOTHFULMEDIA October 2020](https://us-cert.cisa.gov/ncas/analysis-reports/ar20-275a)
 [^182]: [Unit 42 DarkHydrus July 2018](https://researchcenter.paloaltonetworks.com/2018/07/unit42-new-threat-actor-group-darkhydrus-targets-middle-east-government/)
 [^183]: [Cybereason Chaes Nov 2020](https://www.cybereason.com/hubfs/dam/collateral/reports/11-2020-Chaes-e-commerce-malware-research.pdf)
 [^184]: [FireEye MuddyWater Mar 2018](https://www.fireeye.com/blog/threat-research/2018/03/iranian-threat-group-updates-ttps-in-spear-phishing-campaign.html)
 [^185]: [TrendMicro POWERSTATS V3 June 2019](https://blog.trendmicro.com/trendlabs-security-intelligence/muddywater-resurfaces-uses-multi-stage-backdoor-powerstats-v3-and-new-post-exploitation-tools/)
 [^186]: [jRAT Symantec Aug 2018](https://www.symantec.com/blogs/threat-intelligence/jrat-new-anti-parsing-techniques)
 [^187]: [Kaspersky Adwind Feb 2016](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07195002/KL_AdwindPublicReport_2016.pdf)
 [^188]: [Trend Micro Muddy Water March 2021](https://www.trendmicro.com/en_us/research/21/c/earth-vetala---muddywater-continues-to-target-organizations-in-t.html)
 [^189]: [FireEye APT34 Dec 2017](https://www.fireeye.com/blog/threat-research/2017/12/targeted-attack-in-middle-east-by-apt34.html)
 [^190]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
 [^191]: [Unit42 Azorult Nov 2018](https://researchcenter.paloaltonetworks.com/2018/11/unit42-new-wine-old-bottle-new-azorult-variant-found-findmyname-campaign-using-fallout-exploit-kit/)
 [^192]: [Carbon Black HotCroissant April 2020](https://www.carbonblack.com/2020/04/16/vmware-carbon-black-tau-threat-analysis-the-evolution-of-lazarus/)
 [^193]: [Kaspersky StoneDrill 2017](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/07180722/Report_Shamoon_StoneDrill_final.pdf)
 [^194]: [Symantec Catchamas April 2018](https://web.archive.org/web/20190508165711/https://www-west.symantec.com/content/symantec/english/en/security-center/writeup.html/2018-040209-1742-99)
 [^195]: [NKAbuse SL](https://securelist.com/unveiling-nkabuse/111512/)
 [^196]: [PaloAlto CardinalRat Apr 2017](https://researchcenter.paloaltonetworks.com/2017/04/unit42-cardinal-rat-active-two-years/)
 [^197]: [trendmicro xcsset xcode project 2020](https://documents.trendmicro.com/assets/pdf/XCSSET_Technical_Brief.pdf)
 [^198]: [Securelist Octopus Oct 2018](https://securelist.com/octopus-infested-seas-of-central-asia/88200/)
 [^199]: [Security Affairs DustSquad Oct 2018](https://securityaffairs.co/wordpress/77165/apt/russia-linked-apt-dustsquad.html)
 [^200]: [ESET Nomadic Octopus 2018](https://www.virusbulletin.com/uploads/pdf/conference_slides/2018/Cherepanov-VB2018-Octopus.pdf)
 [^201]: [ESET RTM Feb 2017](https://www.welivesecurity.com/wp-content/uploads/2017/02/Read-The-Manual.pdf)
 [^202]: [Unit42 Redaman January 2019](https://unit42.paloaltonetworks.com/russian-language-malspam-pushing-redaman-banking-malware/)
 [^203]: [Microsoft Actinium February 2022](https://www.microsoft.com/security/blog/2022/02/04/actinium-targets-ukrainian-organizations/)
 [^204]: [ESET Machete July 2019](https://www.welivesecurity.com/wp-content/uploads/2019/08/ESET_Machete.pdf)
 [^205]: [Securelist Machete Aug 2014](https://securelist.com/el-machete/66108/)
 [^206]: [Cylance Machete Mar 2017](https://threatvector.cylance.com/en_us/home/el-machete-malware-attacks-cut-through-latam.html)
 [^207]: [360 Machete Sep 2020](https://blog.360totalsecurity.com/en/apt-c-43-steals-venezuelan-military-secrets-to-provide-intelligence-support-for-the-reactionaries-hpreact-campaign/)
 [^208]: [f-secure janicab](https://www.f-secure.com/weblog/archives/00002576.html)
 [^209]: [Janicab](https://web.archive.org/web/20230331162455/https://www.thesafemac.com/new-signed-malware-called-janicab/)
 [^210]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
