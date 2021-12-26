sum = qtt = 0

while True:
    age = int(input())

    if age < 0:
        break

    sum = sum + age
    qtt = qtt + 1

media = sum / qtt

print("{:.2f}".format(media))

