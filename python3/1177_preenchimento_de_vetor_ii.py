t = int(input())
n = []

for i in range(1000):
    for j in range(t):
        n.append(j)

for i in range(1000):
    print("N[{}] = {}".format(i, n[i]))