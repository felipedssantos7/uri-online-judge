n = int(input())

for i in range(n):
    x = int(input())

    sum = 0
    for j in range(1, x):
        if x % j == 0:
            sum = sum + j
    
    if sum == x:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))

