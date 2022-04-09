# TkDiff

Class project made in Python3 with Tkinter.

We were asked to create any kind of software with at least:
- 3 logical instructions,
- 3 graphical elements,
- Communication with anything in any manner (network, COM port, ...).

We thought it would be fun to create a graphical interface for `difflib.unified_diff(f1, f2, lineterm=nl)` (returns diff line-by-line between two files in an array).

## How does it work
- `getIP()` called only on start to print IP on `bottomBar`, returns the main IP of the computer,
- `DiffWindow` contains most functions of the software, `__init__()` has the window,
- `DiffWindow.fileSelctMaster()` shows a file selector for the master file,
- `DiffWindow.fileSlctSlave()` shows a file selector for the slave file,
- `DiffWindow.whereAmI()` is called everytime user clicks on `diffBox` (big text box), returns where the user just clicked on the screen,
- `DiffWindow.connect()` is called whenever user clicks on `connectBtn`, tells `socket` to connect on whatever is entered in `ipEntry` on port `42000`,
- `DiffWindow.changeDiffBox(text)`, as I disable `diffBox`, we cannot tell a function to just write into it, we have to enable it, write `text` and disable it again,
- `DiffWindow.diffServer()`, starts  a server on port `42000` so another window can connect to it and send content,
- `DiffWindow.calcDiff()`, puts a multi line string of the diff between `f1` and `f2` in `diffBox`,
- `DiffWindow.errorHandler(func)`, is called to handle errors, and does it in a very simple way: just prints in a `messagebox`.

Whenever `DiffWindow` is called, a Tkinter window is created, and another thread for `DiffWindow.diffServer()` is started by it, opening port `42000`.

## Known problems
This wasn't supposed to be a huge project, just a simple basic graphical project, so I didn't put a huge effort into it. 

Communication outside of sending to your own client/server doesn't really work for some kind of black magic reason