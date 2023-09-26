ligne = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for l in range(1, 21):  # lignes
    for c in range(2, 21):  # column
        ligne[l] = str(ligne[l]) + " " + str(l * c)
del ligne[0]
print(*ligne, sep="\n")
