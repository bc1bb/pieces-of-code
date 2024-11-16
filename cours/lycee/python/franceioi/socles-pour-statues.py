premierEtage = int(input())
dernierEtage = int(input())
a = 0
for i in range(dernierEtage, premierEtage + 1):
    a = a + i * i
print(a)
