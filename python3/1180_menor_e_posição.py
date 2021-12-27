n = int(input())
a = input().split()
x = []

for i in range(n):
    x.append(int(a[i]))

menor = x[0]
pos = 0
for i in range(1, n):
    if x[i] < menor:
        menor = x[i]
        pos = i
    
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(pos))
