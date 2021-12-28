c = int(input())
t = input()
m = []

for i in range(12):
    r = []
    for j in range(12):
        v = float(input())
        r.append(v)
    m.append(r)

sum = 0
for i in range(12):
    sum = sum + m[i][c]

if t == "S":
    print("{:.1f}".format(sum))
else:
    med = sum / 12
    print("{:.1f}".format(med))
