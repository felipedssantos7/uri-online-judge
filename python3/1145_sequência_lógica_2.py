import math

x, y = input().split()
x = int(x)
y = int(y)
n = 1

for i in range(math.ceil(y / x)):
    for j in range(x):
        if n == y + 1:
            break
        print(n, end="")
        n = n + 1
        if j != x - 1:
            print(" ", end="")
    print()
