while True:
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

    while True:
        print("novo calculo (1-sim 2-nao)")
        global x
        x = int(input())

        if x == 1 or x == 2:
            break

    if x == 2:
        break