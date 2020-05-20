# Get Last GitHub Release Source
This tiny Bash function will get the link of the sources of the last GitHub release of a certain repo

## Usage example
(also available in the file)
```shell script
getLastSource jusdepatate amtenael-linux
getLastSource ish-app ish
# direct output

x="$(getLastSource jusdepatate amtenael-linux)"
echo "$x"
#wget "$x" -O "amtenael-linux.zip"
# put output in variable and use it
```