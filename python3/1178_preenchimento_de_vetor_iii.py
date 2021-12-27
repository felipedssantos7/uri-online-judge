x = float(input())

n = [x]

for i in range(0, 99):
    n.append(n[i] / 2)

for i in range(0, 100):
    print("N[{}] = {:.4f}".format(i, n[i]))
