x = int(input())
y = int(input())

if y < x:
    aux = x
    x = y
    y = aux

if x % 2 == 0: x = x + 1
else: x = x + 2

odd_sum = 0

for i in range(x, y, 2):
    odd_sum = odd_sum + i

print(odd_sum)
