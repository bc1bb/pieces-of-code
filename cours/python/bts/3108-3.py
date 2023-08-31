a=int(input("a="))
b=int(input("b="))
c=0


def pgcd(a, b):
    if b==0:
        return a
    else:
        return pgcd(b, a % b)

print(pgcd(a,b))

