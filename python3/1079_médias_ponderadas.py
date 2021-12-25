n = int(input())

for i in range(n):
    v1, v2, v3 = input().split()
    v1 = float(v1)
    v2 = float(v2)
    v3 = float(v3)

    weighted_average = ((v1 * 2) + (v2 * 3) + (v3 * 5)) / 10

    print("{:.1f}".format(weighted_average))
