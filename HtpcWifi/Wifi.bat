@echo off
sc stop wlansvc >NUL

timeout 2 >NUL

sc start wlansvc >NUL

timeout 2 >NUL

explorer.exe ms-availablenetworks:

timeout 1 >NUL

netsh wlan connect SSID="iPhone de Guillaume" name="iPhone de Guillaume"

pause >NUL
