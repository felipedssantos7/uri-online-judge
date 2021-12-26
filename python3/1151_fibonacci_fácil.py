n = int(input())
x, y = 0, 1
print(x, end="")

if n != 1:
    print("", y, end="")

if n == 2:
    print()
else:
    print(" ", end="")
    i = 2
    while i < n:
        next = x + y
        print(next, end="")
        
        if i != (n - 1):
            print(" ", end="")
        
        x = y
        y = next

        i = i + 1
    print()