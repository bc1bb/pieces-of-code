# ~/module.py :
import os


def multipli(nb, max=10):
    i = 0
    # i is our variable to know how much times the while loop has been executed
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
        # it has been executed one time, i is modified


if __name__ == "__main__":
    multipli(4)
    os.system("pause")
    # part to test module
    # this code will be executed if someone execute this file, if it's just imported, Python will ignore this part

# ~/main.py :
import module

module.multipli(5)


# an __init__.py file can be created and should have a preparation code for the module that will be executed at every import
