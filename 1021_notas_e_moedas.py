N = float(input())

cem = int(N / 100)
resto = N % 100
cinquenta = int(resto / 50)
resto = resto % 50
vinte = int(resto / 20)
resto = resto % 20
dez = int(resto / 10)
resto = resto % 10
cinco = int(resto / 5)
resto = resto % 5
dois = int(resto / 2)
resto = resto % 2

um = int(resto / 1)
resto = resto % 1
resto = round(resto * 100)
cinquenta_centavos = int(resto / 50)
resto = resto % 50
vinte_e_cinco_centavos = int(resto / 25)
resto = resto % 25
dez_centavos = int(resto / 10)
resto = resto % 10
cinco_centavos = int(resto / 5)
resto = resto % 5
um_centavo = int(resto / 1)

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(cem))
print("{} nota(s) de R$ 50.00".format(cinquenta))
print("{} nota(s) de R$ 20.00".format(vinte))
print("{} nota(s) de R$ 10.00".format(dez))
print("{} nota(s) de R$ 5.00".format(cinco))
print("{} nota(s) de R$ 2.00".format(dois))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(um))
print("{} moeda(s) de R$ 0.50".format(cinquenta_centavos))
print("{} moeda(s) de R$ 0.25".format(vinte_e_cinco_centavos))
print("{} moeda(s) de R$ 0.10".format(dez_centavos))
print("{} moeda(s) de R$ 0.05".format(cinco_centavos))
print("{} moeda(s) de R$ 0.01".format(um_centavo))
