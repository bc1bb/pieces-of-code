pos = int(input())
nbVillages = int(input())
villages = []
inRange = 0

for i in range(nbVillages):
    villages.append(int(input()))

for i in range(nbVillages):
    if pos - 50 <= villages[i] <= pos + 50:
        inRange += 1

print(inRange)
