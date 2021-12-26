s = 0
d = 1

for i in range(1, 40, 2):
    s = s + (i / d)
    d = d * 2

print("{:.2f}".format(s))
