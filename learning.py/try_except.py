numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    # try = try then catch the error, if something fail during execution of the code indented with try, it executes the code indented with except.
    numerator = int(numerator)
    denominator = int(denominator)
except:
    print("Error while converting values.")

try:
    print(numerator / denominator)
except NameError:
    # multiple type of errors can happen, except will execute the code corresponding to the error
    print("One or more variable is not defined")
except TypeError:
    print("One or more variable is in an invalid type.")
except ZeroDivisionError:
    print("You dickhead, don't divide by 0.")
finally:
    # code executed in any case
    print("bla bla")

# Other things abu try...except :
# assert : useful to test something,
# if this thing is True nothing happen but if it is False an AssertionError comes.
# pass : put it in an except, it if is here, nothing will happen if this error comes.
# raise x("y") : create an error with type x and message y
#
# lazy format for try...except (bad but easy idea) :
# import sys
#
# try:
#     print(1/0)
# except:
#     print("Houston, we got an error :", sys.exc_info()[0])
