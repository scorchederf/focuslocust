---
parsed_by: focuslocust
source: internalallthethings
type: generated
---
# Elastic EDR

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `internalallthethings` |
| Type | `internal-topic` |
| Record ID | `iatt-redteam-evasion-elastic-edr` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/elastic-edr.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Elastic EDR](../../topics/redteam/elastic-edr.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | iatt-redteam-evasion-elastic-edr |
| name | Elastic EDR |
| type | internal-topic |
| source | internalallthethings |
| url | https://github.com/swisskyrepo/InternalAllTheThings/blob/main/docs/redteam/evasion/elastic-edr.md |

## Preserved Source Material

````yaml
_body: "# Elastic EDR\n\n> Elastic EDR (Endpoint Detection and Response) is a component of Elastic Security designed to address\
  \ cybersecurity threats at the endpoint level. It plays a crucial role in preventing, detecting, and responding to cyber\
  \ threats like ransomware and malware.\n\n* [peasead/elastic-container](https://github.com/peasead/elastic-container) -\
  \ Stand up a simple Elastic container with Kibana, Fleet, and the Detection Engine\n\n## Setup\n\n* First, you need `docker`\
  \ and the `docker-compose` plugin\n\n    ```ps1\n    # Add Docker's official GPG key:\n    sudo apt-get update\n    sudo\
  \ apt-get install ca-certificates curl\n    sudo install -m 0755 -d /etc/apt/keyrings\n    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg\
  \ -o /etc/apt/keyrings/docker.asc\n    sudo chmod a+r /etc/apt/keyrings/docker.asc\n\n    # Add the repository to Apt sources:\n\
  \    echo \\\n    \"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu\
  \ \\\n    $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable\" | \\\n    sudo tee /etc/apt/sources.list.d/docker.list\
  \ > /dev/null\n    sudo apt-get update\n\n    # Install docker from apt\n    sudo apt-get install docker-ce docker-ce-cli\
  \ containerd.io docker-buildx-plugin docker-compose-plugin\n    ```\n\n* You might want to grant the `docker` right to the\
  \ default user\n\n    ```ps1\n    sudo groupadd docker\n    sudo usermod -aG docker $USER\n    ```\n\n* Install the requirements\
  \ for the elastic scripts\n\n    ```ps1\n    apt-get update\n    apt-get install jq git curl\n    ```\n\n* Clone the project\n\
  \n    ```ps1\n    git clone https://github.com/peasead/elastic-container\n    cd elastic-container\n    ```\n\n* Edit `.env`\
  \ to set the credentials and activate rules\n\n    ```ps1\n    ELASTIC_PASSWORD=\"changeme\"\n    KIBANA_PASSWORD=\"changeme\"\
  \n    STACK_VERSION=\"8.11.2\"\n    WindowsDR=1\n    LICENSE=trial # enable the platinum features\n    ```\n\n* Download\
  \ the images and run the containers\n\n    ```ps1\n    chmod +x ./elastic-container.sh\n    ./elastic-container.sh start\n\
  \    ```\n\n* Access the Elastic EDR interface at `https://localhost:5601`\n* Fleet > `Add agent`\n* Enroll in Fleet (recommended)\n\
  * Copy Windows PowerShell one-liner and append the `--insecure` flag if you are using untrusted certificates\n\n    ```ps1\n\
  \    powershell Invoke-WebRequest -Uri https://artifacts.elastic.co/downloads/beats/elastic-agent/elastic-agent-7.15.1-windows-x86_64.zip\
  \ -outfile elastic-agent-7.15.1-windows-x86_64.zip\n    Expand-Archive -Path elastic-agent-7.15.1-windows-x86_64.zip -DestinationPath\
  \ C:\\ElasticAgent\n    C:\\ElasticAgent\\elastic-agent-7.15.1-windows-x86_64\\elastic-agent.exe install -f --fleet-server-es={{\
  \ fleet_server_es }} --fleet-server-service-token={{ fleet_token }} --fleet-server-policy={{ fleet_policy }}\n    ```\n\n\
  * Fleet > Integrations > Elastic Defend\n    * Switch `Prevent` to `Detect`, to keep the execution running\n    * Enable\
  \ these features to collect more data\n\n        ```ps1\n        windows.advanced.memory_protection.shellcode_collect_sample\n\
  \        windows.advanced.memory_protection.memory_scan_collect_sample\n        windows.advanced.memory_protection.shellcode_enhanced_pe_parsing\n\
  \        ```\n\n* Destroy the containers\n\n    ```ps1\n    ./elastic-container.sh destroy\n    ```\n\n## References\n\n\
  * [The Elastic Container Project for Security Research - Andrew Pease, Colson Wilhoit, Derek Ditch - 1 March 2023](https://www.elastic.co/security-labs/the-elastic-container-project)\n\
  * [Cyber Security Lab Basics - Installing EDR in Malware Development Lab - AhmedS Kasmani](https://www.youtube.com/watch?v=1luhjL7TN9U)\n\
  * [Setting Up Elastic 8 with Kibana, Fleet, Endpoint Security, and Windows Log Collection - IppSec - 10 oct. 2022](https://youtu.be/Ts-ofIVRMo4)"
_relative_path: redteam/evasion/elastic-edr.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/internalallthethings/docs/redteam/evasion/elastic-edr.md
````
