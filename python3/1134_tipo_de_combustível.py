a = g = d = 0

while True:
    x = int(input())

    if x == 1:
        a = a + 1
    elif x == 2:
        g = g + 1
    elif x == 3:
        d = d + 1
    elif x == 4:
        break

print("MUITO OBRIGADO")
print("Alcool: {}".format(a))
print("Gasolina: {}".format(g))
print("Diesel: {}".format(d))
