#!/usr/bin/env python3
# Hiber [File/Link] CLI Client
# Jus de Patate - 2020
import sys
import os
import re

try:
    import requests
except ImportError:
    print("Couldn't import requests")
    exit(1)

version = "1.0"

hiberfile = "https://hiberfile.com"
hiberlink = "https://hiber.link"


def shortLink(originalLink):
    try:
        r = requests.post(
            hiberlink + "/link.php",
            data={"link": originalLink},
            headers={"User-Agent": "curl"},
        )
    except requests.exceptions as e:
        print("Couldn't send a request to " + hiberlink + ":")
        sys.exit(1)

    shortLink = r.text

    if shortLink == "erreur":
        print("Server returned an error")
    else:
        print(r.text)


def uploadFile(file):
    fileDict = {"my_file": open(file, "rb")}

    try:
        r = requests.post(
            hiberfile + "/send.php", files=fileDict, data={"time": "7 jours"}
        )
    except requests.exceptions as e:
        print("Upload failed: " + e)
        sys.exit(1)

    fileLink = r.headers["X-HIBERFILE-LINK"]

    if fileLink == "Erreur":
        print("Server returned an error")
        sys.exit(1)
    else:
        print(fileLink)


if not len(sys.argv) > 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Hiber Client for CLI - Jus de Patate - $version")
    print("HiberFile instance is set at $hiberfile")
    print("HiberLink instance is set at $hiberlink")
    print("")
    print("Please use either a file or an url as command argument")
elif os.path.exists(sys.argv[1]):
    uploadFile(sys.argv[1])
elif re.match("^.*[.].*$", sys.argv[1]):
    shortLink(sys.argv[1])
else:
    print("Unrecognized argument")
