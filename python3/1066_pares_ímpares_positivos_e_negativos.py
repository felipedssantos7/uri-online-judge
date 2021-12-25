pairs = 0
odd = 0
positives = 0
negatives = 0

for i in range(5):
    number = int(input())
    
    if number % 2 == 0:
        pairs = pairs + 1
    else:
        odd = odd + 1

    if number > 0:
        positives = positives + 1
    elif number < 0:
        negatives = negatives + 1

print("{} valor(es) par(es)".format(pairs))
print("{} valor(es) impar(es)".format(odd))
print("{} valor(es) positivo(s)".format(positives))
print("{} valor(es) negativo(s)".format(negatives))
