# ZCasino - Roulette - Jus de Patate
# https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/231735-tp-tous-au-zcasino
from random import randrange
# randrange will help us at getting random numbers
from math import ceil
# ceil will help us to round numbers (round function can also be used)
import os

money = 50
# At the begging we get 50$


def pairtest(nb):
    if (nb % 2) == 0:
        return True
    else:
        return False
# I created a function to test number parity easily, it returns True or False (useful for if statements)


def roulette():
    global money
    # I import variable money
    print('Welcome at ZCasino')
    print('Which box do you want to bet on ?')
    box = int(input())
    # we don't forget to transform the input into integer to manipulate it in if statements

    if box < 0:
        print("This number is negative")
        roulette()
    if box > 49:
        print("This number is greater than 49")
        roulette()
    # bad method but idiot-proof

    print("How much do you wanna bet on box", box, "?")
    bet = int(input())
    money -= bet
    if bet > money:
        print("You don't have enough money to bet ", bet, "$")
        os.system("pause")
    else:
        boxgg = randrange(50)
        if boxgg == bet:
            money += bet * 3
            print("Well Played ! The ball fell on the box you choosed !")
            print("You won the triple of your bet, you now have", money, "$")
        else:
            if pairtest(box) == pairtest(boxgg):
                money += ceil( / 2)
                # on arrondi la moitié de la mise pour eviter de se retrouver avec trop de virgule
                print('Well Played ! The box you choosed has the same color as the box the ball fell on')
                print('You won half your bet, you now have', money, '$')
            else:
                print("Oh No ! You lost your bet because the ball fell on another box... Retry anyways !")


while money != 0:
    roulette()
# technique barbare encore une fois
