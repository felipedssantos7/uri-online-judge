x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

menor = x
do_meio = 0
maior = x

if y < menor:
    menor = y
if z < menor:
    menor = z

if y > maior:
    maior = y
if z > maior:
    maior = z

if maior != y and menor != y:
    do_meio = y
elif maior != x and menor != x:
    do_meio = x
else:
    do_meio = z

print(menor)
print(do_meio)
print(maior, end="\n\n")

print(x)
print(y)
print(z)
