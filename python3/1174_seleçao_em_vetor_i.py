p = []
v = []

for i in range(100):
    n = float(input())

    if n <= 10:
        p.append(i)
        v.append(n)

for i in range(len(p)):
    print("A[{}] = {:.1f}".format(p[i], v[i]))
