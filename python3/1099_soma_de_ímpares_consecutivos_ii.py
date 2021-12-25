n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if y < x:
        aux = x
        x = y
        y = aux

    if x % 2 == 0: x = x + 1
    else: x = x + 2

    sum = 0
    for j in range(x, y, 2):
        sum = sum + j

    print(sum)

