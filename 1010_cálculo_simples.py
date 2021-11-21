cod_p1, num_p1, val_p1 = input().split()
cod_p1 = int(cod_p1)
num_p1 = int(num_p1)
val_p1 = float(val_p1)

cod_p2, num_p2, val_p2 = input().split()
cod_p2 = int(cod_p2)
num_p2 = int(num_p2)
val_p2 = float(val_p2)

valor_pagar = (num_p1 * val_p1) + (num_p2 * val_p2)

print("VALOR A PAGAR: R$ {:.2f}".format(valor_pagar))
