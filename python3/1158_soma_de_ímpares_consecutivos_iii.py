n = int(input())

for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)

    if x % 2 == 0: x = x + 1

    sum = 0
    for j in range(x, x + (y * 2), 2):
        sum = sum + j
    print(sum)
