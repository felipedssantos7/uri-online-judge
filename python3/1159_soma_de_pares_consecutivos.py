while True:
    x = int(input())
    if x == 0:
        break

    if x % 2 == 1:
        x = x + 1

    sum = 0
    for i in range(x, x + 10, 2):
        sum = sum + i
    print(sum)
