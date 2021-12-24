salary = float(input())
new_salary = readjustment_value = readjustment_index = 0

if salary >= 0 and salary <= 400.00:
    readjustment_index = 0.15
elif salary >= 400.01 and salary <= 800.00:
    readjustment_index = 0.12
elif salary >= 800.01 and salary <= 1200.00:
    readjustment_index = 0.10
elif salary >= 1200.01 and salary <= 2000.00:
    readjustment_index = 0.07
elif salary > 2000:
    readjustment_index = 0.04

readjustment_value = readjustment_index * salary
new_salary = salary + readjustment_value

print("Novo salario: {:.2f}".format(new_salary))
print("Reajuste ganho: {:.2f}".format(readjustment_value))
print("Em percentual: {} %".format(int(readjustment_index * 100)))
