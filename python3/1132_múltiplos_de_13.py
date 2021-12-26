x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

sum = 0
for i in range(x, y + 1):
    if i % 13 != 0:
        sum = sum + i

print(sum)
