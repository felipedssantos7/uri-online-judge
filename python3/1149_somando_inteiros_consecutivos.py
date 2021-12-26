while True:
    scanner = input().split()
    a = int(scanner[0])
    
    n = scanner[1:]

    for i in range(len(n)):
        n[i] = int(n[i])    
        
        if n[i] <= 0:
            continue
        
        sum = 0
        for j in range(n[i]):
            sum = sum + a + j
        print(sum)
        break
    
    if sum != 0:
        break
