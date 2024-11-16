nbMarchands = int(input())
prix = []
cheapest = [1, 1000000]  # emplacement, prix

for i in range(nbMarchands):
    prix.append(int(input()))

for i in range(nbMarchands):
    if prix[i] <= cheapest[1]:
        cheapest[0] = i
        cheapest[1] = prix[i]

print(cheapest[0] + 1)
