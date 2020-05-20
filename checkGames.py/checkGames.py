from platform import system as OS

if OS() == "Windows":
    import winreg
else:
    raise NotImplementedError("This script only works on Windows.")

# here we import winreg only if user is on Windows


def checkGames(gameId):
    # returns [int gameId, bool isInstalled, string gameName, string installLocation]

    CURRENT_USER = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    LOCAL_MACHINE = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    # reg things that will be useful for this function

    gameId = str(gameId)
    # convert id to str in case function was called with an int so we don't get stupid errors

    try:
        key = winreg.OpenKeyEx(CURRENT_USER, r"Software\Valve\Steam\Apps\\" + gameId)
        gameName = winreg.QueryValueEx(key, "Name")[0]
        isInstalled = winreg.QueryValueEx(key, "Installed")[0]
        # Checking if we can get the game name from the ID using Reg

        if isInstalled == 1:
            key = winreg.OpenKeyEx(
                LOCAL_MACHINE,
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App "
                + gameId,
            )
            installLoc = winreg.QueryValueEx(key, "InstallLocation")[0]
            # Here we get installLocation from red LOCAL_MACHINE

            return [gameId, True, gameName, installLoc]
        else:
            return [gameId, False, gameName, False]
        # here we check if the game is installed

    except FileNotFoundError:
        return [gameId, False, gameId, False]


# <examples>
checkGames(8500)  # EVE Online
checkGames(72850)  # Skyrim
checkGames(489830)  # Skryim: SE
checkGames(620)  # Portal 2
# </example>
