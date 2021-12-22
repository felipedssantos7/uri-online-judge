N = int(input())
valor = N

cem = int(N / 100)
N %= 100

cinquenta = int(N / 50)
N %= 50

vinte = int(N / 20)
N %= 20

dez = int(N / 10)
N %= 10

cinco = int(N / 5)
N %= 5

dois = int(N / 2)

um = N % 2

print(valor)
print(str(cem), "nota(s) de R$ 100,00")
print(str(cinquenta), "nota(s) de R$ 50,00")
print(str(vinte), "nota(s) de R$ 20,00")
print(str(dez), "nota(s) de R$ 10,00")
print(str(cinco), "nota(s) de R$ 5,00")
print(str(dois), "nota(s) de R$ 2,00")
print(str(um), "nota(s) de R$ 1,00")
