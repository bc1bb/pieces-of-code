x = int(input("Entrez x:"))  # Attente entrée utilisateur

historique = [x]  # Stockage des resultats

while x > 1:  # Tant que x est supérieur a 1
    if x % 2 == 0:  # si x est pair
        x = x / 2  # diviser x par deux
    else:
        x = x * 3 + 1  # appliquer 3x+1

    historique.append(int(x))  # ajouter ce x a l'historique

print("Il y a", len(historique), "éléments pour arriver a 1, il faut", len(historique)-1, "itérations:")
print(*historique)