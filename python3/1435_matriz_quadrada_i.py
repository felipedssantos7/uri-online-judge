while True:
    n = int(input())

    if n == 0:
        break

    m = []

    for i in range(n):
        r = []
        for j in range(n):
            r.append(1)
        m.append(r)

    a = 1
    b = n - 1
    c = 2

    for x in range(n):
        for i in range(a, b):
            for j in range(a, b):
                m[i][j] = c
        a += 1
        b -= 1
        c += 1

    for i in range(n):
        text = ""
        for j in range(n):
            text += " %3d" % m[i][j]
        print(text[1:])
    print()
    