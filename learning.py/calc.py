# I made this in like 6 hours on my NumWorks calculator
# Yes I made a calculator in Python in a Calculator
# Features :
#  - Re-use last result (use "k" in calculations)
#  - Pi (use "pi")
#  - SQRT (usr "sq")
#  - Everything in a while loop that you can stop by saying "stop"
#  - Unreadable code cuz wrote on a calculator
#  - Should manage any errors

from math import *

a = "1+1"
c = "0"


def pit(b):
    if b[0] == "pi":
        b[0] = round(pi, 5)
    if b[1] == "pi":
        b[1] = round(pi, 5)


def res(b, c):
    if b[0] == "k":
        b[0] = c
    if b[1] == "k":
        b[1] = c


while True:
    a = input()
    if "+" in a:
        try:
            b = a.split("+")
            pit(b)
            res(b, c)
            c = round(float(b[0]) + float(b[1]), 5)
            print("(" + str(b[0]) + "+" + str(b[1]) + ")\t " + str(c))
        except:
            print("Error")
    elif "-" in a:
        try:
            b = a.split("-")
            pit(b)
            res(b, c)
            c = round(float(b[0]) - float(b[1]), 5)
            print("(" + str(b[0]) + "-" + str(b[1]) + ")\t " + str(c))
        except:
            print("Error")
    elif "*" in a:
        try:
            b = a.split("*")
            pit(b)
            res(b, c)
            c = round(float(b[0]) * float(b[1]), 5)
            print("(" + str(b[0]) + "*" + str(b[1]) + ")\t " + str(c))
        except:
            print("Error")
    elif "/" in a:
        try:
            b = a.split("/")
            pit(b)
            res(b, c)
            c = round(float(b[0]) / float(b[1]), 5)
            print("(" + str(b[0]) + "/" + str(b[1]) + ")\t " + str(c))
        except:
            print("Error")
    elif "sq" in a:
        b = a.split("sq")
        pit(b)
        res(b, c)
        c = round(sqrt(float(b[1])), 5)
        print("(sqrt(" + str(b[1]) + "))\t " + str(c))
    elif a == "stop":
        print("Bye !")
        break
    else:
        print("Unable to find an operator")
