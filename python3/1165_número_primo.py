n = int(input())

for i in range(n):
    x = int(input())

    is_prime = True
    for j in range(2, x):
        if x % j == 0:
            is_prime = False
            break
    
    if is_prime and x != 1:
        print("{} eh primo".format(x))
    else:
        print("{} nao eh primo".format(x))
