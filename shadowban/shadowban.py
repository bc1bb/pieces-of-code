#!/usr/bin/env python3
# very tiny and basic python3 script to check if you are shadow banned by twitter
# Jus de Patate - 2020
import json
import sys

try:
    # Python 3.x
    from urllib.request import Request, urlopen
except ImportError:
    # Python 2.x
    from urllib2 import Request, urlopen

if not len(sys.argv) > 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Missing one argument (should be in the form shadowban @user)")
else:
    screenName = sys.argv[1]
    apiUrl = "https://shadowban.eu/.api/" + screenName

    r = Request(apiUrl)
    r.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0")

    apiJson = urlopen(r)
    apiJson = json.loads(apiJson.read())

    if apiJson["tests"]["ghost"]["ban"]:
        print(screenName + " is shadow ban")
    else:
        print(screenName + " isn't shadow banned")
