o = input()
m = []

for i in range(12):
    r = []
    for j in range(12):
        v = float(input())
        r.append(v)
    m.append(r)

sum = 0
qtt = 0
for i in range(12):
    for j in range(12):
        if i + j <= 10:
            sum = sum + m[i][j]
            qtt = qtt + 1

if o == "S":
    print("{:.1f}".format(sum))
else:
    med = sum / qtt
    print("{:.1f}".format(med))
