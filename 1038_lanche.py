cod, qtd = input().split()
cod = int(cod)
qtd = int(qtd)
val = 0

if cod == 1:
    val = qtd * 4.00
elif cod == 2:
    val = qtd * 4.50
elif cod == 3:
    val = qtd * 5.00
elif cod == 4:
    val = qtd * 2.00
elif cod == 5:
    val = qtd * 1.50

print("Total: R$ {:.2f}".format(val))
