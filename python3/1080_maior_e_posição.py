bigger = 0
bigger_pos = 0

for i in range(100):
    number = int(input())
    if number > bigger:
        bigger = number
        bigger_pos = i + 1

print(bigger)
print(bigger_pos)
