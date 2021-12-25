num_of_pairs = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        num_of_pairs = num_of_pairs + 1

print("{} valores pares".format(num_of_pairs))
