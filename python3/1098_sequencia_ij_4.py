i, j, count = 0, 1, 0
decimals = 0.2

while i <= 2:
    if i == 1.9999999999999998:
        print("I={}".format(round(i)), "J={}".format(int(j)))
    elif i % 1 != 0 and j % 1 != 0:
        print("I={:.1f}".format(i), "J={:.1f}".format(j))
    elif i % 1 != 0 and j % 1 == 0:
        print("I={:.1f}".format(i), "J={}".format(int(j)))
    elif i % 1 == 0 and j % 1 != 0:
        print("I={}".format(int(i)), "J={:.1f}".format(j))
    elif i % 1 == 0 and j % 1 == 0:
        print("I={}".format(int(i)), "J={}".format(int(j)))
        
    count = count + 1
    j = j + 1

    if count % 3 == 0:
        i = i + 0.2
        j = 1 + decimals
        decimals = decimals + 0.2
