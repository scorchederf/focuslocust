---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# AES Encryption Using Crypto++ .lib in Visual Studio C++

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-miscellaneous-reversing-forensics-aes-encryption-example-using-cryptopp-.lib-in-visual-studio-c` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/aes-encryption-example-using-cryptopp-.lib-in-visual-studio-c++.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [AES Encryption Using Crypto++ .lib in Visual Studio C++](../../topics/miscellaneous-reversing-forensics/aes-encryption-using-crypto-.lib-in-visual-studio-c.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | rtt-miscellaneous-reversing-forensics-aes-encryption-example-using-cryptopp-.lib-in-visual-studio-c |
| name | AES Encryption Using Crypto++ .lib in Visual Studio C++ |
| type | redteaming-topic |
| source | redteamingtactics |
| url | https://github.com/mantvydasb/RedTeaming-Tactics-and-Techniques/blob/master/miscellaneous-reversing-forensics/aes-encryption-example-using-cryptopp-.lib-in-visual-studio-c++.md |

## Preserved Source Material

````yaml
_asset_filenames:
- image (187).png
- image (188).png
- image (189).png
- image (190).png
- image (191).png
- image (192).png
- image (193).png
_body: "# AES Encryption Using Crypto++ .lib in Visual Studio C++\n\nThis is a quick note showing how to compile, link and\
  \ include a [Crypto++](https://www.cryptopp.com) static library (cryptlib.lib), compile and execute a sample code that uses\
  \ AES CBC to encrypt and decrypt some string data.\n\n## Compiling cryptlib.lib\n\nOpen the crypto++ solution file cryptest.sln:\n\
  \n![](<../.gitbook/assets/image (193).png>)\n\nChange cryptlib project runtime library to `Multi-threaded` and change configuration\
  \ to `Release` `x64`:\n\n![](<../.gitbook/assets/image (187).png>)\n\nBuild cryptlib project. It will spit out a cryptlib.lib\
  \ static library:\n\n```\nC:\\Users\\mantvydas\\Desktop\\cryptopp\\x64\\Output\\Release\\cryptlib.lib\n```\n\n## Including\
  \ cryptlib.lib in a Project\n\nCreate a new VS project and include cryptlib.lib that you've just compiled:\n\n![](<../.gitbook/assets/image\
  \ (188).png>)\n\nChange project's runtime library to Multi-threaded - it has to use the same runtime library as cryptlib.lib:\n\
  \n![](<../.gitbook/assets/image (189).png>)\n\nCopy over all the header files from the crypto++ project to your project's\
  \ folder like so:\n\n![](<../.gitbook/assets/image (190).png>)\n\nInclude those headers in the project by adding the folder\
  \ to `Include Directories` list:\n\n![](<../.gitbook/assets/image (191).png>)\n\nCopy over the below sample code to your\
  \ main .cpp file and compile:\n\n{% code title=\"crypto.cpp\" %}\n```cpp\n// code copy pasted from here https://www.cryptopp.com/w/images/b/bd/AES-CBC-Filter.zip\n\
  // crypto.cpp : This file contains the 'main' function. Program execution begins and ends there.\n//\n\n#include \"pch.h\"\
  \n#include <iostream>\n#include \"aes.h\"\n#include <Windows.h>\n\n#include \"osrng.h\"\nusing CryptoPP::AutoSeededRandomPool;\n\
  \n#include <iostream>\nusing std::cout;\nusing std::cerr;\nusing std::endl;\n\n#include <string>\nusing std::string;\n\n\
  #include <cstdlib>\nusing std::exit;\n\n#include \"cryptlib.h\"\nusing CryptoPP::Exception;\n\n#include \"hex.h\"\nusing\
  \ CryptoPP::HexEncoder;\nusing CryptoPP::HexDecoder;\n\n#include \"filters.h\"\nusing CryptoPP::StringSink;\nusing CryptoPP::StringSource;\n\
  using CryptoPP::StreamTransformationFilter;\n\n#include \"aes.h\"\nusing CryptoPP::AES;\n\n#include \"ccm.h\"\nusing CryptoPP::CBC_Mode;\n\
  \n#include \"assert.h\"\n\nint main(int argc, char* argv[])\n{\n\tAutoSeededRandomPool prng;\n\n\tbyte key[AES::DEFAULT_KEYLENGTH];\n\
  \tprng.GenerateBlock(key, sizeof(key));\n\n\tbyte iv[AES::BLOCKSIZE];\n\tprng.GenerateBlock(iv, sizeof(iv));\n\n\tstring\
  \ plain = \"CBC Mode Test\";\n\tstring cipher, encoded, recovered;\n\n\t/*********************************\\\n\t\\*********************************/\n\
  \n\t// Pretty print key\n\tencoded.clear();\n\tStringSource(key, sizeof(key), true,\n\t\tnew HexEncoder(\n\t\t\tnew StringSink(encoded)\n\
  \t\t) // HexEncoder\n\t); // StringSource\n\tcout << \"key: \" << encoded << endl;\n\n\t// Pretty print iv\n\tencoded.clear();\n\
  \tStringSource(iv, sizeof(iv), true,\n\t\tnew HexEncoder(\n\t\t\tnew StringSink(encoded)\n\t\t) // HexEncoder\n\t); // StringSource\n\
  \tcout << \"iv: \" << encoded << endl;\n\n\t/*********************************\\\n\t\\*********************************/\n\
  \n\ttry\n\t{\n\t\tcout << \"plain text: \" << plain << endl;\n\n\t\tCBC_Mode< AES >::Encryption e;\n\t\te.SetKeyWithIV(key,\
  \ sizeof(key), iv);\n\n\t\t// The StreamTransformationFilter removes\n\t\t//  padding as required.\n\t\tStringSource s(plain,\
  \ true,\n\t\t\tnew StreamTransformationFilter(e,\n\t\t\t\tnew StringSink(cipher)\n\t\t\t) // StreamTransformationFilter\n\
  \t\t); // StringSource\n\n#if 0\n\t\tStreamTransformationFilter filter(e);\n\t\tfilter.Put((const byte*)plain.data(), plain.size());\n\
  \t\tfilter.MessageEnd();\n\n\t\tconst size_t ret = filter.MaxRetrievable();\n\t\tcipher.resize(ret);\n\t\tfilter.Get((byte*)cipher.data(),\
  \ cipher.size());\n#endif\n\t}\n\tcatch (const CryptoPP::Exception& e)\n\t{\n\t\tcerr << e.what() << endl;\n\t\texit(1);\n\
  \t}\n\n\t/*********************************\\\n\t\\*********************************/\n\n\t// Pretty print\n\tencoded.clear();\n\
  \tStringSource(cipher, true,\n\t\tnew HexEncoder(\n\t\t\tnew StringSink(encoded)\n\t\t) // HexEncoder\n\t); // StringSource\n\
  \tcout << \"cipher text: \" << encoded << endl;\n\n\t/*********************************\\\n\t\\*********************************/\n\
  \n\ttry\n\t{\n\t\tCBC_Mode< AES >::Decryption d;\n\t\td.SetKeyWithIV(key, sizeof(key), iv);\n\n\t\t// The StreamTransformationFilter\
  \ removes\n\t\t//  padding as required.\n\t\tStringSource s(cipher, true,\n\t\t\tnew StreamTransformationFilter(d,\n\t\t\
  \t\tnew StringSink(recovered)\n\t\t\t) // StreamTransformationFilter\n\t\t); // StringSource\n\n#if 0\n\t\tStreamTransformationFilter\
  \ filter(d);\n\t\tfilter.Put((const byte*)cipher.data(), cipher.size());\n\t\tfilter.MessageEnd();\n\n\t\tconst size_t ret\
  \ = filter.MaxRetrievable();\n\t\trecovered.resize(ret);\n\t\tfilter.Get((byte*)recovered.data(), recovered.size());\n#endif\n\
  \n\t\tcout << \"recovered text: \" << recovered << endl;\n\t}\n\tcatch (const CryptoPP::Exception& e)\n\t{\n\t\tcerr <<\
  \ e.what() << endl;\n\t\texit(1);\n\t}\n\n\t/*********************************\\\n\t\\*********************************/\n\
  \n\treturn 0;\n}\n```\n{% endcode %}\n\nSuccess:\n\n![](<../.gitbook/assets/image (192).png>)\n\n## References\n\n{% embed\
  \ url=\"https://www.cryptopp.com/w/images/b/bd/AES-CBC-Filter.zip\" %}\n\n{% embed url=\"https://stackoverflow.com/questions/36000317/link-errors-using-cryptopp-on-vs2012-static-library-console-application-and-clr\"\
  \ %}\n\n{% embed url=\"https://www.cryptopp.com/\" %}"
_relative_path: miscellaneous-reversing-forensics/aes-encryption-example-using-cryptopp-.lib-in-visual-studio-c++.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/miscellaneous-reversing-forensics/aes-encryption-example-using-cryptopp-.lib-in-visual-studio-c++.md
````
