n = int(input())

in_range = 0
out_range = 0

for i in range(0, n):
    x = int(input())
    if x >= 10 and x <= 20:
        in_range = in_range + 1
    else:
        out_range = out_range + 1
    
print("{} in".format(in_range))
print("{} out".format(out_range))

