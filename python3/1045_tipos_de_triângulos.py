A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

menor = do_meio = maior = A

if B < menor:
    menor = B
if C < menor:
    menor = C

if B > maior:
    maior = B
if C > maior:
    maior = C

if (A <= B and A >= C) or (A <= C and A >= B):
    do_meio = A
if (B <= A and B >= C) or (B <= C and B >= A):
    do_meio = B
if (C <= A and C >= B) or (C <= B and C >= A):
    do_meio = C

if maior >= do_meio + menor:
    print("NAO FORMA TRIANGULO")
elif (maior ** 2) == (do_meio ** 2) + (menor ** 2):
    print("TRIANGULO RETANGULO")
elif (maior ** 2) > (do_meio ** 2) + (menor ** 2):
    print("TRIANGULO OBTUSANGULO")
elif (maior ** 2) < (do_meio ** 2) + (menor ** 2):
    print("TRIANGULO ACUTANGULO")

if maior == do_meio and do_meio == menor:
    print("TRIANGULO EQUILATERO")
elif maior == do_meio or maior == menor or do_meio == menor:
    print("TRIANGULO ISOSCELES")
