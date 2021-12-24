salary = float(input())

if salary >= 0.00 and salary <= 2000.00:
    print("Isento")
elif salary >= 2000.01 and salary <= 3000.00:
    print("R$ {:.2f}".format(((salary - 2000) * 8) / 100))
elif salary >= 3000.01 and salary <= 4500.00:
    print("R$ {:.2f}".format(((1000 * 8) / 100) + (((salary - 3000) * 18) / 100)))
elif salary > 4500.00:
    print("R$ {:.2f}".format(((1000 * 8) / 100) + ((1500 * 18) / 100) + (((salary - 4500) * 28) / 100)))
