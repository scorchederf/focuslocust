---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# Crypto CTF Workflow

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-crypto-ctf-workflow-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/crypto/ctf-workflow/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Crypto CTF Workflow](../../topics/crypto/crypto-ctf-workflow.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-crypto-ctf-workflow-readme |
| name | Crypto CTF Workflow |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/crypto/ctf-workflow/README.md |

## Preserved Source Material

````yaml
_body: "# Crypto CTF Workflow\n\n{{#include ../../banners/hacktricks-training.md}}\n\n## Triage checklist\n\n1. Identify what\
  \ you have: encoding vs encryption vs hash vs signature vs MAC.\n2. Determine what is controlled: plaintext/ciphertext,\
  \ IV/nonce, key, oracle (padding/error/timing), partial leakage.\n3. Classify: symmetric (AES/CTR/GCM), public-key (RSA/ECC),\
  \ hash/MAC (SHA/MD5/HMAC), classical (Vigenere/XOR).\n4. Apply the highest-probability checks first: decode layers, known-plaintext\
  \ XOR, nonce reuse, mode misuse, oracle behavior.\n5. Escalate to advanced methods only when required: lattices (LLL/Coppersmith),\
  \ SMT/Z3, side-channels.\n\n## Online resources & utilities\n\nThese are useful when the task is identification and layer\
  \ peeling, or when you need quick confirmation of a hypothesis.\n\n### Hash lookups\n\n- Google the hash (surprisingly effective).\n\
  - [https://crackstation.net/](https://crackstation.net/)\n- [https://md5decrypt.net/](https://md5decrypt.net/)\n- [https://hashes.org/search.php](https://hashes.org/search.php)\n\
  - [https://www.onlinehashcrack.com/](https://www.onlinehashcrack.com/)\n- [https://gpuhash.me/](https://gpuhash.me/)\n-\
  \ [http://hashtoolkit.com/reverse-hash](http://hashtoolkit.com/reverse-hash)\n\n### Identification helpers\n\n- CyberChef\
  \ (magic, decode, convert): https://gchq.github.io/CyberChef/\n- dCode (ciphers/encodings playground): https://www.dcode.fr/tools-list\n\
  - Boxentriq (substitution solvers): https://www.boxentriq.com/code-breaking\n\n### Practice platforms / references\n\n-\
  \ CryptoHack (hands-on crypto challenges): https://cryptohack.org/\n- Cryptopals (classic modern crypto pitfalls): https://cryptopals.com/\n\
  \n### Automated decoding\n\n- Ciphey: https://github.com/Ciphey/Ciphey\n- python-codext (tries many bases/encodings): https://github.com/dhondta/python-codext\n\
  \n## Encodings & classical ciphers\n\n### Technique\n\nMany CTF crypto tasks are layered transforms: base encoding + simple\
  \ substitution + compression. The goal is to identify layers and peel them safely.\n\n### Encodings: try many bases\n\n\
  If you suspect layered encoding (base64 → base32 → …), try:\n\n- CyberChef \"Magic\"\n- `codext` (python-codext): `codext\
  \ <string>`\n\nCommon tells:\n\n- Base64: `A-Za-z0-9+/=` (padding `=` is common)\n- Base32: `A-Z2-7=` (often lots of `=`\
  \ padding)\n- Ascii85/Base85: dense punctuation; sometimes wrapped in `<~ ~>`\n\n### Substitution / monoalphabetic\n\n-\
  \ Boxentriq cryptogram solver: https://www.boxentriq.com/code-breaking/cryptogram\n- quipqiup: https://quipqiup.com/\n\n\
  ### Caesar / ROT / Atbash\n\n- Nayuki auto breaker: https://www.nayuki.io/page/automatic-caesar-cipher-breaker-javascript\n\
  - Atbash: http://rumkin.com/tools/cipher/atbash.php\n\n### Vigenère\n\n- [https://www.dcode.fr/vigenere-cipher](https://www.dcode.fr/vigenere-cipher)\n\
  - [https://www.guballa.de/vigenere-solver](https://www.guballa.de/vigenere-solver)\n\n### Bacon cipher\n\nOften appears\
  \ as groups of 5 bits or 5 letters:\n\n```\n00111 01101 01010 00000 ...\nAABBB ABBAB ABABA AAAAA ...\n```\n\n### Morse\n\
  \n```\n.... --- .-.. -.-. .- .-. .- -.-. --- .-.. .-\n```\n\n### Runes\n\nRunes are frequently substitution alphabets; search\
  \ for \"futhark cipher\" and try mapping tables.\n\n## Compression in challenges\n\n### Technique\n\nCompression shows up\
  \ constantly as an extra layer (zlib/deflate/gzip/xz/zstd), sometimes nested. If output almost parses but looks like garbage,\
  \ suspect compression.\n\n### Quick identification\n\n- `file <blob>`\n- Look for magic bytes:\n  - gzip: `1f 8b`\n  - zlib:\
  \ often `78 01/9c/da`\n  - zip: `50 4b 03 04`\n  - bzip2: `42 5a 68` (`BZh`)\n  - xz: `fd 37 7a 58 5a 00`\n  - zstd: `28\
  \ b5 2f fd`\n\n### Raw DEFLATE\n\nCyberChef has **Raw Deflate/Raw Inflate**, which is often the fastest path when the blob\
  \ looks compressed but `zlib` fails.\n\n### Useful CLI\n\n```bash\npython3 - <<'PY'\nimport sys, zlib\ndata = sys.stdin.buffer.read()\n\
  for wbits in [zlib.MAX_WBITS, -zlib.MAX_WBITS]:\n  try:\n    print(zlib.decompress(data, wbits=wbits)[:200])\n  except Exception:\n\
  \    pass\nPY\n```\n\n## Common CTF crypto constructs\n\n### Technique\n\nThese appear frequently because they are realistic\
  \ developer mistakes or common libraries used incorrectly. The goal is usually recognition and applying a known extraction\
  \ or reconstruction workflow.\n\n### Fernet\n\nTypical hint: two Base64 strings (token + key).\n\n- Decoder/notes: https://asecuritysite.com/encryption/ferdecode\n\
  - In Python: `from cryptography.fernet import Fernet`\n\n### Shamir Secret Sharing\n\nIf you see multiple shares and a threshold\
  \ `t` is mentioned, it is likely Shamir.\n\n- Online reconstructor (handy for CTFs): http://christian.gen.co/secrets/\n\n\
  ### OpenSSL salted formats\n\nCTFs sometimes give `openssl enc` outputs (header often begins with `Salted__`).\n\nBruteforce\
  \ helpers:\n\n- [https://github.com/glv2/bruteforce-salted-openssl](https://github.com/glv2/bruteforce-salted-openssl)\n\
  - [https://github.com/carlospolop/easy_BFopensslCTF](https://github.com/carlospolop/easy_BFopensslCTF)\n\n### General toolset\n\
  \n- RsaCtfTool: https://github.com/Ganapati/RsaCtfTool\n- featherduster: https://github.com/nccgroup/featherduster\n- cryptovenom:\
  \ https://github.com/lockedbyte/cryptovenom\n\n## Recommended local setup\n\nPractical CTF stack:\n\n- Python + `pycryptodome`\
  \ for symmetric primitives and fast prototyping\n- SageMath for modular arithmetic, CRT, lattices, and RSA/ECC work\n- Z3\
  \ for constraint-based challenges (when the crypto reduces to constraints)\n\nSuggested Python packages:\n\n```bash\npip\
  \ install pycryptodome gmpy2 sympy pwntools z3-solver\n```\n\n{{#include ../../banners/hacktricks-training.md}}"
_relative_path: crypto/ctf-workflow/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/crypto/ctf-workflow/README.md
````
