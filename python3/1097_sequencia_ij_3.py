i, j, count = 1, 7, 0

while i <= 9:
    print("I={}".format(i), "J={}".format(j))
    count = count + 1
    j = j - 1

    if count % 3 == 0:
        i = i + 2
        j = j + 5