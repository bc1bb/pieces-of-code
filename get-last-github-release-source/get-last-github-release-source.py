import json

try:
    # Python 3.x
    from urllib.request import urlopen
except ImportError:
    # Python 2.x
    from urllib import urlopen


def getLastSource(user, repo):
    apiUrl = "https://api.github.com/repos/" + user + "/" + repo + "/releases/latest"

    r = urlopen(apiUrl)
    apiJson = json.loads(r.read())
    return apiJson["zipball_url"]


# <example>
print(getLastSource("jusdepatate", "amtenael-linux"))
print(getLastSource("ish-app", "ish"))
# </example>
