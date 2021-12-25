while True:
    m, n = input().split()
    m = int(m)
    n = int(n)

    if m <= 0 or n <= 0:
        break

    if m > n:
        aux = m
        m = n
        n = aux

    sum = 0
    for i in range(m, n + 1):
        print(i, end=" ")
        sum = sum + i
    print("Sum={}".format(sum))
