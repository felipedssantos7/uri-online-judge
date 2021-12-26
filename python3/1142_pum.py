n = int(input())
c = 1

for i in range(n):
    for j in range(3):
        print(c, end=" ")
        c = c + 1
    c = c + 1
    print("PUM")
