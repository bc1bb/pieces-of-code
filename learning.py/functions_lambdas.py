multi = lambda x, y: x * y
# basic multiplication of x by y using a lambda function
# I know it's useless, but I had no other idea to test lambdas functions
add = lambda x, y: x + y
# lambda = one line&one action function

print("PyCalculator")
print("What do you want to do ?")
print("Type 'multi' for a multiplication")
print("Type 'add' or anything else for an additions")
calculatrice = input()
# function input = ask user for an entry

if calculatrice == "multi":
    # guillemets obligatoire pour un if sur un string
    print("choissisez x - multi")
    # '- multi' is mainly for debugging
    x = int(input())
    # function int = transform argument in integer (=considered as number and not text), input is, by default, a string
    print("choissisez y - multi")
    y = int(input())
    print(multi(x, y))
else:
    print("choissisez x - add")
    # '- add' is mainly for debugging
    x = int(input())
    print("choissisez y - add")
    y = int(input())
    print(add(x, y))
