positionDepart = int(input())
largeurEmplacement = int(input())
nbVendeurs = int(input())

print(positionDepart)
a = positionDepart
for i in range(0, nbVendeurs):
    a += largeurEmplacement
    print(a)
