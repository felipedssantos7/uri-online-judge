l = int(input())
t = input()
m = []

for i in range(12):
    c = []
    for j in range(12):
        v = float(input())
        c.append(v)
    m.append(c)

if t == "S":
    sum = 0
    for i in range(12):
        sum = sum + m[l][i]
    print("{:.1f}".format(sum))
else:
    sum = 0
    for i in range(12):
        sum = sum + m[l][i]
    med = sum / 12
    print("{:.1f}".format(med))
