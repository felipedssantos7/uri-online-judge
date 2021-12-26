t = int(input())

for i in range(t):
    pa, pb, g1, g2 = input().split()
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)

    years = 0
    while pa <= pb:
        pa = pa + int((pa * g1) / 100)
        pb = pb + int((pb * g2) / 100)
        years = years + 1
        if years > 100:
            print("Mais de 1 seculo.")
            break
    
    if years <= 100:
        print("{} anos.".format(years))
