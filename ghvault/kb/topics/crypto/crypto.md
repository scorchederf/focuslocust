---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Crypto

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-crypto-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/crypto/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This section focuses on practical cryptography for hacking/CTFs: how to quickly recognize common patterns, pick the right tools, and apply known attacks.

## Preserved Body

```markdown
This section focuses on **practical cryptography for hacking/CTFs**: how to quickly recognize common patterns, pick the right tools, and apply known attacks.

If you're here for hiding data inside files, go to the **Stego** section.

## How to use this section

Crypto challenges reward speed: classify the primitive, identify what you control (oracle/leak/nonce reuse), then apply a known attack template.

### CTF workflow
{{#ref}}
ctf-workflow/README.md
{{#endref}}

### Symmetric crypto
{{#ref}}
symmetric/README.md
{{#endref}}

### Hashes, MACs, and KDFs
{{#ref}}
hashes/README.md
{{#endref}}

### Public-key crypto
{{#ref}}
public-key/README.md
{{#endref}}

### TLS and certificates
{{#ref}}
tls-and-certificates/README.md
{{#endref}}

### Crypto in malware
{{#ref}}
crypto-in-malware/README.md
{{#endref}}

### Misc
{{#ref}}
ctf-misc/README.md
{{#endref}}

## Quick setup

- Python: `python3 -m venv .venv && source .venv/bin/activate`
- Libraries: `pip install pycryptodome gmpy2 sympy pwntools`
- SageMath (often essential for lattice/RSA/ECC): https://www.sagemath.org/
```

## Source Verification

[source record](../../sources/hacktricks/crypto.md)

## Evidence Excerpt

```text
_body: '# Crypto
{{#include ../banners/hacktricks-training.md}}
This section focuses on **practical cryptography for hacking/CTFs**: how to quickly recognize common patterns, pick the
right tools, and apply known attacks.
If you''re here for hiding data inside files, go to the **Stego** section.
## How to use this section
Crypto challenges reward speed: classify the primitive, identify what you control (oracle/leak/nonce reuse), then apply
a known attack template.
```
