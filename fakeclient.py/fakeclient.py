#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Jus de Patate | Farlido Tekitsu - 2020
# This thing connects to any EVE Online server and takes data from it
# Should be executed in Python 2.6 or 2.7

import socket
import sys

try:
    from reverence import blue
except ImportError:
    raise ImportError(
        "Reverence is not installed, install it from https://github.com/ntt/reverence"
    )
except RuntimeError:
    raise ImportError("Reverence requires PyYaml, make sure it's installed")

if len(sys.argv) >= 2:
    arg1 = sys.argv[1]

    if arg1 == "tranquility" or arg1 == "tq":
        addr = "tranquility.servers.eveonline.com"

    elif arg1 == "singularity" or arg1 == "sisi":
        addr = "singularity.servers.eveonline.com"

    elif arg1 == "serenity" or arg1 == "cn" or arg1 == "china":
        addr = "42.186.79.5"

    elif arg1 == "buckingham":
        addr = "buckingham.servers.eveonline.com"

    elif arg1 == "multiplicity":
        addr = "multiplicity.servers.eveonline.com"

    elif arg1 == "alasiya":
        addr = "eve.alasiya.net"

    elif arg1 == "localhost":
        addr = "127.0.0.1"

    elif len(arg1.split(".")) > 1 or len(arg1.split(":")) > 1:
        addr = arg1
        # tiny hack to detect if arg1 is IPv4/v6 or domain

    else:
        raise Exception("Invalid argument")

else:
    addr = "tranquility.servers.eveonline.com"
    # if no argument server will be tq by default

# -- Server List --:
# Tranquility: tranquility.servers.eveonline.com | 87.237.34.200
# Singularity: singularity.servers.eveonline.com | 87.237.38.2
# Serenity: 42.186.79.5
# Buckingham: buckingham.servers.eveonline.com | 87.237.38.5
# Duality: duality.servers.eveonline.com | 87.237.38.11
# Multiplicity: multiplicity.servers.eveonline.com | 87.237.38.3
# Alasiya: eve.alasiya.net | 68.224.222.51

if len(sys.argv) >= 3:
    arg2 = int(sys.argv[2])

    if 1 <= arg2 <= 65535:
        p = arg2

    else:
        raise Exception("Invalid port")

else:
    p = 26000
# default EVE Online server port is 26000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print "Trying to connect to", addr + ":" + str(p) + "\n"

try:
    s.connect((addr, p))
except socket.error as e:
    print e
    exit

size = s.recv(4)
# first 4 bytes = size of the data to receive

try:
    size = 50 + int(size.split("\x00")[0])
except ValueError:
    size = 50
# too much strange workarounds in one line so let me explain:
# apparently there is a bug that makes Python 2.7 (it doesn't appear in Python 3.8) to understand only x when it should understand 50 + x, so I added `50 + x`
# and when x = 0 it tries to do 50 + `\x01` so I added a try/except

print "Size:", size, "\n"

data = s.recv(size)

print "Marshalled data:", data, "\n"
# here we output raw data sent by server

try:
    unmarshalled = blue.marshal.Load(data)
    print "Unmarshalled data:", unmarshalled, "\n"
    # and here we unmarshal it and output it
except EOFError:
    raise Exception("Looks like " + addr + " sent bad data, maybe it's daily downtime")
# (birthday, machoversion, usercount, version, build, codename)
# here is the tuple that the server should be sending us
# at least EVEmu on Crucible (apparently still valid on all servers in 2020)

print "Birthday:", unmarshalled[0]
print "Machonet version:", unmarshalled[1]
print "Connected Players:", unmarshalled[2]
print "Version:", unmarshalled[3]
print "Build:", unmarshalled[4]
print "Codename:", unmarshalled[5]
# so we can extract this data from the server

s.close()
# and don't forget to close that fuckin socket
