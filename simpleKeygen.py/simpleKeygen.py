#!/usr/bin/python3
# simple old school keygen made from https://gurney.dev/posts/mod7/
# Jus de Patate - 2020-2021
import random


def usualSecondPart(startsByZero: bool):
    if not startsByZero:
        second = random.randint(1000000, 9999999)

        while True:
            secondDigits = 0

            secondSpliced = [i for i in str(second)]
            for i in secondSpliced:
                secondDigits = secondDigits + int(i)

            secondLastDigit = secondSpliced[6]

            if (
                not int(secondDigits) % 7 == 0
                or int(secondLastDigit) == 0
                or int(secondLastDigit) >= 8
            ):
                second = random.randint(1000000, 9999999)
            else:
                break
    else:
        second = random.randint(100000, 999999)

        while True:
            secondDigits = 0

            secondSpliced = [i for i in str(second)]
            for i in secondSpliced:
                secondDigits = secondDigits + int(i)

            secondLastDigit = secondSpliced[5]

            if (
                not int(secondDigits) % 7 == 0
                or int(secondLastDigit) == 0
                or int(secondLastDigit) >= 8
            ):
                second = "0" + str(random.randint(100000, 999999))
            else:
                break

    return second


# also works with Windows NT 4.0
def key_w95(oem: bool):
    if not oem:
        # first part: 3 digits long, can be complete random but 333, 444, 555, 666, 777, 888 and 999 are invalid
        # second part: the digit sum should be divisible by 7, last digit shouldn't be 0 nor >= 8
        firstForbidden = [333, 444, 555, 666, 777, 888]
        first = 333
        while first in firstForbidden:
            first = random.randint(100, 998)

        second = usualSecondPart(False)

        key = str(first) + "-" + str(second)
        return key
    if oem:
        # first part: first three digit can be anything between 001 to 366 and the last two are anything from 95 to 03
        # second part: first digit must be 0 + identical as key_w95()
        # third part: anything between 10000 to 99999

        firstPartOne = random.randint(100, 366)

        firstPartTwo = random.randint(95, 99)
        first = str(firstPartOne) + str(firstPartTwo)

        second = usualSecondPart(True)

        third = random.randint(10000, 99999)

        key = str(first) + "-OEM-" + str(second) + "-" + str(third)
        return key


def key_office97():
    # first part: 4 digits between 0001 to 9991, last digit must be 3rd digit + 1 or + 2
    # second part: identical as key_w95()
    first = random.randint(1000, 9991)
    firstSplited = [i for i in str(first)]

    while (
        not int(firstSplited[2]) == int(firstSplited[3]) + 1
        or int(firstSplited[2]) == int(firstSplited[3]) + 2
    ):
        firstSplited = [i for i in str(first)]
        first = random.randint(1000, 9991)

    second = usualSecondPart(False)

    key = str(first) + "-" + str(second)
    return key


print(
    "Welcome to this little old school Windows/Office Keygen.\n"
    "I made it a while ago and never really tried it,\n"
    "This project was made totally at educational purposes,\n"
    "I do not endorse any illegal uses of this script.\n"
    "\n"
    "What do you want to generate ?\n"
    "Available options:\n"
    "w95oem: Generate Windows 95 (& NT4.0) OEM key,\n"
    "w95: Generate Windows 95 (& NT4.0) key,\n"
    "o97: Generate Office 97 key."
)

choice = input()

if choice == "w95o":
    print(key_w95(True))
if choice == "w95":
    print(key_w95(False))
if choice == "o97":
    print(key_office97())
