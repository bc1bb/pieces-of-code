# Fakeclient.py
This thing connects to any EVE Online server and takes data from it (connected players, version, ...).

I do not deserve credit for this, I literally made 1% of the job, @ntt deserves all the credits <3

## Thanks
- To the maker of [reverence](https://github.com/ntt/reverence) (@ntt) this couldn't exist without him,
- EVEmu's community.

## Arguments:
**None are required, if you don't specify any, it'll connect to Tq**

### First argument
First argument should be an address or a (tiny) name

example:
- `./fakeclient tq` will connect to Tranquility
- `./fakeclient singularity` will connect to Singularity
- `./fakeclient example.com` will connect to example.com

Accepted first argument:
- `tranquility` | `tq`
- `sisi` | `singularity`
- `serenity`
- `buckingham`
- `multiplicity`
- `alasiya`
- `localhost`
- any address that contains `.` or `:` (**do not include port**)

### Second argument
Second argument should be a port, so it should be between 1 and 65535, if it's not specified it'll use default port (`26000`)
