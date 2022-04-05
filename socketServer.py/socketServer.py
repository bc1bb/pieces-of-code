#!/usr/bin/env python3
import socket
import sys

s = socket.socket()

ip = "127.0.0.1"
port = int(sys.argv[1])

s.bind((ip, port))
print("Server socket bound on", ip + ":" + str(port))

s.listen()

i = 0
while True:
    c = s.accept()[0]
    i += 1
    print("Accepted", i, "connections so far")
    while True:
        data = c.recv(1024)
        print(data)
        if data != b"":
            print("Connection closed")
            break
