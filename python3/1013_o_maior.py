a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

x = int((a + b + abs(a - b)) / 2)
y = int((x + c + abs(x - c)) / 2)

print("{} eh o maior".format(y))
