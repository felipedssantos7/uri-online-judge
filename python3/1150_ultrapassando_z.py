x = int(input())

while True:
    global y
    y = int(input())
    if y > x:
        break

num_qtt = 0
sum = 0
i = x

while sum <= y:
    sum = sum + i
    num_qtt = num_qtt + 1
    i = i + 1

print(num_qtt)
