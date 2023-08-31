from math import floor
somme = int(input("Entrez la somme en centimes: "))
pieces = [[50, 0], [20, 0], [10, 0], [5, 0], [2, 0], [1, 0]]
for i in pieces:
    if somme >= i[0]:
        i[1] = floor(somme/i[0])
        somme -= i[0] * i[1]
    print(i[1], "pièces de", i[0], "centimes")