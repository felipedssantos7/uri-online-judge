# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

while True:
    global score_1
    score_1 = float(input())

    if score_1 >= 0 and score_1 <= 10:
        break
    else:
        print("nota invalida")

while True:
    global score_2
    score_2 = float(input())

    if score_2 >= 0 and score_2 <= 10:
        break
    else:
        print("nota invalida")

media = (score_1 + score_2) / 2

print("media = {:.2f}".format(media))
