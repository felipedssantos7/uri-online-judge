A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if (A + B > C) and (A + C > B) and (B + C > A):
    print("Perimetro = {:.1f}".format(A + B + C))
else:
    print("Area = {:.1f}".format((A + B) * C / 2))
