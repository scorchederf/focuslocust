---
parsed_by: focuslocust
source: redteamingtactics
type: generated
---
# Spiderfoot 101 with Kali using Docker

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `redteamingtactics` |
| Type | `redteaming-topic` |
| Record ID | `rtt-offensive-security-red-team-infrastructure-spiderfoot-101-with-kali-using-docker` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/redteaming-tactics-and-techniques/offensive-security/red-team-infrastructure/spiderfoot-101-with-kali-using-docker.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This lab walks through some simple steps required to get the OSINT tool Spiderfoot up and running on a Kali Linux using Docker.

## Preserved Body

````markdown
This lab walks through some simple steps required to get the OSINT tool Spiderfoot up and running on a Kali Linux using Docker.

Spiderfoot is an application that enables you as a pentester/red teamer to collect intelligence about a given subject - email address, username, domain or IP address that may help you in planning and advancing your attacks against them.

## Download Spiderfoot

Download the Spiderfoot linux package from [https://www.spiderfoot.net/download/](https://www.spiderfoot.net/download/) and extract it to a location of your choice on your file system.\
I extracted it to `/root/Downloads/spiderfoot-2.12.0-src/spiderfoot-2.12`

and made it my working directory:

```csharp
cd /root/Downloads/spiderfoot-2.12.0-src/spiderfoot-2.12
```

## Upgrade PIP

You may need to upgrade the pip before it starts giving you trouble:

```csharp
pip install --upgrade pip
```

## Build Docker Image

Build the spiderfoot docker image :

```
docker build -t spiderfoot .
```

![](<../../_assets/Screenshot from 2018-12-17 13-13-33.png>)

Check if the image got created successfully:

```
docker images
```

You should see the spiderfoot image creted seconds ago:

![](<../../_assets/Screenshot from 2018-12-17 13-00-55.png>)

## Run the Spiderfoot Docker

```csharp
docker run -p 5009:5001 -d spiderfoot
```

The above will run previously created spiderfoot image in the background and expose a TCP port 5009 on the host computer. Any traffic sent to `host:5009` will be forwarded to the port 5001 on the docker where spiderfoot is running and listening.

To check if the docker image is running, we can do:

```
docker ps
```

The below confirms the docker is indeed running the spiderfoot image and is listening on port 5001:

![](<../../_assets/Screenshot from 2018-12-17 13-20-22.png>)

Below confirms that the host machine has now exposed the TCP port 5009 (which forwards traffic to the docker's port 5001):

![](<../../_assets/Screenshot from 2018-12-17 13-02-03 (1).png>)

## Using Spiderfoot

Navigate to your host:5009 to access the spiderfoot UI and start a new scan:

![](<../../_assets/Screenshot from 2018-12-17 12-57-59.png>)

During the scan, we can start observing various pieces of data being returned from the internet:

![](<../../_assets/Screenshot from 2018-12-17 12-58-32.png>)

Drilling down to one of the above categories - DNS records:

![](<../../_assets/Screenshot from 2018-12-17 12-58-45.png>)

## References
````

## Source Verification

[source record](../../sources/redteamingtactics/spiderfoot-101-with-kali-using-docker.md)

## Evidence Excerpt

```text
_asset_filenames:
- Screenshot from 2018-12-17 12-57-59.png
- Screenshot from 2018-12-17 12-58-32.png
- Screenshot from 2018-12-17 12-58-45.png
- Screenshot from 2018-12-17 13-00-55.png
- Screenshot from 2018-12-17 13-02-03 (1).png
- Screenshot from 2018-12-17 13-13-33.png
- Screenshot from 2018-12-17 13-20-22.png
```
