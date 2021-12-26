n = int(input())

a = [n]

for i in range(0, 10):
    a.append(a[i] * 2)
    print("N[{}] = {}".format(i, a[i]))
