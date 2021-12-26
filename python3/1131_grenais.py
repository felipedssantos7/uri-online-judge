game_qtt = inter = gremio = tie = 0

while True:
    i, g = input().split()
    i = int(i)
    g = int(g)

    game_qtt = game_qtt + 1

    if i == g:
        tie = tie + 1
    elif i > g:
        inter = inter + 1
    else:
        gremio = gremio + 1

    print("Novo grenal (1-sim 2-nao)")
    r = int(input())
    if r == 2:
        break

print("{} grenais".format(game_qtt))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(tie))

if inter == gremio:
    print("Nao houve vencedor")
if inter > gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
