n = []

for i in range(20):
    n.append(int(input()))

new_n = []
for i in range(19, -1, -1):
    new_n.append(n[i])

for i in range(20):
    print("N[{}] = {}".format(i, new_n[i]))
