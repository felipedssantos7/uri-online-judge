# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

even = []
odd = []

for i in range(15):
    n = int(input())

    if n % 2 == 0:
        even.append(n)
        if len(even) == 5:
            for j in range(5):
                print("par[{}] = {}".format(j, even[j]))
            even = []
    else:
        odd.append(n)
        if len(odd) == 5:
            for j in range(5):
                print("impar[{}] = {}".format(j, odd[j]))
            odd = []
    
for i in range(len(odd)):
    print("impar[{}] = {}".format(i, odd[i]))

for i in range(len(even)):
    print("par[{}] = {}".format(i, even[i]))
