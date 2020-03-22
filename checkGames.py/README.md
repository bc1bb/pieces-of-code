# checkGames.py
This tiny script check whenever a game is installed on **Windows** and where it is.
<br>It doesn't check if the files are still in the indicated folder.

The function `checkGames` (that you can add to your code without problems, this repo is under The Unlicense) returns an array like this `[int gameId, bool isInstalled, string gameName, string installLocation]`.
<br>You can use it this way:
```python
from checkGames import *

portal2 = checkGames(620)

if portal2[2]:
	print(gameName, "is installed at", installLocation)
else:
	print(gameId, "is not installed")
```

