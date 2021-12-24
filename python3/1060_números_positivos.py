positives = 0

for i in range(6):
    number = float(input())
    if number > 0:
        positives = positives + 1

print("{} valores positivos".format(positives))
