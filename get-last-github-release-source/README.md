# Get Last GitHub Release Source
Available in: `shell script` and `python` (2.x or 3.x).
<br>This tiny function will get the link of the sources of the last GitHub release of a certain repo.

## Example usage
(also available in the files)
### `shell script`
```shell script
getLastSource jusdepatate amtenael-linux
getLastSource ish-app ish
# direct output

x="$(getLastSource jusdepatate amtenael-linux)"
echo "$x"
#wget "$x" -O "amtenael-linux.zip"
# put output in variable and use it
```

### `python`
```python
print(getLastSource("jusdepatate", "amtenael-linux"))
print(getLastSource("ish-app", "ish"))
```