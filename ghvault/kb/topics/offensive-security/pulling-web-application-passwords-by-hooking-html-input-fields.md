---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Pulling Web Application Passwords by Hooking HTML Input Fields

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-credential-access-and-credential-dumping-stealing-web-application-credentials-by-hooking-input-fields` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/credential-access-and-credential-dumping/stealing-web-application-credentials-by-hooking-input-fields.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A technique for stealing web application passwords from compromised systems by hooking input password fields in HTML applications and effectively implementing a simple keylogger.

## Preserved Body

````markdown
A technique for stealing web application passwords from compromised systems by hooking input `password` fields in HTML applications and effectively implementing a simple keylogger.

## When is it useful?

The technique is useful and can be executed when:

* You have RDP'd into the compromised system, where a target user utilizes some web application to perform his/her daily duties, that is of interest to you
*   You need to get access credentials to that application for whatever reason (i.e collecting passwords for re-use or looking to see how the user usually constructs passwords, etc)

    and can't/don't want to use a keylogger for whatever reason
* Tab with the target web application is open

## Hooking the Password Field

### Events

Password fields in web applications are `input` fields with attribute `type` set to `password` as shown below:

![HTML markup snippet from github.com](<../../_assets/image (417).png>)

All HTML elements can respond to various types of events and execute code when those occur. For example, input fields can respond to events such `onFocus` (when an element gets focus), `onBlur` (when an element loses focus) and many other events amongst which are various keyboard events `onKeyPress`, `onKeyDown`, and `onKeyUp`.&#x20;

For more about events - [https://www.w3schools.com/tags/ref\_eventattributes.asp](https://www.w3schools.com/tags/ref\_eventattributes.asp)

### Hooking

Below is a simple JavaScript/jQuery code that hooks HTML `password` fields:

```javascript
t=""; $('input[type="password"]').onkeypress = function (e) { t+=e.key; console.log(t); localStorage.setItem("pw", t); } 
```
The above code only captures the password field, but username could be captured the same way.
The above code needs to be executed in the context of the target web application you want to capture the password for. Once the above code snippet is executed, it performs the following:

* selects an input field of type `password` inside the HTML page of the target web application
* binds the `onKeyPress` event handler with a function that processes captured keys a user types into the `password` field when logging in to the target application
  * the function prints out captured keys into the browser's console view for this demo's purposes
  * the function stores the captured password in browser's `localStorage` key `pw`
If the user closes the browser or even a tab with the web application you are targeting before the password was captured, the hooks will be cleared and the binding / hooking processes will need to be repeated again.
## Demo

Below shows the hooking in action inside the Chrome dev tools (can be done the same way in IE and FF):

* Inside the dev console (F12 to open/close), the hooking code is inserted
* Dummy password is typed into the password field
* Dummy password is being printed to the dev console
* Dummy password is saved into application's localStorage `pw` key

![](<../../_assets/hooking-web-password-fields (1).gif>)

## Reading Captured Password

Say, you've hooked the password field, stopped the operation for the day and then resumed it next day and now you want to check if the password got captured - there are at least a couple of ways of doing it.

### LocalStorage via Console

You could again RDP into the compromised system, open up Chrome dev tools (F12) and in the console, type:

```javascript
localStorage.pw
```

![Password that was captured earlier](<../../_assets/image (407).png>)

...or simply navigate to the dev console and open Application > LocalStorage section as shown in the above gif.

### LocalStorage Files on the Disk

The `localStorage` information is also stored on the disk. For Chrome, the files of are located here  C:\Users\spotless\AppData\Local\Google\Chrome\User Data\Default\Local Storage\leveldb and is stored in a file XXXXXX.log. In my case, it was the file `009691.log`

Below shows `password` (lime) for github.com (blue) stored in `localStorage` key `pw` (orange):

![009691.log](<../../_assets/image (419).png>)
Use an obscure, but descriptive localStorage key to store the captured password in. It will make it easier for you to retrieve the stored password later.
### Exfiltration

The initial code could be easily adapted to exfiltrate the password to an attacker controlled web server on each key press, taking away the need to RDP to the target system or fiddling with localStorage files.
Use encrypted communications when transferring the password out of the compromised environment.
## Detection

For a start, the .log file (009691.log in my case) in C:\Users\spotless\AppData\Local\Google\Chrome\User Data\Default\Local Storage\leveldb, contains the actual hooking code we inserted into Chrome's dev console for the target web application:&#x20;

![](<../../_assets/image (421).png>)

...suggesting that one could monitor C:\Users\\\<user>\AppData\Local\Google\Chrome\User Data\Default\Local Storage\leveldb for \*.log files that contain jQuery/vanilla JavaScript `password` field selector and keywords `onkeypress`, `onkeyup`, `onkeydown`.&#x20;
````

## Source Verification

[source record](../../sources/redteamingtactics/pulling-web-application-passwords-by-hooking-html-input-fields.md)

## Evidence Excerpt

```text
_asset_filenames:
- hooking-web-password-fields (1).gif
- image (407).png
- image (417).png
- image (419).png
- image (421).png
_body: "---\ndescription: Credential Access, Keylogger\n---\n\n# Pulling Web Application Passwords by Hooking HTML Input Fields\n\
\nA technique for stealing web application passwords from compromised systems by hooking input `password` fields in HTML\
```
