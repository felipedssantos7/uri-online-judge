n = int(input())

total = C = R = S = percC = percR = percS = 0

for i in range(n):
    Quantia, Tipo = input().split()
    Quantia = int(Quantia)

    total = total + Quantia

    if Tipo == "C": C = C + Quantia
    elif Tipo == "R": R = R + Quantia
    else: S = S + Quantia

percC = C / total * 100
percR = R / total * 100
percS = S / total * 100

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(C))
print("Total de ratos: {}".format(R))
print("Total de sapos: {}".format(S))
print("Percentual de coelhos: {:.2f} %".format(percC))
print("Percentual de ratos: {:.2f} %".format(percR))
print("Percentual de sapos: {:.2f} %".format(percS))
