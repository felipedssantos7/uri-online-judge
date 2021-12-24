word_1 = input()
word_2 = input()
word_3 = input()

if word_1 == "vertebrado":
    if word_2 == "ave":
        if word_3 == "carnivoro":
            print("aguia")
        else: # onivoro
            print("pomba")
    else: # mamifero
        if word_3 == "onivoro":
            print("homem")
        else: # herbivoro
            print("vaca")
else: # invertebrado
    if word_2 == "inseto":
        if word_3 == "hematofago":
            print("pulga")
        else: # herbivoro
            print("lagarta")
    else: # anelideo
        if word_3 == "hematofago":
            print("sanguessuga")
        else: # onivoro
            print("minhoca")
